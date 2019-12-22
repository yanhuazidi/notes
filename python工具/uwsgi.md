[TOC]



## uWSGI的安装与配置





### 使用pip3安装 uwsgi

```
pip3 install uwsgi
```



### 配置uwsgi

首先要明确的是，如果你喜欢用命令行的方式（如shell）敲命令，那可以省去任何配置。

但是，绝大多数人，还是不愿意记那么长的命令，反复敲的。所以uwsgi里，就给大家提供了多种配置，省去你启动时候，需要敲一长串命令的过程。

uwsgi 有多种配置可用：

1，**ini** ，

2，**xml** ，

3，**json**

4，**yaml**。



#### 推荐用ini方式，下面的配置都是基于ini的

**ini 格式说明：**

1，ini配置为 key=value 形式

2，在ini配置文件里，#号为注释，

3，布尔值为 true 和 false 

4，在命令行里，uwsgi myconf.ini 等价于 uwsgi --ini myconf.ini 

**ini 配置示例：**

```python
[uwsgi]
socket = 127.0.0.1:8000
workers = 4
```

**uwsgi 选项说明：**

**● 选项的格式：**

1，命令行参数格式：--<option> 

2，配置格式（以ini为例）：option = xxxx 



**● 常用选项：**

**socket** ： 地址和端口号，例如：socket = 127.0.0.1:50000

**processes** ： 开启的进程数量

**workers** ： 开启的进程数量，等同于processes（官网的说法是spawn the specified number of  **workers / processes**）

**chdir** ： 指定运行目录（chdir to specified directory before apps loading）

**wsgi-file** ： 载入wsgi-file（load .wsgi file）

**stats** ： 在指定的地址上，开启状态服务（enable the stats server on the specified address）

**threads** ： 运行线程。由于GIL的存在，我觉得这个真心没啥用。（run each worker in prethreaded mode with the specified number of threads）

**master** ： 允许主进程存在（enable master process）

**daemonize** ： 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。

**log-maxsize ：**以固定的文件大小（单位KB），切割日志文件。 例如：log-maxsize = 50000000  就是50M一个日志文件。 

**pidfile** ： 指定pid文件的位置，记录主进程的pid号。

**vacuum** ： 当服务器退出的时候自动清理环境，删除unix socket文件和pid文件（try to remove all of the generated file/sockets）

**disable-logging** ： 不记录请求信息的日志。只记录错误以及uWSGI内部消息到日志中。如果不开启这项，那么你的日志中会大量出现这种记录：

[pid: 347|app: 0|req: 106/367] 117.116.122.172 () {52 vars in 961 bytes} [Thu Jul  7 19:20:56 2016] POST /post => generated 65 bytes in 6 msecs (HTTP/1.1 200) 2 headers in 88 bytes (1 switches on core 0)



**其他选项说明：**

其他选项，具体可以通过 --help 选项来查看：

uwsgi --help



### 常规的配置：

[uwsgi]
socket = 127.0.0.1:50000
chdir = /home/httpServer/
wsgi-file = httpServer/wsgi.py
processes = 4
stats = 127.0.0.1:9090
daemonize = /home/log/httpServer.log
pidfile = /tmp/uwsgi.pid
vacuum = true

log-maxsize = 50000000

disable-logging = true



## Linux 上的 Django+uwsgi+nginx部署

### 部署环境准备

  1. 确保Django项目能够运行
2. 安装nginx
     sudo apt-get install nginx
3. 启动
     sudo /etc/init.d/nginx restart
4. 验证
     打开浏览器输入: 127.0.0.1:80 -> Welcome to Nginx
5. 安装uwsgi
     sudo pip3 install uwsgi
6. 验证
     uwsgi --http :9000 --chdir /home/tarena/myproject/fruitday/ --module fruitday.wsgi



### 配置uwsgi(配置文件)

和nginx通信端口 自身启动占用的端口

1. 在项目目录(manager.py所在路径)中新建uwsgi启动文件:fruitdayUwsgi.ini
2. 在配置文件中写入如下内容:

```ini
[uwsgi]
#指定和nginx通信的端口
socket=127.0.0.1:8001
#项目路径
chdir=/home/tarena/myproject/fruitday
#wsgi.py路径
wsgi-file=fruitday/wsgi.py
#进程数
processes=4
#线程数
thread=2
#uwsgi自身占用端口
stats=127.0.0.1:8080
```



### 配置nginx(配置文件)

1. sudo -i 

2. cd /etc/nginx/sites-enabled/

3. vi projectNginx.conf

     ```nginx
     server{
     #指定本项目监听端口,浏览器输入端口
         listen 80;
     #域名
         server_name www.rabbit.com;
     #指定字符集
         charset utf-8;
     # 指定收集静态文件路径
         location /static{
             alias /home/tarena/myproject/fruitday/static;
        }
     #和uwsgi通信端口和通信文件
          location /{
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8001;
        }
     }
     ```



### 配置项目

1. 拷贝uwsgi_params到项目根目录
2. sudo -i
3. cd /etc/nginx
4. cp uwsgi_params /home/tarena/myproject/fruitday
5. 改掉nginx默认的server(80)
6. sudo -i 
7. cd /etc/nginx/sites-enabled
8. vi default #把listen的端口由80改为800

```nginx
server {
  listen 800 default_server;
  listen [::]:80 default_server;
        
```
**重启nginx服务**
	sudo /etc/init.d/nginx restart



### 收集静态文件

1. 在settings.py文件中添加路径(STATIC_ROOT)
   STATIC_ROOT = '/home/tarena/myproject/fruitday/static'
2. cd /home/tarena/myproject/fruitday
3. python3 manage.py collectstatic
   如果原项目的静态文件是:'/home/tarena/myproject/fruitday/static'
     且只有这个静态文件夹就不用收集了



### 添加本地DNS解析

1. sudo -i 

2. vi /etc/hosts
         127.0.0.1    www.rabbit.com

3. 重启网络服务
         sudo /etc/init.d/networking restart

         5. uwsgi启动项目

4. 切换到项目目录
         cd /home/tarena/myproject/fruitday 

5. 利用uwsgi启动项目
         uwsgi --ini fruitdayUwsgi.ini 



### 验证

打开浏览器,输入 www.rabbit.com

直接进入项目主页

