[TOC]



## CSS
CSS注释 : /*  */
### 使用方式:

1. **内联样式/行内样式**
           特点：在标签中通过style属性，为元素设置样式
           语法：
               `<标签名 style="属性:值;属性2:值2;..."></标签名>`
   CSS中使用属性和值来声明样式

   常用的CSS属性

   - `font-size` 设置元素的字体大小，取像素值
   - `color` 设置元素的字体颜色，取颜色值
   - `background-color` 设置元素的 背景颜色，取颜色值

2. **文档内嵌**

   特点: 在文档中使用`<style></style>`标签，为文档中的元素设置样式

   语法:

   ```html
   <style type="text/css">
        p{
              color:red;
              font-size:32px
          }
   </style>
   ```

3. **外链**

   特点 : 在HTML文档中引用外部的样式表文件

   使用 :

   	1. 定义外部的样式表文件 以.css为后缀
   
    2. 在HTML文档中使用

          `<link rel="stylesheet" href="url" type="text/css">`



### 样式表的特征：

1. 层叠性
   可以为一个元素设置多个样式，共同起作用
2. 继承性
   子元素可以继承父元素或祖先元素的某些CSS样式
   例如: 大部分的文本属性都可以被继承
            块元素默认宽度与父元素保持一致 h1 p div
3. 样式表的优先级
   从高到低依次为:
   1. 行内样式(最高)
   2. 文档内嵌样式/外链文件中的样式(平级):以代码书写顺序为准,后执行起作用
   3. 继承样式(子元素继承的父元素样式)
   4. 浏览器默认样式
      如果发生样式冲突，参考优先级决定元素最终样式

   调整优先级  !impprtant规则
   把!impprtant放在属性值之后，与值之间用空格分开，作用是提升优先级
   不能加在行内样式上
            `color:blue !impprtant;`

## 选择器

选择器作用:  根据不同的选择器，匹配文档中相应的元素，并为其设置样式

通用选择器
        作用:匹配所有标签
        *{
            样式
        }
        效率极低，尽量减少使用

### 标签选择器

作用:根据标签名匹配文档中所有的该元素

**语法:**
            标签名{
                属性:值;
            }

### id 选择器

根据元素的id属性值匹配元素

注意: 所有的元素都有id属性，属性值自定义, id属性具有唯一性

**语法:**

​         #id属性值{

​                样式
​         }

​	`<div id="box"></div>`

### 类选择器

根据元素的class属性值匹配元素，可以复用,以同名的类为单位统一设置样式

**语法:** 

.class属性值{
                样式
            }
**分类选择器**
标签选择器与类选择器结合使用,找到有这个类属性的标签 

 标签名.类名{
                    样式
 }

标签名必须放在前面， `div.class`

特点:

1. 指向更精确
2. 优先级变高



**多类选择器**

class 属性值可以出现多个，使用空格隔开

`class="c1 c2 c3"`

通过把两个类选择器链接在一起，仅可以选择*同时包含这些类名*的元素（类名的顺序不限）。

如果一个多类选择器包含类名列表中没有的一个类名，匹配就会失败。请看下面的规则：

```css
.important.urgent {background:silver;}
```

它能匹配以下元素：

```css
<p class="important urgent">
<p class="important urgent warning">
```



### 群组选择器

可以为一组元素设置共同样式,可以组合标签，类，ID选择器

**语法:**

选择器1，选择器2，选择器3{
                样式
            }
常见于清除浏览器的默认样式，或设置网页的基本样式



### 后代选择器:

特点: 匹配满足要求的所有后代元素

**语法:** 
            选择器1 选择器2{
                样式
            }
选择器1表示父元素
选择器2表示子元素或后代元素，包含直接间接后代元素



### 子代选择器

只匹配父元素中的直接子元素

**语法:**
            选择器1>选择器2{
                样式
            }



### 相邻兄弟选择器

可选择紧接在另一元素后的元素，且二者有相同父元素。

```css
h1 + p {margin-top:50px;}
```

这个选择器读作：“选择紧接在 h1 元素后出现的段落，h1 和 p 元素拥有共同的父元素”。

相邻兄弟选择器使用了加号（+），即相邻兄弟结合符（Adjacent sibling combinator）。

**注释：**与子结合符一样，相邻兄弟结合符旁边可以有空白符。

```css
li + li {font-weight:bold;}
```

上面这个选择器只会把列表中的第二个和第三个列表项变为粗体。第一个列表项不受影响。



### 后续兄弟选择器

后续兄弟选择器选取所有指定元素之后的相邻兄弟元素。
    语法:
        选择器1~选择器2{
            样式
        }



### 伪类选择器

作用: 针对元素不同的状态，设置不同的样式,必须和其它选择器一起使用

分类:

1. 超链接伪类选择器
   针对超链接不同状态设置样式

2. 动态伪类选择器

   所有元素都可以使用

**超链接伪类选择器使用,超链接独有**

1. 访问前  `:link`

2. 访问后  `:visitek`
   伪类选择器需要与其它选择器结合使用，不能单独使用

   ```css
   a:link{
       设置超链接访问之前的样式
   }
   ```

**动态伪类选择器,所有元素都可用**

1. `:hover`
           鼠标滑过元素时的状态
2. `:active`
      鼠标点按元素时的状态,激活

**超链接使用注意:**

超链接可以设置四种状态的样式

书写时必须按以下顺序定义
                       `:link`
                        `:visitek`
                        `:hover`
                        `:active`

**表单控件伪类选择器**

`:focus`

表示文本框或密码框在获取焦点时的状态
焦点状态: 正接受输入或编辑时的状态

```css
input:focus{
    样式
}
```

`:checked`

表示表单控件-按钮的选中状态



### 属性选择器

**简单属性选择**

把包含标题（title）的所有元素变为红色

```css
*[title] {color:red;}
```

还可以根据多个属性进行选择，只需将属性选择器链接在一起即可。

将同时有 href 和 title 属性的 HTML 超链接的文本设置为红色

```css
a[href][title] {color:red;}
```

**根据具体属性值选择**

```css
a[href="http://www.w3school.com.cn/about_us.asp"] {color: red;}
```

注意，这种格式要求必须与属性值完全匹配。

如果属性值包含用空格分隔的值列表，匹配就可能出问题。

请考虑一下的标记片段：

```html
<p class="important warning">This paragraph is a very important warning.</p>
```

如果写成 `p[class="important"]`，那么这个规则不能匹配示例标记。

要根据具体属性值来选择该元素，必须这样写：

```css
p[class="important warning"] {color: red;}
```

**根据部分属性值选择**

如果需要根据属性值中的词列表的某个词进行选择，则需要使用波浪号（~）。

假设您想选择 class 属性中包含 important 的元素，可以用下面这个选择器做到这一点：

```css
p[class~="important"] {color: red;}
/*p.important 和 p[class="important"] 应用到 HTML 文档时是等价的。
那么，为什么还要有 "~=" 属性选择器呢？因为它能用于任何属性，而不只是 class。*/
```

**子串匹配属性选择器**

| 类型         | 描述                                       |
| :----------- | :----------------------------------------- |
| [abc^="def"] | 选择 abc 属性值以 "def" 开头的所有元素     |
| [abc$="def"] | 选择 abc 属性值以 "def" 结尾的所有元素     |
| [abc*="def"] | 选择 abc 属性值中包含子串 "def" 的所有元素 |


**特定属性选择类型**

```css
*[lang|="en"] {color: red;}
```

上面这个规则会选择 lang 属性等于 en 或以 en- 开头的所有元素。

| 选择器                   | 描述                                                         |
| :----------------------- | :----------------------------------------------------------- |
| [attribute]\[attribute]  | 多属性选择，同时满足                                         |
| [*attribute*]            | 用于选取带有指定属性的元素。                                 |
| [*attribute*=*value*\]   | 用于选取带有指定属性和值的元素。                             |
| [*attribute*~=*value*\]  | 用于选取属性值中包含指定词汇的元素。                         |
| [*attribute*\|=*value*\] | 用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。 |
| [*attribute*^=*value*\]  | 匹配属性值以指定值开头的每个元素。                           |
| [*attribute*$=*value*\]  | 匹配属性值以指定值结尾的每个元素。                           |
| [attribute*=value\]      | 匹配属性值中包含指定值的每个元素。                           |



### 目标伪类选择器

突出显示获得的 html 锚点元素,匹配当前活动的锚点

选择器 : `target{}`

```html
<style>
:target{
     border: 2px solid #D4D4D4;
     background-color: #e5eecc;
}
</style>
<p><a href="#news1">Jump to New content 1</a></p>
<p><a href="#news2">Jump to New content 2</a></p>
<p id="news1"><b>New content 1...</b></p>
<p id="news2"><b>New content 2...</b></p>
```

### 结构伪类选择器

- `:first-child`   匹配属于任意元素的父元素的第一个子元素
- `:last-child`    匹配属于任意元素的父元素的最后一个子元素
- `:nth-child(n)`  匹配属于任意元素的父元素的第n个子元素,n从1开始
- `:nth-last-child(n)`	选择任意元素的父元素的倒数第n个子元素
- `>:first-child`  匹配属于任意元素的第一个子元素
- `p:first-of-type`	选择的每个 p 元素是其父元素的第一个 p 元素 :first-of-type

### 否定伪类选择器

`:not(selector)`	选择所有selector以外的元素

`p:not(:first-child) 选择P元素所有非第一个子元素的子元素`

### 伪元素选择器

1. 内容生成

   `:before`	     在选择的元素之前插入内容(相当于插入一个伪元素)
   `:after`	     在选择的元素之后插入内容

   一般与content 属性一起来指定要插入的内容。

   ```css
   p:after 每个<p>元素之后插入内容：
   { 
        content:"- Remember this";
        display:black;
   }
   ul.breadcrumb li+li:before {
       padding: 8px;
       color: black;
       content: "/\00a0";
   }
   每两个li的组合，第二个li之前加上该css
   ```

2. `:first-letter`	p:first-letter	选择某元素的第一个字母,比:first-line优先

   `:first-line`	    p:first-line	选择每个<p> 元素的第一行字符

3. `::selection`{只能写字体颜色和背景颜色}   被框选的内容

4. 取消滚动条

   ```css
   #divContainer::-webkit-scrollbar {
        border-width:1px;
   }
   ```



### 选择器的优先级

   选择器的优先级
        选择器的优先级看权重(值),权值越大，优先级越高

        基础选择器的权值
            继承样式无权值
            * 选择器    0
            标签选择器   1
            类选择器/伪类选择器  10
            ID选择器       100
            行内样式     1000
            !important  >1000



**组合选择器**

除了群组选择器，其他的选择器权值由各选择器的权值相加得到

```css
div span{   2
    color:red;
}
    span{   1
    color:green;
}
    .d1 .c1{    20
}
```


尺寸属性：
        1.属性 :  width     宽度
                 heigth     高度
                 max-width/min-width    最大/最小宽度
                 max-height/min-heigth  最大/最小高度

        2.单位 :
            绝对单位
                px 默认单位，表示像素
                cm 厘米
                mm 毫米
                pt 磅 1pt = 1/72in
                in 英寸 inch 1英寸 = 2.54cm
            相对单位
                em 相对父元素的倍数
                rem 相对根元素的倍数(body,html)
                % 百分比单位，参照父元素对应属性的值获取尺寸
    
        页面中可以设置尺寸的元素
            1. 所有的块级元素
            2. 所有的行内块: 表单元素(除了单选和复选框)
            3. 本身具备宽高属性的 table,
            大部分的行内元素都不许设置宽高尺寸
    
    颜色取值:
        1. 英文单词表示颜色
            red,green,blue,black,white
        2. rgb(r,g,b);
            使用红绿蓝光学三原色表示，每种颜色取值范围0~255
            red    rgb(255,0,0)
            green  rgb(0,255,0)
            blue   rgb(0,255,0)
            black  rgb(0,0,0)
            white  rgb(255,255,255)
    
        3. rgb(r%,g%,b%) 表示255的百分比  
    
        4.rgba(r,g,b,a)
            a  表示alpha 透明度 ， 取值0-1
            0  表示透明  1 表示不透明
            使用小数表示半透明 0.5 或 .5
    
        5. 十六进制来表示颜色
           语法:  取值范围  0~9,a~f
                 表示颜色 : 以#开头，每两位为一组，代表一种三元色
                 e.g:
                    rgb(255,0,0) -- #ff0000
                    green           #00ff00
                    blue            #0000ff
            短十六进制:
                由三位组成，每一位表示一种三元色,浏览器会自动重复补充为6位十六进制
                #f00 - #ff0000

   




## HTML 元素的分类及特点
### 块级元素

1. 独占一行，不与其它元素共行显示
2. 可以手动设置宽高
3. 默认宽度与父元素保持一致(table除外)

常见块级元素:  boyd, h1~h6 , p , div , ul, table td, form

### 行内元素

1. 可以与其它元素共行显示
2. 默认尺寸由内容多少决定，不能手动设置宽高

常见的行类元素: span  label  i  b  strong  sub  sup  a

### 行内块元素

1. 可以与其它元素共行显示
2. 可以手动设置高宽

常见的行内块元素 : img  表单控件



## 内容溢出

块元素是可以手动设置高宽的，如果内容超出尺寸范围，如何处理？
**属性 :** `overflow`
**取值 :** 

- `visible` 默认值，表示溢出内容可见
- `hidden`  溢出内容隐藏
- `scroll`  为元素添加水平和垂直方向上的滚动条，不管内容有无溢出
- `auto`    在溢出方向添加可用的滚动条



## 边框

CSS中认为所有的元素都是矩形区域, 边框是围绕元素内容出现的线条样式

### 边框实现

**属性 ：** `border`

**取值 ：**`border-width border-style border-color`

- `border-width` : 取像素值，设置四个方向边框宽度
- `border-style` : 边框样式
  - `solid`  实线边框
  - `dashed` 虚线边框
  - `dotted` 点线边框
  - `double` 双线边框
- `border-color` : 设置边框颜色，取颜色值

边框宽度，样式，颜色，三个值缺一不可（即使有些值具有默认值）

**注意 ：**
			1. 使用border属性为元素设置边框，是同时设置
					上 右 下 左四个方向的边框
   			2. 取消默认边框，border : none; (常用于按钮)

**单边边框的设置**

属性 ：

1. `border-top` : 设置顶部边框
2. `border-right` : 设置右边边框
3. `border-bottom` : 设置底部边框
4. `border-left` : 设置左边边框

取值 ：`border-width border-style border-color`



### 网页三角标制作

  		1. 设置空的块元素，宽高为0
  		2. 为元素设置等宽的边框
  		3. 调整边框颜色，显示一个方向的边框，其余边框设置透明边框色 `transparent`

注意 ：四个方向的边框缺一不可，缺少的话，边框会恢复成矩形边框，不再是三角形



## 圆角边框

1. 属性 ：`border-radius`
2. 取值 ：像素值或者百分比

方向:  **上   	右      左   	下**

**实例**

1. `border-radius:20px;`
					一个值表示四个角都以20px做圆角
	
2. `border-radius:20px 40px;`

     取两个值，按照上右下左顺时针方向设置圆角，从左上角开始依次取值，在给两个值的情况下，上下保持一致，左右保持一致

3. `border-radius:10px 20px 30px;`

     取三个值，缺少的第四个值与第二个值保持一致

4. `border-radius:10px 20px 30px 40px;`

     分别设置四个角的圆角程度

**百分比取值实现元素形状改变**

`border-radius:50%;`

注意 ：使用百分比设置圆角边框时，是参照当前元素的尺寸进行计算的,四个角不能同时超过50%,两个角不能同时超过100%
如果元素本身的长方形，设置四个50%的圆角会变成椭圆
如果元素本身是正方形，会变成正圆



## 图片边框

**属性 :**`border-image`

**取值 :** `source slice width outset repeat|initial|inherit;`



### 指定要用于绘制边框的图像的位置

**属性 :**`border-image-source`

**取值 :** 

- `none`没有图像被使用
- `image`边框使用图像的路径



### 图像边界向内偏移

**属性 :** `border-image-slice`

**取值 :** 

- `number` 数字表示图像的像素（位图图像）或向量的坐标（如果图像是矢量图像）
- `%` 百分比图像的大小是相对的：水平偏移图像的宽度，垂直偏移图像的高度
- `fill`保留图像的中间部分



### 图像边界的宽度

**属性 :** `border-image-width`

**取值 :** 

- `number` 表示相应的border-width 的倍数
- `%` 边界图像区域的大小：横向偏移的宽度的面积，垂直偏移的高度的面积
- `auto`如果指定了，宽度是相应的image slice的内在宽度或高度



### 用于指定在边框外部绘制 border-image-area 的量

**属性 :** `border-image-outset`

**取值 :** 

- `length `设置边框图像与边框（border-image）的距离，默认为0。
- number代表相应的 border-width 的倍数
- 

### 图像边界

**属性 :**`border-image-repeat`

**取值 :** 重复（repeat）、拉伸（stretch）或铺满（round）。



## 轮廓线

**属性 ：**`outline`
**取值 ：**`width style color`

**注意 ：**轮廓线围绕在元素内容区域四周，与边框类似，但有区别 ：

​			轮廓线在网页中不占位，边框在网页中是实际占位的

取消轮廓线 ：`outline:none;`



## 盒阴影

为元素添加阴影效果

**属性 ：**`box-shadow`

**取值 ：**`offset-x offset-y blur spread color inset`

1. `offset-x` : 阴影的水平偏移距离，取像素值,必须
2. `offset-y` : 阴影的垂直偏移距离，取像素值,必须
3. `blur` : 阴影的模糊程度，取像素值，值越大越模糊
4. `spread` : 阴影的延伸距离（可选），取像素值，可以扩大阴影的范围
5. `color` : 设置阴影颜色 （默认为黑色）
6. `inset` : 把默认的外部阴影设置为内部阴影 无值



## 浏览器的坐标系:

不管是浏览器窗口中还是元素本身，都存在坐标系，
默认以左上角为原点(0,0)，向右，向下分别代表X和Y轴的正方向
正值代表正方向，负值代表负方向



## 盒模型 （框模型）

在CSS中，认为一切元素都是框，都是矩形区域
**盒模型 ：**计算元素在文档中的实际占位情况

**盒模型组成 ：**margin (外边距) border (边框)padding(内边距) content(元素的宽高尺寸)

**元素在文档中实际尺寸的计算 ：**
标准盒模型 ：
			最终宽度=左右外边距+左右边框+左右内边距+width
			最终高度=上下外边距+上下边框+上下内边距+height
其它盒模型元素尺寸计算(表单元素):
			元素设置的宽高表示包含内容内边距和边框在内的总宽度或总高度
			最终宽度 = width + 左右外边框
			最终高度 = height + 上下外边距

**指定盒模型的计算方式**

**属性**
		`box-sizing`

**取值:**
		1. `content-box` 默认值
		 	元素的width,height属性只设置内容尺寸，最终在文档中占据的尺寸
			 为 margin border padding width/height 累加得到
		2. `border-box`
			元素的width,height属性设置包含边框在内的区域大小
			一旦元素设置内边框和边框，会压缩内容的显示区域
			元素最终在文档中占据的尺寸由margin和width/height相加得到
注意:
		表单按钮默认采用 border-box 计算尺寸

**不同元素类型对盒模型属性的支持情况**
  		1. 块元素完全支持盒模型属性
  		2. 行内元素不完全支持盒模型属性(margin-top/margin-bottom)



## 外边距

元素边框与其他元素边框之间的距离

**属性 :**  `margin`

**取值 ：**像素值

>1. `margin : 10px;`
>
>   表示设置上右下左四个方向都为10px的外边距
>
>2. `margin: 10px 20px;`
>
>   表示上下外边距为10px,左右外边距为20px;
>
>3. `margin: 10px 20px 30px;`
>
>   表示上右下左四个方向上的外边距分别为：10px 20px 30px 20px;
>
>4. `margin: 10px 20px 30px 40px;`
>
>   分别设置四个方向的外边距
>
>

**特殊取值**

1. `margin : 0;` 设置元素外边距为0，常用于初始化页面样式，取消一些元素的默认外边距
2. `margin : 0 auto;` 设置左右外边距自动，用来实现元素的居中效果。auto只对左右外边距起作用
3. 取负值 ：会移动元素的位置，负值表示向上向左移动元素，常用于页面元素位置的微调

**单方向外边距的设置**

属性 ：

>1. `margin-top` : 上方外边距
>2. `margin-right` : 右边的外边距
>3. `margin-bottom`  : 底部外边距
>4. `margin-left`: 左边外边距

取值 ：像素值,只给当前方向设置外边距，给一个值

#### 外边距合并

垂直方向上的外边距(块元素):

问题:给子元素添加的margin-top，作用于父元素上(浏览器渲染bug)

解决办法:
				1. 可以为父元素添加上边框(一般用透明的)
   				2. 可以为父元素设置 padding-top 顶部内边距，加0.1px
   				3. 为父元素添加overflow:hidden;

margin-bottom
				两个块元素分别设置margin-bottom,margin-top最终元素之间的距离取较大的值

**水平方向上的外边距(块元素):**
			默认行内元素水平方向上的外边距会叠加显示



## 内边距

指元素内容与边框之间的距离

**属性 :**  `padding`

取值 : 像素值

- `padding:`一个值
  		 设置上右下左四方向上内容与边框之间的距离
- `padding:`两个值
  		 设置上下内边距为第一个值，左右内边距为第二个值
- `padding:`三个值
  		 设置左右为第二个值
- `padding:` 四个值
  		 上右下左依次取值

单独设置某个方向上的内边距

属性:`padding-top`
		`padding-right`
		`padding-bottom`
		`padding-left`
取值: 给一个值



## 背景

**属性 :** `background `
**取值 :**  `color url() repeat attachment position;`
注意: `background-size` 单独设置
`background: pink url(前端课程资料/img-css/northStar.jpg) no-repeat 10px 10px;`

### 颜色

属性: `background-color`
取值: 颜色值

### 背景图片
属性: `background-image`
取值: `url('')`


### 背景图片重复平铺显示

属性: `background-repeat`
取值: `repeat` (默认)  当图片尺寸小于元素尺寸，会自动沿水平和垂直方向重复平铺。
         `repeat-x` 设置图片沿水平方向上平铺
         `repeat-y` 设置图片沿垂直方向上平铺
         `no-repeat` 设置图片不重复平铺



### 固定背景图像

属性: `background-attachment`
将背景图固定在网页的某个位置，一直在可视区域中，不会随着网页滚动条改变位置
取值: 

- scroll   背景图片随页面的其余部分滚动。这是默认
- fixed    背景图像是固定的
- inherit  指定background-attachment的设置应该从父元素继承



### 背景图片的位置

属性 : `background-position`

取值 :

1. 像素值 x  y
                x 表示背景图片水平偏移距离，正值表示向右
                y 表示背景图片垂直偏移距离，正值表示向下
                默认背景图片从元素左上角显示
2. 百分比 
           0%  0% 显示在左上角
           50% 50%  显示在元素的中间位置
           100% 100%  显示在元素的右下角
3. 方位值
           水平方向 : `left center right`
           垂直方向 : `top center bottom`
           设置方位值时，如果缺省一个，默认为居中

使用场景:
    '精灵图'技术，网页开发过程中为了节省资源，减少网络请求
    通常会将一组小图标以一张图片的形式存储，通过一次网络请求加载图片，配合backgrund-position控制图片切换位置

5. 定位背景图片
            background-Origin属性指定了背景图像的位置区域。
            取值:
                content-box     从content开始填充 
                padding-box     从padding开始填充 
                border-box      从border开始填充  默认

### 背景图片的尺寸

属性: `background-size`
取值: 

- px  取两个值，分别表示背景图片的宽和高,取一个值，设置背景图片宽度，高度等比缩放
- %   取一个值或两个值等同于像素的取值情况,百分比参照当前元素的宽高计算
- cover  覆盖，等比拉伸图片至足够大，完全覆盖元素,超出部分裁剪掉
- contain  包含，等比拉伸图片至刚好被元素容纳的最大尺寸,有空隙



## 背景渐变属性    gradient

CSS3 渐变（gradients）可以让你在两个或多个指定的颜色之间显示平稳的过渡。
 CSS3 定义了两种类型的渐变（gradients）：

- 线性渐变（Linear Gradients）- 向下/向上/向左/向右/对角方向
- 径向渐变（Radial Gradients）- 由它们的中心定义

### 线性渐变

**定义:** 为了创建一个线性渐变，你必须至少定义两种颜色结点。颜色结点即你想要呈现平稳过渡的颜色。同时，你也可以  设置一个起点和一个方向（或一个角度）。

**语法 :** `background: linear-gradient(direction | angle, color-stop1, color-stop2, ...);`

**参数:** 

- background : background-image简写
- linear-gradient : 线性渐变
- direction方向 : `to top|right|bottom|left|bottom right...;`  缺省为从上至下
- angle角度   :  0~359 deg;  顺时针方向, to top为 0 deg
- color : 标准颜色值，可以为透明
- stop  : % | px    渐变范围,可缺省

```css
/* 标准的语法 */
background: linear-gradient(red, blue); 
background: linear-gradient(to right, red , blue);
background: linear-gradient(180deg, red, blue);
background: linear-gradient(to bottom right, red , blue);
background: linear-gradient(red, green 20%, blue 50%, yellow 80%); //使用多个颜色结点
```

### 径向渐变

径向渐变由它的中心定义。

**语法 :**`background:(direction, shape size, start-color stop1, stop2..., last-color stopn);`

**参数:** 

- direction : `center(默认),left,right,bottom right...`   此参数不兼容新写法
                      50% 50% 圆心在元素的相对位置,0% 0% 为 left top

- shape  :   参数定义了形状

  ​			circle 表示圆形
  ​            ellipse 表示椭圆形。默认值。

- size 参数定义了渐变的大小。它可以是以下四个值：

  closest-side    小

  farthest-side

  closest-corner

  farthest-corner  大 默认

```css
/* 标准的语法 */    
background: radial-gradient(red, green, blue); 
background: radial-gradient(red 5%, green 15%, blue 60%);
background: radial-gradient(circle, red, yellow, green);
background: radial-gradient(ellipse  closest-side,red 5%, green 15%, blue 30%);
background: -webkit-radial-gradient(60% 55%, farthest-corner,blue,green,yellow,black);
background: -webkit-radial-gradient(bottom right, farthest-corner,blue,green,yellow,black); /* Safari 5.1 - 6.0 */
```

### 使用透明度（transparent）

CSS3 渐变也支持透明度（transparent），可用于创建减弱变淡的效果。

为了添加透明度，我们使用 rgba() 函数来定义颜色结点。rgba() 函数中的最后一个参数可以是从 0 到 1 的值，它定义了颜色的透明度：0 表示完全透明，1 表示完全不透明。

`background: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1)); /* 标准的语法 */`

重复渐变

- `repeating-linear-gradient()` 函数用于重复线性渐变

  `background: repeating-linear-gradient(red, yellow 10%, green 20%);`

- `repeating-radial-gradient()` 函数用于重复径向渐变

  `background: repeating-radial-gradient(red, yellow 10%, green 15%);`

兼容:这样写不能 to 方向

```css
background: -webkit-linear-gradient(left, red , blue); /* Safari 5.1 - 6.0 */
background: -o-linear-gradient(right, red, blue); /* Opera 11.1 - 12.0 */
background: -moz-linear-gradient(right, red, blue); /* Firefox 3.6 - 15 */
background: -ms-linear-gradient(right, red, blue); /ie
```



## 字体

属性 : `font`

取值 : `style weight size family; (顺序强制)`

语法注意:size,family为必填项



### 指定字体

属性 : `font-family`

取值 : 字体名称

` font-family: Arial,'宋体','Microsoft TaHei';`

语法注意: 

1. 字体名称如果是中文，或者由多个英文单词组成必须加引号

2. 可以设置多个字体名称作备用字体，名称之间用逗号隔开

   

### 字体大小
属性 : `font-size`
取值 : 像素值,em,rem



### 字体加粗

属性 : font-weight
取值 :

 1. 关键字

    `bold`(加粗显示)/`normal`(默认，正常显示)

 2. 取无单位的整百数

    范围 100~900

    400 : 同 normal
    700 : 同 bold



### 设置字体样式(斜体)

属性 : `font-style`

取值 : 

 1. `normal`(默认正常显示)

 2. `italic`  (斜体显示)

 3. `oblique` (文本倾斜显示)

    一般作为italic的替换样式，可以实现斜体效果在某些情况下可以指定倾斜角度

5. 小型大写字母
            font-variant: small-caps;
                            normal 默认

        字体属性简写
            属性 : font
            取值 : style  variant weight size family; (顺序强制)
        语法注意:size,family为必填项

## 文本

### 颜色

属性: `color`
取值: 颜色值

### 水平对齐方式

属性 : `text-align`
取值 : left(默认) / center / right / justify两端对齐

### 文本装饰线

属性 : `text-decoration`
取值 : 

1. `underline`  下划线
2. `overline`  上划线
3. `line-through` 删除线
4. `none`  取消装饰线
        4. 文本首行缩进
            属性: text-indent 规定文本块中首行文本的缩进。
                值	描述
                length px	    定义固定的缩进。默认值：0。
                %	        定义基于父元素宽度的百分比的缩进。
                inherit	    规定应该从父元素继承 text-indent 属性的值。

            注意： 负值是允许的。如果值是负数，将第一行左缩进。

### 行高

属性 : `line-height`
取值 : 像素值
无单位数字, 为字体的倍数
注意: 所有文本在其所属行中都是垂直居中的

使用场景: 
                1.行高可以用来设置一行文本的垂直居中
                    如果行高大于字体本身的大小，该行文本在行高内成垂直居中显示效果
                    把行高和元素设置同样的高度，就能使数据在元素居中

2. 行高可以实现文本在元素中上下位置的微调

   ```css
   {
        height : 100px;
        line-height : 120px;
   }
   ```

    新文本属性
        属性	                    描述
        hanging-punctuation	    规定标点字符是否位于线框之外。
        punctuation-trim	    规定是否对标点字符进行修剪。
        text-align-last	        设置如何对齐最后一行或紧挨着强制换行符之前的行。
        text-emphasis	        向元素的文本应用重点标记以及重点标记的前景色。
        text-justify	        规定当 text-align 设置为 "justify" 时所使用的对齐方法。
        text-outline	        规定文本的轮廓。
        text-overflow	        规定当文本溢出包含元素时发生的事情。
        text-shadow	            向文本添加阴影。
        text-wrap	            规定文本的换行规则。
        word-break	            规定非中日韩文本的换行规则。
        word-wrap	            允许对长的不可分割的单词进行分割并换行到下一行。

   ​     


## 表格

### 表格的尺寸

表格在设置宽高时可以选择

1. 为table设置宽高，单元格自动大小
2. 为单元格设置宽高，由内容决定表格整体大小

**注意:** 只能二选一，表格优先级高于单元格

### 盒模型支持

- `table` 标签完全支持盒模型，默认采用border-box计算尺寸
- `tr,td`标签，不完全支持盒模型
- `td` 不支持margin属性
- `tr` 不支持margin ,padding属性
      

### 表格边框和并

将单元格边框和表格边框合并在一起
**属性:** `border-collapse`
**取值:** `separate` (默认 边框分离)
          `collapse`  设置合并

### 调整单元格之间的距离

**属性 :** `border-spacing`

**取值 :** `h-value v-value` 像素值

语法注意 :

​		h-value 表示水平方向上的边距

​		v-value 表示垂直方向上的边距

该属性必须添加给table标签，要求必须是边框分离状态才起作用



## 过渡    

**属性:**` transition`
    元素在两种状态切换时的平滑过渡效果(默认瞬时)

**取值:** `property duration timing-function delay;`
语法注意: 1.duration是必填项，其它可省
                 2.可以分别为属性设置过渡时长

```css
transition: width 2s,height 3s,background 5s;
```

### 指定过渡属性

属性 : `transition-property`

取值 : 大部分的CSS属性名

语法 :  1.`width` (指定单个属性名)
            2.`width,height` (指定多个属性名使用逗号隔开)
            3.`all` (指定所有发生值改变的属性,默认)



### 指定过渡时长

属性: `transition-duration`
取值: 以秒s/ms为单位



### 指定过渡发生的时间变化曲率

属性: `transition-timing-function`
取值:

		1. `linear` 匀速变化
  		2. `ease`  默认值 慢速开始中间加速慢速结束
  		3. `ease-in` 慢速开始，加速结束
  		4. `ease-out` 快速开始，慢速结束
  		5. `ease-in-out` 慢速开始和结束,中间过程先加速后减速

### 指定延迟时间

属性: `transition-delay`
  eg:
                    transition: width 2s,height 3s,background 5s;
取值: 以秒s/ms为单位的数值，设置过渡效果的延迟执行

        把 transition属性放 : hover 中 只有去的效果，没有回的效果(秒回)



## 布局方式

### 标准流布局(文档流布局，静态布局)

`position : static;`

HTML 元素的默认值，即没有定位，遵循正常的文档流对象。

静态定位的元素不会受到 top, bottom, left, right影响。

特点: 元素按照类型和书写顺序，从左到右，从上到下



### 浮动布局

元素设置浮动之后，可以停靠在其他元素的边缘
**属性:** `float`
**取值:** `left / right / none(默认)`
            `left` 元素左浮动直到紧靠其他元素的边缘
            `right` 元素右浮动，直到紧靠其他元素的边缘
**特点:**

1. 元素浮动之后，会脱离文档流，在文档中不再占位，表现为悬浮在文档上方，后面正常的元素会向前占位
2. 多个元素浮动时，会依次停靠在前一个浮动元素边缘，如果当前父元素中宽度无法容纳，会自动换行显示
3. 任何元素只要设置浮动都可以设置宽高(针对行内元素)
4. 文字环绕效果，浮动元素不占位会遮挡正常元素的显示，只遮挡元素位置，不会影响正常内容显示，内容会围绕
   浮动元素显示
5. 浮动元素水平方向没有缝隙，浮动可以解决行内元素或行内块元素，水平方向上由于换行导致的空隙问题
6.元素浮动只会在当前行浮动，本行位置取消，当前面有元素时，不会往前补位，
                后面的元素补位浮动元素位置。

**浮动问题:**
由于子元素全部浮动，在文档中不占位，造成父元素高度为0，影响页面布局
**解决方法:**

1. 给父元素固定高度
2. 给父元素设置overflow:hidden
3. 标准做法: 清除浮动元素带来的影响
   属性: `clear`
   取值: `left / right / both`
   用法:为元素设置clear属性
                   left : 当前元素不受左浮动元素的影响
                   right : 当前元素不受右浮动元素的影响
                   both ： 不受左浮动或右浮动的影响

**解决父元素高度为0：**
步骤:

1. 在父元素的末尾添加空的子元素(块元素)
2. 为空元素设置clear:both;
   父元素 `::after{content:"";display:block;clear:both;}`
                        

### 定位布局

可以设置元素在网页中的显示位置
**属性:** `position`
**取值:**

1. `static` 静态布局，默认值
2. `relative`相对定位
3. `absolute`绝对定位
4. `fixed` 固定定位
5. `sticky`粘性定位

**注意:**
        只有元素设置position为relative/absolute/fixed，才能称元素为已定位元素
静态定位的元素不会受到 top, bottom, left, right影响。

#### 相对定位
​        `position : relative;`
特点: 元素一旦相对定位，可以参照它在文档中的原始位置进行偏移
​         仍然在元素文档中占位(保留它原始位置)
偏移属性: top /right / bottom / left
取值: 取像素值，设置元素的偏移距离
​            top : 设置元素距离顶部的偏移量，正值下移
​            left : 设置元素距离左侧的偏移量，正值右移
​            bottom : 设置元素距离底部的偏移量，正值上移
​            right : 设置元素距离右部的偏移量，正值左移



#### 绝对定位

​		`position : absolute;`

特点:

1. 元素设置绝对定位，会参照一个离它最近的已经定位(position属性不为static就为已定位)的祖先元素进行偏移,

   如果没有已定位的祖先元素，则参照浏览器窗口的原点进行偏移。

2. 元素设置绝对定位会脱离文档流，父元素高度为0

使用注意：

1. 一般采用父元素相对定位，子元素绝对定位，实现元素偏移
2. 偏移属性是根据元素的参照物进行偏移

#### 固定定位

​    `position : fixed;`
特点 : 元素设置固定定位，参照浏览器窗口进行偏移
​              不会随着页面滚动改变在窗口中的位置
​              Fixed定位使元素的位置与文档流无关，因此不占据空间，上升为块元素
​              Fixed定位的元素和其他元素重叠。
​        eg:
​            position:fixed;
​            top:30px;
​            right:5px;


#### 粘性定位

​     `position: sticky;`

基于用户的滚动位置来定位。

粘性定位的元素是依赖于用户的滚动，在 **position:relative** 与 **position:fixed** 定位之间切换。

它的行为就像 **position:relative;** 而当页面滚动超出目标区域时，它的表现就像 **position:fixed;**，它会固定在目标位置。

元素定位表现为在跨越特定阈值前为相对定位，之后为固定定位。

这个特定阈值指的是 top, right, bottom 或 left 之一，换言之，指定 top, right, bottom 或 left 四个阈值其中之一，才可使粘性定位生效。否则其行为与相对定位相同。



### 元素的堆叠次序

元素出现相互重叠时的显示顺序
**属性 :** `z-index`
**取值 :** 正数或负数的，默认为0，数值越大越靠上显示
**注意 :** 只有当前元素设置定位布局，z-index才有效
**用法 :** 与 :hover 事件配合改变z-index值显示动效

如果两个定位元素重叠，没有指定z - index，最后定位在HTML代码中的元素将被显示在最前面。



### 弹性盒子

弹性盒子由弹性容器(Flex container)和弹性子元素(Flex item)组成。
弹性容器通过设置 display 属性的值为 flex 或 inline-flex将其定义为弹性容器。
弹性容器内包含了一个或多个弹性子元素。
**注意：** 弹性容器外及弹性子元素内是正常渲染的。弹性盒子只定义了弹性子元素如何在弹性容器内布局。
弹性子元素通常在弹性盒子内一行显示。默认情况每个容器只有一行。
以下元素展示了弹性子元素在一行内显示，从左到右:

```css
.flex-container {
    display: -webkit-flex;
    display: flex;
    width: 400px;
    height: 250px;
    background-color: lightgrey;
}
 
.flex-item {
    background-color: cornflowerblue;
    width: 100px;
    height: 100px;
    margin: 10px;
}
```



## 弹性盒子模型（Flexible Box）

主要解决某元素中的子元素的布局方式，为布局提供最大的灵活性

1. 容器
   要布局的子元素的父元素称之为容器，容器中样式写 `display:flex;`

2. 项目

   要布局的子元素称之为项目

3. 主轴

   项目们排列的方向，称之为主轴(水平和垂直)

   如果项目们是按横向排列，x轴就是主轴

   如果项目们是按纵向排列, y轴就是主轴

4. 交叉轴

   与主轴垂直相交的方向轴叫做交叉轴

**语法 :**

将元素变为弹性容器，他所有的子元素将变成弹性项目，按照弹性布局的方式去排列显示

display : flex  将块级元素变为容器
              inline-flex  将行内元素变为容器

元素设置为flex容器之后，子元素一些样式属性失效: float/clear/vertical-align
子元素会转换为行内块元素显示,块元素共行,行内元素可以设置宽高

### 弹性容器的样式属性

    
    1.主轴方向(项目排列方式)
            flex-direction : row 横向左往右 默认值
                             row-reverse 横向右往左
                             column 纵向上往下
                             column-reverse 纵向下往上
    
    2. 当一个主轴排列不下所有项目时，项目的显示方式
            flex-wrap : nowrap  不换行，项目会自动压缩  默认值
                        wrap  换行,项目不压缩
                        wrap-reverse 换行反转
    
    3. flex-flow 是 flex-direction 和 flex-wrap 的缩写
            取值 : row nowrap
    
    4. 定义项目在主轴上的对齐方式
            justify-content : flex-start 主轴起点对齐  默认值
                              space-around  间距相同
                              space-between 两端对齐，中间间距相同
                              flex-end  主轴终点对齐
                              center  在主轴上居中对齐
    
    5. 项目们在交叉轴上的对齐方式(容器高度大于项目高度)
            align-items :  flex-start 交叉轴起点对齐  默认值
                            flex-end  交叉轴终点对齐
                            center  在交叉轴居中对齐
                            baseline 交叉轴基线对齐
                            stretch  如果项目未设置高度，项目高度充满容器
    
            align-content 属性在弹性容器内的各项没有占用交叉轴上所有可用的空间时
                            对齐容器内的各项（垂直）。
                        space-around	元素位于各行之前、之间、之后都留有空白的容器内。
                        space-between	元素位于各行之间留有空白的容器内
                        flex-start	    元素位于容器的开头
                        flex-end	    元素位于容器的结尾。
                        center	        元素位于容器的中心。
                        stretch	        默认值。元素被拉伸以适应容器。



### 项目的样式属性

 项目的属性是单独设置给一个项目的，不影响容器和其他项目


    1. order
            取值为无单位的整数，默认0
            定义项目的排列顺序，值越小离起点越近
        
    2. flex-grow
            取值为无单位的整数，默认0不放大
            定义空间变大时的项目沿主轴的放大比例
            取值越大，此项目占据的剩余空间越多
    
    3. flex-shrink
            定义项目的缩小比例，空间不足时，该项目如何缩小
            取值为无单位的整数，默认为1，空间不足，等比缩小
            取值为0 ，不缩小
            取值越大，占据的空间越小
    
    4. align-self
       控制当前项目在交叉轴上对齐方式，与其他项目无关
                flex-start 交叉轴起点对齐  默认值
                flex-end  交叉轴终点对齐
                center  在交叉轴居中对齐
                baseline 交叉轴基线对齐
                stretch  如果项目未设置高度，项目高度充满容器
                auto    继承容器的 align-items 的效果




## 元素显示

### 设置元素显示与隐藏
属性: `visibility`
取值: 

- `visible` (默认)   可见
- `hidden`    元素隐藏,仍然占位



### 转换元素类型

属性 : `display`
取值 : 

1. `inline`行内元素

2. `block`  块元素

3. `inline-block` 行内块元素

4. `none`  元素隐藏,在文档中不占位

5. `table`让元素表现为table,根据内容改变宽高,独占一行

6. `table-cell`

   


### 元素透明度设置

1. `rgba(r,g,b,a)`  a 取值0~1

2. `opacity`

   属性 : opacity

   取值 : 0-1  (0位透明，1为不透明)

使用:

- opacity会使包含元素自身和其后代元素在内的所有显示效果半透明
- rgba() 只针对当前元素的指定属性实现半透明，文本的半透明效果会被子元素继承
- 子元素与父元素同时设置opacity半透明，子元素中的半透明效果是两个值相乘(在父元素半透明的基础上再次半透明)



### 鼠标形状改变

默认: 鼠标悬停普通文本上显示为 "I",超链接上为"手指",其它为"箭头"

属性 : `cursor`

取值 :  

1. `default`  箭头
2. `pointer`  手指
3. `text`    I
4. `ess`  箭头带圈
   ...

### 行内块元素的垂直对齐方式

行内块元素默认按照文本的基线对齐，会出现元素排列不齐的情况

属性 : vertical-align

取值 : top/middle/bottom

使用 : 为行内块元素设置vertical-align,调整左右元素跟它的对齐方式



### 列表相关的属性

1. `list-style-type`

   设置项目符号的类型

   取值: `square / circle / disc / none`

2. `list-style-image`

   使用图片自定义项目符号

   取值 : `url()`

3. `list-style-position`

   设置项目符号的位置

   默认显示在内容框的左侧

   取值 :

   1. `outside`在内容框外部
   
    	2. `inside` 显示在内容框内部

**简写属性**

`list-style : type/url() position`

**取消项目符号**:`list-style:none;`



## 转换

元素的转换效果主要指元素可以发生平移，缩放，旋转变换

**属性 :** `transform`
**取值 :** 转换函数
        注意: 多个转换函数之间使用空格隔开

### 元素的转换基准点

默认情况下，元素以中心点作为转换的基准点
**属性 :** `transform-origin`
**取值 :** 以左上角为(0,0)  取 x  y 
		可以使用像素值，百分比或方位值表示基准点的位置
		左上角 0px   0px
		右下角 100%  100%
		右上角 100%  0 / right top
     	`left center right`
     	`top  center bottom`

### 平移变换

**作用：**可以改变元素在文档中的位置

**属性 :** `transform`

**取值 :**

1. `translate(x,y)`
  
  x,y分别表示元素在X轴上和Y轴上的平移距离，取像素值，可正可负，区分平移方向
    
2. `translate(x)`

      一个值表示沿X轴平移

3. `translateX(value)`

      指定沿X轴平移

4. `translateY(value)`

      指定沿Y轴平移

### 缩放变换

改变元素的显示尺寸(放大或缩小)

**属性 :** `transform`
**取值 :** `scale(value)`

>value 为无单位的数值，表示为缩放比例
>
>1. value > 1  元素放大
>2. 0 < value < 1 元素缩小
>3. value <0  数值仍然元素缩放比，负号表示元素会被翻转

**其它取值:**

- `scaleX(v)` 沿X轴缩放
- `scaleY(v)` 沿Y轴缩放

### 旋转变换

可以设置元素旋转一定的角度显示

**属性 :** `transform`
**取值 :** `rotate(deg)`

取角度值，以deg为单位

1. rotate() 表示平面旋转

   正值表示顺时针旋转，负值表示逆时针旋转

2. 三D旋转

   `rotateX(deg)` 沿X轴旋转

   `rotateY(deg)` 沿Y轴旋转

### 转换函数的组合使用

`transform : translate() scale() rotate();`


5. 倾斜
        改变元素在页面中的形状
        取值 : skew(deg [,deg])
            包含两个参数值，分别表示向X轴和向Y轴倾斜的角度，
            如果第二个参数为空，则默认为0
            
        skewX(deg);表示让元素向着X轴(水平方向)倾斜，改变的是 Y 轴的角度
            参数为 + 表示逆时针
            参数为 - 表示顺时针
        skewY(deg);表示让元素向着Y轴(水平方向)倾斜，改变的是 X 轴的角度
            参数为 + 表示顺时针
            参数为 - 表示逆时针
   

    6.转换函数的组合使用
        transform : translate() scale() rotate();

三D转换
    属性 : transform

        浏览器不支持 3D的位移
    
    1. 透视距离
        模拟人的眼睛到 3D 转换元素之间的距离
        perspective(n) 该属性要加载转换元素的父元素上
            n 为无单位整数, 越小视距越近
    
        语法
            perspective: number|none;    
    
    2. 3D 函数
        translate3D(x,y,z)	定义 3D 转化。
        translateX(x)	定义 3D 转化，仅使用用于 X 轴的值。
        translateY(y)	定义 3D 转化，仅使用用于 Y 轴的值。
        translateZ(z)	定义 3D 转化，仅使用用于 Z 轴的值。
        scale3D(x,y,z)	定义 3D 缩放转换。
        scaleX(x)	定义 3D 缩放转换，通过给定一个 X 轴的值。
        scaleY(y)	定义 3D 缩放转换，通过给定一个 Y 轴的值。
        scaleZ(z)	定义 3D 缩放转换，通过给定一个 Z 轴的值。
        rotate3D(x,y,z,deg)	定义 3D 旋转。
        rotateX(deg)	定义沿 X 轴的 3D 旋转。滚动
        rotateY(deg)	定义沿 Y 轴的 3D 旋转。门
        rotateZ(deg)	定义沿 Z 轴的 3D 旋转。风车
    
        x , y , z
        取值大于 1 表示旋转
        取值 0 表示不旋转


动画 @keyframes
    @keyframes规则是创建动画。 @keyframes规则内指定一个CSS样式和动画将逐步从目前的样式更改为新的样式。
        语法
            @keyframes animationname {keyframes-selector {css-styles;}}

            值	                    说明
            animationname	    必需的。定义animation的名称。
            keyframes-selector	必需的。动画持续时间的百分比。
                合法值：
                    1.  0-100%
                    2.  from (和0%相同)
                        to (和100%相同)
    
                注意： 您可以用一个动画keyframes-selectors。
    
            css-styles	必需的。一个或多个合法的CSS样式属性
    
    当在 @keyframes 创建动画，把它绑定到一个选择器，否则动画不会有任何效果。
        指定至少这两个CSS3的动画属性绑定向一个选择器：
    
        animation-name	    规定 @keyframes 动画的名称。
        animation-duration	规定动画完成一个周期所花费的秒或毫秒。默认是 0
    
        animation-timing-function	规定动画的速度曲线。默认是 "ease"。
            值	            描述
            linear	    动画从头到尾的速度是相同的。
            ease	    默认。动画以低速开始，然后加快，在结束前变慢。
            ease-in	    动画以低速开始。
            ease-out	动画以低速结束。
            ease-in-out	动画以低速开始和结束。
            cubic-bezier(n,n,n,n)	在 cubic-bezier 函数中自己的值。可能的值是从 0 到 1 的数值
    
        animation-fill-mode	规定当动画不播放时（当动画完成时，或当动画有一个延迟未开始播放时），要应用到元素的样式。
            值	                        描述
            none	    默认值。动画在动画执行之前和之后不会应用任何样式到目标元素。
            forwards	在动画结束后（由 animation-iteration-count 决定），动画将应用该属性值。
            backwards	动画将应用在 animation-delay 定义期间启动动画的第一次迭代的关键帧中定义的属性值。这些都是 from 关键帧中的值（当 animation-direction 为 "normal" 或 "alternate" 时）或 to 关键帧中的值（当 animation-direction 为 "reverse" 或 "alternate-reverse" 时）。
            both	    动画遵循 forwards 和 backwards 的规则。也就是说，动画会在两个方向上扩展动画属性。
            initial	    设置该属性为它的默认值。请参阅 initial。
            inherit	    从父元素继承该属性。请参阅 inherit。        
        
        animation-delay	规定动画何时开始。默认是 0。
    
        animation-iteration-count	规定动画被播放的次数。默认是 1。
            n	        一个数字，定义应该播放多少次动画
            infinite	指定动画应该播放无限次（永远）
    
        animation-direction	规定动画是否在下一周期逆向地播放。默认是 "normal"。
            值	            描述
            normal	    默认值。动画按正常播放。
            reverse	    动画反向播放。
            alternate	动画在奇数次（1、3、5...）正向播放，在偶数次（2、4、6...）反向播放。
            alternate-reverse	动画在奇数次（1、3、5...）反向播放，在偶数次（2、4、6...）正向播放。
            initial	    设置该属性为它的默认值。	
            inherit	    从父元素继承该属性。
    
        animation-play-state	规定动画是否正在运行或暂停。默认是 "running"。
            paused	指定暂停动画
            running	指定正在运行的动画


        简写 :    animation : animationname  animation-duration;
    
        eg:
            div
            {
                width:100px;
                height:100px;
                background:red;
                position:relative;
                animation:myfirst 5s;
                -webkit-animation:myfirst 5s; /* Safari and Chrome */
            }
            @keyframes myfirst
            {
                0%   {background:red; left:0px; top:0px;}
                25%  {background:yellow; left:200px; top:0px;}
                50%  {background:blue; left:200px; top:200px;}
                75%  {background:green; left:0px; top:200px;}
                100% {background:red; left:0px; top:0px;}
            }

媒体 @media
    media : 媒体，看网页的设备

    媒体类型
        允许你指定文件将如何在不同媒体呈现。该文件可以以不同的方式显示在屏幕上，在纸张上，或听觉浏览器等等。
    
        媒体类型	        描述
        all	            用于所有的媒体设备。
        screen	        用于电脑显示器 >=992px。768px<=平板电脑<992px，智能手机等<768px。
        print	        用于打印机和打印预览
        speech	        应用于屏幕阅读器等发声设备


    媒体查询
        Media Query 允许在相同样式表为不同媒体设置不同的样式。
    
       语法 :
            @media  mediatype and (media feature) not|only|and (media feature){
                    CSS-Code;
                }
    
            你也可以针对不同的媒体使用不同 stylesheets :
                <link rel="stylesheet" media="mediatype and|not|only (media feature)" href="mystylesheet.css">
    
        媒体属性是CSS3新增的内容，多数媒体属性带有“min-”和“max-”前缀，用于表达“小于等于”和“大于等于”。
        这避免了使用与HTML和XML冲突的“<”和“>”字符
            width | min-width | max-width
            height | min-height | max-height
            aspect-ratio | min-aspect-ratio | max-aspect-ratio  视口宽高比 @media (min-aspect-ratio: 16/9) 
        注意: 媒体属性必须用括号()包起来，否则无效
    
    逻辑操作符
        　　操作符not、and、only和逗号(,)可以用来构建复杂的媒体查询
    
        and
        　　and操作符用来把多个媒体属性组合起来，合并到同一条媒体查询中。只有当每个属性都为真时，这条查询的结果才为真
    
        　　[注意]在不使用not或only操作符的情况下，媒体类型是可选的，默认为all
        　　满足横屏以及最小宽度为700px的条件应用样式表
                @media all and (min-width: 700px) and (orientation: landscape) { ... }
        　　由于不使用not或only操作符的情况下，媒体类型是可选的，默认为 all，所以可以简写为
                @media (min-width: 700px) and (orientation: landscape) { ... }
        or
        　　将多个媒体查询以逗号分隔放在一起；只要其中任何一个为真，整个媒体语句就返回真，相当于or操作符
    
        　　满足最小宽度为700像素或是横屏的手持设备应用样式表
    
                @media (min-width: 700px), handheld and (orientation: landscape) { ... }
        not
    
        　　not操作符用来对一条媒体查询的结果进行取反
    
        　　[注意]not关键字仅能应用于整个查询，而不能单独应用于一个独立的查询
    
        only
    
        　　only操作符表示仅在媒体查询匹配成功时应用指定样式。可以通过它让选中的样式在老式浏览器中不被应用
    
                media="only screen and (max-width:1000px)"{...}
        　　上面这行代码，在老式浏览器中被解析为media="only"，因为没有一个叫only的设备，所以实际上老式浏览器不会应用样式
    
                media="screen and (max-width:1000px)"{...}
        　　上面这行代码，在老式浏览器中被解析为media="screen"，它把后面的逻辑表达式忽略了。所以老式浏览器会应用样式
    
        　　所以，在使用媒体查询时，only最好不要忽略
    
        如果浏览器窗口小于 500px, 背景将变为浅蓝色：
            @media only screen and (max-width: 500px) {
                body {
                    background-color: lightblue;
                }
            }


    方向：横屏/竖屏
        结合CSS媒体查询,可以创建适应不同设备的方向(横屏landscape、竖屏portrait等)的布局。
    
        语法：
            orientation：portrait | landscape
                portrait：指定输出设备中的页面可见区域高度大于或等于宽度
                landscape： 除portrait值情况外，都是landscape
        实例
            如果是横屏背景将是浅蓝色：
            @media only screen and (orientation: landscape) {
                body {
                    background-color: lightblue;
                }
            }

js改变css样式的三种方法
    第一种:用cssText
        div.style.cssText='width:600px;border:1px red solid';

    第二种：用setProperty()
        div.style.setProperty('width','700px');
        div.style.setProperty('border','1px solid blue');
    
    第三种：使用css属性对应的style属性
        div.style.width = "800px";
        div.style.height = "250px"; 

initial 关键字用于设置 CSS 属性为它的默认值。
    initial 关键字可用于任何 HTML 元素上的任何 CSS 属性。

    JavaScript 语法
    	object.style.property="initial"  //恢复默认值
    CSS 语法
        property: initial;


inherit 关键字指定一个属性应从父元素继承它的值。
    inherit 关键字可用于任何 HTML 元素上的任何 CSS 属性。
    JavaScript 语法
        object.style.property="inherit"     //恢复继承值
    CSS 语法
        property: inherit;

CSS优化
    目的 : 减少服务器压力，提升用户体验
    1. 优化原则
        1. 尽量减少 HTTP 请求的个数
        2. 页面顶部引入css文件
        3. 将 css 和 js 放到外部独立的文件中

    2. CSS代码优化
        1. 缩小样式文件
        2. 减少样式的重写
        3. 避免出现空的 src 和 href
        4. 选择更优的样式属性值 (能使用复合，简写的就使用复合简写)
        5. 代码压缩
