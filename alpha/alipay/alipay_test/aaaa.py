
from alipay import AliPay
import time,qrcode
 
 
alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAjhY1RMmxIvDKFT8Mvs+6yS3HXyFuhNrh2HeRJnuFSVmSEoodrH3YqGcU+HAzEar3APdKJm4yG7nqfqZ14PCD1Vq2TtJmx6EalhK3FEptG+UNZnzknalxGwE5smITxGHSZn6dFBbNhxaoEJ8/VKtu9nnZOsrvFCFU1NJhNB2scusuKtUmWeMEbj2gIrL41waCfwPkOYEiTACkjUrGqwTp7Cup3VWoB0gx6OjIbYHtVIw3rWmkA+aORNmxPgi/nXYYXKin8vZ+GwQgFfOkfivYvOmlPA03DauRLCTyKpee9skZ+rPXnY8j9F6hHso6fUKu2w9iZV4j4/PNRlAYjAO/awIDAQAB
-----END PUBLIC KEY-----'''
 
 
app_private_key_string = '''-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCSWUP/rYLYOsNH1yLbXcDgfQop9JJwPb/8BP5Ll1AES991v/XFBVZxGCSz15da0EZNd+JQJuA+xBN1cqbYB6sseN7PWberk15kYH/3oJgd3IOIR9GeGvw/viBCeaffwHA6UO/OZW3cPiS0auFbzQcQS7pZkpTnEzEnh1vuUlqlnkh/yy5Y6HvQhLq5dLhYlZVrFobxUkUTW+HLM31Aakf13RfuP6Q4nTHJPJGp0JaS4bOBttYGWsd9fyLQ/8HkJKBAG9fVqvxV5zk5RhtFHYzNfK9D0d7ZKxJlDFCDoWg2jNZIZwKSwQmUT9GmEKHOFDhFvszJJWjZPl6v1ND73eGLAgMBAAECggEAVcSK3WTKsf5+Q7QJcZZYWzfspPn4eF84DHLAtXxQILR2mYOOfZDLQCxuFhfbVBWLngsMTvz5ns86uDIhJaoY309XBR4HTj5nq1wCoxUzEQ0S6ONuLcKS4qiCL3Msty0ImKSmZcd7wv+Ic1PQDwTxhtNauvP04BeXTxs8/Ua2aSiYLKPRNXsNmW9Y4opk4lqTdfYuABmHhiYfz/owclUvHIkHFxKG47T4QYSp+qqtMgMKjymcRgPb7DwbxRf3/QvLcCtXL7QOZ8XraizhEI4n+le1Xc7+QZIlXlJ6woUFEwTKy/92vRYxlQThJSbiq/uJpEMvkL50UfiTWK6aaoA9QQKBgQD47rPhu35lzolBBKEvReSUzA1rO95VjdGAW0YgPcnP5oZTK0xUxYIKBLDyf72fprN4+YTjzN4QPozainrHFNGIpdQfQQJwfplOeKS0SuUvmNkHfNde22USqu6niOkSnycOkRBaNJjllUZbhv0tH9elbRCDVIM7BdNxYrP15cogHQKBgQCWgPYKYUq2Q7IWrKVqYY7/VoGktH8HdyjC3pxdMYNKxyPEtSETDB15oKByicGmKVbvtMxKh1Y0SS8fedgFmdEyLxxSLoZTdDPthktD6JNhrm3olI9ZOOe0pW2HkPvKJ01EN+IhYQDZ21/osoMBzjBFoxz1Vxsvy8KNogEbwjynxwKBgEEw6iTkoD5zL1i6qKejqzAYnC8IF7raEBKIVL4e0FpE6cqgHTZaHysWfWyUbYmA86Fr3xR1U3Z3mxWkjHDUj+c0Xm/s64Ggde+qAqBAuPKVGckvNYve8wJHh4aSgU9iJK1Y6ipleeEuDaXsnSMTIrts65UpLdDoPq6EBdMQ4bU1AoGAV96tR7wr+aQmetSLs0OIUI26HWaAb+RjOPrtgf+hbuw7duJlkBBXuSZN5vGEzTV/m24MhErlypsb1x21QPfgSpN0zop5RIooszngAaLtQW+sncj2tJnjtfWLsEW2q/0sQHL8JI7VB1zsbxiiIlC2oEGua5NSvSIS0cxPJ1zNOwsCgYAHy2e2xjltm+N7nB6/SiJnIxAwK1SUVyQhBgf1q/3JBC5HzgzRNJgAtYRZgHCnxeZKUuWUuSmLuQ65DLwHBc5MxCZtgEg6yiPP7z0/VXCpRjbmVhHKHTUsurqxKLwwJ61yBwbVVqD8dn7sPYvz3zmuezDrPYHD65pI/3wLLkXU6w==
-----END PRIVATE KEY-----'''
 
#注意：一个是支付宝公钥，一个是应用私钥
 
APP_ID = '2016093000632636'

 
def init_alipay_cfg():
    '''
    初始化alipay配置
    :return: alipay 对象
    '''
    alipay = AliPay(
        appid=APP_ID,
        # app_private_key_path="keys/app_private_2048.txt",
        # alipay_public_key_path="keys/alipay_public_2048.txt",
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = True  # 默认False ,若开启则使用沙盒环境的支付宝公钥
    )
    return alipay
 
 
def get_qr_code(code_url):
    '''
    生成二维码
    :return None
    '''
    #print(code_url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(code_url)  # 二维码所含信息
    img = qr.make_image()  # 生成二维码图片
    img.save(r'qr_test_ali.png')
    print('二维码保存成功！')
 
 
def preCreateOrder(subject:'order_desc' , out_trade_no:int, total_amount:(float,'eg:0.01')):
    '''
    alipay.trade.precreate统一收单线下交易预创建
    创建预付订单
    :return None：表示预付订单创建失败  [或]  code_url：二维码url
    '''
    result = init_alipay_cfg().api_alipay_trade_precreate(
        subject=subject,
        out_trade_no=out_trade_no,
        total_amount=total_amount)
    print('返回值：',result)
    code_url = result.get('qr_code')
    if not code_url:
        print(result.get('预付订单创建失败：','msg'))
        return
    else:
        get_qr_code(code_url)
        #return code_url

def prePage(subject:'order_desc' , out_trade_no:int, total_amount:(float,'eg:0.01'),return_url=None, notify_url=None):
    a = init_alipay_cfg()
    data = a.api(
        'alipay.trade.page.pay',
        subject=subject,
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        return_url=None,
        notify_url=None)
    url = a.gateway + "?" + data
    return url


def query_order(out_trade_no:int, cancel_time:int and 'secs'):
    '''
    :param out_trade_no: 商户订单号
    :return: None
    '''
    print('预付订单已创建,请在%s秒内扫码支付,过期订单将被取消！'% cancel_time)
    # check order status
    _time = 0
    for i in range(10):
        # check every 3s, and 10 times in all
 
        print("now sleep 5s")
        time.sleep(5)
 
        result = init_alipay_cfg().api_alipay_trade_query(out_trade_no=out_trade_no)
        if result.get("trade_status", "") == "TRADE_SUCCESS":
            print('订单已支付!')
            print('订单查询返回值：',result)
            break
 
        _time += 5
        if _time >= cancel_time:
            cancel_order(out_trade_no,cancel_time)
            return
 
 
def cancel_order(out_trade_no:int, cancel_time=None):
    '''
    撤销订单
    :param out_trade_no:
    :param cancel_time: 撤销前的等待时间(若未支付)，撤销后在商家中心-交易下的交易状态显示为"关闭"
    :return:
    '''
    result = init_alipay_cfg().api_alipay_trade_cancel(out_trade_no=out_trade_no)
    #print('取消订单返回值：', result)
    resp_state = result.get('msg')
    action = result.get('action')
    if resp_state=='Success':
        if action=='close':
            if cancel_time:
                print("%s秒内未支付订单，订单已被取消！" % cancel_time)
        elif action=='refund':
            print('该笔交易目前状态为：',action)
 
        return action
 
    else:
        print('请求失败：',resp_state)
        return
 
 
def need_refund(out_trade_no:str or int, refund_amount:int or float, out_request_no:str):
    '''
    退款操作
    :param out_trade_no: 商户订单号
    :param refund_amount: 退款金额，小于等于订单金额
    :param out_request_no: 商户自定义参数，用来标识该次退款请求的唯一性,可使用 out_trade_no_退款金额*100 的构造方式
    :return:
    '''
    result = init_alipay_cfg().api_alipay_trade_refund(out_trade_no=out_trade_no,
                                                       refund_amount=refund_amount,
                                                       out_request_no=out_request_no)
 
    if result["code"] == "10000":
        return result  #接口调用成功则返回result
    else:
        return result["msg"] #接口调用失败则返回原因
 
 
def refund_query(out_request_no:str, out_trade_no:str or int):
    '''
    退款查询：同一笔交易可能有多次退款操作（每次退一部分）
    :param out_request_no: 商户自定义的单次退款请求标识符
    :param out_trade_no: 商户订单号
    :return:
    '''
    result = init_alipay_cfg().api_alipay_trade_fastpay_refund_query(out_request_no, out_trade_no=out_trade_no)
 
    if result["code"] == "10000":
        return result  #接口调用成功则返回result
    else:
        return result["msg"] #接口调用失败则返回原因
 
 
if __name__ == '__main__':
    # cancel_order()
    subject = "话费余额充值"
    out_trade_no =int(time.time())
    total_amount = 10.1
    preCreateOrder(subject,out_trade_no,total_amount)
    # print(prePage(subject,out_trade_no,total_amount))
 
    query_order(out_trade_no,60)
 
    # print('5s后订单自动退款')
    # time.sleep(5)
    # print(need_refund(out_trade_no,5.00,111))
 
    # print('5s后查询退款')
    # time.sleep(5)
    # print(refund_query(out_request_no=111, out_trade_no=out_trade_no))