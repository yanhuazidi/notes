[TOC]





## Django 相关链接

​	官网: http://www.djangoproject.com
​	中文文档 : http://djangobook.py3k.cn/2.0/

## Django 的安装

​    查看已安装的Django版本

```python
import django 
django.VERSION #查看版本
```

### 在线安装

```powershell
sudo pip3 install django[==1.11.8 指定版本，默认最新]
```
### 离线安装

```powershell
# 下载安装包
sudo pip3 install Django-1.11.8.tar.gz
tar xzvf Django-*.tar.gz 。
cd Django-* 。
sudo python setup.py install
```



## Django内置命令 

### check

```powershell
python3 manage.py check [app1]
```

检查整个Django项目是否存在常见问题。

默认情况下，所有应用都将被选中。可以通过提供app的名字检查指定的应用：

### diffsettings

```powershell
python manage.py diffsettings
```

显示当前设置文件与Django的默认设置之间的差异。

### flush

```powershell
python manage.py flush
```

从数据库中删除所有数据。已应用的迁移不会被清除。只删除具体数据，不删除数据表！

如果您希望从空数据库启动并重新运行所有迁移，则应该删除并重新创建数据库，然后再运行migrate，这样会连原来的数据表都删了。

### makemigrations

```powershell
python manage.py makemigrations [app1 app2]
```

根据检测到的模型创建新的迁移。迁移的作用，更多的是将数据库的操作，以文件的形式记录下来，方便以后检查、调用、重做等等。尤其是对于Git版本管理，它无法获知数据库是如何变化的，只能通过迁移文件中的记录来追溯和保存。

### migrate

```powershell
python manage.py migrate
```

使数据库状态与当前模型集和迁移集同步。说白了，就是将对数据库的更改，主要是数据表设计的更改，在数据库中真实执行。例如，新建、修改、删除数据表，新增、修改、删除某数据表内的字段等等。

### runserver

```powershell
python manage.py runserver
python manage.py runserver 127.0.0.1:8080
```

启用Django为我们提供的轻量级的开发用的Web服务器。默认情况下，服务器运行在IP地址127.0.0.1的8000端口上。如果要自定义服务器端口和地址，可以显式地传递一个IP地址和端口号给它。

### shell

```powershell
python manage.py shell
```

启动带有Django环境的Python交互式解释器，也就是命令行环境。默认使用基本的python交互式解释器。这个命令非常常用，是我们测试和开发过程中不可或缺的部分！

### startapp

```powershell
python manage.py startapp app_name
```

创建新的app。

默认情况下，会在这个新的app目录下创建一系列文件模版，比如models.py、views.py、admin.py等等。

### startproject

```powershell
django-admin startproject project_name
```

新建工程。默认情况下，新目录包含manage.py脚本和项目包（包含settings.py和其他文件）。

### test

```powershell
python manage.py test [test_label [test_label ...]]
```

运行所有已安装的app的测试代码。

### app提供的命令

前面是Django核心提供的命令项，下面则是一些内置app，比如auth等提供的命令项。它们只在对应的app启用的时候才可用。

#### createsuperuser

​	**创建超级管理员**

```powershell
python manage.py createsuperuser
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
```

#### changepassword 

​	**修改用户密码**

```powershell
python manage.py changepassword username
```

#### clearsessions 

如果用户主动退出，session会自动清除，如果没有退出就一直保留，记录数越来越大，要定时清理没用的session。django中已经提供了这个方法，推荐把它加入到crontab中自动清理过期的session，防止session表记录过大，影响访问速度。

```powershell
django manage.py clearsessions
```

#### collectstatic

当部署项目时,在终端输入:

```powershell
python manage.py collectstatic
```

django会把所有的static文件都复制到STATIC_ROOT文件夹下

### 共有参数

–pythonpath PYTHONPATH 
–settings SETTINGS 
–traceback 
–verbosity {0,1,2,3}, -v {0,1,2,3} 
–no-color

有三种方式，可以在cmd窗口中执行Django提供的内置命令：

```powershell
$ django-admin <command> [options]
$ python manage.py <command> [options]
$ python -m django <command> [options]
```

1、django-admin是用于管理Django的命令行工具集，当我们成功安装Django后，在操作系统中就会有这个命令，但是根据安装方式或者系统环境的不同，你可能需要配置一下调用路径。在Linux下，该命令一般位于site-packages/django/bin，最好做一个链接到/usr/local/bin，方便调用。Windows下可以配置系统环境变量

2、manage.py则是每个Django项目中自动生成的一个用于管理项目的脚本文件，需要在cmd窗口中cd到Django项目的manage.py所在的目录后通过python命令执行。



## 创建Django项目

```powershell
语法: django-admin startproject 项目名
```

使用 django-admin 来创建 HelloWorld 项目：

```powershell
django-admin startproject HelloWorld
```

创建完成后我们可以查看下项目的目录结构：

```powershell
$ cd HelloWorld/
$ tree
.
|-- HelloWorld
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

目录说明：

- **HelloWorld:** 项目的容器。
- **manage.py:** 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- **HelloWorld/__init__.py:** 一个空文件，告诉 Python 该目录是一个 Python 包。
- **HelloWorld/settings.py:** 该 Django 项目的设置/配置。
- **HelloWorld/urls.py:** 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- **HelloWorld/wsgi.py:** 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

## Django项目主目录(与项目名称一致的目录)\

### \__init__.py

初始化文件，服务启动时自动运行

### urls.py

项目的基础url配置文件

### wsgi.py

Web Server Gateway Interface
Web  服务   网关      接口

### settings.py

主配置文件，启动项目时自动运行的


```python
BASE_DIR : 获取当前项目的绝对路径
DEBUG : 是否启用调试模式
	True 开发环境中使用
	False 生产环境中使用
ALLOWED_HOSTS 
        设置允许访问到本地项目的地址列表
        如果为空的话，表示只有本机(127.0.0.1/localhost)才能访问

        如果允许在局域网内被其他机器访问的话: 
        推荐写 ['*'],表示任何能够表示该机器的地址都能够访问到当前项目

        如果允许被其他机器访问的话 ，启动服务器时必须使用以下方式:
        ./manage.py runserver 0.0.0.0:port

INSTALLED_APPS
        指定已安装的应用,如果有自定义应用的话，必须在此注册
        INSTALLED_APPS = [
            "应用名称",
        ]
ROOT_URLCONF = 'mysite.urls'
# 相对应的文件是mysite/urls.py
# 当访问 URL /hello/ 时，Django 根据 ROOT_URLCONF 的设置装载 URLconf 。 然后按顺序逐个匹配URLconf里的URLpatterns，直到找到一个匹配的。      

MIDDLEWARE
        指定中间件信息

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',#指定要使用的模板的引擎 
        'DIRS': [],	#指定模板的存放目录,不写 : Django会自动的到每个应用中搜索一个叫做templates的目录来作为,写路径: Django会按照写的路径去搜索[BASE_DIR+"/templates",],
                为模板的存放目录
        'APP_DIRS': True, #是否自动搜索应用中的目录 True : 表示要自动搜索应用中的templates目录 False : 表示不要
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {	#指定数据库配置
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yanhua_blog',
        'USER': 'wei',
        'PASSWORD': '123456',
        'PORT': 3306
    }
}

LANGUAGE_CODE = 'zh-Hans'	#语言设置，如果需要使用中文的话，允许更改为 zh-Hans

TIME_ZONE = 'Asia/Shanghai' #指定时区,如果指定中国时区的话,允许更改为 "Asia/Shanghai"
    
#当auto使用用户表时 让Django使用自定义的表
AUTH_USER_MODEL = 'userinfo.Userinfo'
#app名.类
   
STATIC_URL = '/static/'	#静态文件url
STATICFILES_DIRS=(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
#STATIC_ROOT 是在部署静态文件时,所有的静态文静聚合的目录,STATIC_ROOT要写成绝对地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

```



## 应用

​    什么是应用
​        应用就是网站中的一个独立的程序模块
​        在 Django 中，主目录一般不处理用户的具体请求，主要做项目的初始化配置以及请求的分发(分布式请求处理)
​        具体的请求是由各个应用去处理的

### 创建应用
1.manage.py 指令创建
        ./manage.py startapp 应用名称
​	ex :
        ./manage.py startapp news
2.在 settings.py 中进行注册
​	在 INSTALLED_APPS 中追加应用名称即可
		INSTALLED_APPS = [
   			 "应用名称",
		]

### 应用目录的文件结构

1. migrations 文件夹
    存放数据的中间文件
    与模型相关
2. \__init__.py
    应用的初始化文件
3. admin.py 
    应用的后台管理配置文件

4. app.py
    应用的属性配置文件

5. models.py
    模型的映射文件

6. tests.py
    应用的单元测试文件

7. views.py
    定义视图处理函数的文件



## urls.py文件

路由配置文件，默认在主目录中,包含最基本的地址映射
作用： 通过urls.py 中定义好的地址找到对应的视图处理函数

```python

from django.contrib import admin
from django.urls import path,include
dic = {
     "name":"wangwc",
     "age":18
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
	url(regex,#允许是正则表达式，匹配请求的url
        views, #对应的视图处理函数
        kwargs=None, #字典，用来向 views 传参
        name=None #为 url 起别名，在地址反向解析时使用
       ),
    url(r'^show/(\d{4})/$',show1_views),
    #def show1_views(request,year)
    #使用正则表达式的子组传参 - (), 一个子组就是一个参数
    #多个参数的话要使用多个子组表示，并且中间使用 / 隔开
    url(r'^show/$',show3_views,dic)
    #def show3_views(request,name,age)
]
```



