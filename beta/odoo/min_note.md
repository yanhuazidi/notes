[TOC]



## 资源

https://www.cnblogs.com/ygj0930/category/1459304.html





## 添加home菜单导航

系统模板	website
	控制的视图id 		website.layout

### 原结构

```xml
<xpath expr="//header//ul[@id='top_menu']/li[hasclass('divider')]" position="before">
    <t t-foreach="website.menu_id.child_id" t-as="submenu">
        <t t-call="website.submenu">
            <t t-set="item_class" t-value="'nav-item'"/>
            <t t-set="link_class" t-value="'nav-link'"/>
        </t>
    </t>
</xpath>
```



### 清除原结构：
views/template.xml

```xml
<template id="home_submenu_remove" name="Remove submenu layout"inherit_id="website.layout">
  <xpath expr="//ul[@id='top_menu']/t" position="replace">
  </xpath>
</template>
```



### 添加菜单数据

**添加菜单,执行这一处即可**

data/data.xml

```xml
<odoo>
	<record id="menu_purchase" model="website.menu">
        <field name="name">Purchase</field>名称
        <field name="url">/purchase</field>动作链接
        <field name="parent_id" ref="website.main_menu"/>
        <field name="sequence" type="int">50</field>
	</record>
</odoo>

```



### 选项进行筛选渲染
views/template.xml

```xml
<template id="my_purchase_submenu" name="Submenu layout" inherit_id="website.layout">
  <xpath expr="//ul[@id='top_menu']/li[hasclass('divider')]" position="before">
      <t t-foreach="website.menu_id.child_id.filtered(lambda r: r.url in ['/purchase','/purchase/admin'])" t-as="submenu">
        <t t-call="website.submenu" t-if="submenu.url == '/purchase' or request.env.user.has_group('my_purchase.group_purchase_admin')"/>
          <t t-set="item_class" t-value="'nav-item'"/>
          <t t-set="link_class" t-value="'nav-link'"/>
      </t>
  </xpath>
</template>
```



## 添加静态文件

```xml
<!-- 添加css文件 -->

<template id="_assets_primary_variables" inherit_id="web._assets_primary_variables">
    <xpath expr="//link[last()]" position="after">
        <link rel="stylesheet" type="text/scss" href="/om_purchase/static/src/css/om_purchase_variables.css"/>
    </xpath>
</template>

```





## 定时任务

**在odoo/addons/base/models中打开 ir_cron.py 可以看到该model**

data/data.xml

```xml
<record forcecreate="True" id="自定义" model="ir.cron">
        <field name="name">自定义</field>
        <field name="model_id" ref="model_purchase_requisition"/>
        <field name="state">code</field>
        <field name="code">model.change_the_requisition_state()</field>
        <field name="user_id" ref="base.user_root"/>
        <field name="interval_number">1</field>
        <field name="interval_type">minutes</field>
        <field name="numbercall">-1</field>
        <field name="doall" eval="False"/>
</record>
```

model_id 		后面的ref写model_+数据库里的表名

user_id   		default=lambda self: self.env.user,

state			里的code是可执行python代码，一般来说咱们用都选这个

code			里面是当前模块下的某个函数

interval_number	是时间

interval_type		是时间类型	

default='months'

-  	'days': lambda interval: relativedelta(days=interval),
- ​    'hours': lambda interval: relativedelta(hours=interval),
- ​    'weeks': lambda interval: relativedelta(days=7*interval),
- ​    'months': lambda interval: relativedelta(months=interval),
- ​    'minutes': lambda interval: relativedelta(minutes=interval),

numbercall	是执行次数，-1为无限次数。

doall			是服务器重启后是否立即执行一次

priority  作业的优先级，作为整数:0表示更高的优先级，10表示更低的优先级。default=5

nextcall 



### 或

models/model.py

```python
self.env['ir.cron'].sudo().create({
                'name': self.name,
                'user_id': self.env.uid,
                'model': self._name,
			   'state': 'code',
			   'code' :model.change_the_requisition_state(),
               # 'function': '_send_mail',
                'active': True,
                'priority': 0,
                'numbercall': 1,
                'nextcall': (datetime.datetime.utcnow() + datetime.timedelta(seconds=3)).strftime(DATETIME_FORMAT),
                'interval_type': 'minutes',
                'args': repr([res_id, force_send, raise_exception, email_values])
            })
```



## 返回错误

### JSON

```python
error_code = {
    -1: u'服务器内部错误',
    0: u'接口调用成功',
    403: u'禁止访问',
    405: u'错误的请求类型',
    501: u'数据库错误',
    502: u'并发异常，请重试',
    600: u'缺少参数',
    601: u'无权操作:缺少 token',
    602: u'签名错误',
    700: u'暂无数据',
    701: u'该功能暂未开通',
    702: u'资源余额不足',
    901: u'登录超时',
    300: u'缺少{}参数',
    400: u'域名错误',
    401: u'该域名已删除',
    402: u'该域名已禁用',
    404: u'暂无数据',
    10000: u'微信用户未注册'
}
http.request.make_response(json.dumps({'code': 404, 'msg': error_code[404]}))
```



## 时间日期转换

```python
#postgresql 日期时间
print(purchase_order.quotation_datatime,type(purchase_order.quotation_datatime))
#<class 'datetime.datetime'>
if  time.time() - time.mktime(purchase_order.quotation_datatime.timetuple()) < 60*60*24:
```


