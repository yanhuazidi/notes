[TOC]



## 重定向

1. local_redirect

   ```python
   from odoo import http
   http.local_redirect('/web', query=request.params, keep_hash=True)
   ```

   `keep_hash=True` 会调用  `redirect_with_hash`

2. redirect_with_hash

   ```python
   from odoo import http
   http.redirect_with_hash(redirect)
   ```

3. werkzeug.utils.redirec

   ```python
   import werkzeug
   werkzeug.utils.redirect('/web/login', 303)
   ```

   

### ensure_db

ensure_db()，就是一些确定当前用户是否选择db，没有就跳转到/web/database/selector, 或者/web/database/create，由于上面我说了只使用一个db，因为其他情况不想多讲，所以在ensure_db中，默认替我们选择好了唯一一个db，并且存在request.session中了。

```python
from odoo.addons.web.controllers.main import ensure_db
```



## 请求参数

```python
request.params.get()
request.params['login_success'] = False
values = request.params.copy()
```



## 请求方法

```python
request.httprequest.method == 'GET' 
```



## 超级用户id

```python
odoo.SUPERUSER_ID
```



## 验证登录

```python
uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
```



## session

```python
request.session.get('auth_login')
request.session['auth_login'] ='success'
```



## cookie

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


#读取
request.httprequest.cookies.get('wei')
```





## 设置响应头

```python
response = request.render('web.login', values)
response.headers['X-Frame-Options'] = 'DENY'
return response
```



## 返回json

```python
http.request.make_response(json.dumps({'code': 404, 'msg': error_code[404]}))
```

