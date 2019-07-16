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

### HTML 语法规范  非常宽松

1. HTML 标签不区分大小写的，BODY Body body 标签可以大写，推荐小写
2. 在涉及标签嵌套时保持内部标签适当缩进，增加代码可读性
3. 添加适量注释

### HTML 的注释

语法： `<!--  注释内容  -->`

1. HTML 的注释不能嵌套
2. 标签名中不能嵌套使用注释



## 文档基本结构
1. `<html></html>`标签，表示文档的开始和结束，网页中所有的内容都必须写在html标签中

2. `<head></head>`标签，表示网页的头部内容，设置网页的标题，字符集，引入外部文件等

   ```html
   <title>WeiTianHua</title>
   <meta charset="utf-8">
   ```

3. `<body></body>`标签，表示网页的主体内容，所有呈现在网页窗口中的内容，都应该写在body标签中

4. 标签属性   标签属性用来修饰或补充当前的标签内容

   语法 :  <标签名 属性名="属性值"></标签名>

   每个标签中都可以添加一个或多个标签属性，多个属性之间使用空格隔开



## HTML常用标签
1. 文档类型声明`<!doctype html>`

   对当前的文档类型及版本做出指定(这种声明方式是HTML5的声明方式)关系到页面元素的渲染效果 CSS
   ,书写到`<html>`之前，文档开篇

2. 设置网页的标题，字符集，和选项卡图标

   ```html
   <meta charset="utf-8" />
   <title>WeiTianHua</title>
   <!-- 头图片链接  rel=大小类型  href=路径 type=进一步说明图片类型-->
   <link rel="shortout icon" href="201_1440x900.jpg" type="image/x-icon">
   ```

3. 标题标签

   `<h1>`一级标题`</h1>`

   ...
   `<h6>`六级标题`</h6>`

   标题标签的内容，与普通文本相比，自带文本加粗效果,从 h1 ~ h6 字体大小逐渐减小

4. 常用文本标签

   1. 段落标签,自占一行`<p>`标签内容`</p>`

   2. `<span>`行分区标签`</span>`

   3. `<label>`文本标签`</label>`

   4. `<b></b> ``<strong></strong> `加粗标签, h5之后推荐使用有语义标签 strong 表示强调

   5. `<s></s>`删除线

   6. `<i></i> `斜体显示

   7. `<u></u>`  为文本添加下划线

   8. 上下标 标签

      上标:  ` X<sup>2</sup>`

      下标:  `X<sub>1</sub>`

   9. 格式标签

      换行标签 :` <br/>`

      水平线标签 :` <hr/>`

5. 字体实体    全部 <http://www.w3school.com.cn/tags/html_ref_entities.html>
   1. HTML文档中会忽略多余的空格和换行，只显示为一个空格
   2. 针对HTML文档的特殊性，比如对空格，<>的处理，需要采用特殊的语法表示空格和<>等其他符号

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



## 标签
### 列表标签

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

   

### 图片标签

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

### 超链接标签

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

通过定义锚点，实现跳转至指定文件的指定位置

使用：

1. 定义超链接，链接到本页的指定位置
2. 在页面相应位置添加锚点
    `<a href="#7">7.条目</a>`
   `<h1 id='7'></h1>`锚点定位

**图片超链接**

```html
 <a href="">
     <img src="">
</a>
```



### 表格标签
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



## 表单

作用: 用来接收用户的数据并提交给服务器
表单二要素

        1. 表单元素  `<form></form>`
           2. 表单控件

### 表单元素

**标签**

`<form></form>` 用来提交数据到服务器，表单控件都应写在此标签中

**标签属性**

`method` : 用来设置数据提交方式

​	取值: 	

>`get`(默认)
>
>>1. 数据会以参数的形式拼接在url后面
>>2. 是明文提交，安全性较低
>>3. 最大提交数据2kb
>
>`post `
>
>>1. 数据会打包在请求头中
>>2. 隐式提交，安全性较高
>>3. 没有数据大小限制

`action`  : 必填，指定数据的提交地址

`enctype`   : 指定数据的编码方式

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

`<input>`

标签属性

1. `type` 指定控件类型
2. `name` 指定控件名称，缺少无法提交
3. `value` 指定控件的值，可以通过 js 动态获取
4. `maxlength` 指定最大输入字符数
5. `placeholder` 设置提示文本
6. `autocomplete` 设置是否自动补全 on/off 

#### 单选按钮和复选框

**语法:** 

单选按钮 : `<input type="radio">`

复选框  : `<input type="checkbox">`

**标签属性:**

`name`定义控件名称

​	一组的按钮控件名称必须保持一致

`value` 定义控件的值

​	最终将发送给服务器，按钮的value属性必须指定

`checked`

​	表示默认选择当前按钮

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

#### 下拉选择框

```html
<select name="address">
      <option value="beijing">北京</option>
      <option value="shanghai">上海</option>
</select>
```

第一个位预选中
            预选择选项  selected

#### 文本域

语法: `<textarea name="uinfo"></textarea>`

标签属性:
            `cols` :  指定文本域默认宽度，宽度是通过列数控制的
                   	以英文字符为准，中文减半
            `rows` :  指定文本域行数
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



## HTML 框架

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。

**iframe语法:**

`<iframe src="URL"></iframe>`

该URL指向不同的网页。

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

