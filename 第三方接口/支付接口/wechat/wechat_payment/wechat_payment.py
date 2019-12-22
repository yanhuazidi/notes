# -*- coding: utf-8 -*-

import json
import socket
import time
import random
import hashlib
import xmltodict
from urllib.request import Request,urlopen
import datetime
 
class WX_PayToolUtil():
    """ 微信支付工具 """
 
    def __init__(self, APP_ID, MCH_ID, API_KEY, NOTIFY_URL):
        # ========支付相关配置信息===========
        self._APP_ID = APP_ID  # 公众账号appid
        self._MCH_ID = MCH_ID  # 商户号
        self._API_KEY = API_KEY  # key设置路径：微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置
        # 有关url
        self._host_name = socket.gethostname()
        self._ip_address = socket.gethostbyname(self._host_name)
        self._CREATE_IP = self._ip_address  # 发起支付的ip
        # self._UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"  # 接口链接
        self._UFDODER_URL = "https://api.mch.weixin.qq.com/sandboxnew/pay/unifiedorder" # 测试链接
        self._NOTIFY_URL = NOTIFY_URL  # 异步通知
        # 其他参数
        self._time_start = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
    def getPayUrl(self, orderid, goodsName, goodsPrice, **kwargs):
        """向微信支付端发出请求，获取url"""
 
        appid = self._APP_ID
        mch_id = self._MCH_ID
        key = self._API_KEY
 
        nonce_str = str(int(round(time.time() * 1000))) + str(random.randint(1, 999)) + "".join(random.sample(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 5)).replace(" ", "")  # 生成随机字符串
        spbill_create_ip = self._CREATE_IP
        notify_url = self._NOTIFY_URL
        trade_type = "NATIVE"  # 扫码支付类型
        time_start = self._time_start
 
        params = {'appid': appid, 'mch_id': mch_id, 'nonce_str': nonce_str, 'out_trade_no': orderid, 'total_fee': goodsPrice, 'spbill_create_ip': spbill_create_ip,
                  'notify_url': notify_url, 'body': goodsName, 'trade_type': trade_type, 'time_start': time_start}
 
        # 生成签名
        ret = []
        for k in sorted(params.keys()):
            if (k != 'sign') and (k != '') and (params[k] is not None):
                ret.append('%s=%s' % (k, params[k]))
        params_str = '&'.join(ret)
        params_str = '%(params_str)s&key=%(partner_key)s' % {'params_str': params_str, 'partner_key': key}
 
        # # 这里需要设置系统编码为utf-8，否则下面md5加密会报参数错误
        # import importlib,sys 
        # importlib.reload(sys)
        # sys.setdefaultencoding('utf8')
 
        # MD5加密
        params_str = hashlib.md5(params_str.encode('utf-8')).hexdigest()
        sign = params_str.upper()
        params['sign'] = sign
 
        # 拼接参数的xml字符串
        request_xml_str = '<xml>'
        for key, value in params.items():
            if isinstance(value, str):
                request_xml_str = '%s<%s><![CDATA[%s]]></%s>' % (request_xml_str, key, value, key,)
            else:
                request_xml_str = '%s<%s>%s</%s>' % (request_xml_str, key, value, key,)
        request_xml_str = '%s</xml>' % request_xml_str
 
        # 向微信支付发出请求，并提取回传数据
        res = Request(self._UFDODER_URL, data=request_xml_str.encode("utf-8"))
        res_data = urlopen(res)  # 打开响应流
        res_read = res_data.read()  # 读取响应流中数据
        doc = xmltodict.parse(res_read)  # 数据是xml格式的，转为dict
        return_code = doc['xml']['return_code']  # 根据dict的层级，从顶层开始逐级访问提取所需内容
 
        if return_code == "SUCCESS":
            result_code = doc['xml']['result_code']
            if result_code == "SUCCESS":
                code_url = doc['xml']['code_url']
                return code_url
            else:
                err_des = doc['xml']['err_code_des']
                print("errdes===========" + err_des)
        else:
            fail_des = doc['xml']['return_msg']
            print("fail des=============" + fail_des)


