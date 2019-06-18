#!/usr/bin/env python3
# coding: utf-8

"""
Alipy 支付API   蚂蚁金服开放平台开发文档地址 https://docs.open.alipay.com/api_1/

@Time    : 2019-5-31
@Author  : yanhuazidi
@Email   : yanhuazidi@163.com
@Programming Language : Python3

修改自 python-alipay-sdk包
Cryptodome依赖包使用 pip3 install pycrytodomex下载

应用ip、应用公私匙、支付宝公匙请到蚂蚁金服开放平台获取
"""


import sys
import json
from datetime import datetime
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA, SHA256
from Cryptodome.PublicKey import RSA

from urllib.parse import quote_plus
from urllib.request import urlopen
from base64 import decodebytes, encodebytes
def u(s):
    return s
def b(s):
    return s.encode("utf-8")


class BaseAliPay:
    @property
    def appid(self):
        return self._appid

    @property
    def sign_type(self):
        return self._sign_type

    @property
    def gateway(self):
        return self._gateway

    @property
    def app_private_key(self):
        """应用密匙"""
        return self._app_private_key

    @property
    def alipay_public_key(self):
        """支付宝公匙"""
        return self._alipay_public_key

    def __init__(
        self,
        appid,
        app_private_key_string=None,     
        alipay_public_key_string=None,
        app_private_key_path=None,
        alipay_public_key_path=None,
        sign_type="RSA2",
        debug=False
    ):
        """
        appid应用ID,
        app_private_key_string  应用私匙字符串
        alipay_public_key_string    支付宝公匙字符串
        app_private_key_path    应用私匙文件路径,与应用私匙字符串选填一个即可
        alipay_public_key_path  支付宝公匙文件路径,与应用公匙字符串选填一个即可
        sign_type="RSA2",   密匙加密类型  RSA 或 RSA2
        debug=False     # False 为真实环境 , True 为沙箱环境
        """
        self._appid = str(appid) if type(appid)==int else appid
        self._sign_type = sign_type
        self._app_private_key = self._load_key(app_private_key_string,app_private_key_path)
        self._alipay_public_key = self._load_key(alipay_public_key_string,alipay_public_key_path)

        if debug:
            self._gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self._gateway = "https://openapi.alipay.com/gateway.do"


    def _load_key(self,key_string=None,key_path=None):
        '''加载密匙'''
        if key_string or key_path:
            content = key_string.strip()
            if not content:
                with open(key_path) as fp:
                    content = fp.read()
            content = content.strip()
            if not content.startswith('-----') and not content.endswith('----'):
                content = '-----BEGIN PUBLIC KEY-----\n'+content+'\n-----END PUBLIC KEY-----'
            return RSA.importKey(content)
        else:
            raise ValueError('请传入key字符串或key文件的路径')

    def _sign(self, unsigned_string):
        '''生成签名'''
        """
        通过如下方法调试签名
        方法1
            key = rsa.PrivateKey.load_pkcs1(open(self._app_private_key_path).read())
            sign = rsa.sign(unsigned_string.encode("utf8"), key, "SHA-1")
            # base64 编码，转换为unicode表示并移除回车
            sign = base64.encodebytes(sign).decode("utf8").replace("\n", "")
        方法2
            key = RSA.importKey(open(self._app_private_key_path).read())
            signer = PKCS1_v1_5.new(key)
            signature = signer.sign(SHA.new(unsigned_string.encode("utf8")))
            # base64 编码，转换为unicode表示并移除回车
            sign = base64.encodebytes(signature).decode("utf8").replace("\n", "")
        方法3
            echo "abc" | openssl sha1 -sign alipay.key | openssl base64
        """
        # 开始计算签名
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        if self._sign_type == "RSA2":
            signature = signer.sign(SHA256.new(b(unsigned_string)))
        elif self._sign_type == "RSA":
            signature = signer.sign(SHA.new(b(unsigned_string)))
        else:
            raise ValueError('sign_type 值必须是 "RSA" 或 "RSA2"')
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        return sign

    def _ordered_data(self, data):
        '''排序'''
        complex_keys = [k for k, v in data.items() if isinstance(v, dict)]#把值为字典的键提取出来

        # 将值为字典的数据序列化
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))

        return sorted([(k, v) for k, v in data.items()])

    def _build_body( self, method, biz_content={},
        return_url=None, notify_url=None, version="1.0", format_ =None, app_auth_token = None,
        timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        """
        公共参数
        app_id	        String	是	        32	    支付宝分配给开发者的应用ID	    2014072300007148
        method	        String	是	        128	    接口名称	                   alipay.trade.page.pay
        charset	        String	是	        10	    请求使用的编码格式，如utf-8,gbk,gb2312等	utf-8
        sign_type	    String	是	        10	    商户生成签名字符串所使用的签名算法类型，目前支持RSA2和RSA，推荐使用RSA2	RSA2
        sign	        String	是	        344	    商户请求参数的签名串，详见签名	            详见示例
        timestamp	    String	是	        19	    发送请求的时间，格式"yyyy-MM-dd HH:mm:ss"	2014-07-24 03:07:50
        version	        String	是	        3	    调用的接口版本，固定为：1.0	1.0
        format	        String	否	        40	    仅支持JSON	JSON
        return_url	    String	否	        256	    HTTP/HTTPS开头字符串	        https://m.alipay.com/Gk8NF23
        notify_url	    String	否	        256	    支付宝服务器主动通知商户服务器里指定的页面http/https路径。	http://api.test.alipay.net/atinterface/receive_notify.htm
        app_auth_token  String	否	        40	    详见应用授权概述	
        biz_content
        """
        data = {
            "app_id": self._appid,
            "method": method,
            "charset": "utf-8",
            "sign_type": self._sign_type,
            "return_url":return_url,
            "notify_url":notify_url,
            "format":format_,
            "timestamp":timestamp,
            "version": "1.0",
            "app_auth_token":app_auth_token,
            "biz_content":biz_content,
        }
        l = [k for k,v in data.items() if not v]
        for k in l:
            data.pop(k)
        return data

    def _sign_data(self, data):
        '''签名,返回签名后的字符串'''
        data.pop("sign", None)
        # 排序后的字符串
        ordered_items = self._ordered_data(data)
        unsigned_string = "&".join("{}={}".format(k, v) for k, v in ordered_items)
        sign = self._sign(unsigned_string)
        quoted_string = "&".join("{}={}".format(k, quote_plus(v)) for k, v in ordered_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    def _verify(self, raw_content, signature):
        '''验证签名'''
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        if self._sign_type == "RSA2":
            digest = SHA256.new()
        else:
            digest = SHA.new()
        digest.update(raw_content.encode("utf8"))
        # 验证签名
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False

    def verify(self, data, signature):
        '''验证签名data返回的数据, signature 返回的签名'''
        if "sign_type" in data:
            sign_type = data.pop("sign_type")
            if sign_type != self._sign_type:
                raise AliPayException(None, "未知的sign_type: {}".format(sign_type))
        # 排序后的字符串
        unsigned_items = self._ordered_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)


    def _verify_and_return_sync_response(self, raw_string, response_type):
        """
        验证响应,返回响应内容
        raw_string json字符串,response_type响应的类型
        """

        response = json.loads(raw_string)
        # raise exceptions
        if "sign" not in response.keys():
            result = response[response_type]
            raise AliPayException(
                code=result.get("code", "0"),
                message=raw_string
            )

        sign = response["sign"]

        # 找到待签名的字符串
        plain_content = self._get_string_to_be_signed(raw_string, response_type)

        if not self._verify(plain_content, sign):
            raise AliPayValidationError
        return json.loads(plain_content)

    def _get_string_to_be_signed(self, raw_string, response_type):
        """
        从返回的raw_string里面找到待签名的字符串
        """
        balance = 0
        start = end = raw_string.find("{", raw_string.find(response_type))
        # 从response_type之后的第一个｛的下一位开始匹配，
        # 如果是｛则balance加1; 如果是｝而且balance=0，就是待验签字符串的终点
        for i, c in enumerate(raw_string[start + 1:], start + 1):
            if c == "{":
                balance += 1
            elif c == "}":
                if balance == 0:
                    end = i + 1
                    break
                balance -= 1
        return raw_string[start:end]


#以下接口方法，接受订单数据，返回支付宝请求链接
# 详细参数查看 https://docs.open.alipay.com/api_1/alipay.trade.page.pay/
# 参数	        类型	    是否必填	最大长度	    描述	                                                            示例值
# out_trade_no	String	    必选	    64	    商户订单号,64个字符以内、可包含字母、数字、下划线；需保证在商户端不重复	         20150320010101001
# product_code	String	    必选	    64	    销售产品码，与支付宝签约的产品码名称。 注：目前仅支持FAST_INSTANT_TRADE_PAY	    FAST_INSTANT_TRADE_PAY
# total_amount	Price	    必选	    11	    订单总金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000]。	        88.88
# subject	    String	    必选	    256	    订单标题	                                                                Iphone6 16G

    def api(self, api_name, **kwargs):
        """
        通过api方法可以调用以下各种接口, 以api_name=method 区分
        alipay.api("alipay.trade.page.pay", **kwargs) ==> alipay.api_alipay_trade_page_pay(**kwargs)
        """
        api_name = api_name.replace(".", "_")
        key = "api_" + api_name
        if hasattr(self, key):
            return getattr(self, key)(**kwargs)
        raise AttributeError("Unknown attribute" + api_name)

    def api_alipay_trade_wap_pay(
        self, subject, out_trade_no, total_amount,return_url=None, notify_url=None, **kwargs):
        """手机网站支付接口"""
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "QUICK_WAP_PAY"
        }
        biz_content.update(kwargs)
        data = self._build_body(
            "alipay.trade.wap.pay",
            biz_content,
            return_url=return_url,
            notify_url=notify_url
        )
        return self._sign_data(data)

    def api_alipay_trade_app_pay(
        self, subject, out_trade_no, total_amount, notify_url=None, **kwargs):
        """app支付接口 手机app支付"""
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "QUICK_MSECURITY_PAY"
        }
        biz_content.update(kwargs)
        data = self._build_body("alipay.trade.app.pay", biz_content, notify_url=notify_url)
        return self._sign_data(data)

    def api_alipay_trade_pay(
        self, out_trade_no, scene, auth_code, subject, notify_url=None, **kwargs):
        """统一收单交易支付接口, 付款码支付
        out_trade_no	String	    必选	64	商户订单号
        scene	        String	    必选	32	支付场景 
                条码支付，取值：bar_code 
                声波支付，取值：wave_co
        auth_code	    String	    必选	32	支付授权码
        """
        """
        eg:
            self.api_alipay_trade_pay(
                out_trade_no,
                "bar_code/wave_code",
                auth_code,
                subject,
                total_amount=12,
                discountable_amount=10
            )

        failed response = {
            "alipay_trade_pay_response": {
                "code": "40004",
                "msg": "Business Failed",
                "sub_code": "ACQ.INVALID_PARAMETER",
                "sub_msg": "",
                "buyer_pay_amount": "0.00",
                "invoice_amount": "0.00",
                "point_amount": "0.00",
                "receipt_amount": "0.00"
            },
            "sign": ""
        }
        succeeded response =
            {
              "alipay_trade_pay_response": {
                "trade_no": "2017032121001004070200176846",
                "code": "10000",
                "invoice_amount": "20.00",
                "open_id": "20880072506750308812798160715407",
                "fund_bill_list": [
                  {
                    "amount": "20.00",
                    "fund_channel": "ALIPAYACCOUNT"
                  }
                ],
                "buyer_logon_id": "csq***@sandbox.com",
                "receipt_amount": "20.00",
                "out_trade_no": "out_trade_no18",
                "buyer_pay_amount": "20.00",
                "buyer_user_id": "2088102169481075",
                "msg": "Success",
                "point_amount": "0.00",
                "gmt_payment": "2017-03-21 15:07:29",
                "total_amount": "20.00"
              },
              "sign": ""
            }
        """
        assert scene in ("bar_code", "wave_code"), 'scene not in ("bar_code", "wave_code")'

        biz_content = {
            "out_trade_no": out_trade_no,
            "scene": scene,
            "auth_code": auth_code,
            "subject": subject
        }
        biz_content.update(**kwargs)
        data = self._build_body("alipay.trade.pay", biz_content, notify_url=notify_url)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_pay_response")

    def api_alipay_trade_page_pay(
        self, subject, out_trade_no, total_amount,return_url=None, notify_url=None, **kwargs):
        """统一收单下单并支付页面接口 网站页面扫码"""
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY"
        }
        biz_content.update(kwargs)
        data = self._build_body(
            "alipay.trade.page.pay",
            biz_content,
            return_url=return_url,
            notify_url=notify_url
        )
        return self._sign_data(data)

    def api_alipay_trade_query(
        self, out_trade_no=None, trade_no=None):
        '''查询订单状态,返回支付宝返回结果字典
            out_trade_no    商家订单号
            trade_no        支付宝交易号
        '''
        """
        response = {
          "alipay_trade_query_response": {
            "trade_no": "2017032121001004070200176844",
            "code": "10000",
            "invoice_amount": "20.00",
            "open_id": "20880072506750308812798160715407",
            "fund_bill_list": [
              {
                "amount": "20.00",
                "fund_channel": "ALIPAYACCOUNT"
              }
            ],
            "buyer_logon_id": "csq***@sandbox.com",
            "send_pay_date": "2017-03-21 13:29:17",
            "receipt_amount": "20.00",
            "out_trade_no": "out_trade_no15",
            "buyer_pay_amount": "20.00",
            "buyer_user_id": "2088102169481075",
            "msg": "Success",
            "point_amount": "0.00",
            "trade_status": "TRADE_SUCCESS",
            "total_amount": "20.00"
          },
          "sign": ""
        }
        failed response is like this
        {
          "alipay_trade_query_response": {
            "sub_code": "isv.invalid-app-id",
            "code": "40002",
            "sub_msg": "无效的AppID参数",
            "msg": "Invalid Arguments"
          }
        }
        """
        assert (out_trade_no is not None) or (trade_no is not None),"Both trade_no and out_trade_no are None"

        biz_content = {}
        if out_trade_no:
            biz_content["out_trade_no"] = out_trade_no
        if trade_no:
            biz_content["trade_no"] = trade_no
        data = self._build_body("alipay.trade.query", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_query_response")

    def api_alipay_trade_create(
        self, subject, out_trade_no, total_amount, notify_url=None, **kwargs):
        """统一收单交易创建接口
        "product_code"销售产品码。如果签约的是当面付快捷版，则传OFFLINE_PAYMENT;
                    其它支付宝当面付产品传FACE_TO_FACE_PAYMENT；不传默认使用FACE_TO_FACE_PAYMENT；
        """
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FACE_TO_FACE_PAYMENT"
        }
        biz_content.update(kwargs)
        data = self._build_body(
            "alipay.trade.create",
            biz_content,
            notify_url=notify_url
        )
        return self._sign_data(data)

    def api_alipay_trade_precreate(
        self, subject, out_trade_no, total_amount, **kwargs):
        """统一收单线下交易预创建
            收银员通过收银台或商户后台调用支付宝接口，生成二维码后，展示给用户，由用户扫描二维码完成订单支付

        response
        out_trade_no	String	必填	64	商户的订单号	6823789339978248
        qr_code	String	必填	1024	当前预下单请求生成的二维码码串，可以用二维码生成工具根据该码串值生成对应的二维码	https://qr.alipay.com/bavh4wjlxf12tper3a
        success response  = {
          "alipay_trade_precreate_response": {
            "msg": "Success",
            "out_trade_no": "out_trade_no17",
            "code": "10000",
            "qr_code": "https://qr.alipay.com/bax03431ljhokirwl38f00a7"
          },
          "sign": ""
        }

        failed response = {
          "alipay_trade_precreate_response": {
            "msg": "Business Failed",
            "sub_code": "ACQ.TOTAL_FEE_EXCEED",
            "code": "40004",
            "sub_msg": "订单金额超过限额"
          },
          "sign": ""
        }

        """
        biz_content = {
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "subject": subject
        }
        biz_content.update(**kwargs)
        data = self._build_body("alipay.trade.precreate", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
        #返回html字节串
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_precreate_response")

    def api_alipay_trade_cancel(
        self, out_trade_no=None, trade_no=None):
        """统一收单交易撤销接口
           撤销订单:out_trade_no    商家订单号
                    trade_no        支付宝交易号""" 
        """
        response = {
        "alipay_trade_cancel_response": {
            "msg": "Success",
            "out_trade_no": "out_trade_no15",
            "code": "10000",
            "retry_flag": "N"
          }
        }
        """

        assert (out_trade_no is not None) or (trade_no is not None),"Both trade_no and out_trade_no are None"

        biz_content = {}
        if out_trade_no:
            biz_content["out_trade_no"] = out_trade_no
        if trade_no:
            biz_content["trade_no"] = trade_no

        data = self._build_body("alipay.trade.cancel", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_cancel_response")

    def api_alipay_trade_close(
        self, out_trade_no=None, trade_no=None, operator_id=None):
        """统一收单交易关闭接口
        operator_id	String	可选	28	卖家端自定义的的操作员 ID	YX01
        """
        """
        response = {
            "alipay_trade_close_response": {
                "code": "10000",
                "msg": "Success",
                "trade_no": "2013112111001004500000675971",
                "out_trade_no": "YX_001"
            }
        }
        """

        assert (out_trade_no is not None) or (trade_no is not None),"Both trade_no and out_trade_no are None"

        biz_content = {}
        if out_trade_no:
            biz_content["out_trade_no"] = out_trade_no
        if trade_no:
            biz_content["trade_no"] = trade_no
        if operator_id:
            biz_content["operator_id"] = operator_id

        data = self._build_body("alipay.trade.close", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_close_response")

    def api_alipay_trade_refund(
        self, refund_amount, out_trade_no=None, trade_no=None, **kwargs):
        """统一收单交易退款接口 refund_amount	Price	必选	需要退款的金额，该金额不能大于订单金额"""
        biz_content = {
            "refund_amount": refund_amount
        }
        biz_content.update(**kwargs)
        if out_trade_no:
            biz_content["out_trade_no"] = out_trade_no
        if trade_no:
            biz_content["trade_no"] = trade_no

        data = self._build_body("alipay.trade.refund", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(raw_string, "alipay_trade_refund_response")

    def api_alipay_trade_fastpay_refund_query(
        self, out_request_no, trade_no=None, out_trade_no=None):
        """统一收单交易退款查询
        商户可使用该接口查询自已通过alipay.trade.refund提交的退款请求是否执行成功。 该接口的返回码10000，
        仅代表本次查询操作成功，不代表退款成功。如果该接口返回了查询数据，则代表退款成功，如果没有查询到则代
        表未退款成功，可以调用退款接口进行重试。重试时请务必保证退款请求号一致。
        """
        assert (out_trade_no is not None) or (trade_no is not None),"Both trade_no and out_trade_no are None"

        biz_content = {"out_request_no": out_request_no}
        if trade_no:
            biz_content["trade_no"] = trade_no
        else:
            biz_content["out_trade_no"] = out_trade_no

        data = self._build_body("alipay.trade.fastpay.refund.query", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_trade_fastpay_refund_query_response"
        )

    def api_alipay_fund_trans_toaccount_transfer(
        self, out_biz_no, payee_type, payee_account, amount, **kwargs):
        """单笔转账到支付宝账户接口
        单笔转账到支付宝账户接口是基于支付宝的资金处理能力，为了满足支付宝商家向其他支付宝账户转账的需求，
        针对有部分开发能力的商家，提供通过API接口完成支付宝账户间的转账的功能。 该接口适用行业较广，
        比如商家间的货款结算，商家给个人用户发放佣金等。
        参数	        类型	    是否必填	    最大长度	    描述	    示例值
        out_biz_no	    String	    必选	        64      	商户转账唯一订单号。发起转账来源方定义的转账单据ID，用于将转账回执通知给来源方。 
                                                                            不同来源方给出的ID可以重复，同一个来源方必须保证其ID的唯一性。 
                                                                            只支持半角英文、数字，及“-”、“_”。	3142321423432
        payee_type	    String	    必选	        20	        收款方账户类型。可取值： 
                                                                        1、ALIPAY_USERID：支付宝账号对应的支付宝唯一用户号。以2088开头的16位纯数字组成。 
                                                                        2、ALIPAY_LOGONID：支付宝登录号，支持邮箱和手机号格式。	ALIPAY_LOGONID
        payee_account	String	    必选	        100	        收款方账户。与payee_type配合使用。付款方和收款方不能是同一个账户。	abc@sina.com
        amount	        String	    必选	        16	        转账金额，单位：元。 
                                                                只支持2位小数，小数点前最大支持13位，金额必须大于等于0.1元。 
                                                                最大转账金额以实际签约的限额为准。	12.23
        """

        assert payee_type in ("ALIPAY_USERID", "ALIPAY_LOGONID"), "unknown payee type"
        biz_content = {
            "out_biz_no": out_biz_no,
            "payee_type": payee_type,
            "payee_account": payee_account,
            "amount": amount
        }
        biz_content.update(kwargs)
        data = self._build_body("alipay.fund.trans.", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_fund_trans_toaccount_transfer_response"
        )

    def api_alipay_fund_trans_order_query(
        self, out_biz_no=None, order_id=None):
        """查询转账订单接口
        out_biz_no	String	可选	64	商户转账唯一订单号：发起转账来源方定义的转账单据ID。 
                                                和支付宝转账单据号不能同时为空。当和支付宝转账单据号同时提供时，
                                                将用支付宝转账单据号进行查询，忽略本参数。	3142321423432
        order_id	String	可选	64	支付宝转账单据号：和商户转账唯一订单号不能同时为空。当和商户转账唯一订单号同时提供时
                                        将用本参数进行查询，忽略商户转账唯一订单号。	20160627110070001502260006780837
        """
        if out_biz_no is None and order_id is None:
            raise Exception("Both out_biz_no and order_id are None!")

        biz_content = {}
        if out_biz_no:
            biz_content["out_biz_no"] = out_biz_no
        if order_id:
            biz_content["order_id"] = order_id

        data = self._build_body("alipay.fund.trans.order.query", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_fund_trans_order_query_response"
        )

    def api_alipay_trade_order_settle(
        self,out_request_no,trade_no,royalty_parameters,**kwargs):
        """统一收单交易结算接口
        用于在线下场景交易支付后，进行结算
        royalty_parameters	OpenApiRoyaltyDetailInfoPojo[]	 必选		分账明细信息
        """
        biz_content = {
            "out_request_no": out_request_no,
            "trade_no": trade_no,
            "royalty_parameters": royalty_parameters,
        }
        biz_content.update(kwargs)

        data = self._build_body("alipay.trade.order.settle", biz_content)

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_trade_order_settle_response"
        )



class AliPay(BaseAliPay):
    """
    appid                     应用ID,
    app_private_key_string    应用私匙字符串,
    alipay_public_key_string  支付宝公匙字符串,
    app_private_key_path      应用私匙文件路径,与应用私匙字符串选填一个即可,
    alipay_public_key_path    支付宝公匙文件路径,与应用公匙字符串选填一个即可,
    sign_type="RSA2",         密匙加密类型  RSA 或 RSA2,
    debug=False               # False 为真实环境 , True 为沙箱环境,
    """
    pass


class ISVAliPay(BaseAliPay):
    '''应用授权的场景'''
    def __init__(
        self,
        appid,
        app_notify_url,
        app_private_key_path=None,
        app_private_key_string=None,
        alipay_public_key_path=None,
        alipay_public_key_string=None,
        sign_type="RSA2",
        debug=False,
        app_auth_token=None,
        app_auth_code=None
    ):
        if not app_auth_token and not app_auth_code:
            raise Exception("Both app_auth_code and app_auth_token are None !!!")

        self._app_auth_token = app_auth_token
        self._app_auth_code = app_auth_code
        super(ISVAliPay, self).__init__(
            appid,
            app_notify_url,
            app_private_key_path=app_private_key_path,
            app_private_key_string=app_private_key_string,
            alipay_public_key_path=alipay_public_key_path,
            alipay_public_key_string=alipay_public_key_string,
            sign_type=sign_type,
            debug=debug
        )

    @property
    def app_auth_token(self):
        # 没有则换取token
        if not self._app_auth_token:
            result = self.api_alipay_open_auth_token_app(self._app_auth_code)
            self._app_auth_token = result.get("app_auth_token", None)

        if not self._app_auth_token:
            raise Exception("Get auth token by auth code failed: {}".format(self._app_auth_code))
        return self._app_auth_token

    def build_body(
        self, method, biz_content, return_url=None, notify_url=None, append_auth_token=True
    ):
        return super(ISVAliPay, self)._build_body(
            method, biz_content, return_url, notify_url, append_auth_token
        )

    def api_alipay_open_auth_token_app(self, refresh_token=None):
        """
        换取应用授权令牌
        response = {
          "code": "10000",
          "msg": "Success",
          "app_auth_token": "201708BB28623ce3d10f4f62875e9ef5cbeebX07",
          "app_refresh_token": "201708BB108a270d8bb6409890d16175a04a7X07",
          "auth_app_id": "appid",
          "expires_in": 31536000,
          "re_expires_in": 32140800,
          "user_id": "2088xxxxx
        }
        """

        if refresh_token:
            biz_content = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token
            }
        else:
            biz_content = {
                "grant_type": "authorization_code",
                "code": self._app_auth_code
            }
        data = self.build_body(
            "alipay.open.auth.token.app",
            biz_content,
            append_auth_token=False
        )

        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_open_auth_token_app_response"
        )

    def api_alipay_open_auth_token_app_query(self):
        '''查询某个应用授权AppAuthToken的授权信'''
        biz_content = {
            "app_auth_token": self.app_auth_token
        }
        data = self.build_body(
            "alipay.open.auth.token.app.query",
            biz_content,
            append_auth_token=False
        )
        url = self._gateway + "?" + self._sign_data(data)
        raw_string = urlopen(url, timeout=15).read().decode("utf-8")
        return self._verify_and_return_sync_response(
            raw_string, "alipay_open_auth_token_app_query_response"
        )


class AliPayException(Exception):
    '''接口请求错误'''
    def __init__(self, code, message):
        self.__code = code
        self.__message = message


    if sys.version_info[0] >= 3:
        def to_unicode(self):
            return "AliPayException: code:{}, message:{}".format(self.__code, self.__message)

        def __str__(self):
            return self.to_unicode()

        def __repr__(self):
            return self.to_unicode()
    else:
        def to_unicode(self):
            return u"AliPayException: code:{}, message:{}".format(self.__code, self.__message.decode("utf8"))
        def __str__(self):
            return self.to_unicode().encode('utf8')

        def __repr__(self):
            return self.to_unicode().encode('utf8')


class AliPayValidationError(Exception):
    '''验证错误'''
    pass



# 公共参数	            类型	是否必填	最大长度	    描述	                    示例值
# app_id	        String	是	        32	    支付宝分配给开发者的应用ID	    2014072300007148
# method	        String	是	        128	    接口名称	                   alipay.trade.page.pay
# format	        String	否	        40	    仅支持JSON	JSON
# return_url	    String	否	        256	    HTTP/HTTPS开头字符串	        https://m.alipay.com/Gk8NF23
# charset	        String	是	        10	    请求使用的编码格式，如utf-8,gbk,gb2312等	utf-8
# sign_type	        String	是	        10	    商户生成签名字符串所使用的签名算法类型，目前支持RSA2和RSA，推荐使用RSA2	RSA2
# sign	            String	是	        344	    商户请求参数的签名串，详见签名	            详见示例
# timestamp	        String	是	        19	    发送请求的时间，格式"yyyy-MM-dd HH:mm:ss"	2014-07-24 03:07:50
# version	        String	是	        3	    调用的接口版本，固定为：1.0	1.0
# notify_url	    String	否	        256	    支付宝服务器主动通知商户服务器里指定的页面http/https路径。	http://api.test.alipay.net/atinterface/receive_notify.htm
# app_auth_token    String	否	        40	    详见应用授权概述	
# biz_content	    String	是		    请求参数的集合，最大长度不限，除公共参数外所有请求参数都必须放在这个参数中传递，具体参照各产品快速接入文档


# 同步返回处理（return_url）：是一种可视化的返回，ie页面跳转通知，只要支付成功，支付宝通过get方式跳转到这个地址，并且带有参数给这个页面。
# 客户获取信息受到买家操作的影响。如果买家支付完成后客户服务器响应比较慢，买家在显示支付宝提示的“即时到账支付成功“时关闭页面
# ，那么客户网站是获取不到信息，我们这边称为” 掉单“。而且这个返回处理是一次性调取，即支付成功后才调取同步返回处理。

# 异步返回处理（notify_url）：它的数据交互是通过服务器间进行数据交互,必须将其放置在服务器上(公网)测试，服务器post消息到异步返回处理页面，
# 需要客户技术在异步返回处理页面处理相关的数据处理，然后每一步操作都要返回给支付宝success（不能包含其他的HTML脚本语言，不可以做页面跳转。）
# 这个返回处理如果集成OK，那么基本不会出现掉单，因为支付宝会在24小时之内分6~10次将订单信息返回个给客户网站，直到支付宝捕获success。

# 公共响应参数
# 参数	    类型	是否必填	最大长度	    描述	    示例值
# code	    String	是	        -	    网关返回码,详见文档	40004
# msg	    String	是	        -	    网关返回码描述,详见文档	Business Failed
# sub_code	String	否	        -	    业务返回码，参见具体的API接口文档	ACQ.TRADE_HAS_SUCCESS
# sub_msg	String	否	        -	    业务返回码描述，参见具体的API接口文档	交易已被支付
# sign	    String	是	        -	    签名,详见文档

# 响应参数
# 参数	        类型	    是否必填	最大长度	描述	示例值
# trade_no	    String	    必填	    64	    支付宝交易号	2013112011001004330000121536
# out_trade_no	String	    必填	    64	    商户订单号	6823789339978248
# seller_id	    String	    必填	    16	    收款支付宝账号对应的支付宝唯一用户号。 以2088开头的纯16位数字	2088111111116894
# total_amount	Price	    必填	    11	    交易金额	128.00
# merchant_order_no	String	必填	    32	    商户原始订单号，最大长度限制32位	20161008001