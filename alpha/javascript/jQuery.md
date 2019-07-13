[TOC]





## CDN

百度

```html
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
```

Microsoft:

```html
<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.min.js"></script>
```





## jQuery对象

### 工厂函数 -  $()

- **\$符号是jQuery对象的标志,jQuery对象以$符号与原生的方法区分**

  注意:	原生对象使用原生的方法, jQuery对象使用jQuery方法,不能混用

- **jQuery通过封装，将原生的DOM对象包装成jQuery对象**

### 原生JS对象与jQuery对象转换

1. DOM对象 转换 jQuery对象

   使用$()包装原生DOM对象，返回jQuery对象

   ```javascript
   var h1 =document.getElementsByTagName('h1')[0];
   var $h1 =$(h1);
   ```

   this 当前对象转换

   ```javascript
   $(this).css("background","gray")
   ```

2. jQuery对象 转换 DOM对象

   ```javascript
   var h1 = $('h1')[0] | $h1[0];
   var h1 = $('h1').get(0) | $h1.get(0);
   ```

   

## jQuery选择器

### 基础选择器

1. `$('div')`     标签选择器
2. `$('#id')`    ID选择器
3. ` $('.className')`     类选择器
4. ` $('selector1,selector2,...')`  群组选择器

### 层级选择器(都是从当前元素向后匹配)

1. `$('selector1 selector2');`   后代选择器
2. ` $('selector1>selector2') `     子代选择器
3. `$('selector1+selector2')`     相邻兄弟选择器
           匹配紧靠在selector1后面的兄弟元素，且满足selector2,否则匹配失败
4. `$('selector1~selector2')`     通用兄弟选择器
           匹配紧跟在selector1后面所有满足selector2的兄弟元素

### 过滤选择器(不筛选层级关系，全部包含在内)

1. `:first`匹配一组元素中的第一个元素
    
    ```javascript
    $("p:first");//选取第一个 <p> 元素
    $("ul li:first");//选取第一个 <ul> 元素的第一个 <li> 元素
    ```
    
2. `:last`   匹配一组元素中的最后一个

3. `:not()`否定筛选，匹配除()中列出的元素外，所有元素

    ```javascript
    $(":not(selector1,selector2)");
    ```

4. `:odd`匹配偶数行对应的元素

    ```javascript
    $("#mytable td:odd");
    ```

5. `:even`     匹配奇数行对应的元素

6. `:eq(index)`    匹配指定下标对应的元素,下标从 0 开始

    ```javascript
    $("div p:eq(2)"); //索引选择器 div下的第三个p元素（索引是从0开始）
    ```

7. `:lt(index)`    匹配下标小于index的元素

8. `:gt(index)`    匹配下标大于index的元素 

### 属性选择器

根据元素的标签属性来获取元素

1. `$('[attribute]')`  获取属性，名为attribute的元素
   
   ```javascript
   $("[href]");//选取带有 href 属性的元素
   $('[id]');//包含id属性的元素
   ```
   
2. `$('[attribute=value]')`    获取属性名等于attribute，属性值为value的元素

      ```javascript
      $("a[target='_blank']");//选取所有 target 属性值等于 "_blank" 的 <a> 元素
      $("a[href='www.baidu.com']");  //属性选择器
      ```

3. `[attribute!=value]`   匹配属性值不等于value元素

4. `[attribute^=value]`    匹配属性值以value开头的元素,字符匹配

5. `[attribute$=value]`   匹配属性值以value结尾的元素,字符匹配

6. [`attribute*=value]`     匹配属性值中存在value的元素



### 子元素过滤选择器

1. `:first-child`  匹配属于其父元素中的第一个子元素

   ```javascript
$("ul li:first-child");//选取每个 <ul> 元素的第一个 <li> 元素
   ```

2. `:last-child`  匹配属于其父元素中最后一个子元素

3. `:nth-child(n)`匹配属于其父元素中第n个子元素，给数值

   注意:

   1. n给具体数值，表示具体行号，从1开始计数
   2. n给关键字或表达式，表示传入下标，根据下标获取元素(从下标0开始)
       eg: n=even 奇数下标取元素，对应偶数行
              n=odd  偶数下标取元素，对应奇数行

### 伪类选择器

1. `$(":checked")`  表示表单控件-按钮的选中状态
2. `$(":button")`    选取所有 type="button" 的 <input> 元素 和 <button> 元素
3. `$("p:contains(test)") `    包含text内容的p元素
4. `$(":emtyp")` 所有空标签（不包含子标签和内容的标签）parent 相反
5. `$(":hidden")`所有隐藏元素 visible 
6. `$("input:enabled")` 选取所有启用的表单元素
7. `$(":disabled")`  所有不可用的元素
8. `$("input:checked")`  获取所有选中的复选框单选按钮等
9. `$("select option:selected")`  获取选中的选项元素



## 事件

1. `ready()` 等待文档加载完毕(onload)
   原生: 

   ```javascript
   window.onload = function(){};
   jQuery:
         1.$(document).ready(function(){
               ......
           });
         2.$().ready(function(){
               ......
           });
         3.$(function(){});
   ```

   jQuery:

   ```javascript
   1.$(document).ready(function(){
               ......
           });
   2.$().ready(function(){
               ......
           });
   3.$(function(){});
   ```

   区别:
              1. 原生onload事件函数不能重复调用，重复书写，后面的代码会将前面的onload覆盖掉,Query中优化了ready方法，可以重复使用，不会产生覆盖问题，所有的代码都会执行
              2. jQuery 的入口函数是在 html 所有标签(DOM)都加载之后，就会去执行。JavaScript 的 window.onload 事件是等到所有内容，包括外部图片之类的文件加载完后，才会执行。

2. 事件绑定
   原生的事件处理函数不变，jQuery提供了新的绑定方式
   注意:   事件函数名省略on前缀

   ```javascript
   1.$obj.事件函数名(function(){});
       eg:
           $div.click(function(){});
   2. bind(事件名称，function);
       eg:
           $div.bind("click",function(){});
       bind()方法的底层实现:
           $div.on("click",function(){});
   
       $('h1').click(function(){
           alert('h1被点击');
       });
       $('p').bind("click",function(){
           alert("p被点击");
       });
   ```

   

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [bind()](http://www.w3school.com.cn/jquery/event_bind.asp)   | 向匹配元素附加一个或更多事件处理器                           |
| [blur()](http://www.w3school.com.cn/jquery/event_blur.asp)   | 触发、或将函数绑定到指定元素的 blur 事件                     |
| [change()](http://www.w3school.com.cn/jquery/event_change.asp) | 触发、或将函数绑定到指定元素的 change 事件                   |
| [click()](http://www.w3school.com.cn/jquery/event_click.asp) | 触发、或将函数绑定到指定元素的 click 事件                    |
| [dblclick()](http://www.w3school.com.cn/jquery/event_dblclick.asp) | 触发、或将函数绑定到指定元素的 double click 事件             |
| [delegate()](http://www.w3school.com.cn/jquery/event_delegate.asp) | 向匹配元素的当前或未来的子元素附加一个或多个事件处理器       |
| [die()](http://www.w3school.com.cn/jquery/event_die.asp)     | 移除所有通过 live() 函数添加的事件处理程序。                 |
| [error()](http://www.w3school.com.cn/jquery/event_error.asp) | 触发、或将函数绑定到指定元素的 error 事件                    |
| [event.isDefaultPrevented()](http://www.w3school.com.cn/jquery/event_isdefaultprevented.asp) | 返回 event 对象上是否调用了 event.preventDefault()。         |
| [event.pageX](http://www.w3school.com.cn/jquery/event_pagex.asp) | 相对于文档左边缘的鼠标位置。                                 |
| [event.pageY](http://www.w3school.com.cn/jquery/event_pagey.asp) | 相对于文档上边缘的鼠标位置。                                 |
| [event.preventDefault()](http://www.w3school.com.cn/jquery/event_preventdefault.asp) | 阻止事件的默认动作。                                         |
| [event.result](http://www.w3school.com.cn/jquery/event_result.asp) | 包含由被指定事件触发的事件处理器返回的最后一个值。           |
| [event.target](http://www.w3school.com.cn/jquery/event_target.asp) | 触发该事件的 DOM 元素。                                      |
| [event.timeStamp](http://www.w3school.com.cn/jquery/event_timeStamp.asp) | 该属性返回从 1970 年 1 月 1 日到事件发生时的毫秒数。         |
| [event.type](http://www.w3school.com.cn/jquery/event_type.asp) | 描述事件的类型。                                             |
| [event.which](http://www.w3school.com.cn/jquery/event_which.asp) | 指示按了哪个键或按钮。                                       |
| [focus()](http://www.w3school.com.cn/jquery/event_focus.asp) | 触发、或将函数绑定到指定元素的 focus 事件                    |
| [keydown()](http://www.w3school.com.cn/jquery/event_keydown.asp) | 触发、或将函数绑定到指定元素的 key down 事件                 |
| [keypress()](http://www.w3school.com.cn/jquery/event_keypress.asp) | 触发、或将函数绑定到指定元素的 key press 事件                |
| [keyup()](http://www.w3school.com.cn/jquery/event_keyup.asp) | 触发、或将函数绑定到指定元素的 key up 事件                   |
| [live()](http://www.w3school.com.cn/jquery/event_live.asp)   | 为当前或未来的匹配元素添加一个或多个事件处理器               |
| [load()](http://www.w3school.com.cn/jquery/event_load.asp)   | 触发、或将函数绑定到指定元素的 load 事件                     |
| [mousedown()](http://www.w3school.com.cn/jquery/event_mousedown.asp) | 触发、或将函数绑定到指定元素的 mouse down 事件               |
| [mouseenter()](http://www.w3school.com.cn/jquery/event_mouseenter.asp) | 触发、或将函数绑定到指定元素的 mouse enter 事件              |
| [mouseleave()](http://www.w3school.com.cn/jquery/event_mouseleave.asp) | 触发、或将函数绑定到指定元素的 mouse leave 事件              |
| [mousemove()](http://www.w3school.com.cn/jquery/event_mousemove.asp) | 触发、或将函数绑定到指定元素的 mouse move 事件               |
| [mouseout()](http://www.w3school.com.cn/jquery/event_mouseout.asp) | 触发、或将函数绑定到指定元素的 mouse out 事件                |
| [mouseover()](http://www.w3school.com.cn/jquery/event_mouseover.asp) | 触发、或将函数绑定到指定元素的 mouse over 事件               |
| [mouseup()](http://www.w3school.com.cn/jquery/event_mouseup.asp) | 触发、或将函数绑定到指定元素的 mouse up 事件                 |
| [one()](http://www.w3school.com.cn/jquery/event_one.asp)     | 向匹配元素添加事件处理器。每个元素只能触发一次该处理器。     |
| [ready()](http://www.w3school.com.cn/jquery/event_ready.asp) | 文档就绪事件（当 HTML 文档就绪可用时）                       |
| [resize()](http://www.w3school.com.cn/jquery/event_resize.asp) | 触发、或将函数绑定到指定元素的 resize 事件                   |
| [scroll()](http://www.w3school.com.cn/jquery/event_scroll.asp) | 触发、或将函数绑定到指定元素的 scroll 事件                   |
| [select()](http://www.w3school.com.cn/jquery/event_select.asp) | 触发、或将函数绑定到指定元素的 select 事件                   |
| [submit()](http://www.w3school.com.cn/jquery/event_submit.asp) | 触发、或将函数绑定到指定元素的 submit 事件                   |
| [toggle()](http://www.w3school.com.cn/jquery/event_toggle.asp) | 绑定两个或多个事件处理器函数，当发生轮流的 click 事件时执行。 |
| [trigger()](http://www.w3school.com.cn/jquery/event_trigger.asp) | 所有匹配元素的指定事件                                       |
| [triggerHandler()](http://www.w3school.com.cn/jquery/event_triggerhandler.asp) | 第一个被匹配元素的指定事件                                   |
| [unbind()](http://www.w3school.com.cn/jquery/event_unbind.asp) | 从匹配元素移除一个被添加的事件处理器                         |
| [undelegate()](http://www.w3school.com.cn/jquery/event_undelegate.asp) | 从匹配元素移除一个被添加的事件处理器，现在或将来             |
| [unload()](http://www.w3school.com.cn/jquery/event_unload.asp) | 触发、或将函数绑定到指定元素的 unload 事件                   |









## 遍历节点对象数组

each()

```javascript
$(".imgNav li").each(function(){
    $(this).css("background","gray")
}); 
```



## jQuery操作DOM节点

### 内容操作

        1. html('') 方法
            为元素设置标签内容，可以识别标签
            等价于原生的 innerHTML
            
        2. text('') 方法
            为元素设置文本内容，不能设别标签
            等价于原生的 innerText
            
        3. val() 方法
            
            用来读取或设置文本框或表单控件的值


​            

### 属性操作

```
1. attr() 方法
	设置或读取指定的标签属性,动态添加id/class属性，对应选择器为元素设置样式
	eg :
    	$("div").attr("id","d1");//设置id为d1
    	console.log($("div").attr("id"));
2. removeAttr() 方法
	移除指定的属性，参数为属性名
```



### 样式操作

```
1. addClass("classValue")
   添加class属性值，对应类选择器样式
   eg:
   	$('h2').addClass('c1 c2');
   	$('h3').addClass('c1').addClass('c2');//链式调用
2. removeClass('classValue')
   移除指定的class属性值
3. toggleClass('classValue')
   动态切换类选择器的样式
   存在则删除
   不存在则添加
   
4. css() 方法
    1.css('attr','value')
        为元素设置CSS样式，参数为CSS属性名和对应的属性值,
            如果参数只有属性名，表示读取CSS样式
        eg:
            $("h1").css("color","red").css("background","green");

    2.css(JSON对象)
        JSON对象语法:
            1.使用{}表示对象
            2.对象由属性和值组成(CSS属性:值)
            3.属性与值都使用字符串表示，之间使用 : 分隔
            4.多组属性之间，使用逗号隔开
        eg:
            JSON:
            {
                "width":"190px",
                "height":"190px",
                ...
            }
            $("h1").css({
                "width":"190px",
                "height":"190px",
                ...
            });
```



### 筛选方法

    //not()取元素的相反条件
    //eq(index) 根据下标获取元素
    //not("") 获取元素，给出否定条件
    //input:checked 匹配被选中的输入框
    //size() 获取数组长度，元素个数
        var isAll= $("[name=check]").not("input:checked").size()<=0;
        if (isAll){
            $("#checkall").prop("checked","true");
        }else{
            $("#checkall").removeAttr("checked");
        }




### 获取节点的方法

 根据层次关系获取节点对象

    1. children()/children("selector")
    	获取当前节点下所有的直接子元素
    	或者获取当前节点下，满足选择器的所有直接子元素
    	eg:
            $("#box").children();
            $("#box").children(".c1");
    2. find("selector")
       必须指定选择器参数，获取包含直接和间接的所有后代元素
          eg:
            $("#box").find("p");
    
    3.parent()
       获取当前节点的父元素
          eg:
            $("p").parent()
    
    4.parents(["selector"])
            获取父元素及祖先元素
            或者获取指定选择器的祖先元素
          eg:
            $("p").parents();
            $("p").parents("#box");
    
    5.next()/next("selector")
            获取下一个兄弟元素，或者是指定选择器的兄弟元素
            参考: 相邻兄弟选择器，只匹配第一个
        
    6.prev()/prev("selector")
            获取上一个兄弟元素，或者是指定选择器的兄弟元素
        
    7.siblings()/siblings("selector")
         表示获取所有的兄弟元素，或者是满足选择器的所有兄弟元素
          eg:
            $("h2").siblings()
            $("h2").siblings(".c1")



### 节点操作(创建、添加、删除)

    创建节点
    $("标签语法");
      	eg: 
                var div =("<div></div>");
                div.html("");
                div.attr("id","box").css();
              或var h1 =("<h1 id="d1" class="c1">一级标题</h1>");
    添加节点
        1.内部添加(作为子元素添加)
            新节点不能复用，只能添加一次，需要重复创建新节点
            1. $obj.append($new);
                将$new作为$obj的最后一个子元素添加
            2. $obj.prepend($new);
                将$new作为$obj的第一个子元素添加
        2.外部添加(作为兄弟元素添加)
            1. $obj.after($new);
                将$new作为$obj后一个兄弟元素添加
            2. $obj.before($new);
                将$new作为$obj前一个兄弟元素添加
    
    3.删除节点
            $obj.remove();
            删除$obj节点      



## 事件处理

    等待文档加载完毕(onload)
    原生: window.onload = function(){};
    jQuery:
          1.$(document).ready(function(){
                ......
            });
          2.$().ready(function(){
                ......
            });
          3.$(function(){});
    
    区别:
            1.原生onload事件函数不能重复调用，重复书写，后面的代码
                会将前面的onload覆盖掉
            2.jQuery中优化了ready方法，可以重复使用，不会产生覆盖
                问题，所有的代码都会执行
    
    2.事件绑定
        原生的事件处理函数不变，jQuery提供了新的绑定方式
        注意:   事件函数名省略on前缀
    
        1.$obj.事件函数名(function(){});
            eg:
                $div.click(function(){});
        
        2. bind(事件名称，function);
            eg:
                $div.bind("click",function(){});
            bind()方法的底层实现:
                $div.on("click",function(){});
    
            $('h1').click(function(){
                alert('h1被点击');
            });
            $('p').bind("click",function(){
                alert("p被点击");
            });
        
    3.事件对象
        获取方式及相关属性，同原生JS


​        

​        











