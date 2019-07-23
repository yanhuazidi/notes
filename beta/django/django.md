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

## Django项目主目录(与项目名称一致的目录)

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
	path(regex,#允许是正则表达式，匹配请求的url
        views, #对应的视图处理函数
        kwargs=None, #字典，用来向 views 传参
        name=None #为 url 起别名，在地址反向解析时使用
       ),
    path(r'^show/(\d{4})/$',show1_views),
    #def show1_views(request,year)
    #使用正则表达式的子组传参 - (), 一个子组就是一个参数
    #多个参数的话要使用多个子组表示，并且中间使用 / 隔开
    path(r'^show/$',show3_views,dic)
    #def show3_views(request,name,age)
]
```

### name参数反向解析

​        通过 path() 的别名生成对应的访问地址

        1. 在模板上做反向解析
            1. 基本解析
                
            `{% url '别名' %}`
                
            2. 带参数解析
                `{% url '别名' '参数1' '参数2' ... %}`
            
        2. 在视图上做反向解析
    
            `from django.urls import reverse`
    
            1. 基本解析
    
               `url = reverse("别名")`
    
            2. 带参数解析
    
               `url = reverse("别名",args = ("参数1"，"参数2",....))`



## 模板 (Templates)

 ### 模板的设置

在 settings.by 中 有一个 TEMPLATES 变量

1. BACKEND : 指定要使用的模板的引擎 
2. DIRS : 指定模板的存放目录
   - 不写 : Django会自动的到每个应用中搜索一个叫做temolates的目录来作为为模板的存放目录
   - 写路径: Django会按照写的路径去搜索
3. APP_DIRS : 是否自动搜索应用中的目录
   - True : 表示要自动搜索应用中的templates目录
   - False : 表示不要



## 模板的加载

1. 通过 loader 对象获取模板，在通过HttpResponse进行响应

   ```python
   from django.template import loader
   t = loader.get_template("模板名称")
   html = t.render()将模板渲染成字符串
   return HttpResponse(html)
   ```

2. 通过 render() 加载并响应模板

   ```python
   from django.shortcuts import render
   return render(request,"模板名称")
   ```



## 静态文件

### Django中的静态文件的处理

1. 在 settings.py 中设置静态文件的访问路径

   `STATIC_URL = "/static/"`
   当访问路径为 '/static/' 时 ，就到存储目录中去查找静态文件，而不走路由解析

2. 设置静态文件的存储路径

   `STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)`  元组，可以放多个文件目录

   静态文件目录的存放位置: 

   1. 在项目的根目录处创建一个 static 目录，保存静态文件
   2. 在每个应用中也可以创建一个 static 目录，用于保存静态文件
   3.  Django会自动寻找各个static目录

3. 访问静态文件

   1. 通过静态文件访问路径去访问

      `/static/images/naruto.jpg`

   2. 使用 {% static %} 访问静态资源,动态获取静态文件访问路径，不写死

      1. 在模板的最顶层增加

         `{% load static %}`

      2. 在使用静态资源时

         `<img src={% static "images/naruto.jpg" %}`




STATIC_URL = '/static/'
	STATICFILES_DIRS=(BASE_DIR, 'static') 或		STATIC_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

			#STATIC_ROOT 是在部署静态文件时(pyhton  manage  pycollectstatic)
				所有的静态文静聚合的目录,STATIC_ROOT要写成绝对地址,
				当部署项目时,在终端输入:python manage.py collectstatic
				django会把所有的static文件都复制到STATIC_ROOT文件夹下
	
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
	MEDIA_URL = '/media/'
	
	总 urls.py
		from django.conf.urls import url, include
		from django.contrib import admin
		from sale import views
	
	
		from django.conf.urls.static import static
		from django.conf import settings
	
		urlpatterns = [
			url(r'^admin/', admin.site.urls),
			url(r'^$', views.index, name='index'),
			url(r'^user/', include('userinfo.urls')),
			url(r'^buy/', include('buy.urls')),
			url(r'^sale/', include('sale.urls')),
	
		] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
	
	models.py
		img = models.ImageField(upload_to='img/logo', default='brandlogo.png')


HttpRequest - 请求
	1.什么是HttpRequest
		HttpRequest，就是对请求对象的封装，里面封装的是请求过程中的所有信息。
		在Django中HttpRequest被封装成request对象并封装到视图处理函数中，在调用视图时自动传入
	2.HttpRequest中的主要内容
		1.request.scheme : 请求协议
		2.request.body : 请求主体
		3.request.path : 请求路径
		4.request.get_full_path() : 请求完整的请求路径
		5.request.get_host() : 请求的主机地址 / 域名
		6.request.method 
		7.request.GET : 封装了get请求方式所提交的数据
		8.request.POST : 封装了post请求方式所提交的数据
		9.request.COOKIES : 封装了 cookies 中的所有数据
		10.request.META : 封装了请求的原数据
			request.META.HTTP_REFERER : 封装了请求的源地址
	3.获取请求提交的数据
		1.get 请求
			1.获取数据
				request.GET['名称']
				request.GET.get('名称')
				request.GET.getlist('名称')
			2.使用get方式提交数据的场合
				1.表单中 method 为get 的时候
				2.地址栏上拼查询字符串的时候
					http://localhost:8000/01-request/?id=1&name=xxx

				注意：
					url(r'^01-request/(\d{4})/(\d{1,})',xxx)
					http://localhost:8000/01-request/2018/10
	
					以上方式提交的数据不能使用request.GET来获取，因为以上的方式是 Django 标准而并非 HTTP 标准
			3.练习：
				http://localhost:8000/02-request/?year=2018&month=11&day=19
				接收请求中的数据并打印在终端上：
				年：2018
				月：11
				日：19
	
		2.post 请求     action 地址后面要加 /  或使用别名访问 {% url 'login' %}
			1.获取数据
				request.POST['名称']
				request.POST.get('名称')
				request.POST.getlist('名称')
	
			2.使用POST方式提交数据的场合
	
				1.使用表单提交时可以使用post


			3.CSRF verification failed (403)
				CSRF : Cross-Site Request Forgery
					    跨   站点   请求    伪装  
				
				解决方案：
					1.取消csrf的验证
						删除 settings.py中 MIDDLEWARE 中的 CsrfViewMiddleware 中间件
					2.在处理函数上增加装饰器
	                    需要导入模块
						@csrf_protect
					3.可以在 表单中的 第一行增加:{% csrf_token %}
					
					4.AJXA post提交数据
					<body>
	
					<script>
							$.ajaxSetup({
									data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
							});
					</script>




引用Django自带登录系统	
	把自定义的用户model类附加在Django自带的登录表上
	mysql> desc auth_user;
	+--------------+--------------+------+-----+---------+----------------+
	| Field              | Type             | Null | Key | Default | Extra          |
	+--------------+--------------+------+-----+---------+----------------+
	| id                   | int(11)          | NO   | PRI | NULL     | auto_increment |
	| password      | varchar(128) | NO   |     | NULL       |                           |
	| last_login      | datetime(6)   | YES  |     | NULL       |                           |	最后登录时间
	| is_superuser | tinyint(1)       | NO   |     | NULL       |              				|	超级用户
	| username     | varchar(150)  | NO   | UNI | NULL   |                			|
	| first_name    | varchar(30)     | NO   |     | NULL      |                			|
	| last_name    | varchar(30)     | NO   |     | NULL      |                			|
	| email            | varchar(254)   | NO   |     | NULL      |                			|	
	| is_staff         | tinyint(1)         | NO   |     | NULL       |                			|	后台管理员
	| is_active       | tinyint(1)        | NO   |     | NULL       |                			|	活跃状态
	| date_joined  | datetime(6)    | NO   |     | NULL      |                			|	登记时间
	+--------------+--------------+------+-----+---------+----------------+




model.py
     from django.contrib.auth.models import AbstractUser

	# Create your models here.
	SEX_CHOICES = (
		('0', '男'),
		('1', '女'),
	)

class UserInfo(AbstractUser):
    cellphone = models.CharField(max_length=11, null=False, verbose_name='手机')
    realname = models.CharField(max_length=50, null=False, verbose_name='姓名')
    uidentity = models.CharField(max_length=18, null=False, verbose_name='身份证')
    address = models.CharField(max_length=150, null=False, verbose_name='地址')
    sex = models.CharField(choices=SEX_CHOICES, default='0', max_length=10, verbose_name='性别')


 settings.py           当使用用户表时 让Django使用自定义的表
	AUTH_USER_MODEL = 'userinfo.Userinfo'
	#app名.类名
	
views.py	
	Django自带的登录验证和登录方法与退出登录方法，自动完成一系列动作(session等。。。)
	from django.contrib import auth
	
	验证用户，存在返回用户对象，失败Flase
	user = auth.authenticate(username=username, password=password)
		authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，
		且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出
		来不经过authenticate()的User对象会报错的！！
		from django.contrib import auth  #导入auth模块
		def login(request):
		'''
	登陆
	:param request:
	:return:
	'''
	if request.method == 'POST':
	    user = request.POST.get('user')
	    pwd = request.POST.get('pwd')
	    user = auth.authenticate(username =user,password=pwd)  #自动给你的user表自动校验
	    if user: #登陆成功
	        auth.login(request,user)  #相当于设置session



    return render(request,'login.html')
    	
    用户登录方法
    auth.login(request, user)


​	
	退出登录方法
	auth.logout(request)


​	
	user对象的 is_authenticated()
			如果是真正的 User 对象，返回值恒为 True 。 用于检查用户是否已经通过了认证。
			通过认证并不意味着用户拥有任何权限，甚至也不检查该用户是否处于激活状态，
			这只是表明用户成功的通过了认证。 这个方法很重要, 在后台用request.user.is_authenticated()
			判断用户是否已经登录，如果true则可以向前台展示request.user.name
	
		要求：
			1  用户登陆后才能访问某些页面，
	
			2  如果用户没有登录就访问该页面的话直接跳到登录页面
	
			3  用户在跳转的登陆界面中完成登陆后，自动访问跳转到之前访问的地址
	
		方法1:
	
			直接用auth的is_authenticated()方法验证
	
			def my_view(request):
				if not request.user.is_authenticated():
						return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
						
		方法2:
			根据request.user.username来验证，如果为空，则说明没有登录
	
			def my_view(request):
				if not request.user.username:
					return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
					
		方法3:
	
			django已经为我们设计好了一个用于此种情况的装饰器：login_requierd()
	
			from django.contrib.auth.decorators import login_required
	
				@login_required
				def my_view(request):
	 
			若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' 
			(这个值可以在settings文件中通过LOGIN_URL进行修改)。并传递  当前访问url的绝对路径 
			( 登陆成功后，会重定向到该路径 )。
			修改 login.html 表单中的 action 参数
# views.py
from djanco.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
@login_required
def index(request):
# settings.py
LOGIN_URL = '/accounts/login/' # 根据你网站的实际登陆地址来设置
如果要使用 django 默认登陆地址，则可以通过在 urls.py 中添加如此配置：
# urls.py
url(r'^accounts/login/', views.login),
# login.html
<div class="container">
<form class="form-signin" action="/accounts/login/" method="post">


	创建用户
	
		使用 create_user 辅助函数创建用户:
		from django.contrib.auth.models import User
		user = User.objects.create_user（username='',password='',email=''）
		user.save()

实例		
def sign_up(request):

  state = None
  if request.method == 'POST':

    password = request.POST.get('password', '')
    repeat_password = request.POST.get('repeat_password', '')
    email=request.POST.get('email', '')
    username = request.POST.get('username', '')
    if User.objects.filter(username=username):
        state = 'user_exist'
    else:
        new_user = User.objects.create_user(username=username, 
    							password=password,		#不用make_password，自动加密
    							email=email)
        new_user.save()
      
        return redirect('/book/')
  content = {
    'state': state,
    'user': None,
  }
  return render(request, 'sign_up.html', content)　		
		
	修改密码
		用户需要修改密码的时候 首先要让他输入原来的密码 ，如果给定的字符串通过了密码检查，返回  True
		user = User.objects.get(username=request.POST.get(username))
		passwd = request.POST.get(password)
		newpasswd = request.POST.get(newpassword)
		if user.check_password(passwd):
			使用 set_password() 来修改密码
			user.set_password(password=newpasswd)
			user.save
		
		实例
		@login_required
		def set_password(request):
		user = request.user
		state = None
		if request.method == 'POST':
			old_password = request.POST.get('old_password', '')
			new_password = request.POST.get('new_password', '')
			repeat_password = request.POST.get('repeat_password', '')
			if user.check_password(old_password):
				if not new_password:
					state = 'empty'
				elif new_password != repeat_password:
					state = 'repeat_error'
				else:
					user.set_password(new_password)
					user.save()
					return redirect("/log_in/")
			else:
				state = 'password_error'
		content = {
				'user': user,
				'state': state,
				}
		return render(request, 'set_password.html', content)


​	
------------------------------------------------------------------------------------
让前端直接访问html页面,页面跳转

总urls.py
	from django.conf.urls import url
	from django.contrib import admin
	from ccode import viewUtil
	
	
	from django.views.generic import TemplateView
	
	urlpatterns = [
		url(r'^admin/', admin.site.urls),
		url(r'verifycode',viewUtil.verifycode),
		url(r'^$',TemplateView.as_view(template_name='code.html'),name="index"),
	]


​    
------------------------------------------------------------------------------------------------------------
Django的密码加密工具 

	from django.contrib.auth.hashers import make_password, check_password
	
	#加密
	auth_check = 'MarcelArhut' #自定义
	new_user.password = make_password(request.POST.get('userpwd'), auth_check, 'pbkdf2_sha1')
	
	#对比(明文，密文),一致返回ture，不一致返回Flase
	check_password(request.POST.get('pwd'),user.password)