[TOC]



https://www.kancloud.cn/wangfupeng/wangeditor3

## 创建一个编辑器

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>wangEditor demo</title>
</head>
<body>
    <div id="editor">
        <p>欢迎使用 <b>wangEditor</b> 富文本编辑器</p>
    </div>

    <!-- 注意， 只需要引用 JS，无需引用任何 CSS ！！！-->
    <script type="text/javascript" src="/wangEditor.min.js"></script>
    <script type="text/javascript">
        var E = window.wangEditor
        var editor = new E('#editor')
        // 或者 var editor = new E( document.getElementById('editor') )
        editor.create()
    </script>
</body>
</html>
```





## 同一个页面创建多个编辑器

### 菜单和编辑区域分离

wangEditor 支持一个页面创建多个编辑器

**代码示例**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>wangEditor 一个页面多个编辑器</title>
    <style type="text/css">
        .toolbar {
            background-color: #f1f1f1;
            border: 1px solid #ccc;
        }
        .text {
            border: 1px solid #ccc;
            height: 200px;
        }
    </style>
</head>
<body>
    <div id="div1" class="toolbar">
    </div>
    <div style="padding: 5px 0; color: #ccc">中间隔离带</div>
    <div id="div2" class="text">
        <p>第一个 demo（菜单和编辑器区域分开）</p>
    </div>
    <div id="div3">
        <p>第二个 demo（常规）</p>
    </div>
    <!-- 引用js -->
    <script type="text/javascript" src="/wangEditor.min.js"></script>
    <script type="text/javascript">
        var E = window.wangEditor
        var editor1 = new E('#div1', '#div2')
        editor1.create()
        var editor2 = new E('#div3')
        editor2.create()
    </script>
</body>
</html>
```



## 开启和禁用编辑功能

```js
// 禁用编辑功能
editor.$textElem.attr('contenteditable', false)

// 开启编辑功能
editor.$textElem.attr('contenteditable', true)
```



## 定义 debug 模式

可通过`editor.customConfig.debug = true`配置`debug`模式，`debug`模式下，有 JS 错误会以`throw Error`方式提示出来。默认值为`false`，即不会抛出异常。

但是，在实际开发中不建议直接定义为`true`或者`false`，可通过 url 参数进行干预，示例如下：

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    // 通过 url 参数配置 debug 模式。url 中带有 wangeditor_debug_mode=1 才会开启 debug 模式
    editor.customConfig.debug = location.href.indexOf('wangeditor_debug_mode=1') > 0
    editor.create()
</script>
```



## 设置内容

以下方式中，如果条件允许，尽量使用第一种方式，效率最高。

### html 初始化内容

直接将内容写到要创建编辑器的`<div>`标签中

```html
<div id="div1">
    <p>初始化的内容</p>
    <p>初始化的内容</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    editor.create()
</script>
```

### js 设置内容

创建编辑器之后，使用`editor.txt.html(...)`设置编辑器内容

```html
<div id="div1">
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    editor.create()
    editor.txt.html('<p>用 JS 设置的内容</p>')
</script>
```

### 追加内容

创建编辑器之后，可使用`editor.txt.append('<p>追加的内容</p>')`继续追加内容。

### 清空内容

可使用`editor.txt.clear()`清空编辑器内容



## 读取内容

可以`html`和`text`的方式读取编辑器的内容

```javascript
<div id="div1">
    <p>欢迎使用 wangEditor 编辑器</p>
</div>
<button id="btn1">获取html</button>
<button id="btn2">获取text</button>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    editor.create()

    document.getElementById('btn1').addEventListener('click', function () {
        // 读取 html
        alert(editor.txt.html())
    }, false)

    document.getElementById('btn2').addEventListener('click', function () {
        // 读取 text
        alert(editor.txt.text())
    }, false)

</script>
```

需要注意的是：**从编辑器中获取的 html 代码是不包含任何样式的纯 html**，如果显示的时候需要对其中的`<table>``<code>``<blockquote>`等标签进行自定义样式（这样既可实现多皮肤功能），下面提供了编辑器中使用的样式供参考

```css
/* table 样式 */
table {
  border-top: 1px solid #ccc;
  border-left: 1px solid #ccc;
}
table td,
table th {
  border-bottom: 1px solid #ccc;
  border-right: 1px solid #ccc;
  padding: 3px 5px;
}
table th {
  border-bottom: 2px solid #ccc;
  text-align: center;
}

/* blockquote 样式 */
blockquote {
  display: block;
  border-left: 8px solid #d0e5f2;
  padding: 5px 10px;
  margin: 10px 0;
  line-height: 1.4;
  font-size: 100%;
  background-color: #f1f1f1;
}

/* code 样式 */
code {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  background-color: #f1f1f1;
  border-radius: 3px;
  padding: 3px 5px;
  margin: 0 3px;
}
pre code {
  display: block;
}

/* ul ol 样式 */
ul, ol {
  margin: 10px 0 10px 20px;
}
```



## 自定义菜单

编辑器创建之前，可使用`editor.customConfig.menus`定义显示哪些菜单和菜单的顺序。**注意：v3 版本的菜单不支持换行折叠了（因为换行之后菜单栏是在太难看），如果菜单栏宽度不够，建议精简菜单项。**

**代码示例**

```html
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    // 自定义菜单配置
    editor.customConfig.menus = [
        'head',
        'bold',
        'italic',
        'underline'
    ]
    editor.create()
</script>
```

## 默认菜单

编辑默认的菜单配置如下

```javascript
[
    'head',  // 标题
    'bold',  // 粗体
    'fontSize',  // 字号
    'fontName',  // 字体
    'italic',  // 斜体
    'underline',  // 下划线
    'strikeThrough',  // 删除线
    'foreColor',  // 文字颜色
    'backColor',  // 背景颜色
    'link',  // 插入链接
    'list',  // 列表
    'justify',  // 对齐方式
    'quote',  // 引用
    'emoticon',  // 表情
    'image',  // 插入图片
    'table',  // 表格
    'video',  // 插入视频
    'code',  // 插入代码
    'undo',  // 撤销
    'redo'  // 重复
]
```



## 配置表情

`v3.0.15`开始支持配置表情，支持图片格式和 emoji ，可通过`editor.customConfig.emotions`配置。**注意看代码示例中的注释：**

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')

    // 表情面板可以有多个 tab ，因此要配置成一个数组。数组每个元素代表一个 tab 的配置
    editor.customConfig.emotions = [
        {
            // tab 的标题
            title: '默认',
            // type -> 'emoji' / 'image'
            type: 'image',
            // content -> 数组
            content: [
                {
                    alt: '[坏笑]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/50/pcmoren_huaixiao_org.png'
                },
                {
                    alt: '[舔屏]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/40/pcmoren_tian_org.png'
                }
            ]
        },
        {
            // tab 的标题
            title: 'emoji',
            // type -> 'emoji' / 'image'
            type: 'emoji',
            // content -> 数组
            content: ['😀', '😃', '😄', '😁', '😆']
        }
    ]

    editor.create()
</script>
```

温馨提示：需要表情图片可以去 <https://api.weibo.com/2/emotions.json?source=1362404091> 和 <http://yuncode.net/code/c_524ba520e58ce30> 逛一逛，或者自己搜索。





## 配置字体颜色、背景色

编辑器的字体颜色和背景色，可以通过`editor.customConfig.colors`自定义配置

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    // 自定义配置颜色（字体颜色、背景色）
    editor.customConfig.colors = [
        '#000000',
        '#eeece0',
        '#1c487f',
        '#4d80bf',
        '#c24f4a',
        '#8baa4a',
        '#7b5ba1',
        '#46acc8',
        '#f9963b',
        '#ffffff'
    ]
    editor.create()
</script>
```



## 配置字体

编辑器的字体，可以通过`editor.customConfig.fontNames`自定义配置

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    // 自定义字体
    editor.customConfig.fontNames = [
        '宋体',
        '微软雅黑',
        'Arial',
        'Tahoma',
        'Verdana'
    ]
    editor.create()
</script>
```



## 配置编辑区域的 z-index

编辑区域的z-index默认为10000，可自定义修改，代码配置如下。需改之后，编辑区域和菜单的z-index会同时生效。

```html
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    editor.customConfig.zIndex = 100
    editor.create()
</script>
```



## 粘贴文本

**注意，以下配置暂时对 IE 无效。IE 暂时使用系统自带的粘贴功能，没有样式过滤！**

### 关闭粘贴样式的过滤

当从其他网页复制文本内容粘贴到编辑器中，编辑器会默认过滤掉复制文本中自带的样式，目的是让粘贴后的文本变得更加简洁和轻量。用户可通过`editor.customConfig.pasteFilterStyle = false`手动关闭掉粘贴样式的过滤。

### 忽略粘贴内容中的图片

从其他页面复制过来的内容，除了包含文字还可能包含图片，这些图片一般都是外域的（可能会有盗链）。此时如果想要忽略图片，即只粘贴文字不粘贴图片，可以使用`editor.customConfig.pasteIgnoreImg = true`来控制。默认是可以粘贴图片的。

### 自定义处理粘贴的文本内容

使用者可通过`editor.customConfig.pasteTextHandle`对粘贴的文本内容进行自定义的过滤、处理等操作，然后返回处理之后的文本内容。编辑器最终会粘贴用户处理之后并且返回的的内容。

**示例代码**

```html
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    // 关闭粘贴样式的过滤
    editor.customConfig.pasteFilterStyle = false
    // 忽略粘贴内容中的图片
    editor.customConfig.pasteIgnoreImg = true
    // 自定义处理粘贴的文本内容
    editor.customConfig.pasteTextHandle = function (content) {
        // content 即粘贴过来的内容（html 或 纯文本），可进行自定义处理然后返回
        return content + '<p>在粘贴内容后面追加一行</p>'
    }
    editor.create()
</script>
```



## 插入网络图片的回调

插入网络图片时，可通过如下配置获取到图片的信息。`v3.0.10`开始支持。

```javascript
var E = window.wangEditor
var editor = new E('#div1')
editor.customConfig.linkImgCallback = function (url) {
    console.log(url) // url 即插入图片的地址
}
editor.create()
```



## 插入网络图片的校验

插入网络图片时，可对图片地址做自定义校验。`v3.0.13`开始支持。

```javascript
var E = window.wangEditor
var editor = new E('#div1')
editor.customConfig.linkImgCheck = function (src) {
    console.log(src) // 图片的链接

    return true // 返回 true 表示校验成功
    // return '验证失败' // 返回字符串，即校验失败的提示信息
}
editor.create()
```



## 插入链接的校验

插入链接时，可通过如下配置对文字和链接进行校验。v3.0.10开始支持。

```javascript
var E = window.wangEditor
var editor = new E('#div1')
editor.customConfig.linkCheck = function (text, link) {
    console.log(text) // 插入的文字
    console.log(link) // 插入的链接

    return true // 返回 true 表示校验成功
    // return '验证失败' // 返回字符串，即校验失败的提示信息
}
editor.create()
```



## 多语言

可以通过`lang`配置项配置多语言，其实就是通过该配置项中的配置，将编辑器显示的文字，替换成你需要的文字。

```html
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')

    editor.customConfig.lang = {
        '设置标题': 'title',
        '正文': 'p',
        '链接文字': 'link text',
        '链接': 'link',
        '上传图片': 'upload image',
        '上传': 'upload',
        '创建': 'init'
        // 还可自定添加更多
    }

    editor.create()
</script>
```

**注意，以上代码中的链接文字要写在链接前面，上传图片要写在上传前面，因为前者包含后者。如果不这样做，可能会出现替换不全的问题，切记切记！**



## 隐藏/显示 tab

### 显示“上传图片”tab

默认情况下，编辑器不会显示“上传图片”的tab，因为你还没有配置上传图片的信息。

![img](http://images2015.cnblogs.com/blog/138012/201706/138012-20170601204308039-691571074.png)

参考一下示例显示“上传图片”tab

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')

    // 下面两个配置，使用其中一个即可显示“上传图片”的tab。但是两者不要同时使用！！！
    // editor.customConfig.uploadImgShowBase64 = true   // 使用 base64 保存图片
    // editor.customConfig.uploadImgServer = '/upload'  // 上传图片到服务器

    editor.create()
</script>
```

显示效果

![img](http://images2015.cnblogs.com/blog/138012/201706/138012-20170601204504524-830243744.png)

### 隐藏“网络图片”tab

默认情况下，“网络图片”tab是一直存在的。如果不需要，可以参考一下示例来隐藏它。

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')

    // 隐藏“网络图片”tab
    editor.customConfig.showLinkImg = false

    editor.create()
</script>
```



## wangEditor全屏，插件

插件 <https://github.com/chris-peng/wangEditor-fullscreen-plugin> 

富文本编辑器wangEditor的全屏插件，适用于V3

使用方法：

1. 依赖jquery或者zepto，须先引入jquery或zepto。有兴趣可修改为无依赖版本，代码很简单。

2. 引入wangEditor-fullscreen-plugin.css和wangEditor-fullscreen-plugin.js两个文件。

3. 在wangEditor的create方法调用后，再调用插件的初始化方法，如：

   var E = window.wangEditor; var editor = new E('#editor'); 

   editor.create(); 

   E.fullscreen.init('#editor');	#editor 目录栏的父元素即可

4. 完成。

**wangEditor-fullscreen-plugin.css**

 ```css
@charset "UTF-8";

.w-e-toolbar {
	flex-wrap: wrap;
	-webkit-box-lines: multiple;
}

.w-e-toolbar .w-e-menu:hover{
	z-index: 10002!important;
}

.w-e-menu a {
	text-decoration: none;
	color: rgb(153, 153, 153);
}
.w-e-menu a:hover {
	color:#000;
}

.fullscreen-editor {
	position: fixed !important;
	width: 100% !important;
	height: 100% !important;
	left: 0px !important;
	top: 0px !important;
	background-color: white;
	z-index: 9999;
}

.fullscreen-editor .w-e-text-container {
	width: 100% !important;
	height: 95% !important;
}
 ```



**wangEditor-fullscreen-plugin.js**

```js
/**
 * 
 */
window.wangEditor.fullscreen = {
	// editor create之后调用
	init: function(editorSelector){
		$(editorSelector + " .w-e-toolbar").append('<div class="w-e-menu"><a class="_wangEditor_btn_fullscreen" href="###" onclick="window.wangEditor.fullscreen.toggleFullscreen(\'' + editorSelector + '\')">全屏</a></div>');
	},
	toggleFullscreen: function(editorSelector){
		$(editorSelector).toggleClass('fullscreen-editor');
		if($(editorSelector + ' ._wangEditor_btn_fullscreen').text() == '全屏'){
			$(editorSelector + ' ._wangEditor_btn_fullscreen').text('退出全屏');
		}else{
			$(editorSelector + ' ._wangEditor_btn_fullscreen').text('全屏');
		}
	}
};
```



## 预览源码 & 查看源码

如果需要预览和查看源码的功能，也需要跟全屏功能一样，自己定义按钮。点击按钮时通过`editor.txt.html()`获取编辑器内容，然后自定义实现预览和查看源码功能。通过`editor.txt.html(value)`可以更新源码，这样就可以做到修改源码了。



## 使用 base64 保存图片

如果需要使用 base64 编码直接将图片插入到内容中，可参考一下示例配置

```html
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')
    editor.customConfig.uploadImgShowBase64 = true   // 使用 base64 保存图片
    editor.create()
</script>
```

示例效果如下

![img](http://images2015.cnblogs.com/blog/138012/201706/138012-20170601204759258-1412289899.png)





## 上传图片 & 配置

将图片上传到服务器上的配置方式

> **提示，如果上传图片提示错误，可以 打开 debug 模式 （会在 console.log 提示错误详细信息）来辅助排查错误。**

## 上传图片

参考如下代码

```
<div id="div1">
    <p>欢迎使用 wangEditor 富文本编辑器</p>
</div>

<script type="text/javascript" src="/wangEditor.min.js"></script>
<script type="text/javascript">
    var E = window.wangEditor
    var editor = new E('#div1')

    // 配置服务器端地址
    editor.customConfig.uploadImgServer = '/upload'

    // 进行下文提到的其他配置
    // ……
    // ……
    // ……

    editor.create()
</script>
```

其中`/upload`是上传图片的服务器端接口，接口返回的**数据格式**如下（**实际返回数据时，不要加任何注释！！！**）

```
{
    // errno 即错误代码，0 表示没有错误。
    //       如果有错误，errno != 0，可通过下文中的监听函数 fail 拿到该错误码进行自定义处理
    "errno": 0,

    // data 是一个数组，返回若干图片的线上地址
    "data": [
        "图片1地址",
        "图片2地址",
        "……"
    ]
}
```

## 限制图片大小

默认限制图片大小是 5M

```
// 将图片大小限制为 3M
editor.customConfig.uploadImgMaxSize = 3 * 1024 * 1024
```

## 限制一次最多能传几张图片

默认为 10000 张（即不限制），需要限制可自己配置

```
// 限制一次最多上传 5 张图片
editor.customConfig.uploadImgMaxLength = 5
```

## 自定义上传参数

上传图片时可自定义传递一些参数，例如传递验证的`token`等。参数会被添加到`formdata`中。

```
editor.customConfig.uploadImgParams = {
    // 如果版本 <=v3.1.0 ，属性值会自动进行 encode ，此处无需 encode
    // 如果版本 >=v3.1.1 ，属性值不会自动 encode ，如有需要自己手动 encode
    token: 'abcdef12345'
}
```

如果**还需要**将参数拼接到 url 中，可再加上如下配置

```
editor.customConfig.uploadImgParamsWithUrl = true
```

## 自定义 fileName

上传图片时，可自定义`filename`，即在使用`formdata.append(name, file)`添加图片文件时，自定义第一个参数。

```
editor.customConfig.uploadFileName = 'yourFileName'
```

## 自定义 header

上传图片时刻自定义设置 header

```
editor.customConfig.uploadImgHeaders = {
    'Accept': 'text/x-json'
}
```

## withCredentials（跨域传递 cookie）

跨域上传中如果需要传递 cookie 需设置 withCredentials

```
editor.customConfig.withCredentials = true
```

## 自定义 timeout 时间

默认的 timeout 时间是 10 秒钟

```
// 将 timeout 时间改为 3s
editor.customConfig.uploadImgTimeout = 3000
```

## 监听函数

可使用监听函数在上传图片的不同阶段做相应处理

```
editor.customConfig.uploadImgHooks = {
    before: function (xhr, editor, files) {
        // 图片上传之前触发
        // xhr 是 XMLHttpRequst 对象，editor 是编辑器对象，files 是选择的图片文件
        
        // 如果返回的结果是 {prevent: true, msg: 'xxxx'} 则表示用户放弃上传
        // return {
        //     prevent: true,
        //     msg: '放弃上传'
        // }
    },
    success: function (xhr, editor, result) {
        // 图片上传并返回结果，图片插入成功之后触发
        // xhr 是 XMLHttpRequst 对象，editor 是编辑器对象，result 是服务器端返回的结果
    },
    fail: function (xhr, editor, result) {
        // 图片上传并返回结果，但图片插入错误时触发
        // xhr 是 XMLHttpRequst 对象，editor 是编辑器对象，result 是服务器端返回的结果
    },
    error: function (xhr, editor) {
        // 图片上传出错时触发
        // xhr 是 XMLHttpRequst 对象，editor 是编辑器对象
    },
    timeout: function (xhr, editor) {
        // 图片上传超时时触发
        // xhr 是 XMLHttpRequst 对象，editor 是编辑器对象
    },

    // 如果服务器端返回的不是 {errno:0, data: [...]} 这种格式，可使用该配置
    // （但是，服务器端返回的必须是一个 JSON 格式字符串！！！否则会报错）
    customInsert: function (insertImg, result, editor) {
        // 图片上传并返回结果，自定义插入图片的事件（而不是编辑器自动插入图片！！！）
        // insertImg 是插入图片的函数，editor 是编辑器对象，result 是服务器端返回的结果

        // 举例：假如上传图片成功后，服务器端返回的是 {url:'....'} 这种格式，即可这样插入图片：
        var url = result.url
        insertImg(url)

        // result 必须是一个 JSON 格式字符串！！！否则报错
    }
    }
}
```

## 自定义提示方法

上传图片的错误提示默认使用`alert`弹出，你也可以自定义用户体验更好的提示方式

```
editor.customConfig.customAlert = function (info) {
    // info 是需要提示的内容
    alert('自定义提示：' + info)
}
```

## 自定义上传图片事件

如果想完全自己控制图片上传的过程，可以使用如下代码

```
editor.customConfig.customUploadImg = function (files, insert) {
    // files 是 input 中选中的文件列表
    // insert 是获取图片 url 后，插入到编辑器的方法

    // 上传代码返回结果之后，将图片插入到编辑器中
    insert(imgUrl)
}
```



## 预防 XSS 攻击

> 术业有专攻

要想在前端预防 xss 攻击，还得依赖于其他工具，例如[xss.js](http://jsxss.com/zh/index.html)（如果打不开页面，就从百度搜一下）

代码示例如下

```
<script src='/xss.js'></script>
<script src='/wangEditor.min.js'></script>
<script>
    var E = window.wangEditor
    var editor = new E('#div1')

    document.getElementById('btn1').addEventListener('click', function () {
        var html = editor.txt.html()
        var filterHtml = filterXSS(html)  // 此处进行 xss 攻击过滤
        alert(filterHtml)
    }, false)
</script>
```









