

[TOC]



## Ubuntu 安装 PostgreSQL

```shell
sudo apt-get install postgresql postgresql-client postgresql-contrib
```

### 配置文件的位置为：

```shell
/etc/postgresql/10/main/
```

### 可执行程序为：

```shell
sudo /etc/init.d/postgresql {start|stop|restart|reload|force-reload|status}  
```

### 配置用户

PostgreSQL 默认配置了允许本地机器访问（local access）的权限，PostgreSQL 安装完毕，使用系统账户postgres以postgres角色登录数据库设置密码，命令：

```shell
sudo -u postgres psql
```

登录sql命令界面后，修改 postgres 用户的密码（psql-PostgresQL的命令行客户端）：

```sql
postgres=# ALTER ROLE postgres WITH ENCRYPTED PASSWORD 'mypassword';
postgres=# \q
Ctrl d退出
```

### 设置PostgreSQL启用远程访问

1. 这里设置允许远程连接权限：

   ```shell
   sudo vi /etc/postgresql/10/main/postgresql.conf
   #listen_addresses = 'localhost' 去掉注释并修改为 listen_addresses = '*'
   #password_encryption = on 去掉注释：password_encryption = on
   ```

2. 这里设置允许远程进行数据库操作：

  ```shell
  sudo vi /etc/postgresql/10/main/pg_hba.conf
  #最后添加一行（允许局域网ip段或其他任何ip）：host all all 192.168.1.0/24 md5 其中24是CIDR地址，也可用网关代替。
  ```
  
  ——————–最后pg_hba.conf可能为这样———————
  
  ```python
  # Database administrative login by UNIX sockets
  local all postgres ident
  # TYPE DATABASE USER CIDR-ADDRESS METHOD
  # “local” is for Unix domain socket connections only
  local all all ident
  # IPv4 local connections:
  host all all 127.0.0.1/32 md5
  # IPv6 local connections:
  host all all ::1/128 md5
  host all all 192.168.1.0/24 md5
  ```
  
  

### PostgreSQL创建用户和数据库

登录后使用sql语句：

```sql
postgres=# create user 'pytu' with password 'mypassword' nocreatedb;

postgres=# CREATE DATABASE pytb OWNER pytu ENCODING 'UTF-8';
```

或命令行使用命令创建：

```shell
sudo -u postgres createuser -D -P dbuser 弹出设置密码
sudo -u postgres createdb -O dbuser mydb
```



**最后经过上面的配置记得重启：sudo /etc/init.d/postgresql restart**



### 安装Python 的 PostgreSQL数据库驱动psycopg2

**python2 安装**

```shell
sudo apt-get install python-psycopg2
```

**python3 安装**

```shell
pip3 install psycopg2-binary
```



## pgAdmin远程连接

创建服务器，填入对应的信息即可



