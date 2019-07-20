## 包装对象

​    目的 ：让原始数据类型也和引用数据类型一样，有属性和方法

JS提供三种包装类型
    String  Number  Boolean

```

字符串  String
    创建语法：
        1. 字面量 var str1 ="";
        2. 内置构造方法 var str2 = new String("");
转义字符    \
    \n  换行
    \t  制表符
    \r  返回行首
转为普通字符
    \'  'It\'s a apple'
    \"  "It\"s a apple"
    \\ 
    \%

属性和方法
    1.属性
        str.length : 获取字符串长度(字符个数)

    2.遍历字符串
        由于字符串也是类数组结构，每个字符都会分配下标，
        可以按照数组访问元素的方式访问字符
    
    3.常用方法
        1.转换大小写
            str.toUpperCase()  转换大写，返回新字符串
            str.toLowerCase()  转换小写，返回新字符串

        2.获取指定字符
            str.charAt(index)   获取指定下标位置的字符 , 返回字符

            str.fromCharCode(num) 获取任意Unicode码对应的字符
                    返回Unicode字符

            str.charCodeAt(index)  获取指定位置的Unicode码值
                    参数省略表示获取第一个字符，返回整型

        3.检索字符串
            获取指定字符的下标
            1. str.indexOf(value[,startIndex])  
                参数为字符,可选参数为起始位置下标,向后找
                成功返回字符第一次出现的位置下标(整型)
                失败返回 -1 表示不存在
            
            2. str.lastIndexOf(value[,startIndex])
                参数为字符,可选参数为起始位置下标,向前找
                返回值 : 返回指定字符最后出现位置的下标(整型)
                失败返回 -1 表示不存在
        
        4.截取字符串
            1. str.slice(startIndex[,endIndex]);
                根据起始下标截取子串,省略结束下标，表示截取到末尾
                参数: 字符下标,负数为倒序截取
                返回值: 左闭右开子字符串[startIndex,endIndex)
            2. str.substring(startIndex[,endIndex]);
                根据起始下标截取子串,省略结束下标，表示截取到末尾
                参数: 字符下标,为负数转换为 0
                返回值: 左闭右开子字符串[startIndex,endIndex)
            3. str.substr(startIndex[,count]);
                根据起始下标开始截取指定长度的子字符串
                参数: startIndex:字符下标,可以为负数
                      count : 截取的个数，省略，表示截取到末尾
                返回值: 以startIndex字符为起始的count个长度字符串

        5.分割字符串    
            split() 方法用于把一个字符串分割成字符串数组。

            语法
                stringObject.split(separator[,howmany])
                参数
                    separator	必需。字符串或正则表达式，从该参数指定的地方分割 stringObject。
                    howmany	    可选。该参数可指定返回的数组的最大长度。如果设置了该参数，超过长度个数的子串会丢弃。
                                如果没有设置该参数，整个字符串都会被分割返回，不考虑它的长度。
                返回值
                    一个字符串数组。该数组是通过在 separator 指定的边界处将字符串 stringObject 分割成子串创建的。
                    返回的数组中的字串不包括 separator 自身。
                    如果 separator 是包含子表达式的正则表达式，那么返回的数组中包括与这些子表达式匹配的字串（但不包括与整个正则表达式匹配的文本）。

                提示和注释
                    注释：如果把空字符串 ("") 用作 separator，那么 stringObject 中的每个字符之间都会被分割。
                    注释：String.split() 执行的操作与 Array.join 执行的操作是相反的。
        
        6.模式匹配  
            1.结合正则表达式实现查找和替换指定字符
            2.正则表达式
                var reg1 = /\d{3,5}/;
                var reg2 = /h/;
              模式修饰符:
                i : ignore case 忽略大小写
                g : global 全局匹配,不加只匹配第一处
            eg:
                var reg = /你好/ig;

            3.方法:
                1.  str.match(substr|regExp)    查找子字符串
                        根据指定的字符串或正则模式，查找字符串内容,字符串或者正则模式不加g只匹配第一处
                        返回匹配结果数组
                        var arr = str.match(/a/g);

                1.  str.replace(substr|regExp,newString)    替换字符串
                        根据指定的字符串或正则模式匹配子字符串，并用新字符串替换,字符串或者正则模式不加g只匹配第一处
                        返回替换后的字符串

                3.  str.search(substr|regExp)   查找下标
                        检索字符串中指定的子字符串或正则模式,只匹配第一处,正则模式加g不起作用
                        返回匹配的子字符串起始位置下标,没有返回 -1
                        var n = str.search(/Runoob/i);
```

​     

## Boolean 对象


```

        Boolean 对象表示两个值："true" 或 "false"。
创建 Boolean 对象的语法：
    new Boolean(value);	//构造函数
    Boolean(value);		//转换函数
    隐示转换 : !value
参数
    参数 value 由布尔对象存放的值或者要转换成布尔值的值。

返回值
    当作为一个构造函数（带有运算符 new）调用时，Boolean() 将把它的参数转换成一个布尔值，并且返回一个包含该值的 Boolean 对象。
    如果作为一个函数（不带有运算符 new）调用时，Boolean() 只将把它的参数转换成一个原始的布尔值，并且返回这个值。
    注释：如果省略 value 参数，或者设置为 0、-0、null、""、false、undefined 或 NaN，
            则该对象设置为 false。否则设置为 true（即使 value 参数是字符串 "false"或" ",[],{}S）。

方法 :
    bool.toString()
```





## Number 对象


```

    Number 对象是原始数值的包装对象。
创建 Number 对象的语法：
    var myNum=new Number(value);
    var myNum=Number(value);
参数
    参数 value 是要创建的 Number 对象的数值，或是要转换成数字的值。

返回值
    当 Number() 和运算符 new 一起作为构造函数使用时，它返回一个新创建的 Number 对象。
    如果不用 new 运算符，把 Number() 作为一个函数来调用，它将把自己的参数转换成一个原始的数值，
    并且返回这个值（如果转换失败，则返回 NaN）。

Number 对象属性
属性	        描述
constructor	返回对创建此对象的 Number 函数的引用。
MAX_VALUE	可表示的最大的数。
MIN_VALUE	可表示的最小的数。
NaN	非数字值。
NEGATIVE_INFINITY	负无穷大，溢出时返回该值。
POSITIVE_INFINITY	正无穷大，溢出时返回该值。
prototype	使您有能力向对象添加属性和方法。

Number 对象方法
        方法	        描述
    toString	    把数字转换为字符串，使用指定的基数。
        隐式转换字符串 :   num+''或 ''+num
    toLocaleString	把数字转换为字符串，使用本地数字格式顺序。
    toFixed	        把数字转换为字符串，结果的小数点后有指定位数的数字。
    toExponential	把对象的值转换为指数计数法。
    toPrecision	    把数字格式化为指定的长度。
    valueOf	        返回一个 Number 对象的基本数字值。
Number 对象描述
    在 JavaScript 中，数字是一种基本的数据类型。JavaScript 还支持 Number 对象，该对象是原始数值的包装对象。
    在必要时，JavaScript 会自动地在原始数据和对象之间转换。在 JavaScript 1.1 中，可以用构造函数 Number() 
    明确地创建一个 Number 对象，尽管这样做并没有什么必要。

构造函数 Number() 可以不与运算符 new 一起使用，而直接作为转化函数来使用。以这种方式调用 Number() 时，
    它会把自己的参数转化成一个数字，然后返回转换后的原始数值（或 NaN）。

构造函数通常还用作 5 个有用的数字常量的占位符，这 5 个有用的数字常量分别是可表示的最大数、可表示的最小数、
正无穷大、负无穷大和特殊的 NaN 值。 注意，这些值是构造函数 Number() 自身的属性，而不是单独的某个 Number 对象的属性。

比如这样使用属性 MAX_VALUE 是正确的：
    var big = Number.MAX_VALUE

但是这样是错误的：
    var n= new Number(2);
    var big = n.MAX_VALUE

作为比较，我们看一下 toString() 和 Number 对象的其他方法，它们是每个 Number 对象的方法，
而不是 Number() 构造函数的方法。前面提到过，在必要时，JavaScript 会自动地把原始数值转化
成 Number 对象，调用 Number 方法的既可以是 Number 对象，也可以是原始数字值。

var n = 123;
var binary_value = n.toString(2);
```

