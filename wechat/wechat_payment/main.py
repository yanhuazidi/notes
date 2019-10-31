# -*- coding: utf-8 -*-

#原文：https://blog.csdn.net/Great_Zhou/article/details/83063466 


from wechat_payment import WX_PayToolUtil
import json
 
def WxPay(request):
    # 微信
    if request.is_secure():
        notify_url = "https://%s/xxxx/xxxx/" % request.get_host()  # 获取当前域名
    else:
        notify_url = "http://%s/xxxx/xxxx/" % request.get_host()
    wx_paytoolutil = WX_PayToolUtil(
        APP_ID='',   # 公众账号appid
        MCH_ID='',  # 商户号
        API_KEY='',  # key
        NOTIFY_URL=notify_url # 回调地址
    )
    data = request.GET
    money = data.get('money ')  # 获取前台传的订单金额和订单号
    total = data.get('total ') 
    code_url = wx_paytoolutil.getPayUrl(
        goodsName='',  # 微信 body,例如,小米科技有限公司 
        orderid=total,
        goodsPrice=money ,
    )
    return json.dumps({"code_url": code_url})  # 把url传给前台,前台生成二维码

def WxStatus(request):
    # 支付轮询
    data = request.GET
    total = data.get('total_key') # 获取到前台的订单号
    if PayOrder.objects.filter(order_no=total ).count() == 1:  # 查询数据库
        return json.dumps({"STATUS": "SUCCESS"})
    else:
        return json.dumps({"STATUS": "FAIL"})


