# -*- coding: utf-8 -*-

import logging
from lxml import etree
from werkzeug.utils import redirect
from urllib.parse import quote_plus, urljoin
from odoo import http
from odoo.http import request
from odoo.addons.website_payment_weixin.models import util, weixin

_logger = logging.getLogger(__name__)


class WeixinController(http.Controller):
    _notify_url = '/payment/weixin/notify'

    @http.route(['/shop/payment/checkout'], type="http", auth='user', methods=['GET', 'POST'], website=True)
    def payment_checkout(self, **post):
        if post:
            order_id = post['order_id']
            data = request.env['payment.transaction'].sudo().search_order(order_id)
            if data['result_code'] == 'SUCCESS':
                # request.env['payment.transaction'].sudo().form_feedback(data, 'weixin')
                payment = request.env['payment.transaction'].sudo().search([('reference', '=', order_id)])
                order = request.env['sale.order'].sudo().search([('id', '=', payment.sale_order_id.id)])
                if order and payment and payment.state == 'done' and payment.acquirer_reference:
                    return redirect('/my/orders')
            else:
                message = dict(
                    msg=u"当前订单未完成支付,请您尽快完成支付!"
                )
                return request.render("website_payment_weixin.payment_error", message)

    @http.route(['/shop/payment/cancel'], type="http", auth='user', methods=['GET', 'POST'], website=True)
    def payment_cancel(self, **post):
        if post:
            order_id = post.get('order_id')
            order = request.env['payment.transaction'].sudo().search([('reference', '=', order_id)])
            if order.state == 'done':
                message = dict(
                    msg=u"当前订单已完成支付,无法取消!"
                )
                return request.render("website_payment_weixin.payment_error", message)
            else:
                data = request.env['payment.transaction'].sudo().cancel_order(order_id)

                if data['result_code'] == 'SUCCESS':
                    return redirect('/shop/payment')

    def weixin_validate_data(self, post):
        # 方式一 解析返回信息
        json_data = {}
        for el in etree.fromstring(post):
            json_data[el.tag] = el.text
        orderid = json_data['out_trade_no']
        data = request.env['payment.transaction'].sudo().search_order(orderid)
        if data['result_code'] == 'SUCCESS':
            request.env['payment.transaction'].sudo().form_feedback(data, 'weixin')
            return True
        else:
            return False

    @http.route('/payment/weixin/notify', type='http', auth="none", methods=['GET', 'POST'],
                csrf=False)
    def weixin_notify(self, **post):
        if self.weixin_validate_data(http.request.httprequest.data):
            return 'success'
        else:
            return ''

    def _trade_type(self, data, key):
        url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
        ua = http.request.httprequest.headers['User-Agent']
        mobile = util.judge_pc_or_mobile(ua)
        data['spbill_create_ip'] = http.request.httprequest.remote_addr
        mobile = False
        if not mobile:
            data['trade_type'] = 'NATIVE'
            sign = util.sign(data, key, 'md5')
            data['sign'] = sign
            return_xml = util.request_post(url, data)
            if util.verify_sign(data):
                data.update(
                    qrcode=return_xml.find('code_url').text,
                    client_type='PC',
                    total=int(data['total_fee']) / 100,
                    weixin_key=key,
                )
        else:
            data['trade_type'] = 'MWEB'
            sign = util.sign(data, key, 'md5')
            data['sign'] = sign
            return_xml = util.request_post(url, data)
            if util.verify_sign(data):
                mweb_url = return_xml.find('mweb_url').text
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                redirect_url = base_url + "/shop/payment/h5_done?out_trade_no=%s" % data.get('out_trade_no')
                h5_url = mweb_url + "&redirect_url=%s" % quote_plus(redirect_url)
                data.update(
                    total=int(data['total_fee']) / 100,
                    client_type=mobile,
                    weixin_key=key,
                    url=h5_url,  # H5支付页面
                )
        return data

    @http.route('/payment/action_confirm', type='http', auth="user", website=True)
    def action_confirm(self, **post):
        key = post.pop('weixin_key')
        out_trade_no = post['out_trade_no'].split('x')[0]
        order = request.env['sale.order'].sudo().search([('name', '=', out_trade_no)])

        if order:
            order.state = 'sent'
            self._trade_type(post, key)

        return request.render("website_payment_weixin.action_confirm_button", post)

    @http.route('/my/orders_continue/<int:id>', type='http', auth='public', website=True)
    def wx_continue_order(self, id, **kw):
        order = request.env['sale.order'].sudo().browse(id)

        if order:
            order.state = 'draft'
            request.session.update({
                'sale_order_id': id,
                'sale_transaction_id': False,
                'website_sale_current_pl': False,
            })

            deal = request.env['payment.transaction'].sudo().search([('sale_order_id', '=', id)])
            deal.unlink() if deal else None

            if order.payment_acquirer_id.provider == "wexin":
                request.env['payment.transaction'].sudo().cancel_order(id)

            if order.payment_acquirer_id.provider == "alipay":
                request.env['payment.transaction'].sudo().alipay_trade_close(id)

            return redirect("/shop/payment")

        else:
            message = dict(
                msg=u"当前订单号有误，订单不存在!"
            )
            return request.render("website_payment_weixin.payment_error", message)

    # def jspai_data(self, out_trade_no=None, openid=None):
    #     url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
    #     base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
    #     weixin = request.env['payment.acquirer'].sudo().search([('provider', '=', 'weixin')])
    #     amount = request.env['sale.order'].sudo().search([('name', '=', out_trade_no)]).amount_total
    #     post = {
    #         'appid': weixin.weixin_appid,
    #         'body': out_trade_no,
    #         'mch_id': weixin.weixin_mch_id,
    #         'nonce_str': util.random_generator(),
    #         'notify_url': '%s' % urljoin(base_url, WeixinController._notify_url),
    #         'openid': openid,
    #         'out_trade_no': out_trade_no,
    #         'spbill_create_ip': http.request.httprequest.remote_addr,
    #         'total_fee': int(amount * 100),
    #         'trade_type': 'JSAPI',
    #     }
    #     _, prestr = util.params_filter(post)
    #     sign = util.build_mysign(prestr, weixin.weixin_key, 'MD5')
    #     post.update({
    #         'sign': sign,
    #     })
    #     return_xml = util.request_post(url, post)
    #     prepay_id = return_xml.find('prepay_id').text
    #
    #     jsapi_data = {
    #         'appId': weixin.weixin_appid,
    #         'nonceStr': util.random_generator(),
    #         'package': 'prepay_id=' + prepay_id,
    #         'signType': 'MD5',
    #         'timeStamp': time.time(),
    #     }
    #     _, prestr1 = util.params_filter(jsapi_data)
    #     sign1 = util.build_mysign(prestr1, weixin.weixin_key, 'MD5')
    #     jsapi_data.update({
    #         'paySign': sign1,
    #         'out_trade_no': out_trade_no,
    #     })
    #
    #     _logger.info("jsapi %s" % jsapi_data)
    #     return request.render("website_payment_weixin.action_confirm_jsapi", jsapi_data)

    # # 网页授权验证结束接口
    # @http.route(['/wxverify'], type="http", auth='none', methods=['GET', 'POST'], csrf=False)
    # def wxverify(self, **kwargs):
    #     # 网页授权完毕，进行获取用户信息验证，验证结束登陆到对应的网站
    #     if kwargs:
    #
    #         out_trade_no = kwargs['state']
    #         res_users = self.get_token(kwargs)
    #         openid = res_users['openid']
    #
    #         return self.jspai_data(out_trade_no=out_trade_no, openid=openid)
    #     else:
    #         # 触发微信返回code码
    #         url = self.check_url()
    #         # Header("Location: " + url);
    #         return url

    # def send_url(self, token_url, params):
    #     try:
    #         data = urllib.parse.urlencode(params).encode('utf-8')
    #         req = urllib.request.Request(token_url, data=data)
    #         get_data = urllib.request.urlopen(req).read().decode('utf-8')
    #         sort_data = json.loads(get_data)
    #         return sort_data
    #     except Exception:
    #         _logger.info("获取参数错误：")

    # # 微信用户授权地址
    # def check_url(self, out_trade_no=None):
    #     weixin = request.env['payment.acquirer'].sudo().search([('provider', '=', 'weixin')])
    #     wx_appid = weixin.weixin_appid
    #     redirect_uri = request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/wxverify'
    #     url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + str(wx_appid) + '&' \
    #                                                                                          'redirect_uri=' + str(
    #         redirect_uri) + '&response_type=code&scope=snsapi_base&state=' + out_trade_no + '#wechat_redirect'
    #     return url

    # # 通过code换取网页授权access_token
    # def get_token(self, res_code):
    #     token_url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
    #     weixin = request.env['payment.acquirer'].sudo().search([('provider', '=', 'weixin')])
    #     params = {
    #         'appid': weixin.weixin_appid,
    #         'secret': weixin.weixin_secret,
    #         'code': res_code['code'],
    #         'grant_type': 'authorization_code'
    #     }
    #     return self.send_url(token_url, params)

    # # 网页授权
    # @http.route('/wxverify/MP_verify_l1JijRgASh5SDh0Q.txt', type='http', auth="none", methods=['GET', 'POST'],
    #             csrf=False)
    # def wx_lweb(self, **kw):
    #     return 'l1JijRgASh5SDh0Q'

    @http.route(['/shop/payment/h5_done'], type="http", auth='user', methods=['GET', 'POST'], website=True)
    def payment_done(self, **post):
        if post:
            data = {
                'out_trade_no': post['out_trade_no']
            }
            return request.render("website_payment_weixin.action_h5_payment", data)
        else:
            return redirect('/shop/payment')
