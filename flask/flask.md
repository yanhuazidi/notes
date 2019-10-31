

[TOC]



## Flask 框架

是一个基于python并且依赖于Jinja2模板引擎和Werzeug WSGI服务的一个微型框架

**安装Flask**

`pip3 install flask`



## 配置

```python
app = Flask(__name__,template_folder="templates",
                    static_folder="static",
                    static_url_path="/static")
```

1. `template_folder`
    指定保存模板的文件夹名称    默认 `templates`
2. `static_folder`
    指定保存静态文件的文件夹名称    默认 `static`
3. `static_url_path`
    指定访问静态文件的路径  默认` /static`



## 静态文件

```html
<script type = "text/javascript" src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
```





## 路由

### 路由的体现

Flask中，路由是@app.route() 装饰器来表示的

```python
@app.route("/")
@app.route("/index/")
def index()
    return str
```



### 路由参数

路由中可以携带参数来表示要传递到视图函数中的数据

```python
@app.route("/show/<name>")
def show1(name):
    name: 表示的就是地址栏上传递的数据
    pass
```

**指定参数类型的路由**

允许在声明路由时指定参数类型

```python
@app.route("/show/<name>/<int:age>")
def show(name,age):
    pass
类型转换器          作用
缺省             字符串，不能有斜杠(/)
int：            整型
float：          浮点型
path：           字符串，可以有斜杠(/)
```



### 路由中设置HTTP请求方法

在Flask中默认只能接收GET请求,无法接收POST请求

在Flask中允许设定可以接收的请求方式，如果请求方式不匹配的话，会响应405(Method Not Allowed)


```python
@app.route("/xxx",methods=["POST","GET"])
def xxx()
    该函数即能接收post请求，也能接收get请求
```



### url的反向解析

正向解析: 程序自动解析,根据@app.route()中的访问路径，来匹配处理函数

反向解析: 通过视图处理函数的名称自动生成对应的访问路径

`url_for('funName',**kw)`

- funName : 要生成地址的函数名
- kw : 该地址中需要的参数
- 返回值: funName 的路由字符串

#### 视图中解析


```python
@app.route("/admin/login/form/show/<name>/<age>")
def show1(name,age):
    return "参数name的值为:%s,参数age的值为:%s"%(name,age)

@app.route("/url1/<name1>/<age1>")
def url1(name1,age1):
    url = url_for('show1',name=name1,age=age1)
    return "<a href='%s'>去show1</a>"%url
```

#### 模板中解析

```html
<script type = "text/javascript" src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
```







## 模板 Templates

Flask中 ，模板是依赖于jinja2的模板系统  http://jinja.pocoo.org/

### 模板的渲染

作用: 在视图中，将模板文件(xx.html)渲染成字符串之后，再响应给浏览器
语法:` render_template('xxx.html')`
参数:要渲染的模板
返回值: 该模板中的字符串内容

**传递变量到模板中**

`render_template("xxx.html",变量=值,变量=值...)`

在模板中获取变量的值 {{变量名}}

`return render_template("01-var.html",params =locals())`

在模板中获取变量的值 {{params.name}}



### 过滤器

过滤器是允许在变量输出之前按一定的规则改变变量的值

`{{变量|过滤器}}`

jinja2模板中常见的过滤器

| 过滤器     | 说明                           |
| ---------- | ------------------------------ |
| capitalize | 首字符变大写，其他字符变小写   |
| lower      | 将值转为小写字符               |
| upper      | 将值转为大写字符               |
| title      | 将值中的每个单词的首字符变大写 |
| trim       | 取掉值两端的空格               |



## 标签

### if 标签

```html
{% if 条件 %}
语句块
{% elif条件1 %}
语句块
......
{% else %}
语句块
{% endif %}
```



### for 标签

```html
{% for 变量 in iter %}
语句块
{% endfor %}
```

内置变量: loop

1. 只能在for循环标签中使用
2. 不用声明直接用
3. 记录本次循环的一些信息

**loop 中的常用属性**

1. index  记录当前循环的次数，从1开始计算
   
2. index0 从0开始计算

3. first  表示当前的循环是否为第一次循环，值为布尔值

      True 表示为第一次

      False 表示不是第一次

4. last   表示当前的循环是否为最后一次循环，值为布尔值

      True 表示为是

      False 表示不是

当前循环次数:{{loop.index}}

当前循环下标:{{loop.index0}}



### macro 标签(宏)

相当于在模板中声明函数

{% macro 宏名称(参数列表) %}

 .....
{% endmacro %}

使用宏:{{宏名称(参数列表)}}

 **在独立的模板文件中声明所有的宏**

1. 创建 macro.html 模板文件
   作用: 定义项目中要用到的所有的宏
2. 在使用宏的模板上导入 macro.html

    {% import 'macros.html' as ms %}
    {% for name in params.lis %}
     {{ms.show_li(name)}}
    {% endfor %}





## 模板的继承

### 父模板

需要在父模板中定义哪些内容在子模板中可以被重写

{% block 块名 %}

语句块

{% endblock %}

### 子模板

1. 模板顶部使用标签extends来表示继承

    {% extends '父模板名称' %} **注意这里有引号**

2. 使用  block 来重写父模板中同名块的内容

{% block 块名 %}
语句块，覆盖父模板中同名的block内容
{% endblock %}





## 自定义错误页面

​    404  : Not Found
​    500  : Internerl Server Error

### 404的错误处理

```python
@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html(#自定义)'),404(默认200)
```

### 500的错误处理

```python
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html(#自定义)'),500(默认200)
```

​       



## 请求(request)

### request 的常用成员

1. `scheme` : 获取请求的方案(协议)
2. `method` : 获取请求方式 取值为 post 或 get
3. `args` ：获取使用 get 请求方式提交过来的数据 返回dict
4. ` form `：获取使用post请求方式提交过来的数据  返回dict
5. `cookies` ：获取cookies中的相关信息
6. `headers` ：获取请求消息头的相关信息   返回dict
7. `files` ： 获取上传的文件
8. `path` ： 获取请求的资源的具体路径  www.sdfd.cn/aaaaa/wer/
9. `full_path` ： 获取完整的请求资源的具体路径(带get请求中的参数) www.sdfd.cn/aaaaa/wer/?a=sd&a=345
10. `url` ： 获取完整的请求地址，从协议开始  http://www.sdfd.cn/aaaaa/wer/?a=sd&a=345



            ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
            '__enter__', '__eq__', '__exit__', '__format__', '__ge__', 
            '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', 
            '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
            '__subclasshook__', '__weakref__', '_cached_json', '_get_data_for_json', 
            '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', 
            '_parse_content_type', 'accept_charsets', 'accept_encodings',
            'accept_languages', 'accept_mimetypes', 'access_route', 'application', 'args',
            'authorization', 'base_url', 'blueprint', 'cache_control',
            'charset', 'close', 'content_encoding', 'content_length', 'content_md5',
            'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 
            'disable_data_descriptor', 'encoding_errors', 'endpoint', 'environ', 
            'files', 'form', 'form_data_parser_class', 'from_values', 'full_path',
            'get_data', 'get_json', 'headers', 'host', 'host_url', 'if_match', 
            'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since',
            'input_stream', 'is_json', 'is_multiprocess', 'is_multithread',
            'is_run_once', 'is_secure', 'is_xhr', 'json', 'list_storage_class', 
            'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 
            'max_forwards', 'method', 'mimetype', 'mimetype_params', 
            'on_json_loading_failed', 'parameter_storage_class', 'path', 
            'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 
            'remote_user', 'routing_exception', 'scheme', 'script_root',
            'shallow', 'stream', 'trusted_hosts', 'url', 'url_charset', 
            'url_root', 'url_rule', 'user_agent', 'values', 'view_args',
            'want_form_data_parsed']



## 响应(response) 

### 响应字符串

return '字符串'

### 响应模板

`return render_template('xxx.html')`

其本质 还是响应字符串

### 响应对象 

指将响应内容封装到一个对象中，以便完成更多的响应行为

在Flask中可以使用 `make_response()` 构建一个响应对象

```python
from flask import make_response
def xxx():
    resp = make_response('响应内容')
    resp = make_response(render_template('xxx.html'))
    return resp
#允许调用resp 中的属性或方法以便完成更多的响应行为
```

### 重定向

**redirect()**函数的原型如下：

```
Flask.redirect(location, statuscode, response)
```

在上述函数中：

- **location**参数是应该重定向响应的URL。
- **statuscode**发送到浏览器标头，默认为302。
- **response**参数用于实例化响应。


```python
from flask import redirect

@app.route('/xxx')
def xxx():
    return redirect(url_for('index'))
#为两次请求
```



## 文件上传

### 注意问题

表单中如果有文件上传的话，必须遵循以下两个要求:

1. 表单的提交方式 method 必须为 post
2. 表单的 enctype 属性必须为 multipart/form-data    

`<form method='post' enctype='multipart/form-data'>`

### 文件获取

`request.files`上传的所有文件(字典)

文件可以从**request.files[file]**对象的filename属性中获取。

但是，建议使用**secure_filename()**函数获取它的安全版本。

 `f = request.files['提交的name']`

从上传的文件中，将指定名称的文件获取出来并保存到 f 中

### 保存文件

语法 : f.save('保存的路径')
作用 : 将文件保存到指定目录处
注意 : 

1. 保存的路径可以是相对路径也可以是绝对路径
2. 保存路径要精确到文件名称
3. 保存的目录必须是已存在的

```python
f = request.files['file']
f.save('static/'+secure_filename(f.filename))
f.filename ：能够获取出文件名
```



可以在Flask对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。

`app.config['UPLOAD_FOLDER']`定义上传文件夹的路径

app.config['MAX_CONTENT_PATH']指定要上传的文件的最大大小（以字节为单位）



## cookies

### 获取 cookies 的值

```python
var = request.cookies.get(key,none)
```

### 设置cookies 

响应对象.set_cookie(key,value,max_age)

- key: 字符串， 要保存的cookies的名称
- value: 字符串，要保存的cookies的值
- max_age : 最大的保存时间，取值数值,以 s为单位

**多个cookie键值对**
resp.set_cookie('uname','wangwc',3600)
resp.set_cookie('uage', '555', 600)

```python
resp = make_response(render_template('readcookie.html'))
resp.set_cookie('userID', user)
resp.set_cookie('uname','wangwc',3600)
return resp
```
### 删除 cookies 内容

删除对应的键,就能删除对应的键值对
`resp.del_cookie('key')  `



## session

### 配置 SECRET_KEY
`app.config['SECRET_KEY'] = '自定义字符串'`

### 使用 session

`from flask import session`

#### 向 session 中保存数据
​    session['key'] = str(value)
​    session['key1'] = str(value1)
​    ...

#### 从 session 中获取数据
​    value = session['key']
​    value = session.get('key')

#### 删除 session 中的数据
​    del session['key']

   session.pop('key')

#### 清空session中所有数据：

```
session.clear()
```

session 空间 默认浏览器30分钟不请求会关闭空间，
关闭浏览器页面关闭空间



## 模型    - Models


            数据库工具
                1 . Navicate for MySQL  可视化的数据库管理(重点)
                2 . Power Designer  数据库的建模工具    -ER图(Entity Realtionship)
    
        3.ORM的优点
            1.封装了数据库中所有的操作，大大的提高了开发效率
            2.可以省略庞大的数据访问层，即便不要SQL编码也能完成对数据库的CRUD操作


Flask中的ORM框架
    1.python 中的 ORM
        比较常用的ORM框架 - sqlalchemy

        sqlalchemy安装
            在线: sudo pip3 install sqlalchemy
    
            离线:   $ tar -xf sql....tar.gz
                    $ cd sqlalchemy
                    $ sudo python3 setup.py install
    
    2.在Flask中
        使用的也是sqlalchemy
        但需要安装 Flask-sqlalchemy 插件包
        安装 : sudo pip3 install flask-sqlalchemy


4.创建数据库 - flask
     create database flask default charset utf8 collate utf8_general_ci; 
    
5.在Flask中配置数据库
    1.通过 app(Flask应用实例) 构建配置信息
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://用户名:密码@主机:端口号/数据库"
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/flask"

    2.创建数据库应用实例
        from flask_sqlalchemy import SQLALchemy
        import pymysql
        pymysql.install_as_MySQLdb()
    
        db = SQLALchemy(app)

6.定义模型
    语法:
        class MODELNAME(db.Model):
            __tablename__ = 'TABLENAME'
            COLUMN_NAME = db.Column(db.TYPE,OPTINONS)
        db.create_all() 将创建好的实体类映射到数据库执行


        1.MODELNAME : 定义的模型类的类名，通常参考表名
        2.TABLENAME : 映射到数据库中表达名称是什么(想生成的表名)
        3.COLUMN_NAME : 属性名 ，映射到数据表中就是字段名
        4.TYPE : 映射到字段的数据类型
        5.OPTINONS : 字段选项，(主键,外键，索引，约束，自增)
    
        db.TYPE 字段的数据类型
            类型名          python类型          说明
            Integer         int               32位整型
            SmallInteger    int               16位整型
            BigInteger      long              64位整型
            Float           float             浮点型
            Numeric         decimal.decimal   定点类型
            String          str               变长字符串
            Text            str               变长字符串(更长)
            Boolean         Boolean           布尔值
            Date            datetime.date      日期
            Time            datetime.time      时间
            DateTime        datetime.datetime  日期时间
    
        OPTINONS 字段选项
            选项名         说明
            primary_key    如果设置为True表示该字段为主键,默认自增AUTO_INCREMENT
            unique         如果设置为True表示该字段为唯一索引
            index          如果设置为True表示该字段为索引键
            nullable       如果设置为True表示该字段可以为空，默认允许为空
            default        指定该字段的默认值
    
            **设置多个选项用 , 号隔开


数据库操作
    1.插入
        1. 创建实体类的对象
        2.完成插入
            db.session.add(实体对象)
            db.session.commit()
        
        #指定当视图执行完毕后，自动提交数据库,省略 db.session.commit()
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    
        #指定每次执行数据库操作时打印原始的SQL语句
        app.config['SQLALCHEMY_ECHO']=True


​    
2.查询

基于 db.session 进行查询 支持多表查询
            1. db.session.query(Models1,Models12...) 全部字段查询
              参数: 要查询的实体类(表),如果是多个实体类的话，相当于要做多表连接查询
              返回: 对应的类的查询对象(为表对象) ,打印对象为对应的sql语句

              **必须用查询用执行函数获取结果
             
                1.1 只查询指定的字段
                query = db.session.query(Models1.name,Models1.age,...)
    
            2.查询执行函数
                目的: 在 query()的基础上得到最终的查询结果
                      未加执行函数的操作语句返回结果为对应的模型类的查询对象
    
                语法: db.session.query(Models).查询执行函数()
    
                1. all(): 以列表的方式返回query对象中所有的查询数据记录对象
                          返回结果需要用成员取值符来获取对应的属性值
                    for user in users=[]:
                        print("姓名:%s,年龄:%d,邮箱:%s" % (user.username,user.age,user.email))
    
                2. first(): 返回query对象中的第一条查询数据记录对象，没有结果返回 None
                           返回结果需要用成员取值符来获取对应的属性值  
                        print("姓名:%s,年龄:%d,邮箱:%s" % (user.username,user.age,user.email))
    
                3. first_or_404(): 返回query对象中的第一个查询数据记录对象，同first()
                                    如果没有结果则终止程序，返回404
                4. count(): 返回query对象中的查询结果的记录的数量,整型


​                
​            3.查询过滤器函数
​                作用: 专门对数据进行筛选，返回部分行数据
​    
​                语法:  db.session.query().过滤器函数().执行函数()
​                    
                1. filter()  按指定条件进行查询(单表,多表,定值,不定值)  映射where子句
                2. filter_by() 按等值条件进行过滤
                3. limit() 按限制行数量获取结果     映射 limit子句
                4. order_by() 按指定列进行排序      映射 order by子句
                5. group_by() 按指定条件进行分组    映射 group by子句
    
                    过滤函数 使用顺序 参考 sql语句使用顺序

过滤器函数详解:
    1.filter()
            注意: 条件必须由 实体类.属性 组成

            1.查询年龄大于30的
        user = db.session.query(Users).filter(Users.age>30).all()
    
            2.查询id等于1 的，用 == 号
        user = db.session.query(Users).filter(Users.id==1).first()
    
            3.查询年龄大于30 并且 id大于1 的数据，并列用"," 隔开,等于and
        user = db.session.query(Users).filter(Users.age>30,Users.id>2).all()
    
            4.查询年龄大于30 或者 id大于1 的数据 需要使用or_(条件1,条件2)
                需要导入 from sqlalchemy import or_
        user = db.session.query(Users).filter(or_(Users.age>30,Users.id>2)).all()
    
            5.查询email中包含 'w' Users 的信息  
                使用like关键字查询，每个模型类属性都有lick()方法，_匹配1个或多个,%匹配0个或多个
        user = db.session.query(Users).filter(Users.email.like('%w%')).all()
    
            6. 查询id在[2,4]中的 Users中的信息
                使用 in_([])方法 参数为列表[]
        user = db.session.query(Users).filter(Users.id.in_([2,4])).all()
        
            7. 查询年龄在30到100之间的 Users信息
                使用 between(self,start,end)方法
        users = db.session.query(Users).filter(Users.age.between(30,100)).all()
    
    2. filter_by()
            注意 : 只能判断等值，不能判断不等值
        1. 查询 id 为 1 的users 信息
            user = db.session(Users).filter_by(id=1).first()
    
    3.limit():获取限定行数记录
      offset():指定偏移量
        1. 获取users表中的前2条记录
            result = db.session.query(Users).limit(2).all()
    
        2. 获取users 表中 过滤前3条记录后取2条记录
            result = db.session.query(Users).limit(2).offset(3).all()
    
    4.order_by()
        1.按照 id 倒序排序
            users = db.session.query(Users).order_by("id desc").all()
    
        2.多级排序，先通过age 排序，age相同的再通过id排序
            users = db.session.query(Users).order_by("age desc,id asc").all()
        
    5.group_by()
        1.将 users 表中的数据按照 age 进行分组
            tuple = db.session.query(Users.age).group_by('age').all()
            返回结果为元组元素列表
        
    6.聚合函数
        使用func 对象使用聚合函数(需要导入)
        label() 方法取别名
    
        func.avg()  func.sum()  func.max()  func.min()  func.count()
            普通聚合
            sql : select avg(age) as 'avaAge' from users;
            db.session.query(func.avg(Users.age).label('avaAge')).all()
            分组聚合
            sql :select age,avg(age) from Users group by age
            1.db.session.query(func.avg(Users.age)).group_by('age').all()
            2.db.session.query(Users.age,func.avg(Users.age)).group_by('age').all()
            3.db.session.query(Users.age,func.avg(Users.age),func.sum(Users.age)).group_by('age').all()



基于 Models 类进行查询
    使用 模型类的 query 属性，只能单表查询
    一般单表所有列查询推荐使用

    Models.query.查询过滤器函数().查询执行函数()
    
    # users = Users.query.all()
    users = Users.query.filter(Users.id==3).all()
    for user in users:
        print("姓名:%s,年龄:%d,邮箱:%s" % (user.username, user.age, user.email))



修改
        把 id 为 1 的人年龄改为60岁
    1.查
        user = Users.query.filter_by(id=1).first()
    2.改
        user.age = 60
    
    3.保存
        db.session.add(user)
        db.session.commit()

删除
        删除 id 为 1 的人的信息
    1.查
        user = Users.query.filter_by(id=1).first()
    2.删
        db.session.delete(user)
        db.session.commit()

    一般不会真正删除数据，而是增加一个状态字段，用bool表示用户状态，
        通过改变 True 和 False 来改变用户状态
        isActive = db.Column(db.Boolean,default=True)

--------------------------------------------------------------------
关系映射    见项目 :FlaskDemo05
    所有的映射关系都是建立在数据库的对应关系之上的，只是在其上进行了面对对象的封装，
    任何违背数据库操作逻辑的映射都是不能实现的。

一对多关系映射  
        以"一"所在为主表，"多"所在为从表

        一对多在数据库中实现方式: 主外键关系
        在从表中增加一个列，作为外键，引用"一"个表的主键
    
    在 ORM 中
    语法 :
        1.在从表实体类中增加一个属性，引用自主表(实体类)的主键列(属性)
    
        外键列名 = db.Column(db.Integer[#参考主表的主键数据类型],db.ForeignKey('主表名.主键名')) 
            **在 ORM 中添加外键方式,会作用于数据库，等同于数据库添加主从键


​    
​        2. 在主表实体类中增加关联属性和反向引用关系:
​            为实体类的查询属性，不会作用于数据库
​    
​            关联属性名 = db.reIationship("从表实体类名",backref='反向引用属性名',lazy='')
​                                                        #多个关系选项 用 , 分隔
​    
        关联属性名: 关联属性,变量名自定义   一对多
            1. 为主表实体类对象属性
            2. 通过这个属性能够得到对应的所有的从表实体类记录对象
                返回为记录对象列表，需要用 .all() 执行函数取得查询结果(可以用过滤函数指定)
                eg:
                记录对象列表 = 主表实体类对象.关联属性名.all()
                for 对象 in 记录对象列表:
                    print("姓名:%s,生日:%s"%(对象.属性,对象.属性))
    
        反向引用属性名: 反向引用属性,变量名自定义   一对一
            1. 为从表实体类对象属性
            2. 通过这个属性能够得到对应的主表实体类记录对象
                返回为一个记录对象
                eg:
                    对象 = 从表实体类对象.反向引用属性
                    print("教师姓名:%s"%对象.属性)
    
    3. 数据添加
        主表添加数据: 正常添加，不受从表影响
    
        从表添加数据: 受主表影响
            １．通过关联属性关联数据
                tea1 = Teacher("魏老师",40,'1985-10-01')    #对应初始化方法
                tea1.course_id=1            #从键关联主表主键
                db.session.add(tea1)
                db.session.commit()
    
            2. 通过反向引用属性关联数据
                tea2 = Teacher("王老师",45,'1975-10-01')    #对应初始化方法
                course = Course.query.filter_by(id=1).first()   #获取对应主表对象
                tea2.course = course        #反向引用属性关联主表对象
                db.session.add(tea2)
                db.session.commit()


    关系选项:
    
        选项名                        说明
    
        backref                 在关系的另一个模型中添加的反向引用属性名
                                    (准备在"多"的实体中增加对"一"的实体引用的属性名)
    
        lazy                       指定任何加载当前的相关记录(延迟加载模式)  
                取值: 'select' :    首次访问时加载所有记录
                    'immediate' : 源对象只要加载就马上加载相关记录(连接查询)
                    'subquery' :  效果同上，使用子查询的方式加载记录  
                    'noload' :    永不加载相关记录
                    'dynamic' :   默认也不加载相关记录，当提供记录的查询
    
        uselist     如果设置为False，表示不使用列表表示相关数据而使用标量，
                    在一对一中使用,限定从表唯一
    
        secondary    指定多对多关系中的关联表的名字,在多对多中使用  


一对一关系映射

    1.在SQLAlchemy 中的体现 ，一对一任意指定主从表
        1.在任何一个实体类中增加对另外一个实体类的主从键
    
            外键字段名 = db.Column(db.Integer,db.ForeignKey('主表名.主键名')[,unique=True])
                [,unique=True]可加可不加，在程序中uselist=False会实现唯一约束


        2. 在另一个实体类中要增加关联属性和反向引用关系
            关联属性名 = db.reIationship("从表实体类名",backref="反向引用属性名",uselist=False)
                    uselist: 表示属性不是一个列表 而是一个标量
    
    2.指定关联数据  同一对多
        1. 通过 外键列 指定关联信息
            wife = Wife(xxx)
            wife.users_id = xxx
            db.session.add(wife)
            db.session.commit()
    
        2. 通过 反向引用属性 指定关联信息
            wife = Wife(xxx)
            wife.user = user_obj
            db.session.add(wife)
            db.session.commit()
    
    3. 获取关联数据
        1. 通过 Users 的对象 获取 对应的 Wife 对象
            通过 关联属性 获取对应的 Wife 对象
            user = Users.query.filter_by(id=1).first()
            wife = user.wife
        
        2. 通过 Wife 的对象 获取 对应 Users 的对象
            通过 反向引用属性 获取对应的 Users对象
            wife = Wife.query.filter_by(id=1).first()
            user = wife.user

多对多的关系映射
    1. 什么是多对多
        A表中的一条数据可以与B表中的任意多条数据相关联
        B表中的一条数据可以与A表中的任意多条数据相关联

    2.实现方式
        1. 在数据库中的实现
            1.依托于第三张表来实现的
            2.在关联表中分别添加对A表和B表的从键
    
            3.通过对关联表的数据记录操作(ZSGC)来实现A表和B表的多对多关系映射。
    
                **连接查询不受表和表的关系影响，可以任意连接多张表，
                    只要数据对的上(主从键刚好使数据对的上)


        2. SQLALchemy 实现
            1.创建第三张关联表对应的实体类
            2.在关联实体类中分别创建对 A表和B表 的从键
                语法:
                A表从键属性名 = db.Column(db.Integer,db.ForeignKey('A表名.主键'))
                B表从键属性名 = db.Column(db.Integer,db.ForeignKey('B表名.主键'))
    
            3.在任选A实体类或B实体类中创建关联属性和反向引用属性
                在A中创建:
                语法:
                关联属性名 = db.relationship('B实体类名',secondary='关联表表名',
                            lazy='dynamic',
                            backref=db.backref('反向引用属性名',lazy='dynamic'))
    
            4.在SQLAlchemy中使用A表的关联属性和B表的反向引用属性更方便的实现对关联表
                的数据记录操作(ZSGC)，来实现A表和B表的多对多关系映射
    
              **直接操作A表的关联属性和B表的反向引用属性都是作用于关联表之上，A、B表不受影响
    
            5.关联表中除了主表A、B从键外，也可以有其它字段，
                通过与A或B主表的一对多映射来完成数据的关联，与多对多是隔断的。


​        
​        数据的插入
​            1. A表和B表的记录正常插入，不受影响
​    
​            2. 多对多关联表数据插入，实现A表和B表的多对多映射
​                1.通过关联属性和反向引用属性
​                    在 A表 或 B表中同等操作方式，注意对应关联属性
​                    A表对象 = AClass.query.filter_by(条件).first()  
​                    B表对象 = BClass.query.filter_by(条件).first()
​                    A表对象.关联属性名.append(B表对象)
​                    db.session.add(A表对象)
​                    db.session.commit()
​    
                2.通过关联表实体类
                    关联表实体类对象 = 关联表实体类名()
                    关联表实体类对象.A表从键属性名 = values  #必须是A表主键的值
                    关联表实体类对象.B表从键属性名 = values  #必须是B表主键的值
                    关联表实体类对象.其它属性 = values
                    db.session.add(关联表实体类对象)
                    db.session.commit()
        
        数据的修改
            1. A表和B表的记录正常修改，不受影响，关联表根据其从键设置发生变化
    
            2.多对多关联表数据移除，实现A表和B表的多对多映射
                1.通过关联属性和反向引用属性
                    删除
                    在 A表 或 B表中同等操作方式，注意对应关联属性
                    A表对象 = AClass.query.filter_by(条件).first()  
                    B表对象 = BClass.query.filter_by(条件).first()
                    A表对象.关联属性名.remove(B表对象)
                    db.session.add(A表对象)
                    db.session.commit()
    
                2.通过关联表实体类
                    修改:
                    关联表实体类对象 = 关联表Class.query.filter_by(条件).first() 
                    关联表实体类对象.A表从键属性名 = values  #必须是A表主键的值
                    关联表实体类对象.B表从键属性名 = values  #必须是B表主键的值
                    关联表实体类对象.其它属性 = values
                    db.session.add(关联表实体类对象)
                    db.session.commit()
                    删除:
                    关联表实体类对象 = 关联表Class.query.filter_by(条件).first()
                    db.session.delete(关联表实体类对象)
                    db.session.commit()
            
        查询：
            从A查B 和从B查A 操作相同，(和一对多的 一查多模式相同)
    
            eg:     
                #查询１号用户购买的商品
                user = Users.query.filter_by(id=2).first()
                goods = user.goods.all()
                print("用户姓名:%s"%user.username)
                for g in goods:
                    print("商品名称:%s"%g.gname,end='  ')
                    #查询购买的商品数量
                    cu = user.userGoods.filter_by(goods_id=g.id).first()
                    print("商品数量:%s"%cu.count)
                ------------------------------------------   
                #购买２号商品的用户们
                good = Goods.query.filter_by(id=3).first()
                users = good.users.all()
                print("商品名称:%s"%good.gname)
                for u in users:
                    print('用户名称:%s'%u.username,end='  ')
                    cs = good.goodUsers.filter_by(users_id=u.id).first()
                    print("商品数量:%s"%cs.count)
                return 'OK'




