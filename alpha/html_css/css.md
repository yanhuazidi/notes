[TOC]



## CSS

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

## 选择器

选择器作用:  根据不同的选择器，匹配文档中相应的元素，并为其设置样式

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

**结合元素选择器**

标签选择器与类选择器结合使用

标签名.类名{
                    样式
                }

标签名必须放在前面

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



| 选择器                                                       | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [[*attribute*\]](http://www.w3school.com.cn/cssref/selector_attribute.asp) | 用于选取带有指定属性的元素。                                 |
| [[*attribute*=*value*\]](http://www.w3school.com.cn/cssref/selector_attribute_value.asp) | 用于选取带有指定属性和值的元素。                             |
| [[*attribute*~=*value*\]](http://www.w3school.com.cn/cssref/selector_attribute_value_contain.asp) | 用于选取属性值中包含指定词汇的元素。                         |
| [[*attribute*\|=*value*\]](http://www.w3school.com.cn/cssref/selector_attribute_value_start.asp) | 用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。 |
| [[*attribute*^=*value*\]](http://www.w3school.com.cn/cssref/selector_attr_begin.asp) | 匹配属性值以指定值开头的每个元素。                           |
| [[*attribute*$=*value*\]](http://www.w3school.com.cn/cssref/selector_attr_end.asp) | 匹配属性值以指定值结尾的每个元素。                           |
| [[attribute*=value\]](http://www.w3school.com.cn/cssref/selector_attr_contain.asp) | 匹配属性值中包含指定值的每个元素。                           |



### 伪元素选择器

`:before` 和 `:after` 的主要作用是在元素内容前后加上指定内容

```css
p:before{
   content: 'Hello';
   color: red;
}
p:after{
    content: 'Tom';
    color: red;
}
```

 效果如图：

![img](https://images2015.cnblogs.com/blog/816691/201701/816691-20170105220709050-1981262896.png)     

```css
ul.breadcrumb li+li:before {
    padding: 8px;
    color: black;
    content: "/\00a0";
}
```

每两个li的组合，第二个li之前加上该css



### 选择器的优先级

选择器的优先级看权重(值),权值越大，优先级越高

基础选择器的权值
标签选择器   1
类选择器/伪类选择器  10
ID选择器       100
行类样式     1000



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



## 颜色取值

1. 英文单词表示颜色

2. rgb(r,g,b);

   使用红绿蓝三原色表示，每种颜色取值范围0~255

   - red    rgb(255,0,0)
   - green  rgb(0,255,0)
   - blue   rgb(0,255,0)
   - black  rgb(0,0,0)
   - white  rgb(255,255,255)

3. rgba(r,g,b,a)

   a  表示alpha 透明度 ， 取值0-1

   0  表示透明  1 表示不透明

   使用小数表示半透明 0.5 或 .5

4. 十六进制来表示颜色

   语法:  取值范围  0~9,a~f

   表示颜色 : 以#开头，每两位为一组，代表一种三元色

   rgb(255,0,0) -- #ff0000
   green           #00ff00
   blue            #0000ff

   



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

**取值 ：**`offset-x offset-y blur spread color`

1. `offset-x` : 阴影的水平偏移距离，取像素值
2. `offset-y` : 阴影的垂直偏移距离，取像素值
3. `blur` : 阴影的模糊程度，取像素值，值越大越模糊
4. `spread` : 阴影的延伸距离（可选），取像素值，可以扩大阴影的范围
5. `color` : 设置阴影颜色 （默认为黑色）



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



### 背景图片的尺寸

属性: `background-size`
取值: 

- px  取两个值，分别表示背景图片的宽和高,取一个值，设置背景图片宽度，高度等比缩放
- %   取一个值或两个值等同于像素的取值情况,百分比参照当前元素的宽高计算
- cover  覆盖，等比拉伸图片至足够大，完全覆盖元素,超出部分裁剪掉
- contain  包含，等比拉伸图片至刚好被元素容纳的最大尺寸,有空隙





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



## 文本

### 颜色

属性: `color`
取值: 颜色值

### 水平对齐方式

属性 : `text-align`
取值 : left(默认) / center / right

### 文本装饰线

属性 : `text-decoration`
取值 : 

1. `underline`  下划线
2. `overline`  上划线
3. `line-through` 删除线
4. `none`  取消装饰线

### 行高

属性 : `line-height`
取值 : 像素值
注意: 所有文本在其所属行中都是垂直居中的
使用场景: 

1. 行高可以用来设置一行文本的垂直居中
   行高与元素的高度保持一致

2. 行高可以实现文本在元素中上下位置的微调

   ```css
   {
        height : 100px;
        line-height : 120px;
   }
   ```



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

取值: 以秒s/ms为单位的数值，设置过渡效果的延迟执行



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

**浮动问题:**
由于子元素全部浮动，在文档中不占位，造成父元素高度为0，影响页面布局
解决方法:

1. 给父元素固定高度
2. 给父元素设置overflow:hidden
3. 标准做法: 清除浮动元素带来的影响
   属性: `clear`
   取值: `left / right / both`
   用法:为元素设置clear属性
                   left : 当前元素不受左浮动元素的影响
                   right : 当前元素不受右浮动元素的影响
                   both ： 不受左浮动或右浮动的影响

解决父元素高度为0：
步骤:

1. 在父元素的末尾添加空的子元素(块元素)
2. 为空的子元素元素设置clear:both;
                   

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

5. `table`

6. `table-cell`

   

7. 

   

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



​     