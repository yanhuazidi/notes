

[TOC]



## 运行环境

 	1. 浏览器自带js运行解释器
 	2. 服务器端  nodejs 下的js解释器
    网站:  https://nodejs.org/en/


### js 执行文件(以.js后缀的文件)
 1. 浏览器运行   js文件不能直接在浏览器运行，需要借助html文件

    在HTML文档中引入JS代码，有三种方式

    ```
    1.通过元素绑定事件的方式引入JS代码
    	语法:
          <元素 事件函数名="JS代码语句">
                事件函数:
                    鼠标单击事件 onclick
            JS代码：
                弹框显示信息 alert('文本');
                控制台输出信息 console.log('文本');
    2.通过脚本标签<script></script>书写JS代码，标签内容为JS代码，
                可以在任意位置书写任意多次。
                注意: 浏览器遵循从上到下执行代码，书写位置可能会影响效果
            JS代码语句:
                1.prompt('');带有输入框的弹框，可用来接收用户输入
                2.document.write(''); 在网页中写入内容
                使用: 
                    1.普通的书写方式，按照从上到下的执行顺序，依次在
                    网页的相应位置插入内容，可以识别标签
                    2.如果以元素绑定事件的方式，在页面中写入内容，相当于重写页面
    3.外部的JS文件
            1.创建外部的.js文件
            2.在HTML文档中使用<script src="url"></script>引入
            3.如果<script></script>做外部文件的引入操作，标签内部就不能再写JS代码
    	        <script src="01.js"></script>
    ```

2. 后端执行(终端)
	
	```shell
	node 01.js
	```
	
	

## JS基础语法规则
1. JS代码是由语句组成的，每条语句以分号“ ; ” 为结束的标志,结束分号可加可不加;
2. JS严格区分大小写，标点符号一律采用英文的标点
3. JS中使用   //表示单行注释   /*  */表示多行注释



## JS变量与常量
### 变量

​		指在程序运行过程中可以随时修改的数据
语法:

```
1. var 变量名;     //使用关键字var声明变量
	变量 = 值;      //为变量赋值
2. var 变量名=值;
3. var 变量名1=值1,变量名2=值2,...;
```

1. var 关键字可以省略，但是一般不省略，关系到变量的作用域
2. 变量如果只使用var关键字，不赋值，默认为undefind
3. 如果变量未使用var声明，也不赋值，会报错

#### 变量的命名规范

1.由数字，字母，下划线，$组成，不能以数字开头
2.变量名尽量见名知意，禁止与JS的保留字和关键字冲突
		如: var function while for in each switch case break default continue class name new Number  String Array db if else...
3.如果变量名由多个单词组成，采用小驼峰标识
		eg: nameClass

### 常量

​		常量一经定义就不能更改，强制修改会报错
**语法:** 
​            **const 常量名 = 值;**
​            常量在定义时，必须声明并赋值
**使用:**
​            常量名采用全大写字母，与变量名区分

const 定义的变量并非常量，并非不可变，它定义了一个常量引用一个值。使用 const 定义的对象或者数组，其实是可变的。

```javascript
// 创建常量对象
const car = {type:"Fiat", model:"500", color:"white"};
// 修改属性:
car.color = "red";
// 添加属性
car.owner = "Johnson";
```

但是我们不能对常量对象重新赋值：

```javascript
const car = {type:"Fiat", model:"500", color:"white"};
car = {type:"Volvo", model:"EX60", color:"red"};    // 错误
```

const定义常量与使用let 定义的变量相似：

- 二者都是块级作用域
- 都不能和它所在作用域内的其他变量或函数拥有相同的名称

两者还有以下两点区别：

- const声明的常量必须初始化，而let声明的变量不用
- const 定义常量的值不能通过再赋值修改，也不能再次声明。而 let 定义的变量值可以修改。





## 基础数据类型

基本类型值 primitive type，比如Undefined,Null,Boolean,Number,String。



### Number 数值类型

整数和小数都是Number类型

#### 整数
1. 十进制表示方法
   var n = 100;
2. 八进制表示整数  以 0 为前缀
    var n = 015;
3. 十六进制 以 0x 位前缀
    var n = 0xff

注意: 如果使用 console.log 输出整数值，不管是什么进制表示，都转换为十进制输出

#### 进制转换方法 

```javascript
Number.toString(base=10); 
进制转换方法,base 可以取 2,8,10,16，默认10 返回字符串
```

#### 小数

1. 直接以小数点表示小数
   var f1 =10.5;
2. 科学计数法
    var f2 = 1.5e3;  

#### 小数位的操作

 小数在计算机中存储或是计算都存在误差，不准确，可以设置小数的显示位数


```javascript
float.toFixed(n)    n 表示保留的小数位数    返回字符串
eg:
   var n= 62.8834534;
   var str = n.toFixed(3)
```



### String 字符串类型

1. 所有使用''或者""引起来的内容，都是字符串

2. 字符串中的所有字符都是以Unicode码存储的字母和数值的Unicode码值与ASCII码值一致，中文字符的Unicode编码，在计算机中以16进制存储

3. 查看指定的字符的Unicode码值,只能查看一个，多个字符默认第一个

   ```javascript
   方法 : String.charCodeAt([index])
   index 表示指定字符的下标，字符串中默认从0开始
   ```

4. Unicode码中中文的范围(极少数不处于其中)
       "\u4e00" ~ "\u9fa5"

5. 转义字符

   - \u  把数值转义为Unicode字符

   - \n
   - \t
   - \'
   - \\

   

### Boolean 布尔类型

两个值  true =1 / false =0



### undefined

- 当变量声明未定义，默认值为undefined类型
- 访问对象不存在的属性时，默认值为undefined

```javascript
var a;
console.log(a===undefined);//true
```



### null类型
null 对象
        用于释放引用类型，只有一个值 null
        空类型,取 0 、''...



## 数据类型转换

### 检测数据类型
使用 typeof  可以加括号也可以不加   返回字符串

```javascript
typeof num;
typeof (num + str);
```



### 数据类型转换
#### 自动类型装转换(隐式)
不同数据类型的数据在做运算时，会自动转换

1. 字符串与其它数据类型做 +  运算, 一旦 + 与字符串结合使用，就会成为字符串拼接，其它类型自动转换为String,最终结果都为String

   ```javascript
   'aa'+ true = 'aatrue'
   'aa' + undefined = 'aaundefined'
          
   ```

2. Number + Boolean  = Number    会将boolean类型自动转换为Number类型，结果为Number

   ```javascript
   Number + undefined = NaN 
   Number + null = Number
   ```

3. Boolean + undefined = NaN

   ```javascript
   Boolean + null = 0/1
   ```

4. \-    /    *  运算：

   -  会把两端的数据转换为数值类型再运算
   -  如果有无法转换时，结果一律返回 NaN(Not a Number)
   -  NaN 为 Number类型

#### 强制类型转换

1. 将数值类型或布尔类型转为字符串类型
   1. String(var)
   2. var.toString(base=10);
      var 不能为 null 和 undefined  报错
      true.toString()    // '1'

2. 将任意类型转换为Number类型

   方法 :  Number(var)

    返回结果:

   1. 数字字符串--》 Number
   2. 非数字字符串 --》 失败 返回NaN
   3. 布尔类型--》1/0
   4. undefined --》失败  返回NaN
   5. unll --》 0

#### 数值解析函数

方法 : 
        parseInt(var) :  整数解析方法，解析字符串中的整数部分, 向下取整 parseInt(15.9) // 15
        parseFloat(var) : 解析字符串中的Nunber
参数 :
        如果传递的 var 为非字符串类型，方法会先将参数转换为String,再进行解析
        parseInt(1.2) // 1
        parseInt(true) // NaN

注意 : 
    解析时，从第一个字符开始向后解析，对每一位进行转Uniber的操作
    碰到非数字，停止解析，返回结果
        '100a'  //100
        'a100'  // NaN



## 运算符
1. 赋值运算符
           = :  将右边表达式的值赋值给左边的变量

2. 算术运算符
      \+  \-   \*  /(除)   %(取余)  **(幂运算)
   1. 字符串使用 + ,表示字符串拼接
   2. 在其他的运算符中，会将非数字用Number()转换为Number类型参与运算
         `console/log('aa'*2)// NaN`
   3. NaN 与任意类型结合运算，结果都为NaN
   4. \+ 与  \- 还表示数值的正负, +号可以省略，数值为负时 -号不可省略 

3. 复合赋值算术运算符

   `+=`  `-=`   `*= `  `/=`   `%=`

   

4. 自增和自减运算

   `++`  :  每执行一次作减 1 操作 
   `--`  :  每执行一次做减 1 操作

   做前缀与做后缀的执行顺序不同，前缀先执行后赋值，后缀先赋值后执行。

   

5. 关系运算符(比较)

   运算符  >  <  >=   <=  ==(相等)  !=(不相等)  ===(恒等)  !==(不恒等)

   使用:
           关系运算符用来判断表达式之间的关系，判断结果为布尔值，返回结果

   1. 不同类型比较会用Number()自动转换为Number类型，注意Number()转换特点。
   2. 字符串之间的比较会根据每位字符串的Unicode码值进行比较，如果当前码值相同，比较下一位。
   3. undefined 为NaN ,与任何数据类型比较都返回 false

   **相等与恒等**
           相等: 判断两个操作数值是否相等，包含自动类型转换
           恒等: 判断操作数是否恒等，要求数据类型保持一致，值相等,不会进行数据类型转换

   **不等与不恒等**
        不等: 值不相等，返回true
        不恒等 : 值或数据类型只要有一个不同就返回 true

   

6. 逻辑运算符

   逻辑与: &&     逻辑或: ||     逻辑非: !
           1.逻辑与: 表达式1 && 表达式2    返回逻辑短路表达式结果
           2.逻辑或: 表达式1 || 表达式2    返回逻辑短路表达式结果
           3.逻辑非：!表达式    对其后表达式的boolean值取反,返回布尔值

   注意：
           逻辑短路: &&  当第一个表达式为false时,就不再执行第二个表达式,返回第一个表达式执行结果
                        			当第一个表达式为true时,再执行第二个表达式,返回第二个表达式执行结果
                   		 ||  	当第一个表达式为true时，就不再执行第二个表达式,返回第一个表达式执行结果
                        			当第一个表达式为false时,再执行第二个表达式,返回第二个表达式执行结果

   使用: 逻辑运算符主要用来结合条件表达式，返回结果是逻辑短路表达式结果

   ```javascript
   1. var a=15
      var b = a>10 && 'aaaaa';
      console.log(b); //'aaaaa'
   
   2. var b = 100 && console.log('aaaa'); //'aaaa'
      console.log(b); //undefined
   ```

7. 位运算符

   按位与 :   &  同1为1 

   按位或 :   |  有1为1

   按位异或 : ^  不同为1

   按位左移 : <<   // 7<<2 = 28    在7的二进制后添加0

   按位右移 : >>   // 7>>2 = 1     在7的二进制后删除

   使用:`对数据的二进制中的每一位进行操作    

   ```
   110101 
   >> 100000 + 10000 + 100 + 1 
   >> 2**5 + 2**4 + 2**2 + 2**0
   >> 32 + 16 + 4 + 1
   >> 53
   ```

8. 三目运算符(三元运算符)

   根据操作数的个数划分运算符

   语法:
           表达式1 ? 表达式2 : 表达式3;

    执行 :

   1. 执行表达式1，根据其结果的boolean值(true/false)
   2. true : 返回并执行表达式2
   3. false : 返回并执行表达式3

​    

## 流程控制

### 分支(选择)结构

#### if 语句

        1. 语法一:
            
            ```javascript
            if(条件表达式)
            {
                语句块;
            }
            使用:
            1.{} 可以省略，省略之后，if语句只控制后面的第一条代码语句
            2.非零数据都为真，零为假
            ```
            
        2. 语法二:
    
            ```javascript
            if(条件)
            {
               语句块;
            }else{
               默认执行语句块;
            }
            ```
    
        3. 语法三:
    
            ```javascript
            if(条件1)
            {
               语句块;
            }else if(条件2){
               语句块;
            }
            ......
            else if(条件n){
               语句块;
            }else{
               默认执行语句块;
            }
            ```


​            

#### switch 语句

​    主要用来做值匹配，值恒等时，执行某那段代码

```javascript
switch(变量)
{
    case 1: 
        语句块1;
        break;
    case 2: 
        语句块2;
        break;
    case 3: 
        语句块3;
        break;
    case 4:
        语句块4;
        break;
     ......
    case n:
        语句块n;
        break;
    default:
        默认执行语句块;
        break;
}
```

使用：

1. switch 判断值，用的是恒等，要求数据类型和值都相等才能匹配成功

2. case 用来列出所有可能的值，一旦与变量匹配恒等，就执行当前case中的语句。

3. default 表示匹配失败之后执行的操作，写在末尾。

4. break 表示跳出匹配，不再向后执行。

   可以省略，省略之后，表示从当前匹配到的case向后执行所有的代码语句，不再case匹配，直到遇到break或switch结束。

5. case 可以共用代码语句，列出所有相关的情形，共用一组执行语句：

   case 1:
   case 2:
   ...
         语句块;
         break;

**比较 :**
    相同点: 两者都可以用于多项分支语句
    不同点: if-else if-else可以判断各种表达式,使用范围广泛
            switch 只能用于全等判断，结构更加清晰，多条分支结构效率比 if 语句高。



### 循环结构
#### while 循环
**语法:**

```javascript
  while(循环条件)
{
     循环体;
     循环变量;
}
```

**流程**

1. 定义循环变量
2. 判断循环条件
3. 条件成立，成立循环体
4. 改变循环变量(循环结束的条件)

#### do - while 循环

**语法**

```javascript
do{
    循环体;
    循环变量;
}while(循环条件);
```

**流程**

1. 定义循环变量;
2. 执行循环体，更新循环变量;
3. 判断循环条件，条件成立，执行循环体;

#### while 与do-while 区别

1. while 循环首先判断循环条件是否成立，不成立不执行循环体

2. do-while 循环先执行循环体，再判断循环条件，决定是否执行下次循环。

   

#### for 循环

**语法**

```javascript
for(初始化循环变量;定义循环条件;循环变量)
{
     循环体;
}
```

**流程**

1. 初始化循环变量
2. 判断循环条件
3. 循环首先判断循环条件是否成立
4. 更新循环变量，执行循环体

**变体:**

for后面三个表达式可以不写或引用其他变量，但必须占位for(;;)

```javascript
1.  var i=1;
	for(;i<=10;i++){
		console.log(i);
	}
2.  var i=1;
   	for(;;i++){
		console.log(i);
    }
// 无限循环
3.  var i=1;
    for(;i<=10;){
         console.log(i);
         i++;
    }
4.  for(var i=1,j=5; i<=5; i++,j-=2){
         console.log(i+','+j);
    }
    //  1,5
    	2,3
        3,1
        4,-1
        5,-3
5.  for(var i=1,j=5; i<=5,j>=0; i++,j-=2){
        console.log(i+','+j);
    }
    //  1,5
        2,3
        3,1

循环条件有多个时，以最后一个条件为准, 逗号运算符返回最后一个表达式的值
```

##### For/In 循环

JavaScript for/in 语句循环遍历对象的属性：

**实例**

```javascript
var person={fname:"John",lname:"Doe",age:25}; 
for (x in person)  // x 为属性名
{
    txt=txt + person[x];
}
```

**for in** 循环不仅可以遍历对象的属性，还可以遍历数组。

```javascript
var x
var nums = [1, 3, 5];
for (x in nums)
{
    document.write(nums[x]+ "<br />");  // x 为数组索引
}
```

##### for-of的语法：

**for...of** 是 ES6 新引入的特性。它既比传统的for循环简洁，同时弥补了forEach和for-in循环的短板。

```javascript
for (var value of myArray) {
  console.log(value);
}
```

循环一个数组(Array):

```javascript
let iterable = [10, 20, 30];
for (let value of iterable) {
  console.log(value);
}
// 10
// 20
// 30
```

循环一个字符串：

```javascript
let iterable = "boo";
for (let value of iterable) {
  console.log(value);
}
// "b"
// "o"
// "o"
```

循环一个Map:

```javascript
let iterable = new Map([["a", 1], ["b", 2], ["c", 3]]);
for (let [key, value] of iterable) {
  console.log(value);
}
// 1
// 2
// 3
for (let entry of iterable) {
  console.log(entry);
}
// [a, 1]
// [b, 2]
// [c, 3]
```

循环一个 Set:

```javascript
let iterable = new Set([1, 1, 2, 2, 3, 3]);
for (let value of iterable) {
  console.log(value);
}
// 1
// 2
// 3
```

循环一个 DOM collection

循环一个DOM collections，比如NodeList，之前我们讨论过如何循环一个NodeList，现在方便了，可以直接使用for-of循环：

```javascript
// Note: This will only work in platforms that have
// implemented NodeList.prototype[Symbol.iterator]
let articleParagraphs = document.querySelectorAll("article > p");
for (let paragraph of articleParagraphs) {
  paragraph.classList.add("read");
}
```

循环一个拥有enumerable属性的对象

for–of循环并不能直接使用在普通的对象上，但如果我们按对象所拥有的属性进行循环，可使用内置的Object.keys()方法：

```javascript
for (var key of Object.keys(someObject)) {
  console.log(key + ": " + someObject[key]);
}
```

循环一个生成器(generators)

我们可循环一个生成器(generators):

```javascript
function* fibonacci() { // a generator function
  let [prev, curr] = [0, 1];
  while (true) {
    [prev, curr] = [curr, prev + curr];
    yield curr;
  }
}

for (let n of fibonacci()) {
  console.log(n);
  // truncate the sequence at 1000
  if (n >= 1000) {
    break;
  }
}
```

#### for循环与while循环比较

1. for 循环与 while 循环执行流程相同，书写语法不同
2. for 循环更常见于确定循环次数的场合
   while 循环更适用于不确定循环次数的场合



### 循环控制

1. break  表示结束本层循环，不管还有多少次
2. continue  表示跳出本次循环，开始下次循环



## 函数

### 函数的声明:

```javascript
function 函数名(参数列表){
        函数体;
        return 返回值;
    }
```

**解释:**

1. js 中使用function关键字声明函数
2. 函数名自定义，命名规范参考变量的命名规范
3. 函数体就是代码段，在函数调用时执行
4. return 表示返回值，用来返回给外界函数执行的结果，只能有一个值. 
   不写 return语句或return 空 默认返回 undefined

#### 传参

- 参数列表表示函数体执行所需要使用的数据，可以省略，小括号不能省
- JS 中允许形参和实参个数不匹配
- 实参少传，会按位置传参，无实参的形参值为 undefined
- 实参多传，会按位置传参，多的实参丢弃
- 所有函数的参数都是按值传递的(基本类型复制值，引用类型复制指针值(浅拷贝))




```javascript
1.
var obj1 = {
       name : "111"
    };
var obj2 = obj1;
     console.log(obj2.name); //111
     obj2.name = "222";
     console.log(obj1.name); //222
2.
var person = {
        name : "Tom"
    };
function obj(peo){
      peo.name = "Jerry";
            return peo;
        }
var result = obj(person);
console.log(result.name);// Jerry
console.log(person.name);// Jerry
3.
var person = {
            name : "Tom"
        }; 
function obj(peo){
     peo = {
     		name : "Jerry"
     	};
     return peo;
}
var result = obj(person);
console.log(result.name);// Jerry
console.log(person.name);// Tom
```

#### 函数内部对象 arguments

arguments对象是伴随函数调用自动生成的对象，以数组结构接收函数调用的实参，只能在函数内部使用

```javascript
function f1(a){
     document.write(a,'<br>');  //100
     document.write(arguments[0],arguments[1]);  //100 200
}
f1(100,200);
```


### 匿名函数(函数表达式)

```javascript
1.
var func = function (){
       函数体;
    };
func();
//定义变量保存函数地址，等同于函数名
2.
var func = (function (arg){函数体;});
```



#### 匿名函数自调用 

防止全局变量污染

```javascript
(function (arg){函数体;})();
```



### 函数声明和函数表达式的区别

        1. 函数表达式不存在函数声明提升，只有变量声明提升
        2. 函数表达式只能先创建在调用，函数声明可以先调用再声明    



### 回调函数

把匿名函数以实参的形式传递给函数，此时匿名函数叫回调函数


```javascript
function fun(f){
     f();
}
fun(function (){
     console.log('hello');
     return 1;
});
```


​    

### 系统函数(内置函数) js提供

1. 中文编码和解码
  
   ```javascript
   str = encodeURI('中文')
   str = decodeURI(str)
   ```
   
2. isNaN(var)  检查一个数据是否为NaN, 返回 boolean

3. parseInt(var)    转换数据为整数

   parseFloat(var)  转换数据为浮点型

4. isFinite(var)    检查一个数值是否为有限值，返回 boolean

   ```javascript
   isFinite(1/0);  //false     1/0  IsFinity 无穷值
   ```

5. eval('可执行表达式')   执行字符串中的表达式，相当于命令行

   ```javascript
   eval('function fun(){console.log("aaa");}');
   fun(); // aaa
   ```

   

## 变量的作用域


### 全局变量
在程序的任意地方都可以访问，可以在函数内部访问

### 局部变量

在函数内部 var 声明的变量，只能在函数内部访问,外界不能访问(形参为函数内声明变量)
省略关键字 var 定义的变量为全局变量，函数外也能访问

#### 变量声明提升

js  解释器会在解释代码之前把当前作用域的 var关键字声明的变量提升到当前作用域的最前面,
        赋值操作还是在原位置，没有用 var关键字声明的变量不提升变量声明

```javascript
console.log(a); // undefined
var a = 1;
console.log(b); //报错
b=1;
```



### 作用域链:

访问变量时，会首先在当前作用域中查找，没有会逐级向外链式查找

```javascript
1.
var a = 100;
function f2(){
     document.write(a);
     var a =1000;//变量声明提升,赋值不提升
}
f2();  // undefine
2.
var a = 1;
function f(){
    var a=a+3;
    console.log(a);
}
f();//NaN
console.log(a); //1
```



### 函数变量作用域

全局创建的函数可以全局任意位置调用，局部创建的函数只能在局部作用域调用

函数的声明会被提升到当前作用域最前面,可以先调用再声明


```javascript
f(); // 1
function f(){
    console.log(1);
}
```



#### 函数声明提升和变量声明提升(同作用域为前提)

1. 函数声明优先提升，变量声明后提升
2. 后提升的同名变量会覆盖前面提升的变量

**当同一作用域出现同名的变量声明和函数声明时，变量会覆盖函数声明,不论是否有var关键字声明** 





## 对象  

- 是一种引用类型的数据，存储在堆内存中
- 是一组属性和一组方法的集合
- 是一个具体的实例

对象属性名必须是基本数据类型，Number String undefined unll boolean

```javascript
var a = {undefined:'123',unll:'123',turn:123,123:123,'aaa':'aaa'}
```

对象的属性不能同名，普通属性名会覆盖同名方法名，后面定义的会覆盖前面定义的
对象的属性值可以是任意类型  基本类型，引用类型(函数，对象等)

#### object.prototype属性使您有能力向对象添加属性和方法。

**语法**

```javascript
object.prototype.name=value
```

eg: 

```html
<script type="text/javascript">
    function employee(name,job,born){
        this.name=name;
        this.job=job;
        this.born=born;
    }
    var bill=new employee("Bill Gates","Engineer",1985);
    employee.prototype.salary=null;
    bill.salary=20000;
    document.write(bill.salary);//输出：20000
</script>
```

#### object.constructor 属性返回对创建此对象的构造函数的引用

```html
<script type="text/javascript">
    var test=new Boolean();
	if (test.constructor==Array){
        	document.write("This is an Array");
        }
     if (test.constructor==Boolean){
        	document.write("This is a Boolean");
        }
     if (test.constructor==Date){
        	document.write("This is a Date");
        }
      if (test.constructor==String){
        	document.write("This is a String");
       }
</script>
```



### this

**判断 this 指向谁，看执行时而非定义时，只要函数(function)没有绑定在对象上调用，它的 this 就是 window**

- this 是指向类的当前实例，this 不能赋值。这前提是说 this 不能脱离 类/对象 来说，也就是说 this 是面向对象语言里常见的一个关键字。

- 当你使用 this 时，你应该是在使用对象/类 方式开发，否则 this 只是函数调用时的副作用。

#### JS 里的 this

- 在 function 内部被创建
- 指向调用时所在函数所绑定的对象（拗口）
- this 不能被赋值，但可以被 call/apply  改变

1. this 和构造器

    this 应该挂属性/字段，方法都应该放在原型上。

   ```javascript
   function Tab(nav, content) {
       this.nav = nav
       this.content = content
   }
   Tab.prototype.getNav = function() {
       return this.nav;
   };
   Tab.prototype.setNav = function(nav) {
       this.nav = nav;
   ```

2. this 和对象

   JS 中的对象不用类也可以创建，有人可能奇怪，类是对象的模板，对象都是从模板里 copy 出来的，没有类怎么创建对象？ JS 的确可以，并且你完全可以写上万行功能代码而不用写一个类。话说 OOP 里说的是面向对象编程，也没说面向类编程，是吧 ^_^ 。

   ```javascript
   var tab = {
       nav: '',
       content: '',
       getNav: function() {
           return this.nav;
       },
       setNav: function(n) {
           this.nav = n;
       }
   }
   tab.getNav()//this指向tab对象
   fun = tab.getNav
   fun()//this指向window对象
   ```

3. this 和函数

   this 和独立的函数放在一起是没有意义的，前面也提到过 this 应该是和面向对象相关的。纯粹的函数只是一个低级别的抽象，封装和复用。

   ```javascript
   function showMsg() {
       alert(this.message)
   }
   showMsg() // undefined
   //this指向window
   ```

   ```javascript
   function showMsg() {
       alert(this.message)
   }
   var m1 = {
       message: '输入的电话号码不正确'
   }
   var m2 = {
       message: '输入的身份证号不正确'
   }
   showMsg.call(m1) // '输入的电话号码不正确'
   showMsg.call(m2) // '输入的身份证号不正确'
   //用这种方式可以节省一些代码量，比如当两个 类/对象 有一共相似的方法时，不必写两份，只要定义一个，然后将其绑定在各自的原型和对象上。
   ```

4. 全局环境的 this

    this 是 “**指向调用时所在函数所绑定的对象**”

   浏览器环境中非函数内 this 指向 window:

   ```javascript
   alert(window=== this) // true
   ```

   因此你会看很很多开源 JS lib 这么写

   ```javascript
   (function() {})(this);
   (function() {}).call(this);
   //大意是把全局变量 window 传入匿名函数内缓存起来，避免直接访问。至于为啥要缓存，这跟 JS 作用域链有关系，读取越外层的标识符性能会越差。
   ```

   浏览器中，非函数内直接使用 var 声明的变量默认为全局变量，且默认挂在 window 上作为属性。

   判断 this 指向谁，看执行时而非定义时，只要函数(function)没有绑定在对象上调用，它的 this 就是 window。

5. this 和 DOM/事件

   前面说过 this 是指向当前类的实例对象，对于这些 tag 类来说，它们的很多方法内部用到的 this 是指向自己的。

   ```html
   <!-- this 指向 div -->
   <div onclick="alert(this)"></div>
   <div id="nav"></div>
   <script>
       nav.onclick = function() {
           alert(this) // 指向div#nav
       }
   </script>
   <!-- 在给元素节点添加事件的时候，其响应函数（handler）执行时的 this 都指向 Element 节点自身。 -->
   ```

   jQuery 也保持了和标准一致，但却让人迷惑，按 “**this 指向调用时所在函数所绑定的对象**” 这个定义，jQuery 事件 handler 里的 this，应该指向 jQuery 对象，而非 DOM 节点。因此你会发现在用 jQuery 时，经常需要把事件 handler 里的 element 在用 $ 包裹下变成 jQuery 对象后再去操作。比如

   ```javascript
   $('#nav').on('click', function() {
       var $el = $(this) // 再次转为 jQuery 对象，如果 this 直接为 jQuery 对象更好
       $el.attr('data-x', x)
       $el.attr('data-x', x)
   })
   ```

   

   注意:

   ```html
   <div id="nav" onclick="getId()">ddd</div>
   <script>
       function getId() {
           alert(this.id)
       }
   </script>
   ```

   点击 div 后，为什么 id 是 undefined，不说是指向的 当前元素 div 吗？ 如果记住了前面提到的一句话，就很清楚为啥是 undefined，把这句话再贴出来。

   > **判断 this 指向谁，看执行时而非定义时，只要函数(function)没有绑定在对象上调用，它的 this 就是 window**

   这里函数 getId 调用时没有绑定在任何对象上，可以理解成这种结构

   ```javascript
   div.onclick = function() {
       getId()
   }
   //getId 所处匿名函数里的 this 是 div，但 getId 自身内的 this 则不是了。
   ```

6. this 可以被 call/apply 改变

   call/apply 是函数调用的另外两种方式，两者的第一个参数都可以改变函数的上下文 this。call/apply 是 JS 里动态语言特性的表征。动态语言通俗的定义

   >程序在运行时可以改变其结构，新的函数可以被引进，已有的函数可以被删除，即程序在运行时可以发生结构上的变化

   JS 里的 call/apply 在任何一个流行的 lib 里都会用到，但几乎就是两个作用

   1. 配合写类工具实现OOP，如 [mootools](https://github.com/mootools/mootools-core/blob/master/Source/Class/Class.js), [ClassJS](https://github.com/darlanalves/ClassJS/blob/master/src/class/class.js), [class.js](https://github.com/snandy/class/blob/master/src/class.js),
   2. 修复DOM事件里的 this，如 [jQuery](https://github.com/jquery/jquery/blob/master/src/event.js), [events.js](https://github.com/kbjr/Events.js/blob/master/events.js)

7. me/self/that/_this 暂存 this

   如果采用 OOP 方式写 JS 代码，无可避免的会用到 this，方法内会访问类的内部属性（字段），也可能会调用类的另一个方法。当类的方法内又有一个 function 时，比如浏览器端开发经常遇见的给 DOM 元素添加事件，这时如果事件处理器（handler）中的想调用类的一个方法，此时 handler 内的 this 是 dom 元素而非类的当前对象。这个时候，需要把 this 暂存，开发者发挥着自己的聪明才智留下了几种经典的命名 me, self, that, _this。如

   `var self = this`

7. ES5 中新增的 bind 和 this

   call/apply 在 JS 里体现动态语言特性及动态语言的流行原因，其在 JS 用途如此广泛。ES5发布时将其采纳，提了一个更高级的方法 [bind](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)。

   ```javascript
   var modal = {
       message: 'This is A'
   }
    
   function showMsg() {
       alert(this.message)
   }
    
   var otherShowMsg = showMsg.bind(modal)
   otherShowMsg() // 'This is A'
   ```

   bind 只是 call/apply 的高级版，其它没什么特殊的。

8. ES6 箭头函数(arrow function) 和 this

   箭头函数的一个重要特征就是颠覆了上面的一句话，再贴一次

   > **判断 this 指向谁，看执行时而非定义时，只要函数(function)没有绑定在对象上调用，它的 this 就是 window**

   箭头函数的特征就是，定义在哪，this 就指向那。即箭头函数定义在一个对象里，那箭头函数里的 this 就指向该对象。如下

   ```javascript
   var book = {
       author: 'John Resig',
       init:  function() {
           document.onclick = ev => {
               alert(this.author) ; // 这里的 this 不是 document 了
           }
       }
   };
   book.init()
   ```

   对象 book 里有一个属性 author， 有一个 init 方法， 给 document 添加了一个点击事件，如果是传统的函数，我们知道 this 指向应该是 document，但箭头函数会指向当前对象 book。

   箭头函数让 JS 回归自然和简单，函数定义在哪它 this 就指向哪，定义在对象里它指向该对象，定义在类的原型上，就指向该类的实例，望文知意这样更容易理解。

### 总结： 

函数的上下文 this 是 JS 里不太好理解的，在于 JS 函数自身有[多种用途](http://www.cnblogs.com/snandy/p/4763324.html)。目的是实现各种语言范型（面向对象，函数式，动态）。this 本质是和面向对象联系的，和写类，对象关联一起的， 和“函数式”没有关系的。如果你采用过程式函数式开发，完全不会用到一个 this。 但在浏览器端开发时却无可避免的会用到 this，这是因为浏览器对象模型（DOM）本身采用面向对象方式开发，Tag 实现为一个个的类，类的方法自然会引用类的其它方法，引用方式必然是用 this。当你给DOM对象添加事件时，回调函数里引用该对象就只能用 this 了。



### 内置对象(通用):
   Object Array  String  Number  RegExp   Math  Date...



### 宿主对象：根据不同的执行环境限制使用
​    BOM : 浏览器对象
​    DOM : 必须在浏览器环境下使用

### 自定义对象

1. 对象字面量(直接量)
2. 内置构造函数
    1. 使用 new 关键字加构造方法才能创建对象
    2. 不加 new 关键字构造方法是类型转换函数

3. 自定义构造函数



### 使用字面量创建对象

```javascript
var phone = {}; //创建空对象
var phone1 = {
      color:'red',
      brand:'apple',
      size:5.7,
      'mian-in':'china'
      'a b':333
    };
```

**属性名的引号可加可不加，有特殊字符必须加引号**



### 使用内置构造函数    Object()

```javascript
var book = new Object();  //{}
console.log(book.id); //undefined
book.id = 100; 
console.log(book); //{id:100}
book.id = 'aaaa'; 
console.log(book); //{id:aaaa}  已有属性会重新赋值
book['title'] = '标题'; 
console.log(book); //{id:'aaaa',title:'标题'}
```

- 构造函数调用要使用 new 关键字
- 点成员访问符访问属性时不能加引号
- [‘var’] 访问属性时必须加引号,不然会在当前作用域寻找该变量的值
- 对象.属性 等同 对象['属性']

#### 复制对象


```javascript
var newObject = new 构造方法(oldObject);
//对象为引用类型，此方法能解决两个引用访问同一对象问题
```



## 属性访问

   1. 对象.属性名

   2. 对象['属性名']

    3. 遍历对象属性
        语法 :  
        
        ```javascript
        for(var key in 对象){
           var value = 对象[key]; // 不能使用对象.key和对象['key']，会去访问叫key的属性
        }
        //预定义属性无法遍历(预定义属性为js默认为每一个对象添加的)
        ```



### 检测属性

1. in 关键字    是否在其中 返回boolean

```javascript
var a = {123:'123','key':'value'}
console.log(123 in a);  //true
console.log('key' in a);  //true
```

   2. 对象.hasOwnProperty('属性') 返回 boolean

   3. 对象.属性 === undefined  返回 boolean

   4. 对象['属性'] === undefined  返回 boolean



### 对象中的方法(指向函数的属性)

```javascript
var per = {
    color:'red',
    brand:'apple',
    size:5.7,
    sky : function (){console.log(per.color + this.brand);}
};
per.sky();
```



## JavaScript 全局对象

​    全局属性和函数可用于所有内建的 JavaScript 对象。

### 全局对象描述

- 全局对象是预定义的对象，作为 JavaScript 的全局函数和全局属性的占位符。通过使用全局对象，可以访问所有
  其他所有预定义的对象、函数和属性。全局对象不是任何对象的属性，所以它没有名称。
- 在顶层 JavaScript 代码中，可以用关键字 this 引用全局对象。但通常不必用这种方式引用全局对象，因为全局
  对象是作用域链的头，这意味着所有非限定性的变量和函数名都会作为该对象的属性来查询。例如，当JavaScript 
  代码引用 parseInt() 函数时，它引用的是全局对象的 parseInt 属性。全局对象是作用域链的头，还意味着在顶层
  JavaScript 代码中声明的所有变量都将成为全局对象的属性。
- 全局对象只是一个对象，而不是类。既没有构造函数，也无法实例化一个新的全局对象
- 在 JavaScript 代码嵌入一个特殊环境中时，全局对象通常具有环境特定的属性。实际上，ECMAScript 标准没有规定全局对象的类型，JavaScript 的实现或嵌入的 JavaScript 都可以把任意类型的对象作为全局对象，只要该对象定义
  了这里列出的基本属性和函数。例如，在允许通过 LiveConnect 或相关的技术来脚本化 Java 的 JavaScript 实现中，
  全局对象被赋予了这里列出的 java 和 Package 属性以及 getClass() 方法。而在客户端 JavaScript 中，全局对象
  就是 Window 对象，表示允许 JavaScript 代码的 Web 浏览器窗口。

### 顶层函数（全局函数）

| 函数                 | 描述                                             |
| -------------------- | ------------------------------------------------ |
| decodeURI()          | 解码某个编码的 URI                               |
| decodeURIComponent() | 解码一个编码的 URI 组件                          |
| encodeURI()          | 把字符串编码为 URI                               |
| encodeURIComponent() | 把字符串编码为 URI 组件                          |
| escape()             | 对字符串进行编码                                 |
| eval()               | 计算 JavaScript 字符串，并把它作为脚本代码来执行 |
| getClass()           | 返回一个 JavaObject 的 JavaClass                 |
| isFinite()           | 检查某个值是否为有穷大的数                       |
| isNaN()              | 检查某个值是否是数字                             |
| Number()             | 把对象的值转换为数字                             |
| parseFloat()         | 解析一个字符串并返回一个浮点数                   |
| parseInt()           | 解析一个字符串并返回一个整数                     |
| String()             | 把对象的值转换为字符串                           |
| unescape()           | 对由 escape() 编码的字符串进行解码               |



## 异常处理

- `try` 语句测试代码块的错误。
- `catch` 语句处理错误。
- `throw` 语句创建自定义错误。
- `finally` 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。

```javascript
try {
   ...    //异常的抛出
} catch(err) {
   ...    //异常的捕获与处理
} finally {
   ...    //结束处理
}
```

抛出异常
    throw err;


```javascript
x = document.getElementById("demo").value;
try { 
    if(x == "") throw "is Empty";
    if(isNaN(x)) throw "not a number";
    if(x > 10) throw "too high";
    if(x < 5) throw "too low";
}catch(err) {
    message.innerHTML = "Input " + err;
}
```



## ES6
​    ECMA组织制定js规范,现在的标准  ECMAScrip6

### 块级作用域

在大括号内用 let关键字声明变量,只能在快内访问

语法 :

```javascript
{
    let a=1;    //let关键字声明块级作用域变量,不能用var
}
```


块级作用域 : {}, for, if,while,do-while,switch...



### 箭头函数

是回调函数的另一种写法，和匿名函数不完全一样，不创建局部作用于

```javascript
(arguments)=>{
    代码块;
}
arguments=>{代码块;}
//当代码块只有一行代码，且含有return时可以这样写
(a,b)=>a-b
```



### 缺省参数

允许为形参设置默认值

```javascript
function add(a,b=0){
    return a+b;
}
```



### 模板字符串(格式化字符串)

使用反引号 \` \`括起字符串,使用 ${表达式}导入数据

```javascript
var str = `${year}年${month+1}月${date<10?'0'+date:date}日`
```

在模板字符串中的非{}中可以写任意符号，都会被解释为字符串，{}中可以写任意js语法，会被解释执行



### generator

generator（生成器）是ES6标准引入的新的数据类型。一个generator看上去像一个函数，但可以返回多次。

```javascript
function* foo(x) {
     yield x + 1;
     yield x + 2;
     return x + 3;
}
```

generator和函数不同的是，generator由function\*定义（注意多出的\*号），并且，除了return语句，还可以用yield返回多次.

直接调用一个generator和调用函数不一样，fib(5)仅仅是创建了一个generator对象，还没有去执行它

调用generator对象有两个方法

一是不断地调用generator对象的next()方法：

```javascript
var f = fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: false}
f.next(); // {value: undefined, done: true}
```

- next()方法会执行generator的代码，然后，每次遇到yield x;就返回一个对象{value: x, done: true/false}，然后“暂停”。
- 返回的value就是yield的返回值，done表示这个generator是否已经执行结束了。如果done为true，则value就是return的返回值。
- 当执行到done为true时，这个generator对象就已经全部执行完毕，不要再继续调用next()了。

第二个方法是直接用for ... of循环迭代generator对象，这种方式不需要我们自己判断done：

```javascript
for (var x of fib(10)) {
     console.log(x); // 依次输出0, 1, 1, 2, 3, ...
}
```









