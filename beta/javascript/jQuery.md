[TOC]



## [w3school](http://www.w3school.com.cn/jquery)



## jQuery

- jQuery的基本设计思想和主要用法，就是**"选择某个网页元素，然后对其进行某种操作"**。

- jQuery设计思想之二，就是提供各种强大的[过滤器](http://api.jquery.com/category/traversing/filtering/)，对结果集进行筛选，缩小选择结果。

- jQuery设计思想之三，就是最终选中网页元素以后，可以对它进行一系列操作，并且所有操作可以连接在一起，以链条的形式写出来.

　　`$('div').find('h3').eq(2).html('Hello');`

- jQuery设计思想之四，就是使用同一个函数，来完成取值（getter）和赋值（setter），即"取值器"与"赋值器"合一。到底是取值还是赋值，由函数的参数决定。

  - [.html()](http://api.jquery.com/html/) 取出或设置html内容
  - [.text()](http://api.jquery.com/text/) 取出或设置text内容
  - [.attr()](http://api.jquery.com/attr/) 取出或设置某个属性的值
  - [.width()](http://api.jquery.com/width/) 取出或设置某个元素的宽度
  - [.height()](http://api.jquery.com/height/) 取出或设置某个元素的高度
  - [.val()](http://api.jquery.com/val/) 取出某个表单元素的值

  需要注意的是，如果结果集包含多个元素，那么赋值的时候，将对其中所有的元素赋值；取值的时候，则是只取出第一个元素的值（[.text()](http://api.jquery.com/text/)例外，它取出所有元素的text内容）。

- jQuery设计思想之五，就是提供两组方法，来操作元素在网页中的位置移动。一组方法是直接移动该元素，另一组方法是移动其他元素，使得目标元素达到我们想要的位置。

  - [.insertAfter()](http://api.jquery.com/insertAfter/)和[.after()](http://api.jquery.com/after/)：在现存元素的外部，从后面插入元素

  - [.insertBefore()](http://api.jquery.com/insertBefore/)和[.before()](http://api.jquery.com/before)：在现存元素的外部，从前面插入元素

  - [.appendTo()](http://api.jquery.com/appendTo/)和[.append()](http://api.jquery.com/append)：在现存元素的内部，从后面插入元素

  - [.prependTo()](http://api.jquery.com/prependTo/)和[.prepend()](http://api.jquery.com/prepend)：在现存元素的内部，从前面插入元素

    ```javascript
    $('div').insertAfter($('p'));//把div元素移动p元素后面
    $('p').after($('div'));//把p元素加到div元素前面
    ```

    除了元素的位置移动之外，jQuery还提供其他几种操作元素的重要方法。

    复制元素使用[.clone()](http://api.jquery.com/clone/)。

    删除元素使用[.remove()](http://api.jquery.com/remove/)和[.detach()](http://api.jquery.com/detach/)。两者的区别在于，前者不保留被删除元素的事件，后者保留，有利于重新插入文档时使用。

    清空元素内容（但是不删除该元素）使用[.empty()](http://api.jquery.com/empty/)。

    创建新元素的方法非常简单，只要把新元素直接传入jQuery的构造函数就行了：

    ```javascript
    $('<p>Hello</p>');
    $('<li class="new">new list item</li>');
    $('ul').append('<li>list item</li>');
    ```

- jQuery设计思想之六：除了对选中的元素进行操作以外，还提供一些与元素无关的[工具方法](http://api.jquery.com/category/utilities/)（utility）。不必选中元素，就可以直接使用这些方法。

  它是定义在jQuery构造函数上的方法，即jQuery.method()，所以可以直接使用。而那些操作元素的方法，是定义在构造函数的prototype对象上的方法，即jQuery.prototype.method()，所以必须生成实例（即选中元素）后使用。

  - [$.trim()](http://api.jquery.com/jQuery.trim/) 去除字符串两端的空格。
  - [$.each()](http://api.jquery.com/jQuery.each/) 遍历一个数组或对象。
  - [$.inArray()](http://api.jquery.com/jQuery.inArray/) 返回一个值在数组中的索引位置。如果该值不在数组中，则返回-1。
  - [$.grep()](http://api.jquery.com/jQuery.grep/) 返回数组中符合某种标准的元素。
  - [$.extend()](http://api.jquery.com/jQuery.extend/) 将多个对象，合并到第一个对象。
  - [$.makeArray()](http://api.jquery.com/jQuery.makeArray/) 将对象转化为数组。
  - [$.type()](http://api.jquery.com/jQuery.type/) 判断对象的类别（函数对象、日期对象、数组对象、正则对象等等）。
  - [$.isArray()](http://api.jquery.com/jQuery.isArray/) 判断某个参数是否为数组。
  - [$.isEmptyObject()](http://api.jquery.com/jQuery.isEmptyObject/) 判断某个对象是否为空（不含有任何属性）。
  - [$.isFunction()](http://api.jquery.com/jQuery.isFunction/) 判断某个参数是否为函数。
  - [$.isPlainObject()](http://api.jquery.com/jQuery.isPlainObject/) 判断某个参数是否为用"{}"或"new Object"建立的对象。
  - [$.support()](http://api.jquery.com/jQuery.support/) 判断浏览器是否支持某个特性。

- jQuery设计思想之七，就是把[事件](http://api.jquery.com/category/events/)直接绑定在网页元素之上。

  　[.blur()](http://api.jquery.com/blur/) 表单元素失去焦点。

  　　[.change()](http://api.jquery.com/change/) 表单元素的值发生变化

  　　[.click()](http://api.jquery.com/click/) 鼠标单击

  　　[.dblclick()](http://api.jquery.com/dblclick/) 鼠标双击

  　　[.focus()](http://api.jquery.com/focus/) 表单元素获得焦点

  　　[.focusin()](http://api.jquery.com/focusin/) 子元素获得焦点

  　　[.focusout()](http://api.jquery.com/focusout/) 子元素失去焦点

  　　[.hover()](http://api.jquery.com/hover/) 同时为mouseenter和mouseleave事件指定处理函数

  　　[.keydown()](http://api.jquery.com/keydown/) 按下键盘（长时间按键，只返回一个事件）

  　　[.keypress()](http://api.jquery.com/keypress/) 按下键盘（长时间按键，将返回多个事件）

  　　[.keyup()](http://api.jquery.com/keyup/) 松开键盘

  　　[.load()](http://api.jquery.com/load-event/) 元素加载完毕

  　　[.mousedown()](http://api.jquery.com/mousedown/) 按下鼠标

  　　[.mouseenter()](http://api.jquery.com/mouseenter/) 鼠标进入（进入子元素不触发）

  　　[.mouseleave()](http://api.jquery.com/mouseleave/) 鼠标离开（离开子元素不触发）

  　　[.mousemove()](http://api.jquery.com/mousemove/) 鼠标在元素内部移动

  　　[.mouseout()](http://api.jquery.com/mouseleave/) 鼠标离开（离开子元素也触发）

  　　[.mouseover()](http://api.jquery.com/mouseover/) 鼠标进入（进入子元素也触发）

  　　[.mouseup()](http://api.jquery.com/mouseup/) 松开鼠标

  　　[.ready()](http://api.jquery.com/ready/) DOM加载完成

  　　[.resize()](http://api.jquery.com/resize/) 浏览器窗口的大小发生改变

  　　[.scroll()](http://api.jquery.com/scroll/) 滚动条的位置发生变化

  　　[.select()](http://api.jquery.com/select/) 用户选中文本框中的内容

  　　[.submit()](http://api.jquery.com/submit/) 用户递交表单

  　　[.toggle()](http://api.jquery.com/toggle-event/) 根据鼠标点击的次数，依次运行多个函数

  　　[.unload()](http://api.jquery.com/unload/) 用户离开页面

  以上这些事件在jQuery内部，都是[.bind()](http://api.jquery.com/bind/)的便捷方式。使用[.bind()](http://api.jquery.com/bind/)可以更灵活地控制事件，比如为多个事件绑定同一个函数：

  ```javascript
  $('input').bind('click change', //同时绑定click和change事件
  　　function() {
  　　　　alert('Hello');
  　　}
  );
  ```

  有时，你只想让事件运行一次，这时可以使用[.one()](http://api.jquery.com/one/)方法。

  ```javascript
  $("p").one("click", function() {
  　　alert("Hello"); //只运行一次，以后的点击不会运行
  });
  ```

  [.unbind()](http://api.jquery.com/unbind/)用来解除事件绑定。

  ```javascript
  $('p').unbind('click');
  ```

  所有的事件处理函数，都可以接受一个[事件对象](http://api.jquery.com/category/events/event-object/)（event object）作为参数，比如下面例子中的e：

  ```javascript
  $("p").click(function(e) {
  　　　　alert(e.type); // "click"
  });
  ```

  　　[event.pageX](http://api.jquery.com/event.pageX/) 事件发生时，鼠标距离网页左上角的水平距离

  　　[event.pageY](http://api.jquery.com/event.pageY/) 事件发生时，鼠标距离网页左上角的垂直距离

  　　[event.type](http://api.jquery.com/event.type/) 事件的类型（比如click）

  　　[event.which](http://api.jquery.com/event.which/) 按下了哪一个键

  　　[event.data](http://api.jquery.com/event.data/) 在事件对象上绑定数据，然后传入事件处理函数

  　　[event.target](http://api.jquery.com/event.target/) 事件针对的网页元素

  　　[event.preventDefault()](http://api.jquery.com/event.preventDefault/) 阻止事件的默认行为（比如点击链接，会自动打开新页面）

  　　[event.stopPropagation()](http://api.jquery.com/event.stopPropagation/) 停止事件向上层元素冒泡

  在事件处理函数中，可以用this关键字，返回事件针对的DOM元素：

  ```javascript
  　　$('a').click(function(e) {
  　　　　if ($(this).attr('href').match('evil')) { //如果确认为有害链接
  　　　　　　e.preventDefault(); //阻止打开
  　　　　　　$(this).addClass('evil'); //加上表示有害的class
  　　　　}
  　　});
  ```

  有两种方法，可以自动触发一个事件。一种是直接使用事件函数，另一种是使用[.trigger()](http://api.jquery.com/trigger/)或[.triggerHandler()](http://api.jquery.com/triggerHandler/)。

  ```javascript
  $('a').click();//事件方法
  $('a').trigger('click');
  ```

  







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
      
5. `$('.child', $parent）`

      `$parent.find('.child')`

      `$parent.children('.child')`

      

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

   1. `$obj.事件函数名(function(){});`
   
   2. `bind(事件名称，function(){});`
   
      bind()方法的底层实现:`$div.on("click",function(){});`
   
   ```javascript
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



## on

[jQuery.on() 函数详解](https://codeplayer.vip/p/j7sq1)

on()支持直接在目标元素上绑定事件，也支持在目标元素的祖辈元素上委托绑定。在事件委托绑定模式下，即使是执行on()函数之后新添加的元素，只要它符合条件，绑定的事件处理函数也对其有效。

此外，该函数可以为同一元素、同一事件类型绑定多个事件处理函数。触发事件时，jQuery会按照绑定的先后顺序依次执行绑定的事件处理函数。

要删除通过on()绑定的事件，请使用`$(document).off("click", "td");`函数。如果要附加一个事件，只执行一次，然后删除自己，请使用one()函数

`jQueryObject.on( events [, selector ] [, data ], handler )`

`jQueryObject.on( eventsMap [, selector ] [, data ] )`

| 参数      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| events    | String类型一个或多个用空格分隔的事件类型和可选的命名空间，例如"click"、“focus click”、“keydown.myPlugin”。 |
| eventsMap | Object类型一个Object对象，其每个属性对应事件类型和可选的命名空间(参数events)，属性值对应绑定的事件处理函数(参数handler)。 |
| selector  | 可选/String类型一个jQuery选择器，用于指定哪些后代元素可以触发绑定的事件。如果该参数为null或被省略，则表示当前元素自身绑定事件(实际触发者也可能是后代元素，只要事件流能到达当前元素即可)。 |
| data      | 可选/任意类型触发事件时，需要通过event.data传递给事件处理函数的任意数据。 |
| handler   | Function类型指定的事件处理函数。on()还会为handler传入一个参数：表示当前事件的Event对象。 |

关于参数selector，你可以简单地理解为：如果该参数等于null或被省略，则为当前匹配元素绑定事件；否则就是为当前匹配元素的后代元素中符合selector选择器的元素绑定事件。

```javascript
// 为div中的所有p元素绑定click事件处理程序
// 只有n2、n3可以触发该事件
$("div").on("click", "p", function(event){
	alert( $(this).text() );
});

// 后添加的n6也可以触发上述click事件，因为它也是div中的p元素
$("#n1").append('<p id="n6">上述绑定的click事件对此元素也生效!</p>');
```

参数handler中的this指向当前匹配元素的后代元素中触发该事件的DOM元素。如果参数selector等于null或被省略，则this指向当前匹配元素(也就是该元素)。

参数handler的返回值与DOM原生事件的处理函数返回值作用一致。例如"submit"(表单提交)事件的事件处理函数返回false，可以阻止表单的提交。

如果事件处理函数handler仅仅只为返回false值，可以直接将handler设为false。

**返回值**

on()函数的返回值为jQuery类型，返回当前jQuery对象本身。



## [jQuery的deferred对象详解](<http://www.ruanyifeng.com/blog/2011/08/a_detailed_explanation_of_jquery_deferred_object.html>)



### trigger() 方法

trigger() 方法触发被选元素的指定事件类型。

**语法**

```
$(selector).trigger(event,[param1,param2,...])
```

| 参数                    | 描述                                                         |
| :---------------------- | :----------------------------------------------------------- |
| *event*                 | 必需。规定指定元素要触发的事件。可以使自定义事件（使用 bind() 函数来附加），或者任何标准事件。 |
| [*param1*,*param2*,...] | 可选。传递到事件处理程序的额外参数。额外的参数对自定义事件特别有用。 |

```javascript
$("button").click(function(){
  $("input").trigger("select");
});
```

使用 Event 对象来触发事件

规定使用事件对象的被选元素要触发的事件。

**语法**

```
$(selector).trigger(eventObj)
```

| 参数       | 描述                             |
| :--------- | :------------------------------- |
| *eventObj* | 必需。规定事件发生时运行的函数。 |

```javascript
  $("input").select(function(){
    $("input").after("文本被选中！");
  });
  var e = jQuery.Event("select");
  $("button").click(function(){
    $("input").trigger(e);
  });
```



## detach()方法

对一个DOM元素进行大量处理，应该先用.detach()方法，把这个元素从DOM中取出来，处理完毕以后，再重新插回文档。

- detach() 方法移除被选元素，包括所有文本和子节点。
- 这个方法会保留 jQuery 对象中的匹配的元素，因而可以在将来再使用这些匹配的元素。
- detach() 会保留所有绑定的事件、附加的数据，这一点与 remove() 不同。

```javascript
  var x;
  $("#btn1").click(function(){
    x=$("p").detach();
  });
  $("#btn2").click(function(){
    $("body").prepend(x);
  });
```



## jQuery方法

许多jQuery方法都有两个版本，一个是供**jQuery对象**使用的版本，另一个是供**jQuery函数**使用的版本。下面两个例子，都是取出一个元素的文本，使用的都是text()方法。

你既可以使用针对jQuery对象的版本：

> 　　`var $text = $("#text");`
>
> 　　`var $ts = $text.text();`

也可以使用针对jQuery函数的版本：

> 　　`var $text = $("#text");`
>
> 　　`var $ts = $.text($text);`

由于后一种针对jQuery函数的版本不通过jQuery对象操作，所以相对开销较小，速度比较快。





## call 、bind 、 apply

**call()、apply()、bind() 都是用来重定义 this 这个对象的**

```javascript
var name = '小王',age=17;
var obj = {
    name:'小张',
    objAge:this.age,
    myFun:function(fm,t){
        conslie.log(this.name + "年龄" + this.age,"来自"+ fm + "去往" + t);
    }
}
var bd = {
    name:'德玛',
    age:99
}
obj.myFun.call(db,'成都','上海')；　　　　 // 德玛 年龄 99  来自 成都去往上海
obj.myFun.apply(db,['成都','上海']);      // 德玛 年龄 99  来自 成都去往上海  
obj.myFun.bind(db,'成都','上海')();       // 德玛 年龄 99  来自 成都去往上海
obj.myFun.bind(db,['成都','上海'])();　　 // 德玛 年龄 99  来自 成都, 上海去往 undefined
```

call 、bind 、 apply 这三个函数的第一个参数都是 this 的指向对象，第二个参数差别就来了：

call 的参数是直接放进去的，第二第三第 n 个参数全都用逗号分隔，直接放到后面 **obj.myFun.call(db,'成都', ... ,'string' )**。

apply 的所有参数都必须放在一个数组里面传进去 **obj.myFun.apply(db,['成都', ..., 'string' ])**。

bind 除了返回是函数以外，它 的参数和 call 一样。

当然，三者的参数不限定是 string 类型，允许是各种类型，包括函数 、 object 等等！



## 链式操作

`$('div').find('h3').eq(2).html('Hello');`

这是jQuery最令人称道、最方便的特点。它的原理在于每一步的jQuery操作，返回的都是一个jQuery对象，所以不同操作可以连在一起。

jQuery还提供了[.end()](http://api.jquery.com/end/)方法，使得结果集可以后退一步：

```javascript
　　$('div')

　　　.find('h3')

　　　.eq(2)

　　　.html('Hello')

　　　.end() //退回到选中所有的h3元素的那一步

　　　.eq(0) //选中第一个h3元素

　　　.html('World'); //将它的内容改为World
```



## 特效

常用的特殊效果如下：

- 　　[.fadeIn()](http://api.jquery.com/fadeIn/) 淡入
- 　　[.fadeOut()](http://api.jquery.com/fadeOut/) 淡出
- 　　[.fadeTo()](http://api.jquery.com/fadeTo/) 调整透明度
- 　　[.hide()](http://api.jquery.com/hide/) 隐藏元素
- 　　[.show()](http://api.jquery.com/show/) 显示元素
- 　　[.slideDown()](http://api.jquery.com/slideDown/) 向下展开
- 　　[.slideUp()](http://api.jquery.com/slideUp/) 向上卷起
- 　　[.slideToggle()](http://api.jquery.com/slideToggle/) 依次展开或卷起某个元素
- 　　[.toggle()](http://api.jquery.com/toggle/) 依次展示或隐藏某个元素

除了[.show()](http://api.jquery.com/show/)和[.hide()](http://api.jquery.com/hide/)，所有其他特效的默认执行时间都是400ms（毫秒），但是你可以改变这个设置。

在特效结束后，可以指定执行某个函数。

　　`$('p').fadeOut(300, function() { $(this).remove(); });`

更复杂的特效，可以用[.animate()](http://api.jquery.com/animate/)自定义。

```javascript
$('div').animate(
　　　　{
　　　　　　left : "+=50", //不断右移
　　　　　　opacity : 0.25 //指定透明度
　　　　},
　　　　300, // 持续时间
　　　　function() { alert('done!'); } //回调函数
　　);
```

[.stop()](http://api.jquery.com/stop/)和[.delay()](http://api.jquery.com/delay/)用来停止或延缓特效的执行。

[$.fx.off](http://api.jquery.com/jQuery.fx.off/)如果设置为true，则关闭所有网页特效。





## jQuery操作DOM节点

### 内容操作

        1. html() 方法
            为元素设置标签内容，可以识别标签
            等价于原生的 innerHTML 
        2. text() 方法
            为元素设置文本内容，不能设别标签
            等价于原生的 innerText
        3. val() 方法
            用来读取或设置文本框或表单控件的值


### 属性操作

1. attr() 方法
	设置或读取指定的标签属性,动态添加id/class属性，对应选择器为元素设置样式
	eg :
    	`$("div").attr("id","d1");`//设置id为d1
    	`console.log($("div").attr("id"));`
2. removeAttr() 方法
	移除指定的属性，参数为属性名



### 样式操作

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
    
    ```javascript
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

　　$('div').has('p'); // 选择包含p元素的div元素

　　$('div').not('.myClass'); //选择class不等于myClass的div元素

　　$('div').filter('.myClass'); //选择class等于myClass的div元素

　　$('div').first(); //选择第1个div元素

　　$('div').eq(5); //选择第6个div元素
　　
    $('div').next('p'); //选择div元素后面的第一个p元素

　　$('div').parent(); //选择div元素的父元素

　　$('div').closest('form'); //选择离div最近的那个form父元素

　　$('div').children(); //选择div的所有子元素

　　$('div').siblings(); //选择div的同级元素


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

```

jQuery
    1.介绍
      jQuery是JS的工具库，通过封装原生的JS方法，简化JS操作
        write less , do more

    版本:
        1.xx.xx  兼容IE 6/7/8
        2.xx.xx  不再兼容IE 6.7.8
    
    功能和优势
        1.简化的是DOM操作
        2.可以直接通过选择器设置元素样式
        3.链式调用(核心)
        4.事件的处理更加简便
        ------------------------------
        5.Ajax技术更加完善(网络请求)  异步的网络请求，实现局部刷新
        6.提供各种插件可供使用
        7.允许自定义插件

使用
    1.引入jQuery文件
        <script src=""></script>
    2.使用jQuery
        引入操作必须在代码之前，先引入，才能使用jQuert语法

        1.jQuery对象
            jQuery通过封装，将原生的DOM对象包装成jQuery对象
        注意:
            原生对象使用原生的方法
            jQuery对象使用jQuery方法
            不能混用

        2.jQuery对象以$符号与原生的方法区分

        3. 工厂函数 -  $()
            $符号是jQuery对象的标志
            $() : 支持传递字符串参数，用于获取元素节点
                可以根据选择器匹配并返回元素(jQuery对象)
        
        4.原生JS对象与jQuery对象互相装换
            1. DOM对象 转换 jQuery对象
                使用$()包装原生DOM对象，返回jQuery对象

              eg:
                var h1 =document.getElementsByTagName('h1')[0];
                var $h1 =$(h1);
            
            this 当前对象转换
              eg:
                $(this).css("background","gray")
            
            2. jQuery对象 转换 DOM对象
                var h1 = $('h1')[0] | $h1[0];
                var h1 = $('h1').get(0) | $h1.get(0);
    
jQuery选择器
    1.使用选择器获取jQuery对象
    2.语法:
        $('选择器');
    
    3.分类:
        1.基础选择器
            1.标签选择器
                $('div');
                根据标签名获取元素
            2.ID选择器
                $('#id值');
            3.类选择器
                $('.className');
            4.群组选择器
                $('selector1,selector2,...');

        2.层级选择器(都是从当前元素向后匹配)
            1.后代选择器
                $('selector1 selector2');
            2.子代选择器
                $('selector1>selector2');匹配直接子元素
            3.相邻兄弟选择器
                $('selector1+selector2');
                匹配紧靠在selector1后面的兄弟元素，且满足selector2,否则匹配失败
            4.通用兄弟选择器
                $('selector1~selector2');
                匹配紧跟在selector1后面所有满足selector2的兄弟元素
            
        3.过滤选择器(不筛选层级关系，全部包含在内)
            1. :first
                匹配一组元素中的第一个元素
                eg :
                    $('h1:first');
            
            2. :last
                匹配一组元素中的最后一个

            3. :not()
                否定筛选，匹配除()中列出的元素外，所有元素
                 eg:
                    $(":not(selector1,selector2)");
            4. :odd
                匹配偶数行对应的元素
                eg:
                    $(":odd");
            5. :even
                匹配奇数行对应的元素
                eg:
                    $(":even");
            6. :eq(index)
                匹配指定下标对应的元素,下标从 0 开始
                eg:
                    $("p:eq(2)"); 
            7. :lt(index)
                匹配下标小于index的元素
            8. :gt(index)
                匹配下标大于index的元素 

        4.属性选择器
          根据元素的标签属性来获取元素          
            1. $('[attribute]')
                获取属性，名为attribute的元素
                eg:
                    $('[id]')包含id属性的元素
            2. $('[attribute=value]')
                获取属性名等于attribute，属性值为value的元素
                eg:
                    $("[id=d1]")
                    $("[id='d1']")
            3. [attribute!=value]
                匹配属性值不等于value元素
            4. [attribute^=value]
                匹配属性值以value开头的元素,字符匹配
            5. [attribute$=value]
                匹配属性值以value结尾的元素,字符匹配
            6. [attribute*=value]
                匹配属性值中存在value的元素
        5.子元素过滤选择器
            1. :first-child
              匹配属于其父元素中的第一个子元素
              eg:
                $('p:first-child');
            2. :last-child
              匹配属于其父元素中最后一个子元素
            3. :nth-child(n)
              匹配属于其父元素中第n个子元素，给数值
              注意:
                   1.n给具体数值，表示具体行号，从1开始计数
                   2.n给关键字或表达式，表示传入下标，根据下标获取元素(从下标0开始)
                       eg: n=even 奇数下标取元素，对应偶数行
                           n=odd  偶数下标取元素，对应奇数行

        伪类选择器
                :checked  表示表单控件-按钮的选中状态
                
    遍历节点对象数组
        each()
        eg:
            $(".imgNav li").each(function(){
                        $(this).css("background","gray")
                    }); 

jQuery操作DOM节点
    1.基本操作(标签内容操作)
        1. html('') 方法
            为元素设置标签内容，可以识别标签
            等价于原生的 innerHTML
        2. text('') 方法
            为元素设置文本内容，不能设别标签
            等价于原生的 innerText
        3. val() 方法
            用来读取或设置文本框或表单控件的值
        4. attr() 方法
            设置或读取指定的标签属性
            eg :
                $("div").attr("id","d1");//设置id为d1
                console.log($("div").attr("id"));
        5. removeAttr() 方法
            移除指定的属性，参数为属性名

    样式操作
        1. attr() 方法
            动态添加id/class属性，对应选择器为元素设置样式
        2. 针对类选择器的样式
            eg:
                $('h2').addClass('c1 c2');
                $('h3').addClass('c1').addClass('c2');//链式调用
            1.addClass("classValue")
                添加class属性值，对应类选择器样式
            2.removeClass('classValue')
                移除指定的class属性值
            3.toggleClass('classValue')
                动态切换类选择器的样式
                存在则删除
                不存在则添加

    给元素添加属性
        eg:
            $("[name=check]").prop("checked","true");

    not()取元素的相反条件
        //eq:not()
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

    css() 方法
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
    
节点的层次方法
    根据层次关系获取节点对象
        1.children()/children("selector")
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

节点操作(创建、添加、删除)
    创建节点
        $("标签语法");
        eg: 
            var $div =$("<div></div>");
            $div.html("");
            $div.attr("id","box").css();
          或var h1 =$("<h1 id="d1" class="c1">一级标题</h1>");

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

4.事件处理
    1.等待文档加载完毕(onload)
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
            