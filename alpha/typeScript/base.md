[TOC]



## 安装

### NPM 安装 TypeScript

如果你的本地环境已经安装了 npm 工具，可以使用以下命令来安装：

```shell
npm install -g typescript
```

安装完成后我们可以使用 **tsc** 命令来执行 TypeScript 的相关代码，以下是查看版本号：

```shell
$ tsc -v
Version 3.2.2
```



## 编译

### TypeScript 程序文件

## 实例

`Test.ts`

```typescript
const hello : string = "Hello World!"; console.log(hello)
```

以上代码首先通过 **tsc** 命令编译：

```shell
tsc Test.ts
```

得到如下 js 代码：

```javascript
var message = "Hello World"; console.log(message);
```

最后我们使用 node 命令来执行该 js 代码。

我们可以同时编译多个 ts 文件：

```shell
tsc file1.ts, file2.ts, file3.ts
```



### tsc 常用编译参数

| 编译参数                   |                           **说明**                           |
| :------------------------- | :----------------------------------------------------------: |
| **--help**                 |                         显示帮助信息                         |
| **--module**               |                         载入扩展模块                         |
| **--target**               |                        设置 ECMA 版本                        |
| **--declaration**          | 额外生成一个` .d.ts `扩展名的文件。`tsc ts-hw.ts --declaration`以上命令会生成 ts-hw.d.ts、ts-hw.js 两个文件。 |
| **--removeComments**       |                        删除文件的注释                        |
| **--out**                  |              编译多个文件并合并到一个输出的文件              |
| **--sourcemap**            | 生成一个 sourcemap (.map) 文件。sourcemap 是一个存储源代码与编译代码对应位置映射的信息文件。 |
| **--module noImplicitAny** |           在表达式和声明上有隐含的 any 类型时报错            |
| **--watch**                | 在监视模式下运行编译器。会监视输出文件，在它们改变时重新编译。 |



## 语法

### 空白和换行

TypeScript 会忽略程序中出现的空格、制表符和换行符。

空格、制表符通常用来缩进代码，使代码易于阅读和理解。

### TypeScript 区分大小写

TypeScript 区分大写和小写字符。

### 分号是可选的

每行指令都是一段语句，你可以使用分号或不使用， 分号在 TypeScript 中是可选的，建议使用。

如果语句写在同一行则一定需要使用分号来分隔，否则会报错，如：

```typescript
console.log("Runoob");console.log("Google");
```

### TypeScript 注释

注释是一个良好的习惯，虽然很多程序员讨厌注释，但还是建议你在每段代码写上文字说明。

注释可以提高程序的可读性。

注释可以包含有关程序一些信息，如代码的作者，有关函数的说明等。

编译器会忽略注释。

### TypeScript 支持两种类型的注释

- **单行注释 ( // )** − 在 // 后面的文字都是注释内容。
- **多行注释 (/\* \*/)** − 这种注释可以跨越多行。



## 基础类型

TypeScript 包含的数据类型如下表:

|  数据类型  |  关键字   |                             描述                             |
| :--------: | :-------: | :----------------------------------------------------------: |
|  任意类型  |    any    |           声明为 any 的变量可以赋予任意类型的值。            |
|  数字类型  |  number   | 双精度 64 位浮点值。它可以用来表示整数和分数。`let binaryLiteral: number = 0b1010; // 二进制 let octalLiteral: number = 0o744;    // 八进制 let decLiteral: number = 6;    // 十进制 let hexLiteral: number = 0xf00d;    // 十六进制` |
| 字符串类型 |  string   | 一个字符系列，使用单引号（**'**）或双引号（**"**）来表示字符串类型。反引号（**`**）来定义多行文本和内嵌表达式。`let name: string = "Runoob"; let years: number = 5; let words: string = `您好，今年是 ${ name } 发布 ${ years + 1} 周年`;` |
|  布尔类型  |  boolean  |    表示逻辑值：true 和 false。`let flag: boolean = true;`    |
|  数组类型  |    无     | 声明变量为数组。`// 在元素类型后面加上[] let arr: number[] = [1, 2];  // 或者使用数组泛型 let arr: Array<number> = [1, 2];` |
|    元组    |    无     | 元组类型用来表示已知元素数量和类型的数组，各元素的类型不必相同，对应位置的类型需要相同。`let x: [string, number]; x = ['Runoob', 1];    // 运行正常 x = [1, 'Runoob'];    // 报错 console.log(x[0]);    // 输出 Runoob` |
|    枚举    |   enum    | 枚举类型用于定义数值集合。`enum Color {Red, Green, Blue}; let c: Color = Color.Blue; console.log(c);    // 输出 2` |
|    void    |   void    | 用于标识方法返回值的类型，表示该方法没有返回值。`function hello(): void {     alert("Hello Runoob"); }` |
|    null    |   null    |                       表示对象值缺失。                       |
| undefined  | undefined |                用于初始化变量为一个未定义的值                |
|   never    |   never   | never 是其它类型（包括 null 和 undefined）的子类型，代表从不会出现的值。 |

**注意：**TypeScript 和 JavaScript 没有整数类型。

## Any 类型

任意值是 TypeScript 针对编程时类型不明确的变量使用的一种数据类型，它常用于以下三种情况。

1、变量的值会动态改变时，比如来自用户的输入，任意值类型可以让这些变量跳过编译阶段的类型检查，示例代码如下：

```typescript
let x: any = 1;    // 数字类型
x = 'I am who I am';    // 字符串类型
x = false;    // 布尔类型
```

改写现有代码时，任意值允许在编译时可选择地包含或移除类型检查，示例代码如下：

```typescript
let x: any = 4;
x.ifItExists();    // 正确，ifItExists方法在运行时可能存在，但这里并不会检查
x.toFixed();    // 正确
```

定义存储各种类型数据的数组时，示例代码如下：

```typescript
let arrayList: any[] = [1, false, 'fine'];
arrayList[1] = 100;
```

## Null 和 Undefined

### null

在 JavaScript 中 null 表示 "什么都没有"。

null是一个只有一个值的特殊类型。表示一个空对象引用。

用 typeof 检测 null 返回是 object。

### undefined

在 JavaScript 中, undefined 是一个没有设置值的变量。

typeof 一个没有值的变量会返回 undefined。

Null 和 Undefined 是其他任何类型（包括 void）的子类型，可以赋值给其它类型，如数字类型，此时，赋值后的类型会变成 null 或 undefined。而在TypeScript中启用严格的空校验（--strictNullChecks）特性，就可以使得null 和 undefined 只能被赋值给 void 或本身对应的类型，示例代码如下：

```typescript
// 启用 --strictNullChecks
let x: number;
x = 1; // 运行正确
x = undefined;    // 运行错误
x = null;    // 运行错误
```

上面的例子中变量 x 只能是数字类型。如果一个类型可能出行 null 或 undefined， 可以用 | 来支持多种类型，示例代码如下：

```typescript
// 启用 --strictNullChecks
let x: number | null | undefined;
x = 1; // 运行正确
x = undefined;    // 运行正确
x = null;    // 运行正确
```

更多内容可以查看：[JavaScript typeof, null, 和 undefined](https://www.runoob.com/js/js-typeof.html)

------

## never 类型

never 是其它类型（包括 null 和 undefined）的子类型，代表从不会出现的值。这意味着声明为 never 类型的变量只能被 never 类型所赋值，在函数中它通常表现为抛出异常或无法执行到终止点（例如无限循环），示例代码如下：

```typescript
let x: never;
let y: number;

// 运行错误，数字类型不能转为 never 类型
x = 123;

// 运行正确，never 类型可以赋值给 never类型
x = (()=>{ throw new Error('exception')})();

// 运行正确，never 类型可以赋值给 数字类型
y = (()=>{ throw new Error('exception')})();

// 返回值为 never 的函数可以是抛出异常的情况
function error(message: string): never {
    throw new Error(message);
}

// 返回值为 never 的函数可以是无法被执行到的终止点的情况
function loop(): never {
    while (true) {}
}
```



## 变量声明

变量是一种使用方便的占位符，用于引用计算机内存地址。

我们可以把变量看做存储数据的容器。

TypeScript 变量的命名规则：

- 变量名称可以包含数字和字母。
- 除了下划线 **_** 和美元 **$** 符号外，不能包含其他特殊字符，包括空格。
- 变量名不能以数字开头。

变量使用前必须先声明，我们可以使用 var 来声明变量。

我们可以使用以下四种方式来声明变量：

1. 声明变量的类型及初始值：

   ```
   var [变量名] : [类型] = 值;
   ```

2. 声明变量的类型及但没有初始值，变量值会设置为 undefined：

   ```
   var [变量名] : [类型];
   ```

3. 声明变量并初始值，但不设置类型类型，该变量可以是任意类型：

   ```
   var [变量名] = 值;
   ```

4. 声明变量没有设置类型和初始值，类型可以是任意类型，默认初始值为 undefined：

   ```
   var [变量名];
   ```

**TypeScript 遵循强类型**，如果将不同的类型赋值给变量会编译错误，如下实例：

```typescript
var num:number = "hello"     // 这个代码会编译错误
```



### 类型断言（Type Assertion）

类型断言可以用来手动指定一个值的类型，即允许变量从一种类型更改为另一种类型。

语法格式：

```
<类型>值
```

或:

```
值 as 类型
```

**实例**

```typescript
var str = '1'  var str2:number = <number> <any> str   //str、str2 是 string 类型
```



### 类型推断

当类型没有给出时，TypeScript 编译器利用类型推断来推断类型。

如果由于缺乏声明而不能推断出类型，那么它的类型被视作默认的动态 any 类型。

```typescript
var num = 2;    // 类型推断为 number 
console.log("num 变量的值为 "+num);  
num = "12";    // 编译错误 console.log(num);
```

- 第一行代码声明了变量 num 并=设置初始值为 2。 注意变量声明没有指定类型。因此，程序使用类型推断来确定变量的数据类型，第一次赋值为 2，**num** 设置为 number 类型。

- 第三行代码，当我们再次为变量设置字符串类型的值时，这时编译会错误。因为变量已经设置为了 number 类型。

  ```
  error TS2322: Type '"12"' is not assignable to type 'number'.
  ```



## 变量作用域

变量作用域指定了变量定义的位置。

程序中变量的可用性由变量作用域决定。

TypeScript 有以下几种作用域：

- **全局作用域** − 全局变量定义在程序结构的外部，它可以在你代码的任何位置使用。
- **类作用域** − 这个变量也可以称为 **字段**。类变量声明在一个类里头，但在类的方法外面。 该变量可以通过类的对象来访问。类变量也可以是静态的，静态的变量可以通过类名直接访问。
- **局部作用域** − 局部变量，局部变量只能在声明它的一个代码块（如：方法）中使用。

以下实例说明了三种作用域的使用：

```typescript
var global_num = 12          // 全局变量
class Numbers { 
   num_val = 13;             // 类变量
   static sval = 10;         // 静态变量
   
   storeNum():void { 
      var local_num = 14;    // 局部变量
   } 
} 
console.log("全局变量为: "+global_num)  
console.log(Numbers.sval)   // 静态变量
var obj = new Numbers(); 
console.log("类变量: "+obj.num_val)
```

以上代码使用 tsc 命令编译为 JavaScript 代码为：

```javascript
var global_num = 12; // 全局变量
var Numbers = /** @class */ (function () {
    function Numbers() {
        this.num_val = 13; // 类变量
    }
    Numbers.prototype.storeNum = function () {
        var local_num = 14; // 局部变量
    };
    Numbers.sval = 10; // 静态变量
    return Numbers;
}());
console.log("全局变量为: " + global_num);
console.log(Numbers.sval); // 静态变量
var obj = new Numbers();
console.log("类变量: " + obj.num_val);
```



## 函数

```typescript
function test() {   // 函数定义
    console.log("调用函数"); 
} 
test();      // 调用函数
```

### 函数返回值

```typescript
// 函数定义
function greet():string { // 返回一个字符串
    return "Hello World" 
} 
function caller() { 
    var msg = greet() // 调用 greet() 函数 
    console.log(msg) 
} 
// 调用函数
caller()
```

- return_type 是返回值的类型。
- return 关键词后跟着要返回的结果。
- 一个函数只能有一个 return 语句。
- 返回值的类型需要与函数定义的返回类型(return_type)一致。

### 带参数函数

语法格式如下所示：

```typescript
function add(x: number, y: number): number {
    return x + y;
}
console.log(add(1,2))
```

### 可选参数

在 TypeScript 函数里，如果我们定义了参数，则我们必须传入这些参数，除非将这些参数设置为可选，可选参数使用问号标识 ？。

```typescript
function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}
let result1 = buildName("Bob");  // 正确
let result2 = buildName("Bob", "Adams", "Sr.");  // 错误，参数太多了
let result3 = buildName("Bob", "Adams");  // 正确
```

可选参数必须跟在必需参数后面。 如果上例我们想让 firstName 是可选的，lastName 必选，那么就要调整它们的位置，把 firstName 放在后面。

如果都是可选参数就没关系。

### 默认参数

我们也可以设置参数的默认值，这样在调用函数的时候，如果不传入该参数的值，则使用默认参数，语法格式为：

```
function function_name(param1[:type],param2[:type] = default_value) { 
}
```

注意：参数不能同时设置为可选和默认。

### 剩余参数

有一种情况，我们不知道要向函数传入多少个参数，这时候我们就可以使用剩余参数来定义。

剩余参数语法允许我们将一个不确定数量的参数作为一个数组传入。

```typescript
function buildName(firstName: string, ...restOfName: string[]) {
    return firstName + " " + restOfName.join(" ");
}
let employeeName = buildName("Joseph", "Samuel", "Lucas", "MacKinzie");
```

函数的最后一个命名参数 restOfName 以 ... 为前缀，它将成为一个由剩余参数组成的数组，索引值从0（包括）到 restOfName.length（不包括）。

### 匿名函数

```typescript
var msg = function() { //不带参数匿名函数
    return "hello world";  
} 
console.log(msg())
var res = function(a:number,b:number) { //带参数匿名函数
    return a*b;  
}; 
console.log(res(12,2))
```

### 匿名函数自调用

匿名函数自调用在函数后使用 () 即可：

```typescript
(function () { 
    var x = "Hello!!";   
    console.log(x)     
 })()
```

### Lambda 函数

Lambda 函数也称之为箭头函数。

```typescript
var foo = (x:number)=>10 + x 
console.log(foo(100))      //输出结果为 110
var foo = (x:number)=> {    
    x = 10 + x 
    console.log(x)  
} 
foo(100)
```

单个参数 **()** 是可选的：

```typescript
var display = x => { 
    console.log("输出为 "+x) 
} 
display(12)
```

无参数时可以设置空括号：

```typescript
var disp =()=> { 
    console.log("Function invoked"); 
} 
disp();
```



## 声明数组

```typescript
var array_name[:datatype];        //声明 
array_name = [val1,val2,valn..]   //初始化
```

或者直接在声明时初始化：

```typescript
var array_name[:data type] = [val1,val2…valn]
```

如果数组声明时未设置类型，则会被认为是 any 类型，在初始化时根据第一个元素的类型来推断数组的类型。

## 数组解构

我们也可以把数组元素赋值给变量，如下所示：

```typescript
var arr:number[] = [12,13] 
var[x,y] = arr // 将数组的两个元素赋值给变量 x 和 y
console.log(x) 
console.log(y)
```

## 多维数组

```typescript
var multi:number[][] = [[1,2,3],[23,24,25]]  
console.log(multi[0][0]) 
console.log(multi[0][1]) 
console.log(multi[0][2]) 
console.log(multi[1][0]) 
console.log(multi[1][1]) 
console.log(multi[1][2])
```



## 数组在函数中的使用

### 作为参数传递给函数

```typescript
var sites = new Array("Google", "Runoob", "Taobao", "Facebook");
function disp(arr_sites) {
        for (var i = 0; i < arr_sites.length; i++) {
                console.log(arr_sites[i]);
        }
}
disp(sites);
```



### 作为函数的返回值

```typescript
function disp():string[] { 
        return new Array("Google", "Runoob", "Taobao", "Facebook");
} 
var sites:string[] = disp() 
for(var i in sites) { 
        console.log(sites[i]) 
}
```

## 数组方法

下表列出了一些常用的数组方法：

| 序号 |                         方法 & 描述                          |                             实例                             |
| :--: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  1.  |          concat()连接两个或更多的数组，并返回结果。          | `var alpha = ["a", "b", "c"];  var numeric = [1, 2, 3];  var alphaNumeric = alpha.concat(numeric);  console.log("alphaNumeric : " + alphaNumeric );    // a,b,c,1,2,3   ` |
|  2.  |        every()检测数值元素的每个元素是否都符合条件。         | `function isBigEnough(element, index, array) {          return (element >= 10);  }           var passed = [12, 5, 8, 130, 44].every(isBigEnough);  console.log("Test Value : " + passed ); // false` |
|  3.  |     filter()检测数值元素，并返回符合条件所有元素的数组。     | `function isBigEnough(element, index, array) {     return (element >= 10);  }             var passed = [12, 5, 8, 130, 44].filter(isBigEnough);  console.log("Test Value : " + passed ); // 12,130,44` |
|  4.  |          forEach()数组每个元素都执行一次回调函数。           | `let num = [7, 8, 9]; num.forEach(function (value) {     console.log(value); }); `编译成 JavaScript 代码：`var num = [7, 8, 9]; num.forEach(function (value) {     console.log(value);  // 7   8   9 });` |
|  5.  |       indexOf()搜索数组中的元素，并返回它所在的位置。        | `var index = [12, 5, 8, 130, 44].indexOf(8);  console.log("index is : " + index );  // 2` |
|  6.  |            join()把数组的所有元素放入一个字符串。            | `var arr = new Array("First","Second","Third");             var str = arr.join();  console.log("str : " + str );  // First,Second,Third             var str = arr.join(", ");  console.log("str : " + str );  // First, Second, Third            var str = arr.join(" + ");  console.log("str : " + str );  // First + Second + Third` |
|  7.  | lastIndexOf()返回一个指定的字符串值最后出现的位置，在一个字符串中的指定位置从后向前搜索。 | `var index = [12, 5, 8, 130, 44].lastIndexOf(8);  console.log("index is : " + index );  // 2` |
|  8.  |  map()通过指定函数处理数组的每个元素，并返回处理后的数组。   | `var numbers = [1, 4, 9];  var roots = numbers.map(Math.sqrt);  console.log("roots is : " + roots );  // 1,2,3` |
|  9.  |        pop()删除数组的最后一个元素并返回删除的元素。         | `var numbers = [1, 4, 9];             var element = numbers.pop();  console.log("element is : " + element );  // 9            var element = numbers.pop();  console.log("element is : " + element );  // 4` |
| 10.  |    push()向数组的末尾添加一个或更多元素，并返回新的长度。    | `var numbers = new Array(1, 4, 9);  var length = numbers.push(10);  console.log("new numbers is : " + numbers );  // 1,4,9,10  length = numbers.push(20);  console.log("new numbers is : " + numbers );  // 1,4,9,10,20` |
| 11.  |         reduce()将数组元素计算为一个值（从左到右）。         | `var total = [0, 1, 2, 3].reduce(function(a, b){ return a + b; });  console.log("total is : " + total );  // 6` |
| 12.  |      reduceRight()将数组元素计算为一个值（从右到左）。       | `var total = [0, 1, 2, 3].reduceRight(function(a, b){ return a + b; });  console.log("total is : " + total );  // 6` |
| 13.  |                reverse()反转数组的元素顺序。                 | `var arr = [0, 1, 2, 3].reverse();  console.log("Reversed array is : " + arr );  // 3,2,1,0` |
| 14.  |             shift()删除并返回数组的第一个元素。              | `var arr = [10, 1, 2, 3].shift();  console.log("Shifted value is : " + arr );  // 10` |
| 15.  |        slice()选取数组的的一部分，并返回一个新数组。         | `var arr = ["orange", "mango", "banana", "sugar", "tea"];  console.log("arr.slice( 1, 2) : " + arr.slice( 1, 2) );  // mango console.log("arr.slice( 1, 3) : " + arr.slice( 1, 3) );  // mango,banana` |
| 16.  |         some()检测数组元素中是否有元素符合指定条件。         | `function isBigEnough(element, index, array) {     return (element >= 10);             }             var retval = [2, 5, 8, 1, 4].some(isBigEnough); console.log("Returned value is : " + retval );  // false            var retval = [12, 5, 8, 1, 4].some(isBigEnough);  console.log("Returned value is : " + retval );  // true` |
| 17.  |                 sort()对数组的元素进行排序。                 | `var arr = new Array("orange", "mango", "banana", "sugar");  var sorted = arr.sort();  console.log("Returned string is : " + sorted );  // banana,mango,orange,sugar` |
| 18.  |               splice()从数组中添加或删除元素。               | `var arr = ["orange", "mango", "banana", "sugar", "tea"];   var removed = arr.splice(2, 0, "water");   console.log("After adding 1: " + arr );    // orange,mango,water,banana,sugar,tea  console.log("removed is: " + removed);             removed = arr.splice(3, 1);   console.log("After removing 1: " + arr );  // orange,mango,water,sugar,tea  console.log("removed is: " + removed);  // banana` |
| 19.  |          toString()把数组转换为字符串，并返回结果。          | `var arr = new Array("orange", "mango", "banana", "sugar");          var str = arr.toString();  console.log("Returned string is : " + str );  // orange,mango,banana,sugar` |
| 20.  |  unshift()向数组的开头添加一个或更多元素，并返回新的长度。   | `var arr = new Array("orange", "mango", "banana", "sugar");  var length = arr.unshift("water");  console.log("Returned array is : " + arr );  // water,orange,mango,banana,sugar  console.log("Length of the array is : " + length ); // 5` |



## 元组

我们知道数组中元素的数据类型都是相同的，如果存储的元素数据类型不同，则需要使用元组。

元组中允许存储不同类型的元素，元组可以作为参数传递给函数。

创建元组的语法格式如下：

```typescript
var tuple_name = [value1,value2,value3,…value n]
```

或者我们可以先声明一个空元组，然后再初始化：

```typescript
var mytuple = []; 
mytuple[0] = 120 
mytuple[1] = 234
```

### 访问元组

元组中元素使用索引来访问，第一个元素的索引值为 0，第二个为 1，以此类推第 n 个为 n-1，语法格式如下:

```
tuple_name[index]
```

### 元组运算

我们可以使用以下两个函数向元组添加新元素或者删除元素：

- `push()` 向元组添加元素，添加在最后面。
- `pop()` 从元组中移除元素（最后一个），并返回移除的元素。

```typescript
var mytuple = [10,"Hello","World","typeScript"]; 
console.log("添加前元素个数："+mytuple.length)    // 返回元组的大小
mytuple.push(12)                                    // 添加到元组中
console.log("添加后元素个数："+mytuple.length) 
console.log("删除前元素个数："+mytuple.length) 
console.log(mytuple.pop()+" 元素从元组中删除") // 删除并返回删除的元素
console.log("删除后元素个数："+mytuple.length)
```

### 更新元组

元组是可变的，这意味着我们可以对元组进行更新操作：

```typescript
mytuple[0] = 121  
```

### 解构元组

我们也可以把元组元素赋值给变量，如下所示：

```typescript
var a =[10,"Runoob"] 
var [b,c] = a 
```



## 联合类型

联合类型（Union Types）可以通过管道(|)将变量设置多种类型，赋值时可以根据设置的类型来赋值。

**注意**：只能赋值指定的类型，如果赋值其它类型就会报错。

创建联合类型的语法格式如下：

```typescript
Type1|Type2|Type3 
```

**实例**

```typescript
var val:string|number 
val = 12 
console.log("数字为 "+ val) 
val = "Runoob" 
console.log("字符串为 " + val)
```

也可以将联合类型作为函数参数使用：

```typescript
function disp(name:string|string[]) { 
        if(typeof name == "string") { 
                console.log(name) 
        } else { 
                var i; 
                for(i = 0;i<name.length;i++) { 
                console.log(name[i])
                } 
        } 
} 
disp("Runoob") 
console.log("输出数组....") 
disp(["Runoob","Google","Taobao","Facebook"])
```

### 联合类型数组

```typescript
var arr:number[]|string[]; 
var i:number; 
arr = [1,2,4] 
console.log("**数字数组**")  
for(i = 0;i<arr.length;i++) { 
   console.log(arr[i]) 
}  
arr = ["Runoob","Google","Taobao"] 
console.log("**字符串数字**")  
for(i = 0;i<arr.length;i++) { 
   console.log(arr[i]) 
}
```



## TypeScript 接口

接口是一系列抽象方法的声明，是一些方法特征的集合，这些方法都应该是抽象的，需要由具体的类去实现，然后第三方就可以通过这组抽象方法调用，让具体的类执行具体的方法。

以下实例中，我们定义了一个接口 IPerson，接着定义了一个变量 customer，它的类型是 IPerson。

customer 实现了接口 IPerson 的属性和方法。

```typescript
interface IPerson { 
    firstName:string, 
    lastName:string, 
    sayHi: ()=>string 
} 
var customer:IPerson = { 
    firstName:"Tom",
    lastName:"Hanks", 
    sayHi: ():string =>{return "Hi there"} 
} 
console.log("Customer 对象 ") 
console.log(customer.firstName) 
console.log(customer.lastName) 
console.log(customer.sayHi())  
var employee:IPerson = { 
    firstName:"Jim",
    lastName:"Blakes", 
    sayHi: ():string =>{return "Hello!!!"} 
} 
console.log("Employee  对象 ") 
console.log(employee.firstName) 
console.log(employee.lastName)
```

需要注意接口不能转换为 JavaScript。 它只是 TypeScript 的一部分。

### 联合类型和接口

```typescript
interface RunOptions { 
    program:string; 
    commandline:string[]|string|(()=>string); 
}
// commandline 是字符串
var options:RunOptions = {program:"test1",commandline:"Hello"}; 
console.log(options.commandline)  
// commandline 是字符串数组
options = {program:"test1",commandline:["Hello","World"]}; 
console.log(options.commandline[0]); 
console.log(options.commandline[1]);  
// commandline 是一个函数表达式
options = {program:"test1",commandline:()=>{return "**Hello World**";}}; 
var fn:any = options.commandline; 
console.log(fn());
```



### 接口和数组

接口中我们可以将数组的索引值和元素设置为不同类型，索引值可以是数字或字符串。

```typescript
interface namelist { 
   [index:number]:string 
} 
var list2:namelist = ["John",1,"Bran"] / 错误元素 1 不是 string 类型
interface ages { 
   [index:string]:number 
} 
var agelist:ages; 
agelist["John"] = 15   // 正确 
agelist[2] = "nine"   // 错误
```



### 接口继承

接口继承就是说接口可以通过其他接口来扩展自己。

Typescript 允许接口继承多个接口。

继承使用关键字 **extends**。

#### 单继承实例

```typescript
interface Person { 
   age:number 
} 
interface Musician extends Person { 
   instrument:string 
} 
var drummer = <Musician>{}; 
drummer.age = 27 
drummer.instrument = "Drums" 
console.log("年龄:  "+drummer.age)
console.log("喜欢的乐器:  "+drummer.instrument)
```

#### 多继承实例

```typescript
interface IParent1 { 
    v1:number 
} 
interface IParent2 { 
    v2:number 
} 
interface Child extends IParent1, IParent2 { } 
var Iobj:Child = { v1:12, v2:23} 
console.log("value 1: "+Iobj.v1+" value 2: "+Iobj.v2)
```



## 类

TypeScript 类定义方式如下：

```
class class_name { 
    // 类作用域
}
```

定义类的关键字为 class，后面紧跟类名，类可以包含以下几个模块（类的数据成员）：

- **字段** − 字段是类里面声明的变量。字段表示对象的有关数据。
- **构造函数** − 类实例化时调用，可以为类的对象分配内存。
- **方法** − 方法为对象要执行的操作。

### 创建类的数据成员

以下实例我们声明了类 Car，包含字段为 engine，构造函数在类实例化后初始化字段 engine。

this 关键字表示当前类实例化的对象。注意构造函数的参数名与字段名相同，this.engine 表示类的字段。

此外我们也在类中定义了一个方法 disp()。

```typescript
class Car { 
   // 字段
   engine:string; 
   // 构造函数
   constructor(engine:string) { 
      this.engine = engine 
   }  
   // 方法
   disp():void { 
      console.log("函数中显示发动机型号  :   "+this.engine) 
   } 
} 
// 创建一个对象
var obj = new Car("XXSY1")
// 访问字段
console.log("读取发动机型号 :  "+obj.engine)  
// 访问方法
obj.disp()
```



### 类的继承

TypeScript 支持继承类，即我们可以在创建类的时候继承一个已存在的类，这个已存在的类称为父类，继承它的类称为子类。

类继承使用关键字 **extends**，子类除了不能继承父类的私有成员(方法和属性)和构造函数，其他的都可以继承。

TypeScript 一次只能继承一个类，不支持继承多个类，但 TypeScript 支持多重继承（A 继承 B，B 继承 C）。

```typescript
class Shape { 
   Area:number 
   constructor(a:number) { 
      this.Area = a 
   } 
} 
class Circle extends Shape { 
   disp():void { 
      console.log("圆的面积:  "+this.Area) 
   } 
}
var obj = new Circle(223); 
obj.disp()
```



### 继承类的方法重写

类继承后，子类可以对父类的方法重新定义，这个过程称之为方法的重写。

其中 super 关键字是对父类的直接引用，该关键字可以引用父类的属性和方法。

```typescript
class PrinterClass { 
   doPrint():void {
      console.log("父类的 doPrint() 方法。") 
   } 
} 
 
class StringPrinter extends PrinterClass { 
   doPrint():void { 
      super.doPrint() // 调用父类的函数
      console.log("子类的 doPrint()方法。")
   } 
}
```



### static 关键字

static 关键字用于定义类的数据成员（属性和方法）为静态的，静态成员可以直接通过类名调用。

```typescript
class StaticMem {  
   static num:number; 
   static disp():void { 
      console.log("num 值为 "+ StaticMem.num) 
   } 
} 
StaticMem.num = 12     // 初始化静态变量
StaticMem.disp()       // 调用静态方法
```



### instanceof 运算符

instanceof 运算符用于判断对象是否是指定的类型，如果是返回 true，否则返回 false。

```typescript
class Person{ } 
var obj = new Person() 
var isPerson = obj instanceof Person; 
console.log("obj 对象是 Person 类实例化来的吗？ " + isPerson);
```



### 访问控制修饰符

TypeScript 中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。TypeScript 支持 3 种不同的访问权限。

- **public（默认）** : 公有，可以在任何地方被访问。
- **protected** : 受保护，可以被其自身以及其子类和父类访问。
- **private** : 私有，只能被其定义所在的类访问。

```typescript
class Encapsulate { 
   str1:string = "hello" 
   private str2:string = "world" 
}
var obj = new Encapsulate() 
console.log(obj.str1)     // 可访问 
console.log(obj.str2)   // 编译错误， str2 是私有的
```



### 类和接口

类可以实现接口，使用关键字 implements，并将 interest 字段作为类的属性使用。

以下实例红 AgriLoan 类实现了 ILoan 接口：

```typescript
interface ILoan { 
   interest:number 
} 
class AgriLoan implements ILoan { 
   interest:number 
   rebate:number 
   constructor(interest:number,rebate:number) { 
      this.interest = interest 
      this.rebate = rebate 
   } 
} 
var obj = new AgriLoan(10,1) 
console.log("利润为 : "+obj.interest+"，抽成为 : "+obj.rebate )
```



## 类型模板

假如我们在 JavaScript 定义了一个对象：

```javascript
var sites = { 
   site1:"Runoob", 
   site2:"Google" 
};
```

这时如果我们想在对象中添加方法，可以做以下修改：

```javascript
sites.sayHello = function(){ return "hello";}
```

如果在 TypeScript 中使用以上方式则会出现编译错误，因为Typescript 中的对象必须是特定类型的实例。

```typescript
var sites = {
    site1: "Runoob",
    site2: "Google",
    sayHello: function () { } // 类型模板
};
sites.sayHello = function () {
    console.log("hello " + sites.site1);
};
sites.sayHello();
```

此外对象也可以作为一个参数传递给函数，如下实例：

```typescript
var sites = { 
    site1:"Runoob", 
    site2:"Google",
}; 
var invokesites = function(obj: { site1:string, site2 :string }) { 
    console.log("site1 :"+obj.site1) 
    console.log("site2 :"+obj.site2) 
} 
invokesites(sites)
```



## 命名空间

TypeScript 中命名空间使用 **namespace** 来定义，语法格式如下：

```typescript
namespace SomeNameSpaceName { 
   export interface ISomeInterfaceName {      }  
   export class SomeClassName {      }  
}
```

以上定义了一个命名空间 SomeNameSpaceName，如果我们需要在外部可以调用 SomeNameSpaceName 中的类类和接口，则需要在类和接口添加 **export** 关键字。

要在另外一个命名空间调用语法格式为：

```typescript
SomeNameSpaceName.SomeClassName;
```

如果一个命名空间在一个单独的 TypeScript 文件中，则应使用三斜杠 /// 引用它，语法格式如下：

```typescript
/// <reference path = "SomeFileName.ts" />
```

以下实例演示了命名空间的使用，定义在不同文件中：

**IShape.ts 文件代码：**

```typescript
namespace Drawing { 
    export interface IShape { 
        draw(); 
    }
}
```

**Circle.ts 文件代码：**

```typescript
/// <reference path = "IShape.ts" /> 
namespace Drawing { 
    export class Circle implements IShape { 
        public draw() { 
            console.log("Circle is drawn"); 
        }  
    }
}
```

**Triangle.ts 文件代码：**

```typescript
/// <reference path = "IShape.ts" /> 
namespace Drawing { 
    export class Triangle implements IShape { 
        public draw() { 
            console.log("Triangle is drawn"); 
        } 
    } 
}
```

**TestShape.ts 文件代码：**

```typescript
/// <reference path = "IShape.ts" />   
/// <reference path = "Circle.ts" /> 
/// <reference path = "Triangle.ts" />  
function drawAllShapes(shape:Drawing.IShape) { 
    shape.draw(); 
} 
drawAllShapes(new Drawing.Circle());
drawAllShapes(new Drawing.Triangle());
```

使用 tsc 命令编译以上代码：

```
tsc --out app.js TestShape.ts  
```

## 嵌套命名空间

命名空间支持嵌套，即你可以将命名空间定义在另外一个命名空间里头。

```typescript
namespace namespace_name1 { 
    export namespace namespace_name2 {
        export class class_name {    } 
    } 
}
```

成员的访问使用点号` . `来实现，如下实例：

**Invoice.ts 文件代码：**

```typescript
namespace Runoob { 
   export namespace invoiceApp { 
      export class Invoice { 
         public calculateDiscount(price: number) { 
            return price * .40; 
         } 
      } 
   } 
}
```

**InvoiceTest.ts 文件代码：**

```typescript
/// <reference path = "Invoice.ts" />
var invoice = new Runoob.invoiceApp.Invoice(); 
console.log(invoice.calculateDiscount(500));
```

使用 tsc 命令编译以上代码：

```
tsc --out app.js InvoiceTest.ts
```

得到以下 JavaScript 代码：

```javascript
var Runoob;
(function (Runoob) {
    var invoiceApp;
    (function (invoiceApp) {
        var Invoice = /** @class */ (function () {
            function Invoice() {
            }
            Invoice.prototype.calculateDiscount = function (price) {
                return price * .40;
            };
            return Invoice;
        }());
        invoiceApp.Invoice = Invoice;
    })(invoiceApp = Runoob.invoiceApp || (Runoob.invoiceApp = {}));
})(Runoob || (Runoob = {}));
/// <reference path = "Invoice.ts" />
var invoice = new Runoob.invoiceApp.Invoice();
console.log(invoice.calculateDiscount(500));
```



## 模块

模块是在其自身的作用域里执行，并不是在全局作用域，这意味着定义在模块里面的变量、函数和类等在模块外部是不可见的，除非明确地使用 export 导出它们。类似地，我们必须通过 import 导入其他模块导出的变量、函数、类等。

两个模块之间的关系是通过在文件级别上使用 import 和 export 建立的。

模块使用模块加载器去导入其它的模块。 在运行时，模块加载器的作用是在执行此模块代码前去查找并执行这个模块的所有依赖。 大家最熟知的JavaScript模块加载器是服务于 Node.js 的 CommonJS 和服务于 Web 应用的 Require.js。

此外还有有 SystemJs 和 Webpack。

模块导出使用关键字 **export** 关键字，语法格式如下：

```typescript
// 文件名 : SomeInterface.ts 
export interface SomeInterface { 
   // 代码部分
}
```

要在另外一个文件使用该模块就需要使用 **import** 关键字来导入:

```typescript
import someInterfaceRef = require("./SomeInterface");
```

**实例**

IShape.ts 文件代码：

```typescript
/// <reference path = "IShape.ts" /> 
export interface IShape { 
   draw(); 
}
```

Circle.ts 文件代码：

```typescript
import shape = require("./IShape"); 
export class Circle implements shape.IShape { 
   public draw() { 
      console.log("Cirlce is drawn (external module)"); 
   } 
}
```

Triangle.ts 文件代码：

```typescript
import shape = require("./IShape"); 
export class Triangle implements shape.IShape { 
   public draw() { 
      console.log("Triangle is drawn (external module)"); 
   } 
}
```

TestShape.ts 文件代码：

```typescript
import shape = require("./IShape"); 
import circle = require("./Circle"); 
import triangle = require("./Triangle");  
function drawAllShapes(shapeToDraw: shape.IShape) {
   shapeToDraw.draw(); 
} 
drawAllShapes(new circle.Circle()); 
drawAllShapes(new triangle.Triangle());
```

使用 tsc 命令编译以上代码（AMD）：

```
tsc --module amd TestShape.ts 
```

使用 tsc 命令编译以上代码（Commonjs）：

```
tsc --module commonjs TestShape.ts
```



## 声明文件

TypeScript 作为 JavaScript 的超集，在开发过程中不可避免要引用其他第三方的 JavaScript 的库。虽然通过直接引用可以调用库的类和方法，但是却无法使用TypeScript 诸如类型检查等特性功能。为了解决这个问题，需要将这些库里的函数和方法体去掉后只保留导出类型声明，而产生了一个描述 JavaScript 库和模块信息的声明文件。通过引用这个声明文件，就可以借用 TypeScript 的各种特性来使用库文件了。

使用第三方库，比如 jQuery,我们需要使用 declare 关键字来定义它的类型，帮助 TypeScript 判断我们传入的参数类型对不对：

```typescript
declare var jQuery: (selector: string) => any;
jQuery('#foo');
```

declare 定义的类型只会用于编译时的检查，编译结果中会被删除。

上例的编译结果是：

```
jQuery('#foo');
```

### 声明文件

声明文件以 **.d.ts** 为后缀，例如：

```
runoob.d.ts
```

声明文件或模块的语法格式如下：

```
declare module Module_Name {
}
```

TypeScript 引入声明文件语法格式：

```
/// <reference path = " runoob.d.ts" />
```

当然，很多流行的第三方库的声明文件不需要我们定义了，比如 jQuery 已经有人帮我们定义好了：[jQuery in DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jquery/index.d.ts)。

### 实例

以下定义一个第三方库来演示：

CalcThirdPartyJsLib.js 文件代码：

```js
var Runoob;  
(function(Runoob) {
    var Calc = (function () { 
        function Calc() { 
        } 
    })
    Calc.prototype.doSum = function (limit) {
        var sum = 0; 
 
        for (var i = 0; i <= limit; i++) { 
            sum = sum + i; 
        }
        return sum; 
    }
    Runoob.Calc = Calc; 
    return Calc; 
})(Runoob || (Runoob = {})); 
var test = new Runoob.Calc();
```

如果我们想在 TypeScript 中引用上面的代码，则需要设置声明文件 Calc.d.ts，代码如下：

Calc.d.ts 文件代码：

```typescript
declare module Runoob { 
   export class Calc { 
      doSum(limit:number) : number; 
   }
}
```

声明文件不包含实现，它只是类型声明，把声明文件加入到 TypeScript 中：

CalcTest.ts 文件代码：

```typescript
/// <reference path = "Calc.d.ts" /> 
var obj = new Runoob.Calc(); 
// obj.doSum("Hello"); // 编译错误
console.log(obj.doSum(10));
```

使用 tsc 命令来编译以上代码文件：

```
tsc CalcTest.ts
```

生成的 JavaScript 代码如下：

```js
/// <reference path = "Calc.d.ts" /> 
var obj = new Runoob.Calc();
//obj.doSum("Hello"); // 编译错误
console.log(obj.doSum(10));
```

最后我们编写一个 runoob.html 文件，引入 CalcTest.js 文件及第三方库 CalcThirdPartyJsLib.js：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script src = "CalcThirdPartyJsLib.js"></script> 
<script src = "CalcTest.js"></script> 
</head>
<body>
    <h1>声明文件测试</h1>
    <p>菜鸟测试一下。</p>
</body>
</html>
```

