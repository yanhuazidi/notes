[TOC]





## 数据库管理

### 创建数据库

**命令行使用命令创建：**

```shell
postgres@yanhuazidi:~$ createdb mydb #默认数据库所属当前用户
postgres@yanhuazidi:~$ createdb -O dbuser mydb #设置数据库所属用户
```

createdb 是一个 SQL 命令 CREATE DATABASE 的封装

#### createdb 命令语法格式如下：

```
createdb [option...] [dbname [description]]
```

**参数说明：**

**dbname**：要创建的数据库名。

**description**：关于新创建的数据库相关的说明。

**options**：参数可选项，可以是以下值：

- **-D tablespace **   指定数据库默认表空间
- **-e ** 将 createdb 生成的命令发送到服务端
- **-E encoding **  指定数据库的编码
- **-l locale **   指定数据库的语言环境
- **-T template**     指定创建此数据库的模板
- **-h host**    指定服务器的主机名
- **-p port **    指定服务器监听的端口，或者 socket 文件
- **-U username**     连接数据库的用户名
- **-w**        忽略输入密码
- **-W**          连接时强制要求输入密码
- **--help**     显示 createdb 命令的帮助信息



**登录后使用sql语句：**

```sql
postgres@yanhuazidi:~$ psql
postgres=# CREATE DATABASE dbname;
postgres=# CREATE DATABASE pytb OWNER pytu ENCODING 'UTF-8';
```

