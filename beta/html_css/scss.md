



## 安装

1. 下载ruby地址如下 
   <http://rubyinstaller.org/downloads/> 

2. 安装完Ruby实际上已经安装好了gem

3. 通过Gem安装Compass+Sass

   ```powershell
   gem install compass
   compass -v
   sass -v
   #显示版本号即安装成功
   ```

   使用淘宝的镜像一直报错，换为基于腾讯云的资源

   ```powershell
   gem sources --add https://ruby.taobao.org/ --remove https://rubygems.org/
   上面地址报错的时候为下面的
   gem sources --add http://gems.ruby-china.org/ --remove https://rubygems.org/
   然后执行下面的命令
   gem sources -l
   gem install compass
   compass -v
   sass -v
   ```



## 编译

如果要在命令行中运行 Sass ,只要输入

```
sass input.scss output.css
```

你还可以命令 Sass 监视文件的改动并更新 CSS ：

```
sass --watch input.scss:output.css
```

如果你的目录里有很多 Sass 文件，你还可以命令 Sass 监视整个目录：

```
sass --watch app/sass:public/stylesheets
```



## 引入其他文件

1. 引入其他 **.scss** 文件

   ```scss
   @import 'index.scss'  
   ```

   这样的话，文件在编译后，会自动把引入的文件和当前文件合并为一个.scss文件

2. 引入其他 **.css** 文件

   ```scss
   @import 'index.css'  
   ```

   和引入.scss文件不同，这样引入的.css文件在编译后不会和当前文件合并为一个.scss文件，而是继续保持为外链引入方式

### 使用SASS部分文件

`@import`把`sass`样式分散到多个文件时，你通常只想生成少数几个`css`文件。那些专门为`@import`命令而编写的`sass`文件，并不需要生成对应的独立`css`文件，这样的`sass`文件称为局部文件。对此，`sass`有一个特殊的约定来命名这些文件。

此约定即，`sass`局部文件的文件名以下划线开头。这样，`sass`就不会在编译时单独编译这个文件输出`css`，而只把这个文件用作导入。当你`@import`一个局部文件时，还可以不写文件的全名，即省略文件名开头的下划线。举例来说，你想导入`themes/_night-sky.scss`这个局部文件里的变量，你只需在样式表中写`@import` `"themes/night-sky";`。

局部文件可以被多个不同的文件引用。当一些样式需要在多个页面甚至多个项目中使用时，这非常有用。在这种情况下，有时需要在你的样式表中对导入的样式稍作修改，`sass`有一个功能刚好可以解决这个问题，即默认变量值。

### 嵌套导入

`sass`允许`@import`命令写在`css`规则内。这种导入方式下，生成对应的`css`文件时，局部文件会被直接插入到`css`规则内导入它的地方。

有一个名为`_blue-theme.scss`的局部文件，内容如下:

```scss
aside {
  background: blue;
  color: white;
}
```

然后把它导入到一个CSS规则内，如下所示:

```scss
.blue-theme {
@import
 "blue-theme"}

//生成的结果跟你直接在.blue-theme选择器内写_blue-theme.scss文件的内容完全一样。

.blue-theme {
  aside {
    background: blue;
    color: #fff;
  }
}
```



## 注释方法

1. 块注释

   ```scss
   /*
   */
   ```

2. 行注释

   ```scss
   //
   ```

   

## 变量

1. 常规变量

   ```scss
   $key: value;
   $basic-border: 1px solidblack;
   $nav-color: #F90;
   nav {
     $width: 100px;
     width: $width;
     color: $nav-color;
   }
   //编译后
   nav {
     width: 100px;
     color: #F90;
   }
   ```

2. 默认变量

   ```scss
   $key: value!default;
   //默认变量是可以被覆盖的,具体覆盖方法如下
   $font: 12px;
   $font: 14px!default;
   --------------------------------------------------
   $fancybox-width: 400px !default;
   .fancybox {
   width: $fancybox-width;
   }
   ```

   如果用户在导入你的`sass`局部文件之前声明了一个`$fancybox-width`变量，那么你的局部文件中对`$fancybox-width`赋值`400px`的操作就无效。如果用户没有做这样的声明，则`$fancybox-width`将默认为`400px`。

3. 特殊变量

   ```scss
   $fontSize:14px;
   font:#{$fontSize}
   ```

4. 多值变量

   多值变量分为list和map两种类型，list类似于js的数组，map类似于对象

当变量定义在`css`规则块内，那么该变量只能在此规则块内使用。如果它们出现在任何形式的`{...}`块中(如`@media`或者`@font-face`块)，情况也是如此

## 嵌套

1. 选择器嵌套

   ```scss
   // scss 文件
   ul{
       li{
           a{
           }
       }
   }
   //解析为 css 文件
   ul{
   }  
   ul li {
   }  
   ul li a{
   }
   //scss 在属性选择器中，&表示父元素选择器
   a{
       &:hover{
       }
   }
   //解析为 css 文件
   a{
   }
   a:hover{
   }
   ------------------------------------------------------
   .container {
     h1, h2, h3 {margin-bottom: .8em}
   }
   //解析为 css 文件
   .container h1, .container h2, .container h3 { margin-bottom: .8em }
   ---------------------------------------------------------------
   nav, aside {
     a {color: blue}
   }
   //解析为 css 文件
   nav a, aside a {color: blue}s
   ---------------------------------------------------------
   article {
     ~ article { border-top: 1px dashed #ccc }
     > section { background: #eee }
     dl > {
       dt { color: #333 }
       dd { color: #555 }
     }
     nav + & { margin-top: 0 }
   }
   //解析为 css 文件
   article ~ article { border-top: 1px dashed #ccc }
   article > footer { background: #eee }
   article dl > dt { color: #333 }
   article dl > dd { color: #555 }
   nav + article { margin-top: 0 }
   ```

2. 属性嵌套

   ```scss
   // scss 文件
   div{
       border{
           top:{
               width:1px;
           }
           left:{
               width:2px;
           }
       }
   }
   //解析为 css 文件
   div{
       border-top:1px;
       border-left:2px;
   }
   ------------------------------------------
   nav {
     border: 1px solid #ccc {
     left: 0px;
     right: 0px;
     }
   }
   //解析为 css 文件
   nav {
     border: 1px solid #ccc;
     border-left: 0px;
     border-right: 0px;
   }
   ```

   

## 混合

@mixin 调用@mixin方法需要使用 @include

```scss
// scss 普通混合
@mixin font{
    line-height:10px;
    color: #fff;
}
.footer{
    @include font;
}
// 解析为 css 文件
.footer{
    line-height: 10px;
    color: #fff;
}
// scss 文件
@mixin font($size:12px){  //默认参数 默认12px
    font-size: $size;
}
.footer{
    @include font(16px);
}

-------------------------------------------------------------------
@mixin link-colors($normal, $hover, $visited) {
  color: $normal;
  &:hover { color: $hover; }
  &:visited { color: $visited; }
}
a {
  @include link-colors(blue, red, green);
}
//or
a {
    @include link-colors(
      $normal: blue,
      $visited: green,
      $hover: red
  );
}
//Sass最终生成的是:
a { color: blue; }
a:hover { color: red; }
a:visited { color: green; }
```



## 继承

使用继承会让该选择器继承指定选择器的所有样式,要使用关键词@extend，后面跟上指定的选择器

```scss
// scss文件
.font{
    font-size:14px;
    height: 16px;
}
.footer{
    @extend .font;
    border-width: 2px;
}
//解析问 css 文件
.font, .footer{
    font-size:14px;
    height: 16px;
}
.footer{
    border-width: 2px;
}

```



## 站位选择器

%选择器名，通过@extend 去调用，如果不调用，则文件编译后不会出现改该冗余css文件

```scss
// scss 文件
%dir{
    font-size: 14px;
}
%clear{
    overflow: hidden;
}
div{
    @extend %dir;
}
/*只有 %dir 选择器被调用了，%clear 在编译的时候会被当做冗余文件给过滤掉，不会出现在编译后的.css文件中*/
```



## 函数

sass 内置了很多函数，自己也可以定义函数。以 @function 开始 @return 返回值

```scss
//scss 文件
@function per($data){
    @return $data/10 + px;
}

div{
    font-size: per(140);
}

//解析为 css文件
div{
    font-size: 14px;
}
```





















