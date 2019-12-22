odoo.define("website_payment_weixin.jsapi", function (require) {
    "use strict";

    function jsApiCall() {
        var out_trade_no = document.getElementById("out_trade_no").value
        var appId = document.getElementsByName("appId").value
        var timeStamp = document.getElementsByName("timeStamp").value
        var nonceStr = document.getElementsByName("nonceStr").value
        var prepay_id = document.getElementsByName("prepay_id").value
        var paySign = document.getElementsByName("paySign").value

        WeixinJSBridge.invoke(
            'getBrandWCPayRequest', {
                "appId": appId,     //公众号名称，由商户传入
                "timeStamp": timeStamp,         //时间戳，自1970年以来的秒数
                "nonceStr": nonceStr, //随机串
                "package": "prepay_id=" + prepay_id + "",
                "signType": "MD5",         //微信签名方式：
                "paySign": paySign//微信签名
            },
            function (res) {
                if (res.err_msg == "get_brand_wcpay_request:ok") {
                    // 使用以上方式判断前端返回,微信团队郑重提示：res.err_msg将在用户支付成功后返回    ok，但并不保证它绝对可靠。
                    window.location = '/shop/payment/checkout?order_id=%s' % (out_trade_no);

                }
            }
        );
    }

    function callpay() {
        console.log('1111111111111')
        if (typeof WeixinJSBridge == "undefined") {
            if (document.addEventListener) {
                document.addEventListener('WeixinJSBridgeReady', jsApiCall, false);
            } else if (document.attachEvent) {
                document.attachEvent('WeixinJSBridgeReady', jsApiCall);
                document.attachEvent('onWeixinJSBridgeReady', jsApiCall);
            }
        } else {
            jsApiCall();
        }
    }


})

