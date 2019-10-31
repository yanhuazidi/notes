[TOC]



## HTML

### HTML 概述
​    什么是HTML : HyperText Markup Language   超文本标记语言

### HTML 语法
​    HTML 是标签语法，标签以<> 为标志

#### 分类 ：

1. 单标签
   只有开始标签，没有结束标签
   语法：
   1. <标签名>
   2. <标签名/>
2. 双标签
   又开始标签，有结束标签，成对出现
   语法：
   <标签名>标签内容</标签名>

### 标签的嵌套

1. 在双标签中嵌套使用其他标签，都是嵌套结构
2. 外层元素称为父元素，内层元素称为子元素
3. 多层嵌套结构中，外层元素称为祖先元素，内层元素为后代元素

### HTML 语法规范  

非常宽松

1. HTML 标签不区分大小写的，BODY Body body 标签可以大写，推荐小写
2. 在涉及标签嵌套时保持内部标签适当缩进，增加代码可读性
3. 添加适量注释

### 快速编写 html

```html
父标签>子元素3
table>tr5>td4div>p10>span*3
```

### HTML 的注释

语法： `<!--  注释内容  -->`

1. HTML 的注释不能嵌套
2. 标签名中不能嵌套使用注释



## 文档基本结构
1. `<html></html>`标签，表示文档的开始和结束，网页中所有的内容都必须写在html标签中

2. `<head></head>`标签，表示网页的头部内容，设置网页的标题，字符集，引入外部文件等

   ```html
   <title></title> 网页的标题
   <meta>  元数据,定义网页的全局信息
   <link>  文件链接
   <style></style> 定义标签样式
   <script></script>  定义js代码或引用外部js文件
   ```

3. `<body></body>`标签，表示网页的主体内容，所有呈现在网页窗口中的内容，都应该写在body标签中

4. 标签属性   标签属性用来修饰或补充当前的标签内容

   语法 :  <标签名 属性名="属性值"></标签名>

   每个标签中都可以添加一个或多个标签属性，多个属性之间使用空格隔开

5. 标签事件
   可以使 HTML 事件触发浏览器中的行为，比方说当用户点击某个 HTML 元素时启动一段 JavaScript。



## 标签标准属性

标准属性(通用属性)全局属性      所有的元素都支持的属性

1. `title`       鼠标悬停在元素上时显示的文本

2. `accesskey`	规定访问元素的键盘快捷键,主流浏览器都支持

   ```html
   <element accesskey="character">
   <a href="//www.runoob.com/css/css-tutorial.html" accesskey="c">CSS 教程</a>
   character	指定激活元素的快捷键
   ```

   值 `character`	指定激活元素的快捷键

   注意： 在不同操作系统中不同的浏览器中访问快捷键的方式不同

   Internet Explorer	[Alt] + accesskey

   Chrome	            [Alt] + accesskey
    Firefox	            [Alt] [Shift] + accesskey
   Safari	            [Alt] + accesskey
   Opera 15 or er:  [Alt] + accesskey

3. `class`	    规定元素的类名（用于规定样式表中的类）。

4. `contenteditable`	规定是否允许用户编辑内容。主流浏览器都支持

   ```html
   <element contenteditable="true|false">
   ```

5. `dir`        规定元素中内容的文本方向。

   ```html
   <element dir="ltr|rtl|auto">
   ```

   值	        		描述
   ltr	    	默认。从左向右的文本方向。
   rtl	    	从右向左的文本方向。
   auto		让浏览器根据内容来判断文本方向。仅在文本方向未知时推荐使用。

6.  `draggable`	规定是否允许用户拖动元素。主流浏览器都支持，需要配合h5拖放操作

7. `hidden`	    规定该元素是无关的。被隐藏的元素不会显示。

8. `id`	        规定元素的唯一 ID。

9. `spellcheck`	规定是否必须对元素进行拼写或语法检查。

10. `lang`	    规定元素中内容的语言代码

    ```html
    <html lang="en">
    ```

11. `style`	    规定元素的行内样式。

12. `tabindex`	规定元素的 tab 键控制次序。

    ```html
    <element tabindex="number">
    number	规定元素的 tab 键控制顺序（1 是第一）
    ```

13.  `data-*`      用于存储页面的自定义数据，主流浏览器都支持

    ```html
    <element data-attr="somevalue">
    somevalue	指定属性值 (一个字符串)
    ```

      1. data-* 属性用于存储私有页面后应用的自定义数据。
      2. data-* 属性可以在所有的 HTML 元素中嵌入数据。
      3. 自定义的数据可以让页面拥有更好的交互体验（不需要使用 Ajax 或去服务端查询数据）。
            注意： 自定义属性前缀 "data-" 会被客户端忽略。



## 事件

窗口事件属性（Window Event Attributes）
由窗口触发该事件 (适用于 <body> 标签):

        属性	            值	        描述
        onafterprint	    script	在打印文档之后运行脚本
        onbeforeprint	    script	在文档打印之前运行脚本
        onbeforeonload	    script	在文档加载之前运行脚本
        onblur	            script	当窗口失去焦点时运行脚本
        onerror	            script	当错误发生时运行脚本
        onfocus	            script	当窗口获得焦点时运行脚本
        onhaschange	        script	当文档改变时运行脚本
        onload	            script	当文档加载时运行脚本
        onmessage	        script	当触发消息时运行脚本
        onoffline	        script	当文档离线时运行脚本
        ononline	        script	当文档上线时运行脚本
        onpagehide	        script	当窗口隐藏时运行脚本
        onpageshow	        script	当窗口可见时运行脚本
        onpopstate	        script	当窗口历史记录改变时运行脚本
        onredo          	script	当文档执行再执行操作（redo）时运行脚本
        onresize	        script	当调整窗口大小时运行脚本
        onstorage	        script	当 Web Storage 区域更新时（存储空间中的数据发生变化时）运行脚本
        onundo	            script	当文档执行撤销时运行脚本
        onunload	        script	当用户离开文档时运行脚本
    
    表单事件(Form Events)
        表单事件在HTML表单中触发 (适用于所有 HTML 元素, 但该HTML元素需在form表单内):
    
        属性	            值	            描述
        onfocus	        script	当元素获得焦点时运行脚本
        onblur	        script	当元素失去焦点时运行脚本
        oninput	        script	当元素获得用户输入时即时运行脚本
        onchange	    script	当元素值改变，焦点失去时运行脚本
        onformchange	script	当表单改变时运行脚本
        onforminput	    script	当表单获得用户输入时运行脚本
        oncontextmenu	script	当触发上下文菜单时运行脚本
        oninvalid	    script	当元素无效时运行脚本
        onselect	    script	当选取[框选文本]元素时运行脚本
        onsubmit	    script	当提交表单时运行脚本
        onreset	        script	当表单重置时运行脚本。HTML 5 不支持。
    
        键盘事件（Keyboard Events）
            属性	    值	        描述
            onkeydown	script	当按下按键时运行脚本
            onkeypress	script	当按下并松开按键时运行脚本
            onkeyup	    script	当松开按键时运行脚本
    
    鼠标事件（Mouse Events）
        通过鼠标触发事件, 类似用户的行为:
    
        属性	        值	        描述
        onclick	        script	当单击鼠标时运行脚本
        ondblclick	    script	当双击鼠标时运行脚本
        ondrag	        script	当拖动元素时运行脚本
        ondragend	    script	当拖动操作结束时运行脚本
        ondragenter	    script	当元素被拖动至有效的拖放目标时运行脚本
        ondragleave	    script	当元素离开有效拖放目标时运行脚本
        ondragover	    script	当元素被拖动至有效拖放目标上方时运行脚本
        ondragstart	    script	当拖动操作开始时运行脚本
        ondrop      	script	当被拖动元素正在被拖放时运行脚本
        onmousedown 	script	当按下鼠标按钮时运行脚本
        onmousemove	    script	当鼠标指针移动时运行脚本
        onmouseout	    script	当鼠标指针移出元素时运行脚本
        onmouseover	    script	当鼠标指针移至元素之上时运行脚本
        onmouseup	    script	当松开鼠标按钮时运行脚本
        onmousewheel	script	当转动鼠标滚轮时运行脚本
        onscroll	    script	当滚动元素的滚动条时运行脚本
    
    多媒体事件(Media Events)
        通过视频（videos），图像（images）或者音频（audio） 触发该事件，多应用于HTML媒体元素比如 <audio>, <embed>, <img>, <object>, 和<video>):
    
        属性	            值	        描述
        onabort	            script	当发生中止事件时运行脚本
        oncanplay	        script	当媒介能够开始播放但可能因缓冲而需要停止时运行脚本
        oncanplaythrough	script	当媒介能够无需因缓冲而停止即可播放至结尾时运行脚本
        ondurationchange	script	当媒介长度改变时运行脚本
        onemptied	        script	当媒介资源元素突然为空时（网络错误、加载错误等）运行脚本
        onended	            script	当媒介已抵达结尾时运行脚本
        onerror	            script	当在元素加载期间发生错误时运行脚本
        onloadeddata	    script	当加载媒介数据时运行脚本
        onloadedmetadata	script	当媒介元素的持续时间以及其他媒介数据已加载时运行脚本
        onloadstart	        script	当浏览器开始加载媒介数据时运行脚本
        onpause	            script	当媒介数据暂停时运行脚本
        onplay	            script	当媒介数据将要开始播放时运行脚本
        onplaying	        script	当媒介数据已开始播放时运行脚本
        onprogress	        script	当浏览器正在取媒介数据时运行脚本
        onratechange	    script	当媒介数据的播放速率改变时运行脚本
        onreadystatechange	script	当就绪状态（ready-state）改变时运行脚本
        onseeked	        script	当媒介元素的定位属性 [1] 不再为真且定位已结束时运行脚本
        onseeking	        script	当媒介元素的定位属性为真且定位已开始时运行脚本
        onstalled	        script	当取回媒介数据过程中（延迟）存在错误时运行脚本
        onsuspend	        script	当浏览器已在取媒介数据但在取回整个媒介文件之前停止时运行脚本
        ontimeupdate	    script	当媒介改变其播放位置时运行脚本
        onvolumechange	    script	当媒介改变音量亦或当音量被设置为静音时运行脚本
        onwaiting	        script	当媒介已停止播放但打算继续播放时运行脚本
    
    其他事件
        属性	    值	        描述
        onshow	    script	    当 <menu> 元素在上下文显示时触发
        ontoggle	script	    当用户打开或关闭 <details> 元素时触发



## 结构标签  H5

作用 :代替div(避免多重div混乱)，用于描述整个网页结构，提升标签的语义，等同于div标签



   1. `<header>定义网页或者某个区域的头部块</header>`

   2. `<nav>定义网页的导航链接部分(导航栏)</nav>`

   3. `<section>定义网页的主体内容块</section>`

   4. `<aside>定义网页的侧边栏</aside>`

   5. `<footer>定义网页的底部内容，多用于版权，备案号等</footer>`

    6. `<article>定义与文字相关的内容,论坛，帖子，条目等独立的内容。</article>`
        
   7. `<figure>标签规定独立的流内容（图像、图表、照片、代码等等）。<figure>` 

         元素的内容应该与主内容相关，但如果被删除，则不应对文档流产生影响。

    8. `<figcaption> `标签定义` <figure> `元素的标题.

          `<figcaption>`元素应该被置于 "figure" 元素的第一个或最后一个子元素的位置。

          ```html
          <figure>
                  <img src="img_pulpit.jpg" alt="The Pulpit Rock" width="304" height="228">
                  <figcaption>Fig.1 - A view of the pulpit rock in Norway.</figcaption>
          </figure>
          ```

          
## head标签

### 文档类型声明

`<!doctype html>`

对当前的文档类型及版本做出指定(这种声明方式是HTML5的声明方式)关系到页面元素的渲染效果 CSS
,书写到`<html>`之前，文档开篇

###  元数据标签

 `<meta>`

#### 指定文件解析编码

`<meta charset="utf-8" />`  

#### 定义针对搜索引擎的关键词：排位,网络营销

`<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript" />`

 #### 定义对页面的描述：

`<meta name="description" content="免费的 web 技术教程。" />`

#### 定义页面的最新版本：

`<meta name="revised" content="David, 2008/8/8/" />`

#### 刷新页面：

`<meta http-equiv="refresh" content="5" />`

#### 响应式布局标签 

`<meta name="viewport" content="width=device-width,initial-scale=1">`

     viewport 视口   : 呈现在用户窗口的内容，超出视口的内容需要滑动查看           
     content  设置能够容许网页进行的操作
     width=device-width  表示视口宽度就是设备宽度
     initial-scale=1   视口宽度是否可以缩放 1能缩放  1.0不能缩放
     maximum-scale=1.0   允许缩放的最大倍率 
     user-scalable=0     是否允许用户缩放 1允许 0不允许

```

 属性	        值	                    描述
 charset	    character encoding    定义文档的字符编码。
 	
 content     some_text	          定义与 http-equiv 或 name 属性相关的元信息。
 	
 http-equiv	content-type          把 content 属性关联到 HTTP 头部。
             expires
             refresh
             set-cookie

 name	    author                把 content 属性关联到一个名称。
             description
             keywords
             generator
             revised
             others
```

### 设置网页的标题，字符集，和选项卡图标

```html
<title>WeiTianHua</title>
```



### 基准 URL

`<base>`标签为页面上的所有的相对链接规定默认 URL 或默认目标。规定页面中所有相对链接的基准 URL。

在一个文档中，最多能使用一个 `<base>` 元素。`<base>` 标签必须位于 `<head>` 元素内部。
提示：请把 `<base>` 标签排在 `<head>` 元素中第一个元素的位置，这样 head 区域中其他元素就可以使用 `<base>` 元素中的信息了。
注释：如果使用了 `<base>` 标签，则必须具备 `href` 属性或者 `target` 属性或者两个属性都具备。`target` 属性规定页面中所有的超链接和表单在何处打开。该属性会被每个链接中的 target 属性覆盖。

```html
<head>
     <base href="http://www.runoob.com/images/" target="_blank">
</head>
<body>
    <img src="logo.png" width="24" height="39" alt="Stickman">
</body>
```



### link标签
​    `<link>` 标签定义文档与外部资源的关系。
​    `<link>` 标签最常见的用途是链接样式表。
此元素只能存在于 head 部分，不过它可出现任何次数。

```html
 <head>
      <link rel="stylesheet" type="text/css" href="theme.css">
     <!-- 头图片链接  rel=大小类型  href=路径 type=进一步说明图片类型-->
	<link rel="shortout icon" href="201_1440x900.jpg" type="image/x-icon">
</head>
```


    属性	       值	               描述
    href	    URL	               定义被链接文档的位置。
    hreflang	language_code	   定义被链接文档中文本的语言。
    media	    media_query	       规定被链接文档将显示在什么设备上。
    rel	        alternate          必需。定义当前文档与被链接文档之间的关系。
                archives
                author
                bookmark
                external
                first
                help
                icon
                last
                license
                next
                nofollow
                noreferrer
                pingback
                prefetch
                prev
                search
                sidebar
                stylesheet
                tag
                up	
    sizes	   HeightxWidth        定义了链接属性大小，只对属性 rel="icon" 起作用。
                any	
    type	   MIME_type	      规定被链接文档的 MIME 类型。        


## 文本标签

### 标题标签

`<h1>一级标题</h1>`

​        ...

`<h6>六级标题</h6>`

特点:

1. 自带文本加粗效果

2. 字号变化
   从 h1 ~ h6 字体大小逐渐减小

3. 独占一行，上下有垂直间距

   属性 align 设置标签内容水平方向对齐方式
   取值 : left/center/right

### 段落标签 paragraph

`<p>标签内容</p>突出的表示一段文字`

特点:  独立成行,上下有垂直的间距

属性 align 设置标签内容水平方向对齐方式
取值 : left/center/right

### 换行标签 : 

`<br> `

### 水平线(分割线)标签 :

`<hr>`

属性：

- `width`: "%" or int px   表示水平线的宽度
- `size`: % or int px    表示水平线的粗细
- `align`:left/center/right  设置标签内容水平方向对齐方式
- `color`:"red"    设置水平线的颜色

### 预格式化标签

`<pre></pre>`

 特点:  标签内部的文本，保留其格式(回车，制表位等)，在页面上显示

### 加粗标签

`<b></b> or <strong></strong>`

h5之后推荐使用有语义标签 strong 表示强调

### 斜体标签

`<i></i> or <em>h5之后推荐使用有语义标签</em>`

### 下划线标签

`<u></u>`

### 删除线标签

`<s></s> or <del>h5之后推荐使用有语义标签</del>`

### 上下标标签

上标: `X<sup>2</sup>`
下标: `X<sub>1</sub>`



## 字符实体

**注释：**实体名称对大小写敏感！

| 显示结果 | 描述              | 实体名称          | 实体编号 |
| :------- | :---------------- | :---------------- | :------- |
|          | 空格              | &nbsp;            | &#160;   |
| <        | 小于号            | &lt;              | &#60;    |
| >        | 大于号            | &gt;              | &#62;    |
| &        | 和号              | &amp;             | &#38;    |
| "        | 引号              | &quot;            | &#34;    |
| '        | 撇号              | &apos; (IE不支持) | &#39;    |
| ￠       | 分（cent）        | &cent;            | &#162;   |
| £        | 镑（pound）       | &pound;           | &#163;   |
| ¥        | 元（yen）         | &yen;             | &#165;   |
| €        | 欧元（euro）      | &euro;            | &#8364;  |
| §        | 小节              | &sect;            | &#167;   |
| ©        | 版权（copyright） | &copy;            | &#169;   |
| ®        | 注册商标          | &reg;             | &#174;   |
| ™        | 商标              | &trade;           | &#8482;  |
| ×        | 乘号              | &times;           | &#215;   |
| ÷        | 除号              | &divide;          | &#247;   |



## 元素显示方式

### 块级元素
元素独占一行，不与其它元素共行,从上往下排列
 h1~h6  p  div  

### 行级元素
在网页中其它行内元素，行内块元素共行显示,从左往右排列
        span   strong  label  em  del  u  sub  sup ...

### 行内块元素

显示方式与行内元素相同，但是具备块级元素的特征

### 表格元素

表格的上下单元格宽度必须一致
表格的宽度是由表格的内容决定的，后面的单元格可能改变前面单元格
浏览器会把表格的所有数据预读到内存，一次性画到页面上
其他元素是从上往下，从左往右渲染,表格是一次全画出来



## 列表标签

列表: 一种结构，将数据按照从上到下进行排列显示
分类 :

1. **有序列表 (ordered list)**
   按照数字或字母依次标记每一条数据
   语法：

   ```html
   <ol>
   	<li></li>
   </ol>
   ```

   **标签属性:**

   有序列表默认使用数字标识列表项，从1开始也可以在ol标签中添加属性进行设置

   1. type 属性

      指定项目符号的类型
      可取的值 : 1 a A i I
      希腊数字 : i ii  iii  iv v vi ...

   2. start 属性

      指定从第几个项目符号开始标识数据

      取值 : 无单位的数字

2. **无序列表 (unordered list)**

   **语法 :**

   ```html
   <ul>
      <li></li>
   <ul>
   ```

   type 属性 : 指定项目符号类型

   ​		取值 : disc(默认)  square(实心正方形) circle(空心圆) none

3. **自定义列表**

   **语法:**

   ```html
   <dl>
       <dt>订单跟踪<dt>
       <dd>物流查询</dd>
       <dd>联系客服</dd>
       ...
       <dt>加入我们<dt>
       <dd>门店查询<dd>
       ...
   </dl>
   ```

   

## 图片标签

**语法：**

```html
<img src='url'> 
```

在网页中插入一张图片 ，默认按原始尺寸

**标签属性:**

1. `width` : 取px为单位的像素值，设置图片宽度
2. `height` : 取像素值，设置图片的高度
3. `title` : 用来设置鼠标悬停与图片上时的显示文本
4. `alt` : 当图片加载失败时显示的文本



## 超链接标签



**语法:**

```html
<a href="链接地址">超链接文本</a>
```

**注意：**

1. href 属性是必填项，省略的话，超链接文本和普通文本一样
2. 网络路径必须加协议
3. 本地文件可用
4. a标签不能继承外部元素颜色，要单独设置

**特殊取值:**

- `""`  :  表示连接至本页面，包含刷新操作
- `"#" `:  链接至本页的锚点位置，不刷新(做页面目录)
- `"javascript:void(0)"` : 链接至本页不刷新

**标签属性**

| 属性                                                         | 值                                                           | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [download](https://www.w3cschool.cn/htmltags/att-a-download.html) | *filename*                                                   | 指定下载链接                                                 |
| [href](https://www.w3cschool.cn/htmltags/att-a-href.html)    | *URL*                                                        | 规定链接的目标 URL。                                         |
| [hreflang](https://www.w3cschool.cn/htmltags/att-a-hreflang.html) | *language_code*                                              | 规定目标 URL 的基准语言。仅在 href 属性存在时使用。          |
| [media](https://www.w3cschool.cn/htmltags/att-a-media.html)  | *media_query*                                                | 规定目标 URL 的媒介类型。默认值：all。仅在 href 属性存在时使用。 |
| [rel](https://www.w3cschool.cn/htmltags/att-a-rel.html)      | alternate author bookmark help license next nofollow noreferrer prefetch prev search tag | 规定当前文档与目标 URL 之间的关系。仅在 href 属性存在时使用。 |
| [target](https://www.w3cschool.cn/htmltags/att-a-target.html) | _blank _parent _self _top *framename*                        | 规定在何处打开目标 URL。仅在 href 属性存在时使用。           |
| [type](https://www.w3cschool.cn/htmltags/att-a-type.html)    | *MIME_type*                                                  | 规定目标 URL 的 MIME 类型。仅在 href 属性存在时使用。 注：MIME = Multipurpose Internet Mail Extensions。 |

#### 下载

`<a href="/statics/images/w3c/logo.png" download="w3clogo">`

#### 使用锚点链接
1. 通过定义锚点，实现跳转至指定文件的指定位置

2. 使用：
   **H4 写法**
   在页面相应位置添加锚点
   `<a href="#7">7.条目</a>`
   `<a name="7"></a>`锚点定位，不显示内容
   在其他文件中，跳转至指定文件指定位置
   `<a href="11.9.3.html#7">跳转至11.9.3.html  7.条目</a>`
   使用name属性定义锚点名称，超链接的链接地址中使用#表示连接至本页，跟上锚点名称，表示跳转至锚点位置

    **H5 新写法**               

   `<a href="#任意标签的id">7.条目</a>`

   跳转至指定 id 的元素处

   href="#"  默认返回顶部

#### js脚本
​    `<a href="javascript:alert('弹窗')">弹窗</a>`

#### 新建邮件 , 本机要安装了邮件客户端

`<a href="mailto:yan@tedu.cn">新建邮件</a>`



**图片超链接**

```html
 <a href="">
     <img src="">
</a>
```



## 表格标签

**语法 :**
           1. `<table></table>` 表示表格标签
           2. `<tr></tr>` 表示表格中的一行  table row
           3. `<td></td>` 表示行中的一个单元格  table data
           4. `<th></th>` 同单元格，自带文本加粗居中效果

**标签属性**
table 标签属性 表

- `border` : 为表格设置边框,取像素值px
- `width / height` : 设置表格的宽高大小，取像素值，默认内容自适应 
- `bgcolor `: 表格的背景色设置，取英文颜色单词
- `align` : 设置表格在父元素中的水平对齐方式
  取值: left(默认左对齐)/ center / right
- `cellspacing` : 设置单元格与单元格之间的距离 取像素值
- `cellpadding` : 设置单元格内容与单元格边框之间的距离

tr 标签属性 行

- `bgcolor` : 行的背景色设置，取英文颜色单词
- `align` : 设置每一行单元格的内容的水平对齐方式
                  取值: left(默认左对齐)/ center / right
- `valign` : 设置每一行单元格的内容垂直对齐方式
                  取值 : top / middle(默认) / bottom

td 标签属性  格

- `width / height` : 设置单元格的宽高大小，取像素值
- `align` : 设置单元格的内容的水平对齐方式
              取值: left(默认左对齐)/ center / right
- `valign` : 设置单元格的内容垂直对齐方式
              取值 : top / middle(默认) / bottom 
- `bgcolor` : 单元格的背景色设置，取英文颜色单词

**单元格合并，只作用域td标签**

单元格合并涉及表格结构的调整

1. 跨列合并

   属性 : colspan

   取值 : 无单位的数值，表示跨几列

2. 跨行合并

   属性 : rowspan

   取值 : 无单位的数值，表示跨几行

注意:
           1. 跨行和跨列是单元格的操作，所以属性是单元格td的属性
           2. 旦发生单元格合并，要删除多余的单元格
                 跨列合并：
                     影响当前行中单元格的数量，删除当前行中多余单元格
                 跨行合并：
                     影响其后行中的单元格数量，需要删除后面行中的单元格

**表格行分组**

表格在浏览器中渲染时会自动的添加结构标签

表格可以分为 thead tfoot tbody 三部分,用于CSS动态添加表格记录时分组操作

 `<thead></thead>`标签用来划分表头,表头中可以有若干行组成

`<tfoot></tfoot>`用于划分表尾，由若干行组成

`<tbody></tbody>`用于划分表格主体，默认情况下所有的行会自动加入tbody

注意:

如果涉及在HTML代码中完整书写分组标签，建议按照此顺序

```html
<thead>
	<tr>
		<td></td>
	</tr>
</thead>
<tfoot></tfoot>
<tbody></tbody>
```
**表格中的标题**
`<caption></caption>`必须放置在 `<table>`之后

```html
    <table>
        <caption>标题</caption>
        <tr></tr>
    </table>
```

`<th></th>` 可代替`<td></td>`，自带文本加粗居中效果 

**表格的嵌套**
一张表格中，所有的嵌套只能放置在 <td></td> 中




## 表单

作用: 用来接收用户的数据并提交给服务器
表单二要素

        1. 表单元素  `<form></form>`
           2. 表单控件

### 表单元素

**标签**

`<form></form>` 用来提交数据到服务器，表单控件都应写在此标签中

**标签属性**

1. `method` : 用来指定表单数据的提交方式 

   取值:

   - `get`(默认)  
     1. 数据会以参数的形式拼接在url后面
     2. 明文提交，会显示在地址栏上
     3. 最大提交数据2kb
   - `post`
     1. 数据会打包在请求体中   
     2. 隐式提交，安全性较高
     3. 没有数据大小限制
   - `delete`    在服务器删除资源
   - `put `      往服务器上传资源

2. `action`  : 必填，指定数据的提交地址

3. `enctype`   : 指定数据的编码方式

   提供的类型有：

>1. `application/x-www-form-urlencoded`(默认)
>
>   将表单中是数据装换成字符串格式(name=ss,&pwd=123)附加在url后面，使用?与url隔开
>
>2. `multipart/form-data`
>
>   专门用来上传特殊类型的 如: 图片，文件，mp3...
>   数据的提交方式必须是post
>
>3. `text/plain`
>
>   数据以纯文本形式编码，不含任何控件和格式字符



### 表单控件

表单控件的数据只有放在表单元素中才可以被提交

#### 输入框

`<input> `     内容较多，详见: http://www.runoob.com/tags/tag-input.html

**属性                                        值                                                    描述**

1. type                             button                                                    普通按钮

   ​                                    submit        										   提交按钮

   ​                            		reset         											重置按钮

   ​                    				radio         											单选框

   ​                    				checkbox     										  复选框

   ​                       	 		color         											色彩选择框

   ​                    				date          											年月日期输入框

   ​                    				month         										年月输入框

   ​                    				week          										 年月周输入框

   ​                    				datetime      										日期时间输入框

   ​									datetime-local 									本地日期时间输入框

   ​                    				time          										   时间输入框

   ​                        			file          											文件输入框

   ​									image         										图片按钮

   ​                        			search        										搜索的文本字段，提供快速清除功能 X

   ​                        			email         										邮件输入框，验证输入格式

   ​                        			number        									数值输入框，只能输入数字，并提供滚动

   ​                        			range         									  滑块输入框

   ​                        			password      									密码框

   ​                       			 tel           									    电话号码的文本字段,在移动设备中显示拨号键盘效果

   ​                        			text          											文本框

   ​                        			url           										路径输入框，要http://开头

   ​                        			hidden        									隐藏域

2. name                           text                                                必填， 指定控件名称，缺少无法提交

3. value 	                      text                                                指定控件的值，可以通过 js 动态获取，提交给服务端

4. maxlength                 number                                             指定最大输入字符数

5. placeholder                text                                                  设置提示文本，占位符

6. autocomplete             on/off                                               设置是否自动补全 

7. readonly	                readonly	                                     readonly 属性规定输入字段是只读的，提交值

8. width 	                     pixels	                          width 属性规定 <input> 元素的宽度。 (只针对type="image")

   height	                     pixels	                          规定` <input>`元素的高度。(只针对type="image")

   src                              URL                属性对于 `<input type="image">` 是必需的属性如果 type 属性设置为 image，当用户单击图像时，浏览器将以像素为单位，将鼠标相对于图像边界的偏移量发送到服务器，其中包括从图像左边界开始的水平偏移量，以及从图像上边界开始的垂直偏移量。

9. disabled	                disabled	                 disabled 属性规定应该禁用的 <input> 元素。不提交

10. list	                         datalist_id	                属性引用 <datalist> 元素，其中包含 <input> 元素的预定义选项。

    类似 input加select标签组合

    ```html
    <input list="browsers">
    <datalist id="browsers">
         <option value="Internet Explorer">
         <option value="Firefox">
         <option value="Google Chrome">
         <option value="Opera">
    </datalist>
    ```

11. 用于number | date | range

    max	    number | date	    属性规定 <input> 元素的最大值。
    min	     number | date	    属性规定 <input>元素的最小值。
    step	  number	            step 属性规定 <input type="number"> 元素的滚动数字间隔,步数。

12. required	               required	                                        属性规定必需在提交表单之前填写输入字段。

13. autofocus                autofocus	                                属性规定当页面加载时 <input> 元素应该自动获得焦点。

14. pattern	                  regexp	                                    pattern 属性规定用于验证 <input> 元素的值的正则表达式。

15. multiple  	             multiple	                           属性规定允许用户输入到 <input> 元素多个值 ，用于email 和 file。

 

### 单选按钮和复选框

单选按钮(只能选一个)  : 

```html
<input type="radio" name="gender" value="m">男
<input type="radio" name="gender"  value="w">女
```

复选框(可以选多个)   :

```html
<input type="checkbox" name="happy[]" value="a">aa
<input type="checkbox" name="happy[]" value="b">ss
<input type="checkbox" name="happy[]" value="c">dd
<input type="checkbox" name="happy[]" value="d">ff
```
属性

- `name` 定义控件名称和分组
  一组按钮控件名称必须保持一致
  checkbox的name要写成数组形式, : name[]
- `value` 定义控件的值
  最终将发送给服务器，按钮的value属性必须指定，不然为on
- `checked`
  表示默认选择当前按钮 



**按钮特殊用法**

label for id   将按钮文本与按钮控件绑定在一起，实现点击等价

使用:

1. 使用`<label></label>`标签包裹按钮文本
2. 为按钮控件添加id属性，属性值自定义
3. 为label标签添加for属性，属性值与控件的id保持一致，实现绑定 

#### 隐藏域

`<input type="hidden" name="uid" value"001">`

name 定义控件名称, value 设置控件的值，都是必填项

#### 文件选择框

`<input type="file" name="">`

涉及二进制数据提交，文件，图片，mp3 需要设置form enctype属性，指定数据的提交方式为post
默认只能传输一个文件，可以使用 multiple 属性一次传输多个文件

属性：

multiple  	multiple	属性规定允许用户输入到 <input> 元素多个值 ，用于email 和 file。
name要改为数组 file[]



#### 下拉选择框
        3. 下拉选择框
                <select name="address">
                    <option value="beijing">北京</option>
                    <option value="shanghai">上海</option>
                </select>
                默认单选
    
            1. 当option没有value属性时,select的value为选中的option的内容
               当option有value属性时,select的value为选中的option的value
     
            2. 属性
                <select>
                size  : 默认值为1，定义显示选项的数量，如果值为大于1的数字，
                        下拉列表表现为滚动列表
    
                multiple : 设置多选，无值，改为滚动列表显示 
                        name要用数组
    
                <option>
                selected :无值， 预选择选项, 默认第一个为预选中项
                disabled	disabled	规定此选项应在首次加载时被禁用。
                value	  text	定义送往服务器的选项值。
    
            <optgroup></optgroup> 标签经常用于把相关的选项组合在一起。
                    如果你有很多的选项组合, 你可以使用<optgroup> 标签能够很简单的将相关选项组合在一起。
                eg:
                    <select>
                    <optgroup label="Swedish Cars">
                        <option value="volvo">Volvo</option>
                        <option value="saab">Saab</option>
                    </optgroup>
                    <optgroup label="German Cars">
                        <option value="mercedes">Mercedes</option>
                        <option value="audi">Audi</option>
                    </optgroup>
                    </select>
                属性	    值	            描述
                disabled	disabled	规定禁用该选项组。
                label	    text	    为选项组规定描述。
    
        4. 文本域，可以多行输入
            语法: <textarea name="uinfo"></textarea>
            标签属性:
                cols :  指定文本域默认宽度，宽度是通过列数控制的
                        以英文字符为准，中文占两个或三个
                rows :  指定文本域行数
                readonly :指定只读
            特点 : 文本域的大小可以由用户调整

```html
<select name="address">
      <option value="beijing">北京</option>
      <option value="shanghai">上海</option>
</select>
```

第一个位预选中
            预选择选项  selected



#### 文本域，可以多行输入
`<textarea name="uinfo"></textarea>`
标签属性:

- `cols` :  指定文本域默认宽度，宽度是通过列数控制的
  以英文字符为准，中文占两个或三个
- `rows` :  指定文本域行数
- `readonly` :指定只读

特点 : 文本域的大小可以由用户调整



#### 按钮

1. 提交按钮: 点击表单数据发送给服务器

   `<input type="submit" value=''>`

   value 属性是设置按钮的显示文本

2. 重置按钮: 点击时，会将表单数据还原成默认状态
           `<input type="reset" value"">`

3. 普通按钮: 绑定自定义事件
           `<input type="button" value=""> `
4. `<button>按钮显示文本</button>`
   1. 按钮标签，可以在HTML中任意地方使用，需要绑定自定义事件
   2. 如果按钮标签放在form标签中使用，默认具备提交功能，等于submit

### 分组标签

```html
<fieldset>
  <legend>组标题</legend>
  <input>
</fieldset>
---组标题-----------------------
|                               |
|                               |

```


                -------------------------------

## 框架标签

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。

**iframe语法:**

`<iframe src="URL"></iframe>`

该URL指向不同的网页。

 常规属性:

- src = "url" 网页地址
- width =     一般 100%
- height = ""     高度存在问题，需要用 js.dom来解决
- scrolling="no"  不显示滚动条
- frameborder="0"  不显示边框

**标签属性**

| 属性                                                         | 值                                                           | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [frameborder](https://www.runoob.com/tags/att-iframe-frameborder.html) | 1 0                                                          | HTML5 不支持。规定是否显示 <iframe> 周围的边框。             |
| [height](https://www.runoob.com/tags/att-iframe-height.html) | *pixels*                                                     | 规定 <iframe> 的高度。                                       |
| [longdesc](https://www.runoob.com/tags/att-iframe-longdesc.html) | *URL*                                                        | HTML5 不支持。规定一个页面，该页面包含了有关 <iframe> 的较长描述。 |
| [marginheight](https://www.runoob.com/tags/att-iframe-marginheight.html) | *pixels*                                                     | HTML5 不支持。规定 <iframe> 的顶部和底部的边距。             |
| [marginwidth](https://www.runoob.com/tags/att-iframe-marginwidth.html) | *pixels*                                                     | HTML5 不支持。规定 <iframe> 的左侧和右侧的边距。             |
| [name](https://www.runoob.com/tags/att-iframe-name.html)     | *name*                                                       | 规定 <iframe> 的名称。                                       |
| [sandbox](https://www.runoob.com/tags/att-iframe-sandbox.html) | "" allow-forms allow-same-origin allow-scripts allow-top-navigation | 对 <iframe> 的内容定义一系列额外的限制。                     |
| [scrolling](https://www.runoob.com/tags/att-iframe-scrolling.html) | yes no auto                                                  | HTML5 不支持。规定是否在 <iframe> 中显示滚动条。             |
| [seamless](https://www.runoob.com/tags/att-iframe-seamless.html) | seamless                                                     | 规定 <iframe> 看起来像是父文档中的一部分。                   |
| [src](https://www.runoob.com/tags/att-iframe-src.html)       | *URL*                                                        | 规定在 <iframe> 中显示的文档的 URL。                         |
| [srcdoc](https://www.runoob.com/tags/att-iframe-srcdoc.html)**New** | *HTML_code*                                                  | 规定页面中的 HTML 内容显示在 <iframe> 中。                   |
| [width](https://www.runoob.com/tags/att-iframe-width.html)   | *pixels*                                                     | 规定 <iframe> 的宽度。                                       |



### 使用iframe来显示目标链接页面

iframe可以显示一个目标链接的页面

目标链接的属性必须使用iframe的属性，如下实例:

```html
<iframe src="demo_iframe.htm" name="iframe_a"></iframe>
<p><a href="http://www.runoob.com" target="iframe_a">RUNOOB.COM</a></p>
```



## 特殊标签

### 缩写提示标签

`<abbr></abbr>` The<abbr title="World Health Organization">WHO</abbr> was founded in 1948.

### 标签定义文档作者/所有者的联系信息。

`<address></address>`  元素的文本通常呈现为斜体。大多数浏览器会在该元素的前后添加换行。

### 图像映射

`<map><area></map>`

带有可点击区域的图像映射：

`<area>`标签定义图像映射内部的区域（图像映射指的是带有可点击区域的图像）。

`<area> `元素始终嵌套在` <map>` 标签内部

注释： <img> 标签中的 usemap 属性与 <map> 元素中的 name 相关联，以创建图像与映射之间的关系。

```html
<img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">
<map name="planetmap">
      <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
      <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
      <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
</map>
```

### 音频标签

`<audio></audio>`

标签定义声音，比如音乐或其他音频流。目前，<audio> 元素支持的3种文件格式：MP3、Wav、Ogg。

```html
<audio controls>
      <source src="horse.ogg" type="audio/ogg">
      <source src="horse.mp3" type="audio/mpeg">
</audio>
```

### 视频标签

`<video></video>`

标签定义视频，比如电影片段或其他视频流。目前<video> 元素支持三种视频格式：MP4、WebM、Ogg。

可以在 <video> 和 </video> 标签之间放置文本内容，这样不支持 <video> 元素的浏览器就可以显示出该标签的信息

```html
<video width="320" height="240" controls>
       <source src="movie.mp4" type="video/mp4">
       <source src="movie.ogg" type="video/ogg">
       <track src="subtitles_no.vtt" kind="subtitles" srclang="no" label="Norwegian">
</video>
```

可选属性：HTML5 中的新属性。

| 属性     | 值                        | 描述                                                         |
| -------- | ------------------------- | ------------------------------------------------------------ |
| autoplay | autoplay                  | 如果出现该属性，则视频在就绪后马上播放。                     |
| controls | controls                  | 如果出现该属性，则向用户显示控件，比如播放按钮。             |
| height   | pixels                    | 设置视频播放器的高度。                                       |
| loop     | loop                      | 如果出现该属性，则当媒介文件完成播放后再次开始播放。         |
| muted    | muted                     | 如果出现该属性，视频的音频输出为静音。                       |
| poster   | URL                       | 规定视频正在下载时显示的图像，直到用户点击播放按钮。         |
| preload  | auto  \| metadata \| none | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
| src      | URL                       | 要播放的视频的 URL。                                         |
| width    | pixels                    | 设置视频播放器的宽度。                                       |

- `<track>` 标签为媒体元素（比如 <audio> and <video>）规定外部文本轨道。字幕，弹屏

- `<source>`标签为媒体元素（比如 <video> 和 <audio>）定义媒体资源。

  `<source>` 标签允许您规定两个视频/音频文件共浏览器根据它对媒体类型或者编解码器的支持进行选择。

  - media	media_query	规定媒体资源的类型，供浏览器决定是否下载。
  - src	    URL	        规定媒体文件的 URL。
  - type	MIME_type	规定媒体资源的 MIME 类型





    
    <bdi></bdi>
        bdi 指的是 bidi 隔离（Bi-directional Isolation）。
        <bdi> 标签允许您设置一段文本，使其脱离其父元素的文本方向设置。
        在发布用户评论或其他您无法完全控制的内容时，该标签很有用。
        
    <bdo dir="rtl"></bdo>
        <p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
        bdo元素一般用于把一段文本的方向规定为与周围文本的自然方向相反的方向。方向由必需属性dir=rtl ltr指定。
    
    <dfn>定义项目</dfn><br>
    <code>一段电脑代码</code><br>
    <samp>计算机样本</samp><br>
    <kbd>键盘输入</kbd><br>
    <var>变量</var>
    <mark> 标签定义带有记号的文本。请在需要突出显示文本时使用标签 </mark>
    
    <cite></cite> 
            <cite> 标签定义作品（比如书籍、歌曲、电影、电视节目、绘画、雕塑等等）的标题。
            注释：人名不属于作品的标题。


    <ruby></ruby>    标签定义及使用说明
        <ruby> 标签定义 ruby 注释（中文注音或字符）。
    
        在东亚使用，显示的是东亚字符的发音。
    
        将 <ruby> 标签与 <rt> 和 <rp> 标签一起使用： 
        <ruby> 元素由一个或多个需要解释/发音的字符和一个提供该信息的 <rt> 元素组成，还包括可选的 <rp> 元素，定义当浏览器不支持 "ruby" 元素时显示的内容。
        eg:
            <ruby>
                汉 <rp>(</rp><rt>Han</rt><rp>)</rp>
                字 <rp>(</rp><rt>zi</rt><rp>)</rp>
            </ruby>
    
    <ins></ins> 标签
            提示：您也可以看看标记已删除文本的 <del> 标签。
    
            提示：<del> 和 <ins>
    
    <progress></progress> 标签定义运行中的任务进度（进程）。进度条
        提示：请将 <progress> 标签与 JavaScript 一起使用来显示任务的进度。
        eg:
            <progress value="22" max="100"></progress>
    
        属性	       值	         描述
        max	        number	    规定需要完成的值。
        value	    number	    规定进程的当前值。


    <meter></meter>标签定义度量衡。仅用于已知最大和最小值的度量。
        磁盘使用情况，查询结果的相关性等。
        eg:
            <meter value="2" min="0" max="10">2 out of 10</meter><br>
            <meter value="0.6">60%</meter>
    
        属性	        值	        描述
        form	    form_id	    规定 <meter> 元素所属的一个或多个表单。
        high	    number	    规定被界定为高的值的范围。
        low	        number	    规定被界定为低的值的范围。
        max	        number	    规定范围的最大值。
        min  	    number	    规定范围的最小值。
        optimum	    number	    规定度量的最优值。
        value	    number	    必需。规定度量的当前值。


    <object></object>定义一个嵌入的对象。此元素允许您规定插入 HTML 文档中的对象的数据和参数，以及可用来显示和操作数据的代码。
            <object> 标签用于包含对象，比如图像、音频、视频、Java applets、ActiveX、PDF 以及 Flash。
            如果未显示 object 元素，就会执行位于 <object> 和 </object> 之间的代码。
            通过这种方式，我们能够嵌套多个 object 元素（每个对应一个浏览器）。
        eg:
        <object width="400" height="400" data="helloworld.swf"></object>
    
        属性	    值	            描述
        data	    URL	         规定对象使用的资源的 URL。
        height	    pixels	     规定对象的高度。
        width	    pixels	     规定对象的宽度。
        name	    name	     为对象规定名称
        orm     	form_id	     规定对象所属的一个或多个表单。
        ype	        MIME_type	 规定 data 属性中规定的数据的 MIME 类型。
        usemap  	#mapname	 规定与对象一同使用的客户端图像映射的名称。


    <details></details>
            <details> 标签规定了用户可见的或者隐藏的需求的补充细节。
            <details> 标签用来供用户开启关闭的交互式控件。任何形式的内容都能被放在 <details> 标签里边。
            <details> 元素的内容对用户是不可见的，除非设置了 open 属性。
        eg:
            <details>
                <summary>Copyright 1999-2011.</summary>
                <p> - by Refsnes Data. All Rights Reserved.</p>
                <p>All content and graphics on this web site are the property of the company Refsnes Data.</p>
            </details>
    
         属性	    值	        描述
        open	    open	    规定 details 是否可见
    
    <summary></summary><summary> 标签为 <details> 元素定义一个可见的标题。 当用户点击标题时会显示出详细信息。
        <summary> 元素应该是 <details> 元素的第一个子元素。







## Canvas

`<canvas>` 元素用于图形的绘制，通过脚本 (通常是JavaScript)来完成.

`<canvas>` 标签只是图形容器，您必须使用脚本来绘制图形。

[学习 HTML5 Canvas 这一篇文章就够了](https://www.runoob.com/w3cnote/html5-canvas-intro.html)



## [内联 SVG](https://www.runoob.com/svg/svg-tutorial.html)

- SVG 指可伸缩矢量图形 (Scalable Vector Graphics)
- SVG 用于定义用于网络的基于矢量的图形
- SVG 使用 XML 格式定义图形
- SVG 图像在放大或改变尺寸的情况下其图形质量不会有损失
- SVG 是万维网联盟的标准

**SVG优势**

与其他图像格式相比（比如 JPEG 和 GIF），使用 SVG 的优势在于：

- SVG 图像可通过文本编辑器来创建和修改
- SVG 图像可被搜索、索引、脚本化或压缩
- SVG 是可伸缩的
- SVG 图像可在任何的分辨率下被高质量地打印
- SVG 可在图像质量不下降的情况下被放大



## Video(视频)

语法：

```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
您的浏览器不支持Video标签。
</video>
```

`<video>` 元素提供了 播放、暂停和音量控件来控制视频。


同时 <video> 元素也提供了 width 和 height 属性控制视频的尺寸.如果设置的高度和宽度，所需的视频空间会在页面加载时保留。如果没有设置这些属性，浏览器不知道大小的视频，浏览器就不能再加载时保留特定的空间，页面就会根据原始视频的大小而改变。

`<video> 与</video>` 标签之间插入的内容是提供给不支持 video 元素的浏览器显示的。

`<video>` 元素支持多个 `<source>` 元素. `<source>` 元素可以链接不同的视频文件。浏览器将使用第一个可识别的格式

当前， <video> 元素支持三种视频格式： MP4, WebM, 和 Ogg:

- MP4 = 带有 H.264 视频编码和 AAC 音频编码的 MPEG 4 文件
- WebM = 带有 VP8 视频编码和 Vorbis 音频编码的 WebM 文件
- Ogg = 带有 Theora 视频编码和 Vorbis 音频编码的 Ogg 文件



HTML5 `<video>` 和 `<audio>` 元素同样拥有方法、属性和事件。

`<video>` 和 `<audio>`元素的方法、属性和事件可以使用JavaScript进行控制.

其中的方法用于播放、暂停以及加载等。其中的属性（比如时长、音量等）可以被读取或设置。其中的 DOM 事件能够通知您，比方说，`<video>` 元素开始播放、已暂停，已停止，等等。



`<video>`定义一个视频

| 属性                                                         | 值                 | 描述                                                         |
| :----------------------------------------------------------- | :----------------- | :----------------------------------------------------------- |
| [autoplay](https://www.runoob.com/tags/att-video-autoplay.html) | autoplay           | 如果出现该属性，则视频在就绪后马上播放。                     |
| [controls](https://www.runoob.com/tags/att-video-controls.html) | controls           | 如果出现该属性，则向用户显示控件，比如播放按钮。             |
| [height](https://www.runoob.com/tags/att-video-height.html)  | *pixels*           | 设置视频播放器的高度。                                       |
| [loop](https://www.runoob.com/tags/att-video-loop.html)      | loop               | 如果出现该属性，则当媒介文件完成播放后再次开始播放。         |
| [muted](https://www.runoob.com/tags/att-video-muted.html)    | muted              | 如果出现该属性，视频的音频输出为静音。                       |
| [poster](https://www.runoob.com/tags/att-video-poster.html)  | *URL*              | 规定视频正在下载时显示的图像，直到用户点击播放按钮。         |
| [preload](https://www.runoob.com/tags/att-video-preload.html) | auto metadata none | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
| [src](https://www.runoob.com/tags/att-video-src.html)        | *URL*              | 要播放的视频的 URL。                                         |
| [width](https://www.runoob.com/tags/att-video-width.html)    | *pixels*           | 设置视频播放器的宽度。                                       |



`<source>`定义多种媒体资源,比如 <video> 和<audio>

| 属性                                                       | 值            | 描述                                       |
| :--------------------------------------------------------- | :------------ | :----------------------------------------- |
| [media](https://www.runoob.com/tags/att-source-media.html) | *media_query* | 规定媒体资源的类型，供浏览器决定是否下载。 |
| [src](https://www.runoob.com/tags/att-source-src.html)     | *URL*         | 规定媒体文件的 URL。                       |
| [type](https://www.runoob.com/tags/att-source-type.html)   | *MIME_type*   | 规定媒体资源的 MIME 类型。                 |



`<track>`定义在媒体播放器文本轨迹

| 属性                                                         | 值                                                | 描述                                                         |
| :----------------------------------------------------------- | :------------------------------------------------ | :----------------------------------------------------------- |
| [default](https://www.runoob.com/tags/att-track-default.html) | default                                           | 规定该轨道是默认的。如果用户没有选择任何轨道，则使用默认轨道。 |
| [kind](https://www.runoob.com/tags/att-track-kind.html)      | captions chapters descriptions metadata subtitles | 规定文本轨道的文本类型。                                     |
| [label](https://www.runoob.com/tags/att-track-label.html)    | *text*                                            | 规定文本轨道的标签和标题。                                   |
| [src](https://www.runoob.com/tags/att-track-src.html)        | *URL*                                             | 必需的。规定轨道文件的 URL。                                 |
| [srclang](https://www.runoob.com/tags/att-track-srclang.html) | *language_code*                                   | 规定轨道文本数据的语言。如果 kind 属性值是 "subtitles"，则该属性是必需的。 |



### [HTML 音频/视频 DOM 参考手册](https://www.runoob.com/tags/ref-av-dom.html)

```html
<!DOCTYPE html> 
<html> 
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body> 

<div style="text-align:center"> 
  <button onclick="playPause()">播放/暂停</button> 
  <button onclick="makeBig()">放大</button>
  <button onclick="makeSmall()">缩小</button>
  <button onclick="makeNormal()">普通</button>
  <br> 
  <video id="video1" width="420">
    <source src="mov_bbb.mp4" type="video/mp4">
    <source src="mov_bbb.ogg" type="video/ogg">
    您的浏览器不支持 HTML5 video 标签。
  </video>
</div> 

<script> 
var myVideo=document.getElementById("video1"); 

function playPause()
{ 
	if (myVideo.paused) 
	  myVideo.play(); 
	else 
	  myVideo.pause(); 
} 

	function makeBig()
{ 
	myVideo.width=560; 
} 

	function makeSmall()
{ 
	myVideo.width=320; 
} 

	function makeNormal()
{ 
	myVideo.width=420; 
} 
</script> 

</body> 
</html>
```

