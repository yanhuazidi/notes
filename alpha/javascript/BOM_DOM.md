

BOM
    浏览器对象模型。提供浏览器相关的属性和方法




浏览器函数   

1. alert('警示框');
2. var input = prompt('输入框');
   typeof(input) // String

    window 对象跟随浏览器运行自动产生，每个窗口都对应有自己的window对象
    window 对象可以省略，直接使用相关属性和方法
    
    window对象
        跟随网页运行自动创建，表示当前窗口对象
        所有的全局变量和函数，都是window的对象的属性和方法
        对话框都是window对象的方法
    
        1.弹框
            警告框
            window.alert("文本")  
            输入框
            window.prompt("提示文本",defulet) defulet 默认值，返回输入字符串
            确认框
            window.confirm("提示文本") 返回true/false ,只有点击确认按钮返回true
    
    定时器方法
        1.周期性定时器(间歇调用)
            每隔一段时间，执行一次代码
    
            语法:
                setInterval(function,time);  开启周期性定时器
                参数: 
                    function :要执行的代码，函数封装
                    time : 表示时间间隔，以毫秒为单位  1s = 1000ms
                返回值 : 定时器的ID(整数值)
            
            关闭周期定时器 :
                clearInterval(timerID);
                停止定时器，参数为定时器ID
        
        2.一次性定时器(超时调用)
            等待一段时间之后执行一次代码
            语法:
                setTimeout(function,delay); 开启一次性定时器
                参数:
                    function : 需要执行的代码
                    delay  :  延迟执行的时长，默认毫秒为单位
                    返回值 : 定时器的ID
    
            关闭超时调用
                clearTimeout(timerID);
            
    window 属性
        window对象中大部分属性右都是对象类型，包含自身的属性和方法
        
        window.document;
        window.document.write();
    
        1.screen 对象
            包含与屏幕相关的信息
            属性：
                1.width/height ： 屏幕的宽高
                2.availWidth/availHeight  ： 屏幕实际可用的高宽
        
        2.history 对象
            保存当前窗口访问过的 URL 
            1. 属性
                length ：当前窗口访问过的URL数量，至少为1
    
            2.方法
            
                back()  : 退回上一条url (浏览器后退按钮)
                forward() : 访问下一条url (前进按钮)
                go(num)  :  跳转至指定的url，通过参数控制
                        参数为整数，正值为前进，负值为后退
                
        3.location 对象
            保存地址栏信息(URL)
    
            location.hostname 返回 web 主机的域名
            location.pathname 返回当前页面的路径和文件名
            location.port 返回 web 主机的端口 （80 或 443）
            location.protocol 返回所使用的 web 协议（http:// 或 https://）
            location.assign("http://www.w3cschool.cc") 加载新的文档
    
            1. 属性
                href : 返回当前窗口的URL
                如果给href赋值，相当于跳转页面
    
            2.方法
                reloat([param]) : 重新载入页面(刷新)
                参数 : 选填 ，true/false
                    true : 忽略缓存，从服务器端重新加载
                    false : 默认值，从缓存中加载
    
        4.navigator 对象
            window.navigator 对象包含有关访问者浏览器的信息
                            (版本，内核，代理...)
    
    window.open() - 打开新窗口
    window.close() - 关闭当前窗口
    window.moveTo() - 移动当前窗口
    window.resizeTo() - 调整当前窗口的尺寸

DOM 
    介绍:
        文档对象模型，提供操作文档对象的属性和方法
        DOM 的核心对象 document(文档对象)
        document 是window的属性
        顶层对象是document对象，其属性和方法有W3C国际组织进行规范和推广

    节点和节点树
        网页在加载过程中，会自动生成节点树(DOM树)，节点对象
        封装网页中所有的内容(标签，文本，标签属性，注释...)
    
        节点树中保存所有的节点对象，表示各节点之间的层级关系
    
    节点分类
        1.元素节点 
            文档中的标签
        2.文本节点
            标签中的文本内容
        3.属性节点
            标签属性
        4.注释节点
            注释
        5.文档节点
            document
        
    节点操作
        1.获取节点对象
        2.修改节点
        3.删除节点
        4.增加节点

获取节点
    涉及到获取元素节点，必须考虑代码的解析顺序，必须等到文档元素
    加载完毕之后，才能获取到节点对象
    获取操作必须写在body末尾

    1.根据标签名获取节点对象，返回节点列表(类数组)
        方法:
            document.getElementsByTagName('标签名');
            返回值: 节点列表，可以通过下标访问具体节点对象
    
    2.根据元素的ID属性值获取元素
        方法:
            document.getElementById("ID属性值");
            返回值: 
                返回具体的节点对象
                多个ID相同时只返回第一个寻找到的。


​    
    3.根据元素的class属性值获取元素节点的数组
        方法:
            document.getElementsByClassName("class属性值");
            返回值:
                元素节点数组
    
    4.根据表单控件的name属性值获取元素节点数组
        方法:
            document.getElementsByName("name属性值");
            返回值:
                元素节点数组

操作元素节点的属性
    1.获取指定属性的值
        getAttribute('attrName');
        根据传入的属性名获取对应的属性值
    
    2.为元素节点设置属性
        setAttribute('attrName','value');
    
    3.移除指定属性
        removeAttribute('attrName');
    
    4.标签属性就是元素节点对象的属性
        可以使用成员访问符 . 访问
        获取:
            elem.id   获取id 属性值
            elem.className  获取class属性值
        
        设置:
            elem.id = 'd1';
            elem.className = 'c1'; 可以赋多个类名 'c1 c2 c3';
        
        移除:
            elem.id = null;

操作元素样式
    1.基于id/class选择器，为元素添加样式
        通过操作元素in/class属性，对应选择器样式
        setAttribute();
        elem.id = '';
        elem.className = '';

    2.通过style标签属性，操作元素样式
      语法:
        elem.style.CSS属性名 = '';
      注意:
        CSS属性名中出现的连接符 - ，在JS中一律改为驼峰标识
    
        eg:
            font-size -->  fontSize

操作元素内容
    1.属性 : innerHTML  能添加HTML标签
        设置或读取标签内容，可以识别HTML标签

        h1s[1].innerHTML = "<a href='#'>超链接</a>";  


    2.属性 : innerText   不能添加标签,只能纯文本
        设置或读取标签内容，不能识别HTML标签
    
        h1.innerText="hahaha,快下课了";
    
    3.属性 : value
        获取表单控件的值
    
        input.value;

节点的分类与名称
    1. 属性 nodeType  
        查看节点类型

        返回数值
        元素节点 : 1
        属性节点 : 2
        文本节点 : 3
        -----------------------------------
        注释节点 : 8
        文档节点 : 9
    
    2. 属性 nodeName  
        查看节点名称    
        
        返回值:    
        元素节点 : 标签名
        属性节点 : 属性名
        文本节点 : #text
        注释节点 : #comment
        文档节点 : #document
    
    3.属性 nodeValve
        查看节点的值
    
        元素节点 :  null
        属性节点 :  属性值
        文本节点 :  文本内容

节点的层次属性
    基于层次关系获取节点(父子关系，兄弟关系)
    1. parentNode 属性
        获取当前节点的父节点，只有唯一的父节点

    2. childNode 属性
        获取当前元素所有的子节点，包含换行,以数组形式返回
        <h1 id='aa'>标签</h1>
        标签属性与文本内容会以子节点的形式返回，对应属性节点和文本节点
    
    3. children 属性
        获取当前元素子节点数组，不包含文本节点，只返回元素节点
        返回的子元素中只包含直接子元素，不包含间接子元素
    
    4. nextSibling 属性
        获取下一个兄弟节点
    
    4.1. nextElementSibling 属性
        获取下一个元素兄弟节点，略过其它节点
    
    5. previousSibling 属性
        获取前一个兄弟节点
    
    5.1 previousElementSibling
        获取前一个元素兄弟节点
    
    6.  attributes 属性
        获取元素所有的属性节点


节点操作(创建，增加，删除)
    动态修改网页内容
        1.创建节点

          创建元素节点:
                document.createElement("标签名")
                返回创建好的元素节点对象
          创建文本节点
                document.createTextNode("文本内容")
                返回创建好的文本节点对象
          
          属性节点可以通过成员访问符直接访问和设置
             div.id = "d1";
    
        2.添加节点
            1.创建好的节点对象只有添加在网页中才能显示
            2.涉及节点的添加，删除，都是父节点的操作
            3.语法:
                1. 追加在父元素的末尾
                    parentNode.appendChild(node);
                    parentNode :父节点对象(body可以直接 document.body调用，不用获取)
                    node : 创建好的节点
    
                注意: 文本节点是元素节点的子节点，为元素添加文本内容，也可以通过
                    appendChild() 方法添加文本节点
                
                2.在父元素中指定位置添加子节点
                    parentNode.insertBefore(newnode,oldnode);
                    表示在oldnode之前插入新节点
                
        3.移除节点
            语法:
                parentNode.removeChild(node);
                将指定的节点对象从父元素中移除

事件
    指用户行为激发的操作

    事件处理函数:
        系统定义好的，针对用户不同的行为提供的函数
        事件函数由用户行为触发，浏览器自动调用
        我们只需要实现函数，定义事件发生后需要执行的操作
    
                属性	当以下情况发生时，出现此事件	FF	N	IE
                onabort	图像加载被中断	1	3	4
                onblur	元素失去焦点	1	2	3
                onchange	用户改变域的内容	1	2	3
                onclick	鼠标点击某个对象	1	2	3
                ondblclick	鼠标双击某个对象	1	4	4
                onerror	当加载文档或图像时发生某个错误	1	3	4
                onfocus	元素获得焦点	1	2	3
                onkeydown	某个键盘的键被按下	1	4	3
                onkeypress	某个键盘的键被按下或按住	1	4	3
                onkeyup	某个键盘的键被松开	1	4	3
                onload	某个页面或图像被完成加载	1	2	3
                onmousedown	某个鼠标按键被按下	1	4	4
                onmousemove	鼠标被移动	1	6	3
                onmouseout	鼠标从某元素移开	1	4	4
                onmouseover	鼠标被移到某元素之上	1	2	3
                onmouseup	某个鼠标按键被松开	1	4	4
                onreset	重置按钮被点击	1	3	4
                onresize	窗口或框架被调整尺寸	1	4	4
                onselect	文本被选定	1	2	3
                onsubmit	提交按钮被点击	1	2	3
                onunload	用户退出页面
    分类
        1. 鼠标事件函数
            onclick     鼠标单击
            ondblclick  鼠标双击
            onmouseover 鼠标移入元素时触发
            onmousemove 鼠标在元素中移动时不断触发
            onmouseout  鼠标移出元素时触发
        
        2.文档或元素加载完毕后触发
            onload
        
        3.表单控件状态改变事件
            onfocus     元素获取焦点时触发
            onblur      元素失去焦点时触发
            onchange    元素内容发生改变，并且失去焦点之后触发
            oninput     元素正在输入，value值发生变化时触发
            onsubmit    点击提交按钮时触发 form.onsubmit
                    //当用户点击了提交按钮时自动触发form的onsubmit事件
                    //onsubmit 事件用于验证表单中的数据是否可以提交
                    //允许返回布尔值，true是可提交，false不可提交
    
        4.键盘事件
            onkeydown   键盘按键被按下
            onkeypress  按键按压
            onkeyup     按键抬起
    
    事件绑定
        指 事件交由哪个元素触发
        1.元素内联绑定
            事件函数以标签属性的方式，绑定给函数
            eg: <button onclick=''></button>
            <h1 onclick="this.innerHTML='Ooops!'">点击文本!</h1>
        2.js 中动态绑定事件
            语法:
                事件函数都是元素节点对象的方法
                eg : node.onclick = function(){};
        
        3.W3C 标准的事件监听函数
            node.addEventListener("click",function[,false]);
            参数:
                1.省略 “ on ” 前缀的事件函数名
                2.事件触发后要执行的操作(封装为函数),函数名
                3.可选参数，设置事件传递机制，默认为 false
        
        4. this 关键字
            指代函数或者方法的调用者，当前元素对象
            全局函数是window对象的方法，全局函数中的this表示window对象

事件对象
    事件对象是伴随事件触发自动产生
    包含着与当前事件相关的信息(鼠标位置,按的什么键...)

    获取事件对象
        浏览器会将我们的事件对象以参数的形式传递给事件处理函数
    
        eg:
            div.onclick = function(evt){
                console.log(evt);
            };
    
    事件对象常用属性
        不同的事件类型，事件对象的信息(属性) 也不相同
    
        共有属性 evt.target 触发事件的节点对象(元素)
    
        鼠标事件
            1. offsetX  offsetY
              获取鼠标在元素中坐标位置，以元素左上角(0,0)点，向右向下为正方向
    
            2. clientX clientY
              获取鼠标在网页中的坐标位置，以...
    
            3. screenX screenY
              获取鼠标在屏幕中的坐标信息，以.....

键盘事件对象
    1. onkeydown/onkeyup
        which属性:
            获取当前按键的编码值:键盘上所有按键都对应有自己的码值(键码),
            数字和字母的编码值与ASCII对照一致，不区分大小写，统一返回大写码值

    2. onkeypress
        只有在键盘输入内容(数字，字母，字符) 才会触发，
        键盘上的功能键(大写锁定，shift...)不会触发
        which属性:
            返回按键字符对应的ASCII码值，区分大小写
        key 属性
            返回当前键位表示的字符


事件的传递机制
    1. 事件传递
        当我们页面上某一个元素被点击，相关的元素都能接受到这个事件
        可以选择是否处理

    2. 事件传递机制
        实际上是事件传递给相关元素的顺序
    
        默认: 冒泡传递，从触发元素开始逐级向外传递，
    
        特殊: 捕获传递，事件发生后，从外向里逐级传递
             IE浏览器不支持捕获，默认机制都是冒泡
    
             addEventListener('事件',function,false);
             false : 冒泡传递(默认)
             true : 捕获传递
            
    3.阻止事件传递
        通过事件对象阻止事件向其他元素传递
        evt.stopPropagation();
    
        eg:
            document.body.addEventListener('click',function(evt){
                alert('body被点击');
                evt.stopPropagation();
            },true);