[TOC]



## URL:
​    结构:  协议 + 主机地址 + 目录结构 + 文件名称

**完整结构**: `<scheme>://<user>:<pwd>@<host>:<port>/<path>;<params>?<query>#<frag>`

- `scheme`  方案、协议，以哪种方式获取服务器资源，不区分大小写

  | 常见协议 | 默认端口号 |       应用       |
  | :------: | :--------: | :--------------: |
  |   http   |     80     |    超文本传输    |
  |  https   |    443     | 加密的超文本传输 |
  |   ftp    |     21     |     文件传输     |
  |   SSH    |     22     |  安全的远程登录  |
  |  TELNet  |     23     |     远程登录     |
  |   SMTP   |     25     |   邮件传输协议   |
  |   POP3   |    110     |     邮件接收     |
  |   DNS    |     53     |     域名解析     |

- `user`    :   用户名

- `pwd`     :   密码

- `host`   :   主机名      IP地址

- `port`    :   端口号

- `path`    :   资源在服务器上存放的位置

- `params`  :   参数，服务器端使用  session  cookie

- `query`   :   查询字符串

- `frag`    :   锚点



## AJAX核心对象(XMLHttpRequeset)

### XMLHttpRequeset简介

异步对象, 简称 xhr

为 window属性   支持`XMLHttpRequeset`的浏览器，`window.XMLHttpRequeset`为`true`
作用: 代替浏览器向服务器发送异步的请求并接收响应



### 创建异步对象

主流的异步对象是 `XMLHttpRequeset` 类型的，并且所有的主流浏览器(IE7+,Chrome,Firefox,Safari,Opera)也都支持`XMLHttpRequeset`.但在IE低版本浏览器(IE7以及以下)，就不支持`XHLHttpRequeset`，需要使用 `ActiveXObject()` 来创建异步对象

**如果支持 XMLHttpRequeset**

```javascript
var xhr = new XMLHttpRequeset();
```

**如果不支持 XMLHttpRequeset**

```javascript
var xhr = new ActiveXObject('Microsoft.XMLHTTP');
```



### xhr 成员

**方法 - open()        xhr.open()**

作用 : 创建请求
语法: `open(method,url,async)`
参数:

- `method` : 请求方式，取值 'get' 或 'post'
- `url` : 请求地址，字符串
- `async` : Asynchronous 是否采用异步的方式发送请求
  取值: `true`(异步) | `false`(同步)

**属性 - readyState    xhr.readyState**

作用: 表示请求的状态，通过不同的请求状态值来表示xhr与服务器的交互情况,由 0 - 4 共5个值表示5个不同的状态
            0 : 请求尚未初始化(未创建请求)
            1 : 已经与服务器建立连接了
            2 : 服务器端已经接收请求
            3 : 请求正在处理中
            4 : 响应已经完成

**属性 - status    xhr.status**

作用 : 表示的是服务器端的响应状态码
        200 : 表示服务器已经正确处理请求并给出响应
        404 : 请求资源不存在
        500 : 服务器内部错误
        ......

**属性 - responseText      xhr.responseText**

作用: 接收服务器端响应回来的数据



**事件 - onreadystatechange**

作用: 每当 xhr 的 `readyState`值发生改变的时候都要触发的行为操作 - 回调函数
关注:

- xhr 的 `readyState` 是否为 4
- xhr 的` status` 是否为 200

如果以上两点同时满足的话，则接收响应数据(responseText)

```javascript
xhr.onreadystatechange = function(){
   if(xhr.readyState==4&&xhr.status==200){
       console.log(xhr.responseText);
   }
}
```

**方法 - send()**

作用 : 通知 xhr 开始向服务器发送请求
语法 :
        `xhr.send(body)`

- get : body的值为 null
          xhr.send(null)
- post : body的值为具体的请求提交数据
          xhr.send('请求数据')



## AJAX的操作步骤

### GET 请求

  1.创建 xhr 对象
  2.创建请求 - open()
      `xhr.open('get','/server',true);`
  3.设置回调函数 - `onreadystatechange`
      判断状态,接收响应,业务处理
  4.发送请求 - `send(null)`

```javascript
function createXhr(){
          if(window.XMLHttpRequest){
              var xhr = new XMLHttpRequest();
          }else {
              var xhr = new ActiveXObject("Microsoft.XMLHTTP");
          }
          return xhr
}
function btnAjax() {
          var xhr = createXhr();
          xhr.open('get','/server',true);
          xhr.onreadystatechange = function () {
              if(xhr.readyState==4 && xhr.status==200){
                  document.getElementById('show').innerHTML=xhr.responseText
              }
          }
          xhr.send(null);
}
```

### post 请求

1. 请求数据要放在send()提交

   ```javascript
   var xhr = createXhr();
       xhr.open('post','url',true);
       xhr.onreadystatechange = function(){
   }
   xhr.send("uname=wwww&uage=35");
   ```

2. `Content-Type` 的问题

   AJAX的post请求，默认会将 Content-Type消息头的值更改为"text/plain"，所以导致提交参数无法获取

   解决方案: 将`Content-Type`的值更改为`application/x-www-form-urlencoded`即可

   在创建 xhr之后，发送请求之前执行:

   ```javascript
   xhr.setRequestHeader("Content-Type",'application/x-www-form-urlencoded')
   ```



## JSON 

### JSON介绍
​	JSON : JavaScript Object Notation(JS对象表现形式)
​	将复杂结构的字符串转换成为JS对象的表现形式，方便前端解析

### JSON的表现

1. JSON表示单个对象

   1. 使用{}表示一个对象
   2. 在{}中使用 key:value 的形式来表示属性(数据)
   3. key必须使用""引起来
   4. value如果是字符串的话，也必须使用""引起来
   5. 多对 key:value 之间用 , 隔开

2. 使用 JSON表示一个数组

   1. 使用 [] 来表示一个数组

   2. 数组中允许包含若干字符串 或 JS 对象

      1. 使用 JSON 数组来表示若干字符串

         ```json
         var arr = ["String","String1","String2"];
         ```

      2. 使用 JSON 数组来表示若干对象

         ```json
         var arr = [
         {
              "name":"1",
              "age": 3,
              "gender" : ""
         },{
              "name":"2",
              "age": 3,
              "gender":""
         },{
              "name":"3",
              "age":3,
              "gender":""
         }]
         ```

         

### JSON转换

`JSON.parse(text[, reviver])`	
用于将一个 JSON 字符串转换为 JavaScript 对象。
参数说明：

- `text`:必需， 一个有效的 JSON 字符串。既然是字符串就是用引号包裹起来的，有json格式的字符串
- `reviver`: 可选，一个转换结果的函数， 将为对象的每个成员调用此函数。

返回值：
        返回给定 JSON 字符串转换后的对象。

`JSON.stringify(value[, replacer[, space]])`
用于将 JavaScript 值转换为 JSON 字符串。
参数说明：

- `value`:必需， 要转换的 JavaScript 值（通常为对象或数组）

- `replacer`:可选。用于转换结果的函数或数组。

  如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。

  如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。

- `space`:可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。

返回值：
    返回包含 JSON 文本的字符串。



**JSON - 转换为 JavaScript 对象**

JSON 文本格式在语法上与创建 JavaScript 对象的代码相同。

由于这种相似性，无需解析器，JavaScript 程序能够使用内建的 eval() 函数，用 JSON 数据来生成原生的 JavaScript 对象。



## 使用 jQuery 操作 AJAX

1. `$obj.load(url[,data][,callback])`
   作用 : 远程加载数据并加载到$obj元素中

   参数:

   - `url` ： 远程请求的地址

   - `data`: 要传递的参数

     字符串拼参数，采用 get 方式请求
     ON 对象，采用 post 方式请求

   - `callback` :请求和响应完成之后的回调函数

     ```javascript
     function(resText,statusText){
     	resText:响应回来的数据
     	statusText:响应回来的状态文本
     }
     ```

2. `$.get(url[,data][,callback][,type])`

   作用 : 使用 get 方式异步的向服务器发送请求

   参数:

   - `url` ： 远程请求的地址  

   - `data`: 要传递的参数，支持拼接字符串和JSON

   - `callback` :请求和响应完成之后的回调函数

     ```javascript
     function(resText,statusText){
             resText:响应回来的数据
             statusText:响应回来的状态文本
     }
     ```

   - `type` : 响应回来的数据的数据类型(把响应回来的数据转换为指定数据类型)

     1. `html` : 响应回来的文本当成HTML文本处理
     2. `text` ： 响应回来的文本当成text文本处理
     3. `json` : 响应回来的文本当成JSON进行处理
     4. `script`: 响应回来的文本当成JS代码片段执行

3. `$.post(url[,data][,callback][,type])`

   作用 : 使用 post 方式异步的向服务器发送请求

4. `$.ajax()`

   语法: `$.ajax({})`

   {} : 请求的相关参数

   1. `url` : 字符串 ,请求地址

   2. `type` : 字符串，表示请求方式， get | post

   3. `data` : 传递到服务器的参数

      1. 可以是字符串拼接
      2. JSON

   4. `dataType` : 字符串，表示服务器端响应回来的数据的格式

      1. `html`
      2. `xml`
      3. `text`
      4. `script`
      5. `json`
      6. `jsonp`  跨域时使用

   5. `async` : 布尔值，表示是否采用异步方式

      - `ture` : 采用异步
      - `false` : 采用同步

   6. `success`: 回调函数，请求和响应成功后的操作

      function(data){
                      data 表示是响应回来的数据
       }

   7. `error`: 回调函数，请求或响应失败时回来执行的操作

      function(error){
                      error 表示错误的数据
      }

   8. `beforeSend` : 回调函数，发送ajax请求之前要执行的操作

      如果 `return false` 则终止发送请求



## 跨域( Cross Domain)

### 什么是跨域
HTTP协议中有一种 "同源策略"
    同源 : 在多个地址中，相同协议，相同域名，相同端口 被视为"同源"
    在 HTTP 中，必须是同源地址才能相互发送请求，非同源的请求会被拒绝(`<script>`和`<img>`例外)

localhost(本地地址，不走网络) 和 127.0.0.1(本地网络回环地址,要走网络) 是不同的地址

跨域: 非同源的网页，相互发送请求的操作就是跨域操作



### 解决方案

通过 `<script>` 向服务器端发送请求

由服务器资源指定前端页面的哪个方法来执行响应的数据

实现步骤：

1. 前端中想实现跨域操作时。动态创建 script 标记
    `var script = document.createElement("script")`
   
2. 为script 元素设置相应的属性值

   1. 设置 type 的值为 `text/Javascript`
   2. 设置 src 的值为 请求地址

3. 发送请求

   将创建好的 script 元素追加到网页中即可
   `var body = document.getElementsByTagName("body")[0]`
   `body.append(script)`

4. 在前端，创建处理数据的响应方法

   function process(data){
               ...............
           }

5. 在服务器端，响应数据

   特点: 指定调用前端的哪个处理方法
           def xxx():
               return "process('xxxx')"



### jQuery 的跨域

jsonp : Json with padding

前端


```javascript
$.ajax({
        url:'xxxx',
        type:"get/post",
        dataType:"jsonp" //指定为跨域访问
        success:function(data){响应成功后的处理}
        jsonp: "callback", //定义callback的参数名
        jsonpCallback : "xxx" //定义 jsonp 的回调函数名
});

```
 服务器：

```javascript
@app.route('/03-jq-cross')
def jq_cross():
     cd = request.args.get('callback')
     return cd+'("这是服务器端响应的内容");'
```

