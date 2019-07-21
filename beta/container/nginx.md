[TOC]



## 安装

### ubuntu

​	`sudo apt-get install nginx`

​	启动
​	`sudo /etc/init.d/nginx restart`

## 配置文件

#### 主配置文件	/etc/nginx/nginx.conf 

```powershell
root@ad0f4bd3acab:/# cat /etc/nginx/nginx.conf 
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';

access_log  /var/log/nginx/access.log  main;

sendfile        on;
#tcp_nopush     on;

keepalive_timeout  65;

#gzip  on;

include /etc/nginx/conf.d/*.conf;
}
```
#### 局域配置文件		/etc/nginx/conf.d/default.conf 

```powershell
root@ad0f4bd3acab:/etc/nginx/conf.d# cat default.conf 
server {
    listen       80;
    server_name  localhost;
	#charset koi8-r;
	#access_log  /var/log/nginx/host.access.log  main;

	location / {
    	root   /usr/share/nginx/html;
    	index  index.html index.htm;
	}

	#error_page  404              /404.html;

	# redirect server error pages to the static page /50x.html
	#
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
    	root   /usr/share/nginx/html;
	}

	# proxy the PHP scripts to Apache listening on 127.0.0.1:80
	#
	#location ~ \.php$ {
	#    proxy_pass   http://127.0.0.1;
	#}

	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	#
	#location ~ \.php$ {
	#    root           html;
	#    fastcgi_pass   127.0.0.1:9000;
	#    fastcgi_index  index.php;
	#    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
	#    include        fastcgi_params;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#    deny  all;
	#}
}
```
- 1、**全局块**：配置影响nginx全局的指令。一般有运行nginx服务器的用户组，nginx进程pid存放路径，日志存放路径，配置文件引入，允许生成worker process数等。
- 2、**events块**：配置影响nginx服务器或与用户的网络连接。有每个进程的最大连接数，选取哪种事件驱动模型处理连接请求，是否允许同时接受多个网路连接，开启多个网络连接序列化等。
- 3、**http块**：可以嵌套多个server，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置。如文件引入，mime-type定义，日志自定义，是否使用sendfile传输文件，连接超时时间，单连接请求数等。
- 4、**server块**：配置虚拟主机的相关参数，一个http中可以有多个server。
- 5、**location块**：配置请求的路由，以及各种页面的处理情况。

#### 配置文件详解

```powershell
########### 每个指令必须有分号结束。#################
#user administrator administrators;  #配置用户或者组，默认为nobody nobody。
#worker_processes 2;  #允许生成的进程数，默认为1
#pid /nginx/pid/nginx.pid;   #指定nginx进程运行文件存放地址
error_log log/error.log debug;  #制定日志路径，级别。这个设置可以放入全局块，http块，server块，级别以此为：debug|info|notice|warn|error|crit|alert|emerg
events {
    accept_mutex on;   #设置网路连接序列化，防止惊群现象发生，默认为on
    multi_accept on;  #设置一个进程是否同时接受多个网络连接，默认为off
    #use epoll;      #事件驱动模型，select|poll|kqueue|epoll|resig|/dev/poll|eventport
    worker_connections  1024;    #最大连接数，默认为512
}
http {
    include       mime.types;   #文件扩展名与文件类型映射表
    default_type  application/octet-stream; #默认文件类型，默认为text/plain
    #access_log off; #取消服务日志    
    log_format myFormat '$remote_addr–$remote_user [$time_local] $request $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for'; #自定义格式
    access_log log/access.log myFormat;  #combined为日志格式的默认值
    sendfile on;   #允许sendfile方式传输文件，默认为off，可以在http块，server块，location块。
    sendfile_max_chunk 100k;  #每个进程每次调用传输数量不能大于设定的值，默认为0，即不设上限。
    keepalive_timeout 65;  #连接超时时间，默认为75s，可以在http，server，location块。

    upstream mysvr {   
      server 127.0.0.1:7878;
      server 192.168.10.121:3333 backup;  #热备
    }
    error_page 404 https://www.baidu.com; #错误页
    server {
        keepalive_requests 120; #单连接请求上限次数。
        listen       4545;   #监听端口
        server_name  127.0.0.1;   #监听地址       
        location  ~*^.+$ {       #请求的url过滤，正则匹配，~为区分大小写，~*为不区分大小写。
           #root path;  #根目录
           #index vv.txt;  #设置默认页
           proxy_pass  http://mysvr;  #请求转向mysvr 定义的服务器列表
           deny 127.0.0.1;  #拒绝的ip
           allow 172.18.5.54; #允许的ip           
        } 
    }
}
```

上面是nginx的基本配置，需要注意的有以下几点：

1、几个常见配置项：

- 1.\$remote_addr 与 $http_x_forwarded_for 用以记录客户端的ip地址；
- 2.$remote_user ：用来记录客户端用户名称；
- 3.$time_local ： 用来记录访问时间与时区；
- 4.$request ： 用来记录请求的url与http协议；
- 5.$status ： 用来记录请求状态；成功是200；
- 6.$body_bytes_s ent ：记录发送给客户端文件主体内容大小；
- 7.$http_referer ：用来记录从那个页面链接访问过来的；
- 8.$http_user_agent ：记录客户端浏览器的相关信息；

2、惊群现象：一个网路连接到来，多个睡眠的进程被同事叫醒，但只有一个进程能获得链接，这样会影响系统性能。

3、每个指令必须有分号结束。

## 日志地址

### 日志地址

​	**/var/log/nginx/**
​	**access.log  error.log**

### 日志配置

#### 全局配置

error_log  /var/log/nginx/error.log warn;	错误

access_log  /var/log/nginx/access.log  main; 访问

#### 局部配置

server {
	#access_log  /var/log/nginx/host.access.log  main;	

}

#制定日志路径，级别。这个设置可以放入全局块，http块，server块，级别以此为：debug|info|notice|warn|error|crit|alert|emerg



## Nginx多服务结构

**通过不同的子域名来访问不同的服务**

访问www.yanhuazidi.xyz  one.yanhuazidi.xyz  two.yanhuazidi.xyz 会进入不同的服务器

```nginx
server {
    listen       80;
    server_name  www.yanhuazidi.xyz;
	location / {
    	root   /usr/share/nginx/html;
    	index  index1.html index.htm;
		}
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
    	root   /usr/share/nginx/html;
	}
}
server {
    listen       80;
    server_name  one.yanhuazidi.xyz;
	location / {
    	root   /usr/share/nginx/html;
    	index  index1.html index.htm;
		}
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
    	root   /usr/share/nginx/html;
	}
}
server {
    listen       80;
    server_name  two.yanhuazidi.xyz;
	location / {
    	root   /usr/share/nginx/html;
    	index  index1.html index.htm;
		}
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
    	root   /usr/share/nginx/html;
	}
}
```



## Nginx 负载均衡详解

**upstream**

首先给大家说下upstream这个配置的，这个配置是写一组被代理的服务器地址，然后配置负载均衡的算法。这里的被代理服务器地址有2中写法。

```nginx
upstream myserver { 
    server 192.168.10.121:3333;
    server 192.168.10.122:3333;
}
server {
    ....
    location  ~*^.+$ {         
        proxy_pass  http://mysvr;  #请求转向mysvr 定义的服务器列表         
    }
}
```



### 1、热备

如果你有2台服务器，当一台服务器发生事故时，才启用第二台服务器给提供服务。服务器处理请求的顺序：AAAAAA突然A挂啦，BBBBBBBBBBBBBB.....

```nginx
upstream mysvr { 
    server 127.0.0.1:7878; 
    server 192.168.10.121:3333 backup;  #热备     
}
```

### 2、轮询

nginx默认就是轮询其权重都默认为1，服务器处理请求的顺序：ABABABABAB.... 

轮询是upstream的默认分配方式，即每个请求按照时间顺序轮流分配到不同的后端服务器，
            如果某个后端服务器down掉后，能自动剔除

```nginx
upstream mysvr { 
    server 127.0.0.1:7878;
    server 192.168.10.121:3333;       
}
```

### 3、加权轮询

轮询的加强版，即可以指定轮询比率，weight和访问几率成正比，主要应用于后端服务器异质的场景下。

```nginx
upstream mysvr { 
    server 127.0.0.1:7878 weight=1;
    server 192.168.10.121:3333 weight=2;
}
```

### 4、ip_hash

nginx会让相同的客户端ip请求相同的服务器。  可以解决session一致问题。

```nginx
upstream mysvr { 
    server 127.0.0.1:7878; 
    server 192.168.10.121:3333;
    ip_hash;
}
```

### 5、fair

 顾名思义，公平地按照后端服务器的响应时间（rt）来分配请求，响应时间短即rt小的后端服务器优先分配请求。

```nginx
 upstream backend {
            server 192.168.1.101;
            server 192.168.1.102;
            server 192.168.1.103;
             fair;
        }
```
### 6、url_hash
与ip_hash类似，但是按照访问url的hash结果来分配请求，使得每个url定向到同一个后端服务器，主要应用于后端服务器为缓存时的场景下。

```nginx
  upstream backend {
            server 192.168.1.101;
            server 192.168.1.102;
            server 192.168.1.103;
             hash $request_uri;
             hash_method crc32;
        }
```

 	其中，hash_method为使用的hash算法，需要注意的是：此时，server语句中不能加weight等参数。

**关于nginx负载均衡配置的几个状态参数讲解。**

- down，表示当前的server暂时不参与负载均衡。
- backup，预留的备份机器。当其他所有的非backup机器出现故障或者忙的时候，才会请求backup机器，因此这台机器的压力最轻。
- max_fails，允许请求失败的次数，默认为1。当超过最大次数时，返回proxy_next_upstream 模块定义的错误。
- fail_timeout，在经历了max_fails次失败后，暂停服务的时间。max_fails可以和fail_timeout一起使用。

```nginx
upstream mysvr { 
    server 127.0.0.1:7878 weight=2 max_fails=2 fail_timeout=2;
    server 192.168.10.121:3333 weight=1 max_fails=2 fail_timeout=1;    
}
```

到这里应该可以说nginx的内置负载均衡算法已经没有货啦。如果你像跟多更深入的了解nginx的负载均衡算法，nginx官方提供一些插件大家可以了解下。

> 原文地址：https://www.cnblogs.com/knowledgesea/p/5199046.html



## 反向代理多个服务器(域名级)

```nginx
server one{ 
  listen  9922; 
  server_name firstProxyServer; 
  location / { 
   proxy_pass http://localhost:8989; 
  } 
  error_page 500 502 503 504 /50x.html; 
  location = /50x.html { 
   root html; 
  } 
 } 
 
  server two{ 
  listen  9977; 
  server_name secondProxyServer; 
  location / { 
   proxy_pass http://localhost:8080; 
  } 
  error_page 500 502 503 504 /50x.html; 
  location = /50x.html { 
   root html; 
  } 
 } 
```

开启被代理服务器监听8989端口,开启nginx服务器监听9922端口，通过9922访问nginx等于访问8989端口服务器

被代理服务器 为 tomcet或。。。



## 反向代理多个服务器(路由级)

**同一服务器上部署多个不同的web应用**

举个例子：假如 www.aabbccdd.com 站点有好几个web  App（web应用）: finance（金融）、product（产品）、admin（用户中心）。

访问这些应用的方式通过上下文(context)来进行区分:

www.aabbccdd.com/finance/

www.aabbccdd.com/product/

www.aabbccdd.com/admin/

```nginx
server {
   #监听80端口，80端口是知名端口号，用于HTTP协议
   listen       80;
         
    #定义使用www.xx.com访问
    server_name  www.aabbccdd.com;
    
    #首页
    index index.jsp
    
    #指向webapp的目录
    root C:/XMCARES_X/WorkSpace/nginx/src/main/webapp;
    
    #编码格式
    charset utf-8;
    
    #代理配置参数
    proxy_connect_timeout 180;
    proxy_send_timeout 180;
    proxy_read_timeout 180;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarder-For $remote_addr;
    #默认指向product的server
    location / {
        proxy_pass http://product_server;
    }
 
	#使用location对不同请求做相应处理
    location /product/{
        proxy_pass http://product_server;
    }
 
    location /admin/ {
        proxy_pass http://admin_server;
    }
    
    location /finance/ {
        proxy_pass http://finance_server;
    }
}
```





## 反向代理与负载均衡组合

debugo01和debugo02作为两台负载均衡服务器，debugo03和debugo04作为两台web server。下面打开配置文件

```nginx
vim nginx.conf
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    keepalive_timeout  65;
    include upstream.conf;
}

vim upstream.conf
upstream debugo_servers {
	server debugo03:80 weight=5;
	server debugo04:80 weight=10;
}
server {
	listen debugo01:80;
	location / {
		proxy_pass http://debugo_servers;
	}
}

测试如下，验证了轮询算法+权重的有效性。可以根据机器性能和模板设置不同的权重。

root@debugo01 ~]# curl debugo01
debugo04
[root@debugo01 ~]# curl debugo01
debugo03
[root@debugo01 ~]# curl debugo01
debugo04
[root@debugo01 ~]# curl debugo01
debugo04
[root@debugo01 ~]# curl debugo01
debugo03
[root@debugo01 ~]# curl debugo01
debugo04
[root@debugo01 ~]# curl debugo01
debugo04
[root@debugo01 ~]# curl debugo01
debugo03
```


