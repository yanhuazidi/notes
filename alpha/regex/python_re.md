

[TOC]







## 正则表达式  regex

**定义：**

即文本的高级匹配模式，提供搜索，替换等功能。其本质是一系列由字符和特殊符号组成的字符串，这个字符串即正则表达式

**匹配原理：**

由普通字符和特殊符号构成，通过描述字符的重复，位置，种类等行为达到匹配某一类字符串的目的



## 元字符

| 字符         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| 普通字符     | 字母a-zA-Z，数字0-9，_ , 汉字,每个字符匹配到对应字符(组合一起是整体匹配)，能汉字匹配，空格算字符 |
| \            | 将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。 |
| ^            | 匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。 |
| $            | 匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。 |
| *            | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
| +            | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
| ?            | 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。 |
| {n}          | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
| {n,}         | n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。 |
| {n,m}        | m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。 |
| ?            | 当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。 |
| .            | 匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"**(.\|\n)**"的模式。 |
| (pattern)    | 匹配 pattern 并获取这一匹配。所获取的匹配可以从产生的 Matches 集合得到，在VBScript 中使用 SubMatches 集合，在JScript 中则使用 $0…$9 属性。要匹配圆括号字符，请使用 '\(' 或 '\)'。 |
| (?:pattern)  | 匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (\|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y\|ies) 就是一个比 'industry\|industries' 更简略的表达式。 |
| (?=pattern)  | 正向肯定预查（look ahead positive assert），在任何匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，"Windows(?=95\|98\|NT\|2000)"能匹配"Windows2000"中的"Windows"，但不能匹配"Windows3.1"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。 |
| (?!pattern)  | 正向否定预查(negative assert)，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如"Windows(?!95\|98\|NT\|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。 |
| (?<=pattern) | 反向(look behind)肯定预查，与正向肯定预查类似，只是方向相反。例如，"`(?<=95|98|NT|2000)Windows`"能匹配"`2000Windows`"中的"`Windows`"，但不能匹配"`3.1Windows`"中的"`Windows`"。 |
| (?<!pattern) | 反向否定预查，与正向否定预查类似，只是方向相反。例如"`(?<!95|98|NT|2000)Windows`"能匹配"`3.1Windows`"中的"`Windows`"，但不能匹配"`2000Windows`"中的"`Windows`"。 |
| x\|y         | 匹配 x 或 y。例如，'z\|food' 能匹配 "z" 或 "food"。'(z\|f)ood' 则匹配 "zood" 或 "food"。 |
| [xyz]        | 字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。 |
| [^xyz]       | 负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。 |
| [a-z]        | 字符范围。匹配指定范围内的任意字符。例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。 |
| [^a-z]       | 负值字符范围。匹配任何不在指定范围内的任意字符。例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符。 |
| \b           | 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。 |
| \B           | 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。 |
| \cx          | 匹配由 x 指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。 |
| \d           | 匹配一个数字字符。等价于 [0-9]。                             |
| \D           | 匹配一个非数字字符。等价于 [^0-9]。                          |
| \f           | 匹配一个换页符。等价于 \x0c 和 \cL。                         |
| \n           | 匹配一个换行符。等价于 \x0a 和 \cJ。                         |
| \r           | 匹配一个回车符。等价于 \x0d 和 \cM。                         |
| \s           | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。 |
| \S           | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。                  |
| \t           | 匹配一个制表符。等价于 \x09 和 \cI。                         |
| \v           | 匹配一个垂直制表符。等价于 \x0b 和 \cK。                     |
| \w           | 匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。               |
| \W           | 匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。           |
| \xn          | 匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长。例如，'\x41' 匹配 "A"。'\x041' 则等价于 '\x04' & "1"。正则表达式中可以使用 ASCII 编码。 |
| \num         | 匹配 num，其中 num 是一个正整数。对所获取的匹配的引用。例如，'(.)\1' 匹配两个连续的相同字符。 |
| \n           | 标识一个八进制转义值或一个向后引用。如果 \n 之前至少 n 个获取的子表达式，则 n 为向后引用。否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值。 |
| \nm          | 标识一个八进制转义值或一个向后引用。如果 \nm 之前至少有 nm 个获得子表达式，则 nm 为向后引用。如果 \nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的向后引用。如果前面的条件都不满足，若 n 和 m 均为八进制数字 (0-7)，则 \nm 将匹配八进制转义值 nm。 |
| \nml         | 如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八进制转义值 nml。 |
| \un          | 匹配 n，其中 n 是一个用四个十六进制数字表示的 Unicode 字符。例如， \u00A9 匹配版权符号 (?)。 |







## re模块
​    re.findall(pattern,string)
​    功能 ：提取所有的正则匹配内容
​    参数 ：pattern  正则表达式
​          string    目标字符串
​    返回值：列表，所有提取到的内容



正则表达式转义
    在正则表达式中  如果需要匹配特殊符号，需要加 \ 作为转义
    e.g  匹配 .   需要使用 \.

    python          正则            目标字符串
    
    '\\$\\d+'      \$\d+               $10
    
    *raw 字符串，是不对字符串内容进行转义处理
        '\\$\\d+'   --->    r'\$\d+'

匹配 . * ？ ^ $ 等元字符需要用转义或 []括起来
    需要使用\.来匹配一个小数点
    当然如果是在[.]里面的话 是不需要加\的

    空字符可以用\s表示 如 :  ([.]|[*]|\s|[?])


贪婪 和 非贪婪

    贪婪模式 ： 正则表达式的重复匹配默认总是尽可能的向后匹配更多内容
        *   +   ?    {m,n}
    
    非贪婪模式(懒惰模式)： 尽可能少的匹配，取最少值。  贪婪后面加问号
        *?   +?    ??    {m,n}?
    
        In [106]: re.findall(r"ab+?","abbbbbbbb")
        Out[106]: ['ab']
    
        In [107]: re.findall(r"ab??","abbbbbbbb")
        Out[107]: ['a']

正则表达式分组
    使用()可以为正则表达式建立内部分组，子组为正则表达式的一部分，
    可以看作一个内部整体

    * 有子组的正则表达式任然是整体去匹配内容，子组需在整体能够匹配到内容的前提下发挥作用
    
    子组的作用：
        1.作为内部整体可以改变某些元字符的行为
    
            re.search(r"(ab)+\d+","ababab1234").group()
            'ababab1234'
    
            re.search(r"\w+@\w+\.(com|cn)","abc@123.com").group()
            'abc@123.com'
    
        2. 子组在某些操作中可以单独提取出匹配内容
    
            re.search(r"(https|http|ftp)://\S+","https://www.baidu.com").group(1)
            Out[121]: 'https'
    
    子组使用注意事项
        * 一个正则表达式中可以有多个子组
        * 子组一般由外到内，由左到右称之为第一，第二 ，第三....子组
                ((ad)aa)ddd(sdf)ddf
        * 子组不能重叠，嵌套也不宜很多  
                a(df(as)df)afffff

捕获组 和 非捕获组
    格式 ： (?P<name>pattern)    大写的P
    e.g.
        re.search(r"(?P<dog>ab)cdef",'abcdefghti').group('dog')
        Out[130]: 'ab'

        作用 ： 名字可以表达一定含义，可以通过组名更方便获取某组内容

正则表达式设计原则
    1. 正确性 ，能正确匹配到目标内容
    2. 排他性 ，除了要匹配的内容，尽可能不会匹配与到其他内容
    3. 全面性 ，需要对目标字串的各种情况考虑全面，做到不遗漏

re模块

    regex = re.compile(pattern,flags = 0)
    功能 ： 生成正则表达式对象
    参数 ： pattern  正则表达式
            flags   功能标志位，丰富正则表达式的匹配功能
    返回值 : 返回正则表达式对象
    
    re.findall(pattern,string,flags=0)
    功能 ：从目标字符串查找正则匹配内容
    参数 ： pattern  正则表达式
            string  目标字符串
            flags   标志位
    返回值 ： 返回匹配到的内容列表
        如果正则有子组则只返回子组对应内容，多个子组以[(1),(2)..]返回
    
    regex.findall(string,pos=None,endpos=None)
    功能 ：从目标字符串查找正则匹配内容
    参数 ： string  目标字符串
            pos     匹配目标的起始位置
            endpos  匹配目标的终止位置
    返回值 ： 返回匹配到的内容列表
        如果正则有子组则只返回子组对应内容，多个子组以[(1),(2)..]返回
    
    re.split(pattern,string,flags = 0)
    功能：根据正则匹配内容切割字符串
    参数： pattern  string  flags
    返回值： 返回列表，列表中为切割掉正则之后的内容
    
    re.sub(pattern,replaceStr,string,count=0,flags=0)
    功能： 替换正则匹配到的内容
    参数：  pattern
            replaceStr ： 用作替换的内容
            string 
            count        最多替换几处 默认全部替换
            flags
    返回值 ： 返回替换后的字符串
    
    re.subn(pattern,replaceStr,string,count=0,flags=0)
    功能： 替换正则匹配到的内容
    参数： pattern
        replaceStr ： 用作替换的内容
        string 
        count   最多替换几处 默认全部替换
        flags
    返回值 ： 返回一个元组，为实际(替换后的字符串,替换了几处)


    re.finditer(pattern,string,flags=0)
    功能： 使用正则表达式匹配目标字符串
    参数： pattern  string flags
    返回值： 返回一个可迭代对象，
            迭代到的内容是一个match对象，位置span=(:)
            可用group()方法取值
    
    re.fullmatch(pattern,string,flags=0)
    功能： 完全匹配目标字符串，相当于在pattern加了 ^和$
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None
    
    re.match(pattern,string,flags=0)
    功能： 匹配目标字符串开头位置,相当于在pattern加了 ^
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None


    re.search(pattern,string,flags)
    功能： 正则表达式匹配目标字符串，只匹配第一处
    参数： pattern,string,flags
    返回值：返回匹配到的match对象
            如果没匹配成功返回None
    
    compile生成对象regex的属性：
    
        pattern    ： 属性值为正则表达式
        flags      ： 表示标志位常量值
        groups     ： 正则表达式有多少子组，没有为 0
        groupindex ： 捕获组形成组名和序列号的字典，
                      组名为键，第几组为值
                      要是捕获组才有效，不然返回{}


match object 方法和属性

属性变量
    pos         匹配目标字符串的开始位置
    endpos      匹配目标字符串的结束位置
    re          正则表达式
    string      目标字符串
    lastgroup   最后一组的组名
    lastindex   最后一组是第几组

属性方法
    span()      匹配到的内容在字符串中的起止位置
    start()     匹配到的内容在字符串中的开始位置
    end()       匹配到的内容在字符串中的结束位置

    group()
        功能: 获取match对象获取到的内容
        参数: 默认为 0 表示获取整个正则匹配到的内容
             如果为序列号或者子组名，则表示获取某个子组对应的内容
        返回值: 返回获取到的内容
    
    groupdict()     获取捕获组字典，组名作为键，对应内容作为值
    groups()        获取多个子组值的集合，返回元组

flags  参数的使用
    作用 : 辅助正则表达式，丰富匹配效果
        同时使用多个标志位   flags = re.I|re.M
          

    I == IGNORECASE  匹配时忽略字母大小写
    S == DOTALL      作用于元字符 .    使 . 可以匹配换行
    M == MULTILLINE  作用于 ^  $  使其匹配每一行的开头和结尾
    X == VERBOSE     可以给正则表达式添加注释