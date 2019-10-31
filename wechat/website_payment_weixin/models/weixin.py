# -*- coding: utf-'8' "-*-"
from odoo.addons.website_payment_weixin.controllers.controllers import WeixinController
import json
import logging
import urllib
import requests
from lxml import etree
from urllib.parse import urljoin

from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.http import request
from odoo import api, fields, models

from . import util

_logger = logging.getLogger(__name__)


class AcquirerWeixin(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('weixin', 'weixin')])
    weixin_appid = fields.Char(string='Weixin APPID', required_if_provider='weixin')
    weixin_mch_id = fields.Char(string=u'微信支付商户号', required_if_provider='weixin')
    weixin_key = fields.Char(string=u'API密钥 ', required_if_provider='weixin')
    weixin_secret = fields.Char(string='Weixin Appsecret', required_if_provider='weixin')

    def _get_weixin_urls(self, environment):
        if environment == 'prod':
            return {
                'weixin_url': 'https://api.mch.weixin.qq.com/pay/unifiedorder'
            }
        else:
            return {
                'weixin_url': 'https://api.mch.weixin.qq.com/pay/unifiedorder'
            }

    @api.one
    def _get_weixin_key(self):
        return self.weixin_key

    _defaults = {
        'fees_active': False,
    }

    def _try_url(self, request, tries=3):
        done, res = False, None
        while (not done and tries):
            try:
                res = urllib.request.urlopen(request)
                done = True
            except urllib.HTTPError as e:
                res = e.read()
                e.close()
                if tries and res and json.loads(res)['name'] == 'INTERNAL_SERVICE_ERROR':
                    _logger.warning('Failed contacting Paypal, retrying (%s remaining)' % tries)
            tries = tries - 1
        if not res:
            pass
        result = res.read()
        res.close()
        return result

    @api.one
    def get_wx_appid(self):
        return self.weixin_appid

    @api.multi
    def weixin_form_generate_values(self, tx_values):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        amount = int(tx_values.get('amount', 0) * 100)
        nonce_str = util.random_generator()
        data_post = {
            'appid': self.weixin_appid,
            'body': tx_values['reference'],
            'mch_id': self.weixin_mch_id,
            'nonce_str': nonce_str,
            'notify_url': '%s' % urljoin(base_url, WeixinController._notify_url),
            'out_trade_no': tx_values['reference'],
            # 'spbill_create_ip': self.environ['REMOTE_ADDR'],  # util._get_ipaddress(),
            'weixin_key': self.weixin_key,
            'total_fee': amount,
        }
        tx_values.update(data_post)
        return tx_values

    @api.multi
    def weixin_get_form_action_url(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        return base_url + '/payment/action_confirm'
        # return self._get_weixin_urls(self.environment)['weixin_url']


class TxWeixin(models.Model):
    _inherit = 'payment.transaction'

    weixin_txn_id = fields.Char(string='Transaction ID')
    weixin_txn_type = fields.Char(string='Transaction type')

    # --------------------------------------------------
    # FORM RELATED METHODS
    # --------------------------------------------------
    # 付款交易订单查询是否存在
    def _weixin_form_get_tx_from_data(self, data):
        reference, txn_id = data.get('transaction_id'), data.get('out_trade_no')
        if not reference or not txn_id:
            error_msg = 'weixin: received data with missing reference (%s) or txn_id (%s)' % (reference, txn_id)
            raise ValidationError(error_msg)

        # find tx -> @TDENOTE use txn_id ?
        tx_ids = self.search([('reference', '=', txn_id)])
        if not tx_ids or len(tx_ids) > 1:
            error_msg = 'weixin: received data for reference %s' % (reference)
            if not tx_ids:
                error_msg += '; no order found'
            else:
                error_msg += '; multiple order found'
            raise ValidationError(error_msg)
        return tx_ids[0]

    # #付款交易金额检查--交易币种检查
    # def _weixin_form_get_invalid_parameters(self, data):
    #     invalid_parameters = []
    #
    #     if float_compare(float(data.get('total_fee', '0.0')), self.amount, 2) != 0:
    #         invalid_parameters.append(('amount', data.get('total_fee'), '%.2f' % self.amount))
    #     if data.get('fee_type') != self.currency_id.name:
    #         invalid_parameters.append(('currency', data.get('fee_type'), self.currency_id.name))
    #
    #     return invalid_parameters

    def _weixin_form_validate(self, data):

        status = data.get('return_code')
        data = {
            'acquirer_reference': data.get('transaction_id'),
            'weixin_txn_id': data.get('transaction_id'),
            'weixin_txn_type': data.get('fee_type'),
        }

        if status == 'SUCCESS':
            data.update(state='done', date_validate=data.get('time_end', fields.datetime.now()))
            return self.write(data)

        else:
            error = 'Received unrecognized status for weixin payment %s: %s, set as error' % (self.reference, status)
            data.update(state='error', state_message=error)
            return self.write(data)

    @api.multi
    def weixin_action_returns_commit(self):
        # ==================
        # 确认退款操作
        # ==================
        data = {
            'appid': self.acquirer_id.weixin_appid,
            'mch_id': self.acquirer_id.weixin_mch_id,
            'nonce_str': util.random_generator(),
            'out_refund_no': self.reference,
            # 'out_trade_no': self.reference,
            'refund_fee': int(self.amount * 100),
            'total_fee': int(self.amount * 100),
            'transaction_id': self.acquirer_reference,

        }
        sign = util.sign(data, self.acquirer_id.weixin_key, 'md5')
        data.update({'sign': sign})
        url = 'https://api.mch.weixin.qq.com/secapi/pay/refund'
        return_xml = util.request_post(url, data, True)
        if util.verify_sign(data):
            transaction_id = return_xml.find('transaction_id').text
            out_refund_no = return_xml.find('out_refund_no').text
            res = self.env['payment.transaction'].sudo().search(
                [('acquirer_reference', '=', transaction_id), ('reference', '=', out_refund_no)])
            if res:
                return True
            else:
                return False

    def post_order_info(self, out_trade_no, url):
        weixin = request.env['payment.acquirer'].search([('provider', '=', 'weixin')])
        nonce_str = util.random_generator()
        data_post = {
            'appid': weixin.weixin_appid,
            'mch_id': weixin.weixin_mch_id,
            'out_trade_no': out_trade_no,
            'nonce_str': nonce_str,
        }
        sign = util.sign(data_post, weixin.weixin_key, 'md5')
        data_post['sign'] = sign
        request_data = requests.post(url, data=util.json2xml(data_post))
        result = request_data.text.encode("utf-8")
        json = {}
        for el in etree.fromstring(result):
            json[el.tag] = el.text
        if json['result_code'] == "FAIL":
            raise ValidationError("%s, %s" % (json['err_code'], json['err_code_des']))
        return json

    # 主动查询支付交易订单
    def search_order(self, out_trade_no):
        url = 'https://api.mch.weixin.qq.com/pay/orderquery'
        return self.post_order_info(out_trade_no, url)

    # 主动取消支付交易订单
    def cancel_order(self, out_trade_no):
        url = 'https://api.mch.weixin.qq.com/pay/closeorder'
        return self.post_order_info(out_trade_no, url)
