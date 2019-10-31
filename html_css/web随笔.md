

## redirect

### HTML 重定向/Meta 刷新
将下面 HTML 重定向代码放在网页的 <head> 节点内：

```html
<meta HTTP-EQUIV="REFRESH" content="0; url=http://www.yourdomain.com"> 
```

上述代码立即将访客重定向到另外一个页面，你可以修改 content 中 的 0 这个值来表示几秒钟后才进行重定向。

例如 content="3; url=http://www.oschina.net/" 表示三秒后再重定向。



### Javascript URL Redirect


```html
<head>
	<script type="text/javascript">
		window.location.href='http://www.newdomain.com/';
	</script>
</head>
```



前端标签
    <fieldset>
        <legend>aaaa</legend>
        ---aaaa-----------------------
        |                                             |
        |                                             |

        |                                             |
        -------------------------------

1.CSS文件首行写 :@charset "utf-8";
    表明CSS文件的页面编码为UTF-8。。如果这个CSS的文件编码也是UTF-8的话。
    那么在浏览器中看到的CSS文件的页面中中文的注释或者中文字体就可以正确显示为中文，
    如果CSS的文件编码和页面不一致的话。那么这个CSS文件的中文则会显示为乱码。
    特别是定义中文字体的时候。就不能正确识别。其他则没有多大影响。



3.font: 15px "Microsoft YaHei", Arial, Helvetica, sans-serif; 多个字体默认显示

4.转换元素类型 **多个地方出现
    属性 : display
    取值 :  1.inline 行内元素
            2.block  块元素
            3.inline-block 行内块元素
            4.none  元素隐藏,在文档中不占位

5.a 标签属性    ** a标签不能继承外部元素颜色，要单独设置 
        target : 设置目标文件的打开方式，默认在当前窗口打开，覆盖原文本
            取值:  _self  默认值
                   _blank  新建页面窗口打开
      
        text-decoration: none; 取消下划线(CSS)

动态伪类选择器,所有元素都可用
    1. :hover
        鼠标滑过元素时的状态
    2. :active
        鼠标点按元素时的状态,激活
        超链接使用注意:
             1.超链接可以设置四种状态的样式，
                    书写时必须按以下顺序定义
                            :link       访问前,超链接独有
                            :visitek    访问后,超链接独有
                            :hover
                            :active
        3 :focus
        表示文本框或密码框在获取焦点时的状态
        焦点状态: 正接受输入或编辑时的状态
                   input:focus{
                       样式
                   }









我们可以看到使用header我们定义了一篇文章的标题和内容。这里header标签的使用并不是页面的页头，而是文章的页头。
所以在HTML5中，header的使用更加灵活，你可以根据你的需要来定义和组织document结构。

```html
<header>
    <h1>HTML5基本标签使用，header，Nav和footer</h1>
    <div class="post-meta">
        <p>作者信息:gbin1.com</a> <span class="category">文章创建类别：HTML5/CSS3</span></p>  
    </div>
</header>
```



Nav标签全称navigation，顾名思义，是导航的意思
页面中的一个用来链接到其它页面或者当前页面的区域：一个含有导航链接的区域
这里非常清楚的定义了nav标签的功能，这里和header类似并没有指定必须是主导航，也可以是页面其它部分的子导航。

```html
<nav>
    <ul>
        <li><a href="#html5">HTML5文章介绍</a></li>
        <li><a href="#css3">CSS3文章介绍</a></li>
        <li><a href="#jquery">jQuery文章介绍</a></li>
    <ul>
</nav>
```



footer标签，即，页底标签。使用这个标签你可以定义页面的低端结构，当然，和上面我们介绍header标签
或者nav标签一样，它并不是仅仅使用在整个页面的页尾处

```html
<footer>
    <div class="tags">
        <span class="tags-title">相关标签</span> <a href="#" rel="tag">html5</a>, <a href="#" rel="tag">nav</a>, <a href="#" rel="tag">header</a>, <a href="#" rel="tag">footer</a>
    </div>
    <div class="source">
        <div>来源：<a href="http://gbin1.com">html5/css3教程</a></div> 
    </div>
</footer>
```



```html
<article> 标签定义外部的内容。
    外部内容可以是来自一个外部的新闻提供者的一篇新的文章，或者来自 blog 的文本，或者是来自论坛的文本。
    亦或是来自其他外部源内容
    <article> 标签的内容独立于文档的其余部分。
<article>
    <a href="http://www.apple.com">Safari 5 released</a><br />
    7 Jun 2010. Just after the announcement of the new iPhone 4 at WWDC, 
    Apple announced the release of Safari 5 for Windows and Mac......
</article>
```



redirect
    1. HTML 重定向/Meta 刷新
    将下面 HTML 重定向代码放在网页的 <head> 节点内：
    <meta HTTP-EQUIV="REFRESH" content="0; url=http://www.yourdomain.com"> 
    上述代码立即将访客重定向到另外一个页面，你可以修改 content 中 的 0 这个值来表示几秒钟后才进行重定向。
    例如 content="3; url=http://www.oschina.net/" 表示三秒后再重定向。


    2. Javascript URL Redirect

    <head>
    <script type="text/javascript">
    window.location.href='http://www.newdomain.com/';
    </script>
    </head>


1.CSS文件首行写 :@charset "utf-8";
    表明CSS文件的页面编码为UTF-8。。如果这个CSS的文件编码也是UTF-8的话。
    那么在浏览器中看到的CSS文件的页面中中文的注释或者中文字体就可以正确显示为中文，
    如果CSS的文件编码和页面不一致的话。那么这个CSS文件的中文则会显示为乱码。
    特别是定义中文字体的时候。就不能正确识别。其他则没有多大影响。

2. * { margin: 0; padding: 0 }
    * 这东西叫“通配符”用来匹配页面上所有元素。方便清除默认样式

3.font: 15px "Microsoft YaHei", Arial, Helvetica, sans-serif; 多个字体默认显示

4.转换元素类型 **多个地方出现
    属性 : display
    取值 :  1.inline 行内元素
            2.block  块元素
            3.inline-block 行内块元素
            4.none  元素隐藏,在文档中不占位

5.a 标签属性    ** a标签不能继承外部元素颜色，要单独设置 
        target : 设置目标文件的打开方式，默认在当前窗口打开，覆盖原文本
            取值:  _self  默认值
                   _blank  新建页面窗口打开
      
        text-decoration: none; 取消下划线(CSS)


动态伪类选择器,所有元素都可用
    1. :hover
        鼠标滑过元素时的状态
    2. :active
        鼠标点按元素时的状态,激活
        超链接使用注意:
             1.超链接可以设置四种状态的样式，
                    书写时必须按以下顺序定义
                            :link       访问前,超链接独有
                            :visitek    访问后,超链接独有
                            :hover
                            :active
    3 :focus
        表示文本框或密码框在获取焦点时的状态
        焦点状态: 正接受输入或编辑时的状态
                   input:focus{
                       样式
                   }

我们可以看到使用header我们定义了一篇文章的标题和内容。这里header标签的使用并不是页面的页头，而是文章的页头。
所以在HTML5中，header的使用更加灵活，你可以根据你的需要来定义和组织document结构。
<header>
    <h1>HTML5基本标签使用，header，Nav和footer</h1>
    <div class="post-meta">
        <p>作者信息:gbin1.com</a> <span class="category">文章创建类别：HTML5/CSS3</span></p>  
    </div>
</header>


Nav标签全称navigation，顾名思义，是导航的意思
页面中的一个用来链接到其它页面或者当前页面的区域：一个含有导航链接的区域
这里非常清楚的定义了nav标签的功能，这里和header类似并没有指定必须是主导航，也可以是页面其它部分的子导航。
<nav>
    <ul>
        <li><a href="#html5">HTML5文章介绍</a></li>
        <li><a href="#css3">CSS3文章介绍</a></li>
        <li><a href="#jquery">jQuery文章介绍</a></li>
    <ul>
</nav>

footer标签，即，页底标签。使用这个标签你可以定义页面的低端结构，当然，和上面我们介绍header标签
或者nav标签一样，它并不是仅仅使用在整个页面的页尾处
<footer>
    <div class="tags">
        <span class="tags-title">相关标签</span> <a href="#" rel="tag">html5</a>, <a href="#" rel="tag">nav</a>, <a href="#" rel="tag">header</a>, <a href="#" rel="tag">footer</a>
    </div>
    <div class="source">
        <div>来源：<a href="http://gbin1.com">html5/css3教程</a></div> 
    </div>
</footer>


<article> 标签定义外部的内容。
    外部内容可以是来自一个外部的新闻提供者的一篇新的文章，或者来自 blog 的文本，或者是来自论坛的文本。
    亦或是来自其他外部源内容
    <article> 标签的内容独立于文档的其余部分。
<article>
    <a href="http://www.apple.com">Safari 5 released</a><br />
    7 Jun 2010. Just after the announcement of the new iPhone 4 at WWDC, 
    Apple announced the release of Safari 5 for Windows and Mac......
</article>
            
​            