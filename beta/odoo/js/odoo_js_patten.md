



[TOC]



## 静态文件导入

在odoo中，最重要的包在`addons/web/views/webclient_templates.xml`文件中定义。

相关静态文件的组织和导入次序可以自行了解

1. 需要对前端所有页面可见的静态文件导入

   ```xml
   <template id="自定义唯一" inherit_id="web.assets_common" name="自定义">
        <xpath expr="." position="inside">
        <!-- 或者<xpath expr="//script[last()]" position="after"> -->
   		<script type="text/javascript" src="/模块名/static/src/js/js.js"></script>
   		<link rel="stylesheet" type="text/css"href="/模块名/static/src/css/css.css"/>
     </xpath>
   </template>
   ```
   
2. 需要对前端特别是后台/操作管理器/视图页面可见的静态文件导入

   ```xml
   <template id="自定义唯一" inherit_id="web.assets_backend" name="自定义">
        <xpath expr="." position="inside">
        <!-- 或者<xpath expr="//script[last()]" position="after"> -->
   		<script type="text/javascript" src="/模块名/static/src/js/js.js"></script>
   		<link rel="stylesheet" type="text/css"href="/模块名/static/src/css/css.css"/>
        </xpath>
   </template>
   ```

3. 需要对前端公共网站的内容：电子商务、论坛、博客、事件管理……可见的静态文件导入

   ```xml
   <template id="自定义唯一" inherit_id="web.assets_frontend" name="自定义">
        <xpath expr="." position="inside">
        <!-- 或者<xpath expr="//script[last()]" position="after"> -->
   		<script type="text/javascript" src="/模块名/static/src/js/js.js"></script>
   		<link rel="stylesheet" type="text/css"href="/模块名/static/src/css/css.css"/>
        </xpath>
   </template>
   ```

如果不清楚前端页面属于后台还是前台，可以在浏览器调试中看js文件是``web.assets_frontend`还是`web.assets_backend`

最好不要写入`web.assets_common`



## 定义javascript模块

```javascript

// in file a.js
odoo.define('module.A', function (require) {//'module.A'为此js模块名,必填并保证唯一
    "use strict";//严格模式,必填
    var A = ...;//自定义的执行代码
    return A;//模块返回值,用于导入此模块的模块接收调用
});
// in file b.js
odoo.define('module.B', function (require) {
    "use strict";
    var A = require('module.A');//依赖项
    var B = ...; // something that involves A
    return B;
});

//定义模块的另一种方法是在第二个参数中显式地给出依赖项列表。
odoo.define('module.Something', ['module.A', 'module.B'], function (require) {
    "use strict";
    var A = require('module.A');
    var B = require('module.B');
    // some code
});
```

### 定义模块

`odoo.define`方法有三个参数：

- 模块名称：javascript模块的名称。它是一个不能重名的字符串。最好是在odoo模块的名字后面加上一个具体的描述。如果名称不唯一，将引发异常并显示在控制台中。
- 依赖项：第二个参数是可选的。如果给定，它应该是一个字符串列表，每个字符串对应一个JavaScript模块。这描述了在执行模块之前需要加载的依赖项。如果这里没有显式地给出依赖项，那么模块系统将通过对其调用ToString从函数中提取它们，然后使用`regexp`查找所有`Require`语句。
- 最后一个参数是定义模块的函数。它的返回值是模块的值，可以传递给其他需要它的模块。

如果发生错误，将在控制台中记录（在调试模式下）：

- `Missing dependencies`: 报错模块不能加载。可能是`javascript`文件不存在或模块名称错误。
- `Failed modules`: 检测到一个`javascript`代码错误
- `Rejected modules`: 异步模块加载失败。它（及其相关模块）未加载。
- `Rejected linked modules`: 异步模块连接失败。
- `Non loaded modules`: 依赖模块不存在或报错的模块



## 保证js模块在DOM加载完成之后再执行

在自定义代码执行之前加上这行代码即可

```javascript
require('web.dom_ready');
```



## AJAX

### 访问模型

本质是`ajax.jsonRpc()`方法封装

`addons\web\static\src\js\core\rpc.js`

```javascript
var rpc = require('web.rpc');
//直接查询模型字段
rpc.query({
     model: 'barcode.nomenclature',//模型名
     method: 'search_read',//等同 search（）
     domain?: [['barcode_nomenclature_id', '=', self.nomenclature.id]],//筛选域
     fields?: ['name', 'sequence', 'type', 'encoding', 'pattern', 'alias'],//查询参数
     groupBy?: ['sequence'];
     limit?: 5;
     offset?: 3;
     orderBy?: [{name: 'yop', asc: true}, {name: 'aa', desc: false}];
     //args: [['barcode_nomenclature_id', '=', self.nomenclature.id]],//筛选域
           //['name', 'sequence', 'type', 'encoding', 'pattern', 'alias'],//查询参数
     //kwargs: {},
}).then(function(rules){//成功方法
    rules = rules.sort(function(a, b){ return a.sequence - b.sequence; });
);
    
    
//调用模型方法
rpc.query({
     model: 'barcode.nomenclature',//模型名
     method: '模型方法名',//模型方法
     args: [],//位置参数
     kwargs: {},//关键字参数
}).then(function(rules){//成功方法
    rules = rules.sort(function(a, b){ return a.sequence - b.sequence; });
);
    
```



### json请求控制器

`addons\web\static\src\js\core\ajax.js`

```javascript
var ajax = require('web.ajax');
ajax.jsonRpc('/mailing/blacklist/check', 'call', {'email': email})
.then(function (result) {})//成功函数
.fail(function (error) {});//失败函数
```

控制器

```python
@http.route('/mailing/blacklist/check', type='json', auth='none')
def blacklist_check(self, email):
    return 'error'
```





## 前端cookies操作

```javascript
var utils = require('web.utils');//导入库
var cookie = utils.get_cookie('im_livechat_session');//获取
utils.set_cookie('im_livechat_session', "", -1); //删除
utils.set_cookie('im_livechat_session', JSON.stringify(data, 60*60);//设置
```



## 翻译

```javascript
var core    = require('web.core');
var _t      = core._t;
message: _t('Handling transaction...'),
```



## token

```javascript
var csrf_token = $('meta[name=csrf-token]').attr('content');
//or
require('web.core').csrf_token
```

