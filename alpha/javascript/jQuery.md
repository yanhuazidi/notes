[TOC]





## 使用jQuery

引入操作必须在代码之前，先引入，才能使用jQuert语法

```html
   <script src=""></script>
```



## jQuery对象

jQuery通过封装，将原生的DOM对象包装成jQuery对象

注意:

​	原生对象使用原生的方法, jQuery对象使用jQuery方法,不能混用

jQuery对象以$符号与原生的方法区分



### 工厂函数 -  $()

\$符号是jQuery对象的标志

\$() : 支持传递字符串参数，用于获取元素节点
            可以根据选择器匹配并返回元素(jQuery对象)



### 原生JS对象与jQuery对象互相装换

DOM对象 转换 jQuery对象

使用$()包装原生DOM对象，返回jQuery对象

```javascript
var h1 =document.getElementsByTagName('h1')[0];
var $h1 =$(h1);
```

this 当前对象转换

```javascript
$(this).css("background","gray")
```

jQuery对象 转换 DOM对象

```javascript
var h1 = $('h1')[0] | $h1[0];
var h1 = $('h1').get(0) | $h1.get(0);
```



## jQuery选择器

使用选择器获取jQuery对象
语法:
        $('选择器');
    

### 基础选择器

1. 标签选择器
               \$('div');根据标签名获取元素
2. ID选择器
              \$('#id值');
3. 类选择器
               \$('.className');
4. 群组选择器
               $('selector1,selector2,...');

### 层级选择器(都是从当前元素向后匹配)

1. 后代选择器
               \$('selector1 selector2');
2. 子代选择器
               ​\$('selector1>selector2');匹配直接子元素
3. 相邻兄弟选择器
               ​\$('selector1+selector2');
   匹配紧靠在selector1后面的兄弟元素，且满足selector2,否则匹配失败
4. 通用兄弟选择器
               \$('selector1~selector2');
   匹配紧跟在selector1后面所有满足selector2的兄弟元素



### 过滤选择器(不筛选层级关系，全部包含在内)

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



### 属性选择器

根据元素的标签属性来获取元素

1. \$('[attribute]')
       获取属性，名为attribute的元素
       eg:
                $('[id]')包含id属性的元素
       
2. $('[attribute=value]')

      获取属性名等于attribute，属性值为value的元素

      eg:

      ​	\$("[id=d1]")
      ​    $("[id='d1']")

3. [attribute!=value]

      匹配属性值不等于value元素

4. [attribute^=value]

      匹配属性值以value开头的元素,字符匹配

5. [attribute$=value]

      匹配属性值以value结尾的元素,字符匹配

6. [attribute*=value]

      匹配属性值中存在value的元素



### 子元素过滤选择器

1. :first-child

   匹配属于其父元素中的第一个子元素

   eg:

   ​	$('p:first-child');

2. :last-child

   匹配属于其父元素中最后一个子元素

3. :nth-child(n)

   匹配属于其父元素中第n个子元素，给数值

   注意:
                  1.n给具体数值，表示具体行号，从1开始计数
                  2.n给关键字或表达式，表示传入下标，根据下标获取元素(从下标0开始)
                      eg: n=even 奇数下标取元素，对应偶数行
                          n=odd  偶数下标取元素，对应奇数行

### 伪类选择器

:checked  表示表单控件-按钮的选中状态



## 遍历节点对象数组

each()

```javascript
$(".imgNav li").each(function(){
    $(this).css("background","gray")
}); 
```



## jQuery操作DOM节点



### 标签内容操作

        1. html('') 方法
            为元素设置标签内容，可以识别标签
            等价于原生的 innerHTML
            
        2. text('') 方法
            为元素设置文本内容，不能设别标签
            等价于原生的 innerText
            
        3. val() 方法
            
            用来读取或设置文本框或表单控件的值
            
            

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











