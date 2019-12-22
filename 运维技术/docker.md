[TOC]





## 安装Docker

### Ubuntu 16.04

1.选择国内的云服务商，这里选择阿里云为例

```powershell
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
```

2.安装所需要的包

```powershell
sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
```

3.添加使用 HTTPS 传输的软件包以及 CA 证书

```powershell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
```

4.添加GPG密钥

```powershell
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```

5.添加软件源

```powershell
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
```

6.添加成功后更新软件包缓存

```powershell
sudo apt-get update
```

7.安装docker

```powershell
sudo apt-get install docker-engine
```

8.启动 docker

```powershell
sudo systemctl enable docker
sudo systemctl start docker
```



## Docker 配置文件

### /etc/docker/daemon.json

日志驱动类型。

- none：容器不输出任何日志；
- json-file：容器输出的日志以 JSON 格式写入文件中（默认）；
- syslog：容器输出的日志写入宿主机的 Syslog 中；
- journald：容器输出的日志写入宿主机的 Journald 中；
- gelf：容器输出到日志以 GELF（Graylog Extended Log Format）格式写入 Graylog中；
- fluentd：容器输出的日志写入宿主机的 Fluented 中；
- awslogs：容器输出的日志写入 Amazon CloudWatch Logs 中；
- splunk：容器输出的日志写入 splunk 中；
- etwlogs：容器输出的日志写入 ETW （Event Tracing for Windows）；
- mats：容器输出的日志写入 NATS 服务中；

我们可以在 docker run 命令中通过  --log-driver 参数来设置具体的 Docker 日志驱动，也可以通过 --log-opt 参数来指定对应日志驱动的相关选项。就拿 json-file 来说，其实可以这样启动 Docker 容器：

```
docker run \
-d \
-p 80:80 \
--log-driver json-file \
--log-opt max-size=10m \
--log-opt max-file=3 \
--name nginx \
nginx
```

通过 --log-opt 参数为 json-file 日志驱动添加了两个选项，max-size=10m 表示  JSON 文件最大为 10MB（超过 10MB 就会自动生成新文件），max-file=3 表示 JSON 文件最多为3个（超过3个就会自动删除多余的旧文件）
 除了在启动 Docker 容器时，可指定日志驱动以外，还可以通过修改 Docker 配置文件来指定日志驱动。

然后重启 docker

```
systemctl restart docker
```



## 运行容器

### 要使用root权限	docker run*

Docker 允许你在容器内运行应用程序， 使用 **docker run** 命令来在容器内运行一个应用程序。

输出Hello world

```
runoob@runoob:~$ docker run ubuntu:15.10 /bin/echo "Hello world"
Hello world
```

- **docker:** Docker 的二进制执行文件。
- **run:**与前面的 docker 组合来运行一个容器。
- **ubuntu:15.10**指定要运行的镜像，Docker首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
- **/bin/echo "Hello world":** 在启动的容器里执行的命令

以上命令完整的意思可以解释为：Docker 以 ubuntu15.10 镜像创建一个新容器，然后在容器里执行 bin/echo "Hello world"，然后输出结果。



### 运行交互式的容器	docker run -i -t

我们通过docker的两个参数 -i -t，让docker运行的容器实现"对话"的能力

```powershell
runoob@runoob:~$ docker run -i -t ubuntu:15.10 /bin/bash
root@dc0050c79503:/#
```

各个参数解析：

- **-t:**在新容器内指定一个伪终端或终端。
- **-i:**允许你对容器内的标准输入 (STDIN) 进行交互。

此时我们已进入一个 ubuntu15.10系统的容器

我们可以通过运行exit命令或者使用CTRL+D来退出容器。



### -v挂载主机上的文件到容器

Docker容器启动的时候，如果要挂载宿主机的一个目录，可以用-v参数指定。

譬如我要启动一个centos容器，宿主机的/test目录挂载到容器的/soft目录，可通过以下方式指定：

\# docker run -it -v /test:/soft centos /bin/bash

这样在容器启动后，容器内会自动创建/soft的目录。通过这种方式，我们可以明确一点，即-v参数中，冒号":"前面的目录是宿主机目录，后面的目录是容器内目录。

```
-v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf 
-v $PWD/log:/var/log/nginx 
-v $PWD/html:/usr/share/nginx/html
```

**容器目录不可以为相对路径**

**宿主机目录如果不存在，则会自动生成**



### 启动容器（后台模式）docker run -d 

使用以下命令创建一个以进程方式运行的容器

```powershell
runoob@runoob:~$ docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63
```

在输出中，我们没有看到期望的"hello world"，而是一串长字符

**2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63**

这个长字符串叫做容器ID，对每个容器来说都是唯一的，我们可以通过容器ID来查看对应的容器发生了什么。



## 查看容器列表	docker ps

首先，我们需要确认容器有在运行，可以通过 **docker ps** 来查看

```powershell
root@VM-0-17-ubuntu:~# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
5dcca695b320        ubuntu:15.10        "/bin/sh -c 'while..."   4 seconds ago       Up 3 seconds                            objective_hawking

```

**CONTAINER ID:**容器ID

**NAMES:**自动分配的容器名称



## 查看容器运行记录

**docker logs**

#### 在容器内使用docker logs命令，查看容器内的标准输出,参数为  id   或  容器名字

```powershell
runoob@runoob:~$ docker logs 5dcca695b320
runoob@runoob:~$ docker logs objective_hawking
```



## 进入容器

先运行容器

然后使用如下命令进入交互式终端：

```
`docker exec -it mynginx /bin/bash`
```



## 停止容器	docker stop

我们使用 **docker stop** 命令来停止容器:

```powershell
root@VM-0-17-ubuntu:~# docker stop 5dcca695b320
root@VM-0-17-ubuntu:~# docker stop objective_hawking
5dcca695b320
```



## Docker 客户端

docker 客户端非常简单 ,我们可以直接输入 docker 命令来查看到 Docker 客户端的所有命令选项。

```
runoob@runoob:~# docker
```

可以通过命令 **docker command --help** 更深入的了解指定的 Docker 命令使用方法。

```
runoob@runoob:~# docker stats --help
```



### **-P :**将容器内部使用的网络端口映射到我们使用的主机上。

- **-P :**是容器内部端口随机映射到主机的高端口。
- **-p :** 是容器内部端口绑定到指定的主机端口

```
runoob@runoob:~# docker run -d -P training/webapp python app.py
```

```
runoob@runoob:~#  docker ps
CONTAINER ID        IMAGE               COMMAND             ...        PORTS                 
d3d5e39ed9d3        training/webapp     "python app.py"     ...        0.0.0.0:32769->5000/tcp
```

这里多了端口信息。

```
PORTS
0.0.0.0:32769->5000/tcp
```

Docker 开放了 5000 端口（默认 Python Flask 端口）映射到主机端口 32769 上。

我们通过   ip:32769  访问此应用

我们也可以通过 -p 参数来设置不一样的端口：

​	容器内部的 5000 端口映射到我们本地主机的 5000 端口上。

```
runoob@runoob:~$ docker run -d -p 5000:5000 training/webapp python app.py
```

### 使用 **docker port** 可以查看指定 （ID 或者名字）容器的某个确定端口映射到宿主机的端口号。

```powershell
runoob@runoob:~$ docker port bf08b7f2cd89
runoob@runoob:~$ docker port wizardly_chandrasekhar
5000/tcp -> 0.0.0.0:5000
```

我们可以指定容器绑定的网络地址，比如绑定 127.0.0.1。

```
runoob@runoob:~$ docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
95c6ceef88ca3e71eaf303c2833fd6701d8d1b2572b5613b5a932dfdfe8a857c
```

这样我们就可以通过访问 127.0.0.1:5001 来访问容器的 5000 端口。

上面的例子中，默认都是绑定 tcp 端口，如果要绑定 UDP 端口，可以在端口后面加上 **/udp**。

```
runoob@runoob:~$ docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
```



## 查看 WEB 应用程序日志

docker logs [ID或者名字] 可以查看容器内部的标准输出。

```
runoob@runoob:~$ docker logs -f bf08b7f2cd89
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
192.168.239.1 - - [09/May/2016 16:30:37] "GET / HTTP/1.1" 200 -
192.168.239.1 - - [09/May/2016 16:30:37] "GET /favicon.ico HTTP/1.1" 404 -
```

**-f:** 让 **docker logs** 像使用 **tail -f** 一样来输出容器内部的标准输出。

## 检查 WEB 应用程序

使用 **docker inspect** 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

```json
runoob@runoob:~$ docker inspect wizardly_chandrasekhar
[
    {
        "Id": "bf08b7f2cd897b5964943134aa6d373e355c286db9b9885b1f60b6e8f82b2b85",
        "Created": "2018-09-17T01:41:26.174228707Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 23245,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2018-09-17T01:41:26.494185806Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
......
```



## 停止 WEB 应用容器

```
runoob@runoob:~$ docker stop wizardly_chandrasekhar   
wizardly_chandrasekhar
```

------

## 重启WEB应用容器

已经停止的容器，我们可以使用命令 docker start 来启动。

```
runoob@runoob:~$ docker start wizardly_chandrasekhar
wizardly_chandrasekhar
```

docker ps -l 查询最后一次创建的容器：

```
#  docker ps -l 
CONTAINER ID        IMAGE                             PORTS                     NAMES
bf08b7f2cd89        training/webapp     ...        0.0.0.0:5000->5000/tcp    wizardly_chandrasekhar
```

## 正在运行的容器，我们可以使用 docker restart 命令来重启



## 移除WEB应用容器

### 我们可以使用 docker rm 命令来删除不需要的容器

```
runoob@runoob:~$ docker rm wizardly_chandrasekhar  
wizardly_chandrasekhar
```

#### 删除容器时，容器必须是停止状态，否则会报如下错误

```
runoob@runoob:~$ docker rm wizardly_chandrasekhar
Error response from daemon: You cannot remove a running container bf08b7f2cd897b5964943134aa6d373e355c286db9b9885b1f60b6e8f82b2b85. Stop the container before attempting removal or force remove
```



# Docker 镜像使用

当运行容器时，使用的镜像如果在本地中不存在，docker 就会自动从 docker 镜像仓库中下载，默认是从 Docker Hub 公共镜像源下载。

## 列出镜像列表

​	我们可以使用 **docker images** 来列出本地主机上的镜像。

```
runoob@runoob:~$ docker images           
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
php                 5.6                 f40e9e0f10c8        9 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        4 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
training/webapp     latest              6fae60ef3446        11 months ago       348.8 MB
```

各个选项说明:

- **REPOSITORY：**表示镜像的仓库源
- **TAG：**镜像的标签
- **IMAGE ID：**镜像ID
- **CREATED：**镜像创建时间
- **SIZE：**镜像大小

同一仓库源可以有多个 TAG，代表这个仓库源的不同个版本，如ubuntu仓库源里，有15.10、14.04等多个不同的版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。

所以，我们如果要使用版本为15.10的ubuntu系统镜像来运行容器时，命令如下：

```
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash 
root@d77ccb2e5cca:/#
```

如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker 将默认使用 ubuntu:latest 镜像。

## 获取一个新的镜像	docker pull 

当我们在本地主机上使用一个不存在的镜像时 Docker 就会自动下载这个镜像。如果我们想预先下载这个镜像，我们可以使用 docker pull 命令来下载它。

```
runoob@runoob:~# docker pull training/webapp
```

## 查找镜像

我们可以从 Docker Hub 网站来搜索镜像，Docker Hub 网址为： https://hub.docker.com/

我们也可以使用 docker search 命令来搜索镜像。比如我们需要一个httpd的镜像来作为我们的web服务。我们可以通过 docker search 命令搜索 httpd 来寻找适合我们的镜像。

```
root@VM-0-17-ubuntu:~# docker search httpd
NAME                          DESCRIPTION                  		STARS     OFFICIAL   AUTOMATED
httpd                         The Apache HTTP Server Project    2447      [OK]       
hypriot/rpi-busybox-httpd     Raspberry Pi compatible Docker  	46                     [OK]
```

**NAME:**镜像仓库源的名称

**DESCRIPTION:**镜像的描述

**OFFICIAL:**是否docker官方发布



## 创建镜像

当我们从docker镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。

- 1.从已经创建的容器中更新镜像，并且提交这个镜像
- 2.使用 Dockerfile 指令来创建一个新的镜像

### 更新镜像

更新镜像之前，我们需要使用镜像来创建一个容器。

```
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash
root@e218edb10161:/# 
```

在运行的容器内使用 apt-get update 命令进行更新。

```
root@d161f9a55b05:/# apt-get update
```

在完成操作之后，输入 exit命令来退出这个容器。

此时ID为e218edb10161的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit来提交容器副本。

```
runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8
```

各个参数说明：

- **-m:**提交的描述信息
- **-a:**指定镜像作者
- **e218edb10161：**容器ID
- **runoob/ubuntu:v2:**指定要创建的目标镜像名

我们可以使用 **docker images** 命令来查看我们的新镜像 **runoob/ubuntu:v2**：

```
runoob@runoob:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/ubuntu       v2                  70bf1840fd7c        15 seconds ago      158.5 MB
ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
php                 5.6                 f40e9e0f10c8        9 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        4 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
training/webapp     latest              6fae60ef3446        12 months ago       348.8 MB
```

使用我们的新镜像 **runoob/ubuntu** 来启动一个容器

```
runoob@runoob:~$ docker run -t -i runoob/ubuntu:v2 /bin/bash                            
root@1a9fbdeb5da3:/#
```

### 构建镜像

我们使用命令 **docker build** ， 从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。

```
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7
MAINTAINER      Fisher "fisher@sudops.com"

RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd runoob
RUN     /bin/echo 'runoob:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
EXPOSE  22
EXPOSE  80
CMD     /usr/sbin/sshd -D
```

每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。

## Dockerfile的基本结构

Dockerfile 一般分为四部分：基础镜像信息、维护者信息、镜像操作指令和容器启动时执行指令，’#’ 为 Dockerfile 中的注释。

**FROM：指定基础镜像，必须为第一个命令**

```
格式：
　　FROM <image>
　　FROM <image>:<tag>
　　FROM <image>@<digest>
示例：
　　FROM mysql:5.6
注：
　　tag或digest是可选的，如果不使用这两个值时，会使用latest版本的基础镜像
```

**MAINTAINER: 维护者信息**

```
格式：
    MAINTAINER <name>
示例：
    MAINTAINER Jasper Xu
    MAINTAINER sorex@163.com
    MAINTAINER Jasper Xu <sorex@163.com>
```

#### RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。

```
RUN用于在镜像容器中执行命令，其有以下两种命令执行方式：
shell执行
格式：
    RUN <command>
exec执行
格式：
    RUN ["executable", "param1", "param2"]
示例：
    RUN ["executable", "param1", "param2"]
    RUN apk update
    RUN ["/etc/execfile", "arg1", "arg1"]
注：
　　RUN指令创建的中间镜像会被缓存，并会在下次构建中使用。如果不想使用这些缓存镜像，可以在构建时指定--no-cache参数，如：docker build --no-cache
```

**ADD：将本地文件添加到容器中，tar类型文件会自动解压(网络压缩资源不会被解压)，可以访问网络资源，类似wget**

```
格式：
    ADD <src>... <dest>
    ADD ["<src>",... "<dest>"] 用于支持包含空格的路径
示例：
    ADD hom* /mydir/          # 添加所有以"hom"开头的文件
    ADD hom?.txt /mydir/      # ? 替代一个单字符,例如："home.txt"
    ADD test relativeDir/     # 添加 "test" 到 `WORKDIR`/relativeDir/
    ADD test /absoluteDir/    # 添加 "test" 到 /absoluteDir/
```

**COPY：功能类似ADD，但是是不会自动解压文件，也不能访问网络资源**

**CMD：构建容器后调用，也就是在容器启动时才进行调用。**

```
格式：
    CMD ["executable","param1","param2"] (执行可执行文件，优先)
    CMD ["param1","param2"] (设置了ENTRYPOINT，则直接调用ENTRYPOINT添加参数)
    CMD command param1 param2 (执行shell内部命令)
示例：
    CMD echo "This is a test." | wc -
    CMD ["/usr/bin/wc","--help"]
注：
 　　CMD不同于RUN，CMD用于指定在容器启动时所要执行的命令，而RUN用于指定镜像构建时所要执行的命令。
```

**ENTRYPOINT：配置容器，使其可执行化。配合CMD可省去"application"，只使用参数。**

```
格式：
    ENTRYPOINT ["executable", "param1", "param2"] (可执行文件, 优先)
    ENTRYPOINT command param1 param2 (shell内部命令)
示例：
    FROM ubuntu
    ENTRYPOINT ["top", "-b"]
    CMD ["-c"]
注：
　　　ENTRYPOINT与CMD非常类似，不同的是通过docker run执行的命令不会覆盖ENTRYPOINT，而docker run命令中指定的任何参数，都会被当做参数再次传递给ENTRYPOINT。Dockerfile中只允许有一个ENTRYPOINT命令，多指定时会覆盖前面的设置，而只执行最后的ENTRYPOINT指令。
```

**LABEL：用于为镜像添加元数据**

```
格式：
    LABEL <key>=<value> <key>=<value> <key>=<value> ...
示例：
　　LABEL version="1.0" description="这是一个Web服务器" by="IT笔录"
注：
　　使用LABEL指定元数据时，一条LABEL指定可以指定一或多条元数据，指定多条元数据时不同元数据之间通过空格分隔。推荐将所有的元数据通过一条LABEL指令指定，以免生成过多的中间镜像。
```

**ENV：设置环境变量**

```
格式：
    ENV <key> <value>  #<key>之后的所有内容均会被视为其<value>的组成部分，因此，一次只能设置一个变量
    ENV <key>=<value> ...  #可以设置多个变量，每个变量为一个"<key>=<value>"的键值对，如果<key>中包含空格，可以使用\来进行转义，也可以通过""来进行标示；另外，反斜线也可以用于续行
示例：
    ENV myName John Doe
    ENV myDog Rex The Dog
    ENV myCat=fluffy
```

**EXPOSE：指定于外界交互的端口**

```
格式：
    EXPOSE <port> [<port>...]
示例：
    EXPOSE 80 443
    EXPOSE 8080
    EXPOSE 11211/tcp 11211/udp
注：
　　EXPOSE并不会让容器的端口访问到主机。要使其可访问，需要在docker run运行容器时通过-p来发布这些端口，或通过-P参数来发布EXPOSE导出的所有端口
```

**VOLUME：用于指定持久化目录**

```
格式：
    VOLUME ["/path/to/dir"]
示例：
    VOLUME ["/data"]
    VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"
注：
　　一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能：
1 卷可以容器间共享和重用
2 容器并不一定要和其它容器共享卷
3 修改卷后会立即生效
4 对卷的修改不会对镜像产生影响
5 卷会一直存在，直到没有任何容器在使用它
```

**WORKDIR：工作目录，类似于cd命令**

```
格式：
    WORKDIR /path/to/workdir
示例：
    WORKDIR /a  (这时工作目录为/a)
    WORKDIR b  (这时工作目录为/a/b)
    WORKDIR c  (这时工作目录为/a/b/c)
注：
　　通过WORKDIR设置工作目录后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY等命令都会在该目录下执行。在使用docker run运行容器时，可以通过-w参数覆盖构建时所设置的工作目录。
```

**USER:****指定运行容器时的用户名或 UID，后续的 RUN 也会使用指定用户。使用USER指定用户时，可以使用用户名、UID或GID，或是两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所需要的用户**

 格式:
　　USER user
　　USER user:group
　　USER uid
　　USER uid:gid
　　USER user:gid
　　USER uid:group

 示例：
　　USER www

 注：

　　使用USER指定用户后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT都将使用该用户。镜像构建完成后，通过`docker run`运行容器时，可以通过-u参数来覆盖所指定的用户。

**ARG：用于指定传递给构建运行时的变量**

```
格式：
    ARG <name>[=<default value>]
示例：
    ARG site
    ARG build_user=www
```

**ONBUILD：用于设置镜像触发器**

```
格式：
　　ONBUILD [INSTRUCTION]
示例：
　　ONBUILD ADD . /app/src
　　ONBUILD RUN /usr/local/bin/python-build --dir /app/src
注：
　　当所构建的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被钥触发
```

**以下是一个小例子：**

```
# This my first nginx Dockerfile
# Version 1.0

# Base images 基础镜像
FROM centos

#MAINTAINER 维护者信息
MAINTAINER tianfeiyu 

#ENV 设置环境变量
ENV PATH /usr/local/nginx/sbin:$PATH

#ADD  文件放在当前目录下，拷过去会自动解压
ADD nginx-1.8.0.tar.gz /usr/local/  
ADD epel-release-latest-7.noarch.rpm /usr/local/  

#RUN 执行以下命令 
RUN rpm -ivh /usr/local/epel-release-latest-7.noarch.rpm
RUN yum install -y wget lftp gcc gcc-c++ make openssl-devel pcre-devel pcre && yum clean all
RUN useradd -s /sbin/nologin -M www

#WORKDIR 相当于cd
WORKDIR /usr/local/nginx-1.8.0 

RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre && make && make install

RUN echo "daemon off;" >> /etc/nginx.conf

#EXPOSE 映射端口
EXPOSE 80

#CMD 运行以下命令
CMD ["nginx"]
```

### 然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。

```
runoob@runoob:~$ docker build -t runoob/centos:6.7 .
Sending build context to Docker daemon 17.92 kB
Step 1 : FROM centos:6.7
 ---&gt; d95b5ca17cc3
Step 2 : MAINTAINER Fisher "fisher@sudops.com"
 ---&gt; Using cache
 ---&gt; 0c92299c6f03
Step 3 : RUN /bin/echo 'root:123456' |chpasswd
 ---&gt; Using cache
 ---&gt; 0397ce2fbd0a
Step 4 : RUN useradd runoob
......
```

参数说明：

- **-t** ：指定要创建的目标镜像名
- **.** ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径

我们可以使用新的镜像来创建容器

```
runoob@runoob:~$ docker run -t -i runoob/centos:6.7  /bin/bash
[root@41c28d18b5fb /]# id runoob
uid=500(runoob) gid=500(runoob) groups=500(runoob)
```

## 设置镜像标签

我们可以使用 docker tag 命令，为镜像添加一个新的标签。

```
runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev
```

docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。

## 删除指定的镜像

通过sudo docker rmi xxx 来删除指定的镜像，镜像存在依赖关系，先删除最下层，最后删除顶层，建议根据镜像名字来删除

## 修改镜像

pull到的镜像肯定有很多需要修改的地方，比如配置文件等或者要自己增加些什么玩意儿进去

```
runoob@runoob:~$ docker exec -it 54d26bbce3d6 /bin/bash
```

通过exec命令进入到容器内部进行操作， 其中红色部分可以是容器id或容器名字

进入之后就和操作新的系统一样，操作完成之后输入exit退出

## 保存修改的镜像到本地镜像库

```
runoob@runoob:~$ docker commit nginx_xiao xiaochangwei/nginx:v1.0
```



# Docker 容器连接

端口映射并不是唯一把 docker 连接到另一个容器的方法。

docker 有一个连接系统允许将多个容器连接在一起，共享连接信息。

docker 连接会创建一个父子关系，其中父容器可以看到子容器的信息。

### 容器命名

当我们创建一个容器的时候，docker 会自动对它进行命名。另外，我们也可以使用 **--name** 标识来命名容器，例如：

```
runoob@runoob:~$  docker run -d -P --name runoob training/webapp python app.py
```



## **搭建自己的Dockers Registry**

利用Docker容器安装一个Registry十分简单，只需要运行对应的容器即可。

docker run -d -p 5000:5000 registry

此时，我们已经启动了一个本地的registry。下面，我们需要使用本地的registry为我们想要推送的镜像打好标签。

docker tag 镜像id 127.0.0.1:5000/wangzhe0912/nginx

然后直接直接docker push命令来推送即可。

docker push 127.0.0.1:5000/wangzhe0912/nginx

Docker从1.3.X之后，与docker registry交互默认使用的是https，然而此处搭建的私有仓库只提供http服务，所以当与私有仓库交互式就会有上面的错误。

解决办法:

编辑/etc/docker/daemon.json   加入

```
"insecure-registries":["192.168.121.143:5000"] 
```

最后/etc/docker/daemon.json文件内容如下:

```
{"registry-mirrors":["http://hub-mirror.c.163.com"],"insecure-registries":["192.168.121.143:5000"] }
```

其中registry-mirrors是我加的docker镜像源。

编辑完成后，重启docker。

```
# systemctl restart docker
```

**但这种方法比较麻烦，需要修改每台宿主机上的/etc/docker/daemon.json**  



sudo docker run -d -p 5000:5000 --name registry-ser --restart=always --privileged=true  -v /docker/registry:/var/lib/registry  registry

启动镜像服务器
–restart=always 表示自动启动容器 
-v <宿主机目录>:<容器目录> 将宿主机的目录映射到容器上 
–privileged=true 给容器加权限，这样上传就不会因为目录权限出错 

# docker镜像导入导出

save指令导出镜像

```javascript
sudo docker save image > image.tar 
```

load指令导入镜像

```
sudo docker load < image.tar 
```