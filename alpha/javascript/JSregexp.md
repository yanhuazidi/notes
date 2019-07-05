正则表达式  RegExp 对象
    1.正则表达式 Regular Expression
        设置模式，匹配或验证字符串格式

2.创建正则表达式对象
    1. 直接量语法   /pattern/attributes
        var reg = /^\d{6}$/ig;
    2. 创建 RegExp 对象的语法：new RegExp(pattern, attributes);
        var reg = new RegExp("模式","ig 修饰符");
    
    参数
      pattern 是一个字符串，指定了正则表达式的模式或其他正则表达式。
    
      attributes 是一个可选的字符串，包含属性 "g"、"i" 和 "m"，分别用于指定全局匹配、区分大小写的匹配和多行匹配。
                ECMAScript 标准化之前，不支持 m 属性。如果 pattern 是正则表达式，而不是字符串，则必须省略该参数。
    
    返回值
        一个新的 RegExp 对象，具有指定的模式和标志。如果参数 pattern 是正则表达式而不是字符串，那么 RegExp() 
        构造函数将用与指定的 RegExp 相同的模式和标志创建一个新的 RegExp 对象。
        如果不用 new 运算符，而将 RegExp() 作为函数调用，那么它的行为与用 new 运算符调用时一样，只是当 pattern 是正则表达式时，
        它只返回 pattern，而不再创建一个新的 RegExp 对象。
    
    注意: 模式用字符串表示时元字符要多加转义\,避免转义解析。

模式修饰符:
        i : ignore case 忽略大小写
        g : global 全局匹配,不加只匹配第一处
        m :	执行多行匹配。

方括号
        方括号用于查找某个范围内的字符：

        表达式	描述
        [abc]	查找方括号之间的任何字符。
        [^abc]	查找任何不在方括号之间的字符。
        [0-9]	查找任何从 0 至 9 的数字。
        [a-z]	查找任何从小写 a 到小写 z 的字符。
        [A-Z]	查找任何从大写 A 到大写 Z 的字符。
        [A-z]	查找任何从大写 A 到小写 z 的字符。
        [adgk]	查找给定集合内的任何字符。
        [^adgk]	查找给定集合外的任何字符。
        (red|blue|green)	查找任何指定的选项。

元字符
        元字符（Metacharacter）是拥有特殊含义的字符：

        元字符	描述
        .	查找单个字符，除了换行和行结束符。
        \w	查找单词字符。
        \W	查找非单词字符。
        \d	查找数字。
        \D	查找非数字字符。
        \s	查找空白字符。
        \S	查找非空白字符。
        \b	匹配单词边界。
        \B	匹配非单词边界。
        \0	查找 NUL 字符。
        \n	查找换行符。
        \f	查找换页符。
        \r	查找回车符。
        \t	查找制表符。
        \v	查找垂直制表符。
        \xxx	查找以八进制数 xxx 规定的字符。
        \xdd	查找以十六进制数 dd 规定的字符。
        \uxxxx	查找以十六进制数 xxxx 规定的 Unicode 字符。

量词
        量词	描述
        n+	匹配任何包含至少一个 n 的字符串。
        n*	匹配任何包含零个或多个 n 的字符串。
        n?	匹配任何包含零个或一个 n 的字符串。
        n{X}	匹配包含 X 个 n 的序列的字符串。
        n{X,Y}	匹配包含 X 至 Y 个 n 的序列的字符串。
        n{X,}	匹配包含至少 X 个 n 的序列的字符串。
        n$	匹配任何结尾为 n 的字符串。
        ^n	匹配任何开头为 n 的字符串。
        ?=n	匹配任何其后紧接指定字符串 n 的字符串。
        ?!n	匹配任何其后没有紧接指定字符串 n 的字符串。

RegExp 对象属性
        属性	    描述
        global	    RegExp 对象是否具有标志 g。
        ignoreCase	RegExp 对象是否具有标志 i。
        lastIndex	一个整数，标示开始下一次匹配的字符位置。
                指定下一次匹配的起始索引，只有在设置了全局匹配才起作用
                这是创建全局匹配正则的属性
                原则上，同一个正则表达式不要重复使用,lastIndex每次起始索引不同，影响验证结果
                当reg.lastIndex设置为0时，每次都从0位开始索引
        multiline	RegExp 对象是否具有标志 m。
        source	    正则表达式的源文本。

RegExp 对象方法
        方法	    描述
        compile	编译正则表达式。
            compile() 方法用于在脚本执行过程中编译正则表达式。
            compile() 方法也可用于改变和重新编译正则表达式。

            语法
                RegExpObject.compile(regexp,modifier)
                参数	    描述
                regexp	    正则表达式。
                modifier	规定匹配的类型。"g" 用于全局匹配，"i" 用于区分大小写，"gi" 用于全局区分大小写的匹配。
    
            eg: 
                var str="Every man in the world! Every woman on earth!";
    
                patt=/man/g;
                str2=str.replace(patt,"person");
                document.write(str2+"<br />");
    
                patt=/(wo)?man/g;
                patt.compile(patt);
                str2=str.replace(patt,"person");
                document.write(str2);
    
        exec	检索字符串中指定的值。返回找到的值，并确定其位置。
            reg.exec() 方法是一个正则表达式方法。
                用于检索字符串中的正则表达式的匹配。
                该函数返回一个数组，其中存放匹配的结果。
                如果未找到匹配，则返回值为 null。
                /e/.exec("The best things in life are free!");
    
        test	检索字符串中指定的值。返回 true 或 false。
            reg.text(param)
                参数: 要验证的字符串
                返回值: ture/false 表示字符串中是否包含满足正则模式的内容
                /e/.test("The best things in life are free!");

支持正则表达式的 String 对象的方法
        方法	描述
        search	检索与正则表达式相匹配的值。
        match	找到一个或多个正则表达式的匹配。
        replace	替换与正则表达式匹配的子串。
        split	把字符串分割为字符串数组。