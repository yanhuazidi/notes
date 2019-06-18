

[TOC]



##  控制器环境

**from odoo import http **

### http.Controller

控制器类必须直接或间接继承这个类

```python
class OmPurchase(http.Controller):
    @http.route('/', type='http', auth='public', website=True)
    def purchase_requisition_details(self,purchase_requisition_id,**kw):
        pass
```



## 路由

### http.route(route=None, **kw) 装饰器

可以将对应方法装饰为处理对应的http请求，该方法须是Controller的子类

|  参数   |       取值       | 详解                                                         |
| :-----: | :--------------: | :----------------------------------------------------------- |
|  route  |                  | 字符串或数组，决定哪个http请求匹配所装饰的方法，可以是单个字符串、或多个字符串的数组 |
|  type   |    http或json    | 请求的类型，可以是http或json                                 |
|  auth   |       user       | 必须是认证的用户，该请求基于已认证的用户                     |
|         |      public      | 当不通过认证访问时使用公用的认证                             |
|         |       none       | 相应的方法总是可用，一般用于框架和认证模块，对应请求没有办法访问数据库或指向数据库的设置 |
| methods | ["GET","POST",,] | 这个请求所应用的一系列http方法，如果没指定则是所有方法       |
|  cors   |                  | 跨域资源cors参数                                             |
|  csrf   |     boolean      | 是否开启CSRF保护，默认True<br/>1.如果表单是用python代码生成的，可通过request.csrf_token() 获取csrf<br/>2.如果表单是用javascript生成的，CSRF token会自动被添加到QWEB环境变量中，通过require('web.core').csrf_token使用<br/>3.如果终端可从其他地方以api或webhook形式调用，需要将对应的csrf禁用，此时最好用其他方式进行验证 |
| website |     boolean      |                                                              |

```python
@http.route(['/purchase',
                '/purchase/state/<state>',#采购协议状态筛选
                '/purchase/datetame/<datetame_category>/<sort_way>' #采购协议日期排序
            ],type='http', auth='public', website=TruAe)
```

在xml文件from中添加

```xml
<input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
```





## 请求

### http.request	请求对象

请求对象在收到请求时自动设置到odoo.http.request

class odoo.http.WebRequest(httprequest)   所有odoo WEB请求的父类，一般用于进行请求对象的初始化

请求对象属性和方法

|         属性和方法          | 详解                                                         |
| :-------------------------: | ------------------------------------------------------------ |
|         httprequest         | 原始的werkzeug.wrappers.Request对象                          |
|           params            | 请求参数的映射字典                                           |
|             cr              | 当前方法调用的初始游标，当使用none的认证方式时读取游标会报错 |
|           context           | 当前请求的上下文键值映射                                     |
|             env             | 绑定到当前请求的环境                                         |
|           session           | 储存当前请求session数据的OpenERPSession                      |
|            debug            | 指定当前请求是否是debug模式                                  |
|             db              | 当前请求所关联的数据库，当使用none认证时为None               |
| csrf_token(time_limit=3600) | 为该请求生成并返回一个token（参数以秒计算，默认1小时，如果传None表示与当前用户session时间相同 |



### request

```json
{
    "httprequest": "< Request 'http: //localhost:8069/purchase/line_ids/7' [GET] >",
 	"httpresponse": "None",
    "disable_db": False,
    "endpoint": "< odoo.http.EndPoint object at 0x0D3149D0 >" ,
    "endpoint_arguments": { "purchase_requisition_id": 7 },
    "auth_method": "public",
    "_cr": < odoo.sql_db.Cursor object at 0x06C979F0 > ,
    "_uid": 2,
    "_context": { "map_website_id": 1,
                "route_map_website_id": 1,
                "route_start_partner_id": 3,
                "lang": "zh_CN",
                "tz": "Asia/Shanghai",
                "uid": 2,
                "website_id": 1 },
    "_env": < odoo.api.Environment object at 0x06C97C10 > ,
    "_failed": None,
    "session": < OpenERPSession { "db": "erp", 
                                "uid": 2, 
                                "login": "admin", 
                             	"session_token":
						"aada24ea164989699a6b084dfdafd21ba2796cadb103f380d70b6f6bf7be3104", 
                                 "context": { "map_website_id": 1, 
                                             "route_map_website_id": 1, 
                                             "route_start_partner_id": 3, 
                                             "lang": "zh_CN", 
                                             "tz": "Asia/Shanghai", 
                                             "uid": 2 },
                                 "geoip": {}, 
                                 "sale_order_id": 13, 
                                 "my_purchases_history": [18, 17, 1] } > ,
    "params": OrderedDict(),
    "routing_iteration": 2,
    "is_frontend": True,
    "is_frontend_multilang": True,
    "redirect": < function IrHttp._dispatch. < locals > . < lambda > at 0x0C6E2738 > ,
    "website": website(1, ),
    "lang": "zh_CN",
    "rerouting": ["/zh_CN/purchase/line_ids/7", "/purchase/line_ids/7"]
    }

```

### httprequest

```json
{"environ": {
    "wsgi.version": (1, 0),
    "wsgi.url_scheme": "http",
    "wsgi.input": < _io.BufferedReader name = 1096 > ,
    "wsgi.errors": < _io.TextIOWrapper name = '<stderr>' mode = 'w' encoding = 'utf - 8' > ,
    "wsgi.multithread": True,
    "wsgi.multiprocess": False,
    "wsgi.run_once": False,
    "werkzeug.server.shutdown": < function WSGIRequestHandler.make_environ. < locals >.shutdown_server at 0x0D06E4F8 > ,
    "SERVER_SOFTWARE": "Werkzeug/0.11.15",
    "REQUEST_METHOD": "GET",
    "SCRIPT_NAME": "",
    "PATH_INFO": "/purchase/line_ids/7",
    "QUERY_STRING": "",
    "CONTENT_TYPE": "",
    "CONTENT_LENGTH": "",
    "REMOTE_ADDR": "127.0.0.1",
    "REMOTE_PORT": 51217,
    "SERVER_NAME": "0.0.0.0",
    "SERVER_PORT": "8069",
    "SERVER_PROTOCOL": "HTTP/1.1",
    "HTTP_HOST": "localhost:8069",
    "HTTP_CONNECTION": "keep-alive",
    "HTTP_UPGRADE_INSECURE_REQUESTS": "1",
    "HTTP_USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "HTTP_ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "HTTP_REFERER": "http://localhost:8069/zh_CN/purchase",
    "HTTP_ACCEPT_ENCODING": "gzip, deflate, br",
    "HTTP_ACCEPT_LANGUAGE": "zh-CN,zh;q=0.9",
    "HTTP_COOKIE": "Hm_lvt_06fb34acf0b36e035e966786befa7645=1559379571,1559523094,1559611520,1559693855; session_id=ad2521154a7ff01919c0682c78cb5e82b135c07b;
frontend_lang=zh_CN; 
im_livechat_history=[" / my / purchase / 18 "," / my / home "," / my / purchase ? filterby = done "," / my / purchase ? filterby = all "," / my / purchase / page / 1 "," / my / purchase / page / 3 "," / "," / purchase "," / my / purchase "," / web / login ? redirect = http % 3 A % 2 F % 2 Flocalhost % 3 A8069 % 2 Fmy "," / my "," / web / login "," / zh_CN / purchase "," / zh_CN / "," / zh_CN / purchase / line_ids / 7 "];
Hm_lpvt_06fb34acf0b36e035e966786befa7645=1559727102",
 	"werkzeug.request": < Request"http://localhost:8069/purchase/line_ids/7" [GET] >
},

"shallow": False,
"app": < odoo.http.Root object at 0x060B2850 > ,
"parameter_storage_class": < class "werkzeug.datastructures.ImmutableOrderedMultiDict" > ,
"args": ImmutableOrderedMultiDict([]),

"headers": EnvironHeaders([("Content-Type", ""), ("Content-Length", ""),("Host","localhost:8069"),("Connection", "keep-alive"), ("Upgrade-Insecure-Requests", "1"), ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"), ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"),("Referer", "http://localhost:8069/zh_CN/purchase"), ("Accept-Encoding", "gzip, deflate, br"), ("Accept-Language", "zh-CN,zh;q=0.9"),("Cookie","Hm_lvt_06fb34acf0b36e035e966786befa7645=1559379571,1559523094,1559611520,1559693855; session_id=ad2521154a7ff01919c0682c78cb5e82b135c07b; frontend_lang=zh_CN;im_livechat_history=[" / my / purchase / 18 "," / my / home "," / my / purchase ? filterby = done "," / my / purchase ? filterby = all "," / my / purchase / page / 1 "," / my / purchase / page / 3 "," / "," / purchase "," / my / purchase "," / web / login ? redirect = http % 3 A % 2 F % 2 Flocalhost % 3 A8069 % 2 Fmy "," / my "," / web / login "," / zh_CN / purchase "," / zh_CN / "," / zh_CN / purchase / line_ids / 7 "]; Hm_lpvt_06fb34acf0b36e035e966786befa7645=1559727102")]),

"cookies": { "Hm_lvt_06fb34acf0b36e035e966786befa7645":
            "1559379571,1559523094,1559611520,1559693855", 
            "session_id": "ad2521154a7ff01919c0682c78cb5e82b135c07b",
    		"frontend_lang": "zh_CN",
    		"im_livechat_history": [" / my / purchase / 18 ",
                " / my / home ",
                " / my / purchase ? filterby = done ",
                " / my / purchase ? filterby = all ",
                " / my / purchase / page / 1 ",
                " / my / purchase / page / 3 ",
                " / ",
                " / purchase ",
                " / my / purchase ",
                " / web / login ? redirect = http % 3 A % 2 F % 2 Flocalhost % 3 A8069 % 2 Fmy ",
                " / my ",
                " / web / login ",
                " / zh_CN / purchase ",
                " / zh_CN / ",
                " / zh_CN / purchase / line_ids / 7 "],
    		"Hm_lpvt_06fb34acf0b36e035e966786befa7645": "1559727102" 
           },
"session": < OpenERPSession { "db": "erp",
                             "uid": 2,
                             "login": "admin", 
                             "session_token": "aada24ea164989699a6b084dfdafd21ba2796cadb103f380d70b6f6bf7be3104", 
                             "context": { "map_website_id": 1, 
                                         "route_map_website_id": 1, 
                                         "route_start_partner_id": 3, 
                                         "lang": "zh_CN", 
                                         "tz": "Asia/Shanghai", 
                                         "uid": 2 }, 
                             "geoip": {}, 
                             "sale_order_id": 13, 
                             "my_purchases_history": [18, 17, 1] } > ,
    "_parsed_content_type": ('', {}),
    "stream": < _io.BytesIO object at 0x02C67C00 > ,
    "form": ImmutableOrderedMultiDict([]),
    "files": ImmutableOrderedMultiDict([]),
    "path": "/purchase/line_ids/7",
    "url": "http://localhost:8069/purchase/line_ids/7"
}
```

### env

```json
{'cr': <odoo.sql_db.Cursor object at 0x0BF9BF90>, 
 'uid': 2, 
 'context': {'map_website_id': 1, 
         'route_map_website_id': 1, 
         'route_start_partner_id': 3, 
         'lang': 'zh_CN', 
         'tz': 'Asia/Shanghai', 
         'uid': 2, 
         'website_id': 1}, 
'args': (<odoo.sql_db.Cursor object at 0x0BF9BF90>, 2, 
         {'map_website_id': 1, 
         'route_map_website_id': 1, 
         'route_start_partner_id': 3, 
         'lang': 'zh_CN', 
         'tz': 'Asia/Shanghai', 
         'uid': 2, 
         'website_id': 1}), 
'registry': <odoo.modules.registry.Registry object at 0x06B2E110>, 
'cache': <odoo.api.Cache object at 0x0BF9BC50>, 
'_protected': <odoo.tools.misc.StackMap object at 0x0BF9B650>, 
'dirty': defaultdict(<class 'set'>, {}), 
'all': <odoo.api.Environments object at 0x0BF9BBB0>
}
```



### cookies

#### 设置

```python
#响应模板对象设置
response =  request.render("om_purchase.purchase_requisition_list",
        {'purchaseList':purchase_requisition_List,
        'breadcrumbsList':breadcrumbsList
        })
response.set_cookie('wei','tianhua')
return response
#重定向设置
redirect = werkzeug.utils.redirect(r or ('/%s' % lang), 303)
redirect.set_cookie('frontend_lang', lang)
return redirect
#响应对象设置
response = Response(data, headers=headers)
if cookies:
	for k, v in cookies.items():
		response.set_cookie(k, v)
return response
```

#### 读取

```python
request.httprequest.cookies.get('wei')
```



### session设置-读取

```python
request.session['key']=value
```



## 响应

### request.render(template, qcontext=None, lazy=True, **kw)

渲染qweb模板，在调度完成后会对给定的模板进行渲染：

参数：
template (basestring) -- 用于渲染的模板
qcontext (dict) -- 用于渲染的上下文环境
lazy (bool) -- 渲染动作是否应该拖延到最后执行
kw -- 转发到werkzeug响应对象



## 图片响应

### 数据库二进制图片

Controller.py

```python
import base64
from odoo.tools import image_resize_image
from odoo.addons.web.controllers.main import Binary

def resize_to_48(b64source):
    '''图片处理'''
    if not b64source:
        b64source = base64.b64encode(Binary().placeholder())
    return image_resize_image(b64source, size=(48, 48))

return request.render("om_purchase.purchase_requisition_details",
        {'resize_to_48':resize_to_48})


```

templates.xml

```xml
<img t-att-src="image_data_uri(resize_to_48(product.product_id.image))" alt="Product"/>
image_data_uri 为渲染模型函数
product.product_id.image 为fields.Binary()字段
```



