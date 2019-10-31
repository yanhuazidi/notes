日期对象 Date
    1.提供获取客户端时间与日期的方法
    2.创建日期对象,nodejs下会转换为0时区时间
        1. var date1 = new Date();  获取当前系统时间

  2. 根据指定的日期时间创建对象
        var date1 = new Date("2018-11-11 10:10:10");
        var date2 = new Date("2018/11/11 10:10:10");
        var date3 = new Date(2018,10,11,10,10,10);//月份0~11,写12年加一
        var date4 = new Date(1000); //表示1000毫秒 1970-01-01 00:00:01
        

3.方法
    1.设置或获取当前时间对象的毫秒数
        date.getTime();  获取当前日期对象距离1970-01-01 00:00:00 之间的毫秒数

        var n =new Date();
        console.log(n.getTime());
    2.date.setTime(millisec); //millisec毫秒
        把date设置为距离时间元年1970-01-01 00:00:00 millisec毫秒的日期时间
        返回值 ：参数 millisec
        eg:
            var n =new Date();
            n.setTime(100000000)
            console.log(n); //Fri Jan 02 1970 11:46:40 GMT+0800 (中国标准时间)
    
    3.获取时间分量
        date.getFullYear()
        获取当前日期对象中的年份信息
        返回四位年份数字
    
        date.getMonth()
        获取日期对象中的月份信息
        返回值0-11 对应12个月，需要+1显示
    
        date.getDate()
        获取日期对象中的日子信息
        返回值 : 正常的号数
    
        date.getDay()
        获取日期对象中的星期信息
        返回值 0-6 对应 日-六
    
        date.getHours()
        获取小时数
    
        date.getMinutes()
        获取分钟数
    
        date.getSeconds()
        获取秒数
    
        date.getMilliseconds()
        获取毫秒
    
    设置时间
        date.setFullYear(Year)
    
        parse()	返回1970年1月1日午夜到指定日期（字符串）的毫秒数。
        setDate()	设置 Date 对象中月的某一天 (1 ~ 31)。
        setMonth()	设置 Date 对象中月份 (0 ~ 11)。
        setFullYear()	设置 Date 对象中的年份（四位数字）。
        setHours()	设置 Date 对象中的小时 (0 ~ 23)。
        setMinutes()	设置 Date 对象中的分钟 (0 ~ 59)。
        setSeconds()	设置 Date 对象中的秒钟 (0 ~ 59)。
        setMilliseconds()	设置 Date 对象中的毫秒 (0 ~ 999)。
日期转字符串格式
    date.toString()  原样转换为字符串
    date.toLocaleString() 按本地日期时间格式转换为字符串
    date.toLocaleDateString()  按本地日期格式转换为字符串
    date.toLocaleTimeString()  按本地时间格式转换为字符串