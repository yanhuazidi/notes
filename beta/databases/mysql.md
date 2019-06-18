[TOC]



## 安装和配置

### Ubuntu 安装MySQL 服务

#### 安装服务端

```powershell
sudo apt_get install mysql_server
```

#### 安装客户端

```powershell
sudo apt_get install mysql_client
```
### MySQL   数据存放地址

1.   是基于硬盘的
2.   所有数据都是以文件形式存放在数据库目录下
3.   数据库目录: **/var/lib/mysql**

### 配置文件地址

​	**/etc/mysql/mysql.conf.d/mysqld.cnf**

#### 更改库的默认字符集

1. cd /etc/mysql/mysql.conf.d

2. vi mysqld.cnf

3. 第36行后加：character_set_server = utf8

4. 重启mysql服务

   ​	**/etc/init.d/mysql restart**

5. 验证

#### 开启远程连接

1. sudo -i
2. cd /etc/mysql/mysql.conf.d/
3. vi mysqld.cnf
4. 第四十三行 bind-address = 1.27.0.0.1    加#
5. /etc/init.d/mysql restart

## MYSQL服务

### 服务端运行命令

```
sudo /etc/init.d/mysql start
sudo /etc/init.d/mysql status(状态)| stop(停止服务)| restart(重启服务)|reload(重新加载配置文件)
```

```powershell
windows
		net start mysql
```



#### 检查MySQL服务器是否启动

```
ps -ef | grep mysqld
```

### 客户端连接

```
mysql -h主机地址 -u用户名 -p密码
```

- **-h** : 指定客户端所要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略;

  ​	用户要有使用指定ip登录的权限

- **-u** : 登录的用户名;

- **-p** : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项。



## MySQL命令行规则

​	mysql>

1.   MySQL 命令必须以   ;   结尾
2.   MySQL 命令不区分大小写
3.   使用 \c 来终止命令执行

## 命名规则

1. 数字、字母、_，不能纯数字
2. 区分大小写
3. 不能使用特殊字符和MySQL关键字



## 通配符

***** :  	匹配全部

**%**：表示任意 0 个或多个字符。可匹配任意类型和长度的字符，有些情况下若是中文，请使用两个百分号（%%）表示。

**_**：表示任意单个字符。匹配单个任意字符，它常用来限制表达式的字符长度语句。

查询内容包含通配符时,由于通配符的缘故，导致我们查询特殊字符 “%”、“_”、“[” 的语句无法正常实现，而把特殊字符用 “[ ]” 括起便可正常查询。

    _%_  至少有两个字符   ___至少有三个字符  



## MySQL 正则表达式

**下表中的正则模式可应用于 REGEXP 操作符中**

| 模式       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| ^          | 匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。 |
| $          | 匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。 |
| .          | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。 |
| [...]      | 字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。 |
| [^...]     | 负值字符集合。匹配未包含的任意字符。例如， '\[^abc]' 可以匹配 "plain" 中的'p'。 |
| p1\|p2\|p3 | 匹配 p1 或 p2 或 p3。例如，'z\|food' 能匹配 "z" 或 "food"。'(z\|f)ood' 则匹配 "zood" 或 "food"。 |
| *          | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
| +          | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
| {n}        | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
| {n,m}      | m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。 |

**实例**

查找name字段中以'st'为开头的所有数据：

```mysql
mysql> SELECT name FROM person_tbl WHERE name REGEXP '^st';
```

查找name字段中以'ok'为结尾的所有数据：

```mysql
mysql> SELECT name FROM person_tbl WHERE name REGEXP 'ok$';
```

查找name字段中包含'mar'字符串的所有数据：

```mysql
mysql> SELECT name FROM person_tbl WHERE name REGEXP 'mar';
```

查找name字段中以元音字符开头或以'ok'字符串结尾的所有数据：

```mysql
mysql> SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok$';
```



## 模糊查询(LIKE 子句)

**查询条件**

```mysql
where 字段名 like 表达式;

```

**查看库**

```mysql
show databases like "__sfdd" ;
```

**查看表**

```mysql
show tables like "_san%" ;
```

**查变量名**

```mysql

```



## binary 关键字

MySQL 的 WHERE 子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

```mysql
select * from STUDENT where name='wei';
+------+------+------+------+
| id   | name | age  | sex  |
+------+------+------+------+
|    1 | wei  |   22 | 女   |
|    1 | WEI  |   33 | 男   |
+------+------+------+------+
select * from STUDENT where binary name='wei';
+------+------+------+------+
| id   | name | age  | sex  |
+------+------+------+------+
|    1 | wei  |   22 | 女   |
+------+------+------+------+
```



## MySQL 用户管理

#### 添加 MySQL 用户

##### 在 mysql 数据库中的 user 表添加新用户

以下为添加用户的的实例，用户名为guest，密码为guest123，并授权用户可进行 SELECT, INSERT 和 UPDATE操作权限：

```mysql
root@host# mysql -u root -p
Enter password:*******
mysql> use mysql;
Database changed
mysql> INSERT INTO user 
          (host, user, password, 
           select_priv, insert_priv, update_priv) 
           VALUES ('localhost', 'guest', 
           PASSWORD('guest123'), 'Y', 'Y', 'Y');
Query OK, 1 row affected (0.20 sec)
mysql> FLUSH PRIVILEGES;
```

**注意：**在 MySQL5.7 中 user 表的 password 已换成了**authentication_string**。

**注意：**password() 加密函数已经在 8.0.11 中移除了，可以使用 MD5() 函数代替。

**注意：**在注意需要执行 **FLUSH PRIVILEGES** 语句刷新权限。 这个命令执行后会重新载入授权表。

**注意：**my-default.ini中有一条语句：

​	指定了严格模式，为了安全，严格模式禁止通过 insert 这种形式直接修改 mysql 库中的 user 表进行添加新用户

​	sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

​	将 STRICT_TRANS_TABLES 删掉之后即可使用 insert 添加



##### 另外一种添加用户的方法为通过 GRANT 命令

用有添加用户权限的用户登录mysql	一般是root
        mysql>**grant 权限列表 on 库.表 to "新建用户名"@"%" identified by "密码" with grant option;**

> **权限列表** ： all、select、insert、update、delete、create、drop、alter、execute、index、references
>
> ​	**grant 数据库开发人员，创建表、索引、视图、存储过程、函数。。。等权限。** 
>
> **库.表**  ： * 表示所有	\*.*所有表和库    
>
> **%** ： 登录ip地址限制	%表示全部 | localhost 本地  | 127.0.0.1 本机 | '192.168.0.%' 指定ip
>
> **with grant option**  : 让授权的用户，也可以将这些权限 grant 给其他用户

以下命令会给指定数据库TUTORIALS添加用户 zara ，密码为 zara123 。 

```mysql
root@host# mysql -u root -p
Enter password:*******
mysql> use mysql;
Database changed
mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
    -> ON TUTORIALS.*
    -> TO 'zara'@'localhost'
    -> IDENTIFIED BY 'zara123';
```

以上命令会在mysql数据库中的user表创建一条用户信息记录。

#### MySQL grant 权限

**分别可以作用在多个层次上**

1. grant 作用在整个 MySQL 服务器上：

```
grant select on *.* to dba@localhost; -- dba 可以查询 MySQL 中所有数据库中的表。
grant all on *.* to dba@localhost; -- dba 可以管理 MySQL 中的所有数据库
```

2. grant 作用在单个数据库上：

```
grant select on testdb.* to dba@localhost; -- dba 可以查询 testdb 中的表。
```

3. grant 作用在单个数据表上：

```
grant select, insert, update, delete on testdb.orders to dba@localhost;
```

这里在给一个用户授权多张表时，可以多次执行以上语句。例如：

```
grant select(user_id,username) on smp.users to mo_user@'%' identified by '123345';
grant select on smp.mo_sms to mo_user@'%' identified by '123345';
```

4. grant 作用在表中的列上：

```
grant select(id, se, rank) on testdb.apache_log to dba@localhost;
```

#### 查看 MySQL 用户权限

查看当前用户（自己）权限：

```
show grants;
```

查看其他 MySQL 用户权限：

```
show grants for dba@localhost;
```



#### 撤销已经赋予给 MySQL 用户权限的权限。

revoke 跟 grant 的语法差不多，只需要把关键字 to 换成 from 即可：

```
grant all on *.* to dba@localhost;
revoke all on *.* from dba@localhost;
```

**注意** :grant, revoke 用户权限后，该用户只有重新连接 MySQL 数据库，权限才能生效。

**注意**：创建完成后需要执行 **FLUSH PRIVILEGES** 语句



#### MySQL 8.0.11 版本之后创建用户方法如下：

​	CREATE USER 'laowang'@'localhost' IDENTIFIED BY '123456';
授予账户权限的方法如下：

​	GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON *.* TO 'laowang'@'localhost';

### 删除用户

**drop**
        drop user XXX;  删除已存在的用户，默认删除的是'XXX'@'%'这个用户，如果还有其他的用户			

​	如'XXX'@'localhost'等，不会一起被删除。

​	如果要删除'XXX'@'localhost'，使用drop删除时需要加上host即drop user 'XXX'@'localhost'。
 **delete**
        delete from user where user='XXX' and host='localhost';其中XXX为用户名，localhost为主机名。

**区别**

 	drop不仅会将user表中的数据删除，还会删除其他权限表的内容。而delete只删除user表中的内容，所以使用delete	删除用户后需要执行**FLUSH PRIVILEGES**;刷新权限，否则下次使用create语句创建用户时会报错。

### 修改指定用户密码

  　　mysql>update mysql.user set authentication_string=password('新密码') where User="test" and Host="localhost";

  　　mysql>flush privileges;



## 数据类型

### 数值类型

#### 整型 

| **MySQL数据类型** | **含义（有符号）**                    |
| ----------------- | ------------------------------------- |
| tinyint(m)        | 1个字节  范围(-128~127)               |
| smallint(m)       | 2个字节  范围(-32768~32767)           |
| mediumint(m)      | 3个字节  范围(-8388608~8388607)       |
| int(m)            | 4个字节  范围(-2147483648~2147483647) |
| bigint(m)         | 8个字节  范围(+-9.22*10的18次方)      |

取值范围如果加了 unsigned，则最大值翻倍，如 tinyint unsigned 的取值范围为(0~255)。

int(m) 里的 m 是表示 SELECT 查询结果集中的显示宽度，并不影响实际的取值范围，没有影响到显示的宽度，不知道这个 m 有什么用

#### 浮点型

| **MySQL数据类型** | **含义**                                                     |
| ----------------- | ------------------------------------------------------------ |
| float(m,d)        | 单精度浮点型    8位精度(4字节)     m总个数(最高7)，d小数位   |
| double(m,d)       | 双精度浮点型    16位精度(8字节)    m总个数(最高15位)，d小数位 |

设一个字段定义为 float(5,3)，如果插入一个数 123.45678,实际数据库里存的是 123.457，但总个数还以实际为准，即 6 位。

**定点数**

浮点型在数据库中存放的是近似值，而定点类型在数据库中存放的是精确值。

decimal(m,d) 参数 m<65 是总个数，d<30 且 d<m 是小数位。

 整数和小数分开存储
   		 (m,n)   最高20位 
    		将9的倍数封装成4个字节
    		存储空间:
      			 余数   字节
        		   0      0
       			1~2     1
       			3`4     2
       			5~6     3
       			7~8     4
    		decimal(19,9)
         		10/9 = 1 余1   4+1 = 5
         		9/9  = 1 余0     4+0 = 4

### 字符类型

| **MySQL数据类型** | **含义**                                          |
| ----------------- | ------------------------------------------------- |
| char(n)           | 固定长度，最多255个字符,浪费空间  性能高          |
| varchar(n)        | 可变长度，最多65535个字符,判断字符长度 ，节省空间 |
| tinytext          | 可变长度，最多255个字符                           |
| text              | 可变长度，最多65535个字符                         |
| mediumtext        | 可变长度，最多2的24次方-1个字符                   |
| longtext          | 可变长度，最多2的32次方-1个字符                   |

**char 和 varchar：**

- 1.char(n) 若存入字符数小于n，则以空格补于其后，查询之时再将空格去掉。所以 char 类型存储的字符串末尾不能有空格，varchar 不限于此。
- 2.char(n) 固定长度，char(4) 不管是存入几个字符，都将占用 4 个字节，varchar 是存入的实际字符数 +1 个字节（n<=255）或2个字节(n>255)，所以 varchar(4),存入 3 个字符将占用 4 个字节。
- 3.char 类型的字符串检索速度要比 varchar 类型的快。

**varchar 和 text：**

- 1.varchar 可指定 n，text 不能指定，内部存储 varchar 是存入的实际字符数 +1 个字节（n<=255）或 2 个字节(n>255)，text 是实际字符数 +2 个字节。
- 2.text 类型不能有默认值。
- 3.varchar 可直接创建索引，text 创建索引要指定前多少个字符。varchar 查询速度快于 text, 在都创建索引的情况下，text 的索引似乎不起作用。

**二进制数据(Blob 、 longblob)**

- 1._BLOB和_text存储方式不同，_TEXT以文本方式存储，英文存储区分大小写，而_Blob是以二进制方式存储，不分大小写。
- 2.BLOB存储的数据只能整体读出。
- 3._TEXT可以指定字符集，_BLO不用指定字符集。

字符类型宽度和数值类型宽度的区别
    1、数值类型宽度为显示宽度，只用于select查询时显示，
    		和存储无关，可以省略
    		可用 | 类型 zerofill | 查看效果（用零填充）
    2、字符类型宽度超过后无法存储

### 枚举类型

​    	1、单选：enum(值1，值2，值3...)

​	2、多选；set(值1，值2，值3...)

### 日期时间类型

| **MySQL数据类型** | **含义**                      |
| ----------------- | ----------------------------- |
| date              | 日期 '2008-12-2'              |
| time              | 时间 '12:25:36'               |
| datetime          | 日期时间 '2008-12-2 22:06:44' |
| timestamp         | 自动存储记录修改时间          |

若定义一个字段为timestamp，这个字段里的时间数据会随其他字段修改的时候自动刷新，所以这个数据类型的字段可以存放这条记录最后被修改的时间。

**日期时间函数**
    now()		:	返回当前时间(日期加时间)  YYYY-MM-DD HH:MM:SS
    curdate()	:	返回当前日期    YYYY-MM-DD
    curtime()	:	返回当前时间    HH:MM:SS
    curyear()
	给参数的：
    		year(字段):取出年份      YYYY
   		 date(字段):取出日期      YYYY-MM-DD
   		 time(字段):取出时间      HH:MM:SS

例：

```mysql
select year(jrtime) from sanguo;
select time(jrtime) from sanguo; 
update sanguo set jrtime=curdate() where id>3 and id <6;
```

**日期时间的预算**
    语法格式：

```mysql
select * from 表名 where 字段名 运算符(now()-interval 时间间隔单位)；

时间间隔单位： 1 day | 2 hour | 3 year | 4 month 
查询1天以内的时间记录
     select * from t1 where cztime>=(now()-interval 1 day);
查询1天以前的时间记录
     select * from t1 where cztime<(now()-interval 1 day);  
```



## 运算符

### 算术运算符

MySQL 支持的算术运算符包括:

| 运算符   | 作用 |
| -------- | ---- |
| +        | 加法 |
| -        | 减法 |
| *        | 乘法 |
| / 或 DIV | 除法 |
| % 或 MOD | 取余 |

在除法运算和模运算中，如果除数为0，将是非法除数，返回结果为NULL。

### 比较运算符

SELECT 语句中的条件语句经常要使用比较运算符。通过这些比较运算符，可以判断表中的哪些记录是符合条件的。比较结果为真，则返回 1，为假则返回 0，比较结果不确定则返回 NULL。

| 符号            | 描述                       | 备注                                                         |
| --------------- | -------------------------- | ------------------------------------------------------------ |
| =               | 等于                       |                                                              |
| <>, !=          | 不等于                     |                                                              |
| >               | 大于                       |                                                              |
| <               | 小于                       |                                                              |
| <=              | 小于等于                   |                                                              |
| >=              | 大于等于                   |                                                              |
| BETWEEN         | 在两值之间                 | >=min&&<=max                                                 |
| NOT BETWEEN     | 不在两值之间               |                                                              |
| IN              | 在集合中                   |                                                              |
| NOT IN          | 不在集合中                 |                                                              |
| <=>             | 严格比较两个NULL值是否相等 | 两个操作码均为NULL时，其所得值为1；而当一个操作码为NULL时，其所得值为0 |
| LIKE            | 模糊匹配                   |                                                              |
| REGEXP 或 RLIKE | 正则式匹配                 |                                                              |
| IS NULL         | 为空                       | where 字段名 is/is not  NULL  (不能用=)                      |
| IS NOT NULL     | 不为空                     | (where 字段名 = '' 空字符只能用= 或!= 去匹配)                |

#### exists   /    not exists

exists 与 in 作用相同

not in 效果不完全等同于 not exists , 如果子查询中出现空记录, 则整个查询语句不会返回数据

```mysql
SELECT a.* FROM tableA a
WHERE a.column1 not in (SELECT column2 FROM tableB);
#等同  
SELECT a.* FROM tableA a
WHERE NOT EXISTS(SELECT b.column2 FROM tableB b WHERE a.colunm1=b.column2)
```

exists对外表用loop逐条查询，每次查询都会查看exists的条件语句，当 exists里的条件语句能够返回记录行时(无论记录行是的多少，只要能返回)，条件就为真，返回当前loop到的这条记录，反之如果exists里的条 件语句不能返回记录行，则当前loop到的这条记录被丢弃，exists的条件就像一个bool条件，当能返回结果集则为true，不能返回结果集则为 false

n查询的子条件返回结果必须与比较条件等字段，例如

```mysql
select * from user where userId in (select id from B);
或 
select * from user where (userId,aaa) in (select id,bbb from B);
```

而不能是

select * from user where userId in (select id, age from B);

而exists就没有这个限制



### 逻辑运算符

逻辑运算符用来判断表达式的真假。如果表达式是真，结果返回 1。如果表达式是假，结果返回 0。

| 运算符号 | 作用     |
| -------- | -------- |
| NOT 或 ! | 逻辑非   |
| AND      | 逻辑与   |
| OR       | 逻辑或   |
| XOR      | 逻辑异或 |

### 位运算符

位运算符是在二进制数上进行计算的运算符。位运算会先将操作数变成二进制数，进行位运算。然后再将计算结果从二进制数变回十进制数。

| 运算符号 | 作用     |
| -------- | -------- |
| &        | 按位与   |
| \|       | 按位或   |
| ^        | 按位异或 |
| !        | 取反     |
| <<       | 左移     |
| >>       | 右移     |

## 运算符优先级

最低优先级为： **:=**。

![img](https://www.runoob.com/wp-content/uploads/2018/11/1011652-20170416163043227-1936139924.png)

最高优先级为： **!**、**BINARY**、[COLLATE](https://www.cnblogs.com/qcloud1001/p/10033364.html)

## 库的管理命令

**创建数据库**

```mysql  
创建库(指定字符集)
	create database 库名 character set utf8;	
	CREATE DATABASE IF NOT EXISTS 库名 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
创建数据库，该命令的作用：
	如果数据库不存在则创建，存在则不创建。
	创建RUNOOB数据库，并设定编码集为utf8
```

**查看已有库**

```mysql  
show databases;
```

**查看创建库的语句**

```mysql  
show create database 库名;
```

**查看当前库**

```mysql  
select database();
```

**切换库**选择要操作的Mysql数据库，使用该命令后所有Mysql命令都只针对该数据库

```mysql  
use 库名;
```

**删除库**

```mysql  
drop database 库名;
```

**修改库名**

第一种方法：

​		1.创建需要改成新名的数据库。
​		2.mysqldum 导出要改名的数据库
​		3.删除原来的旧库（确定是否真的需要）
​		当然这种方法虽然安全，但是如果数据量大，会比较耗时

第二种方法：

​	用一个脚本

```shell
#!/bin/bash
# 假设将sakila数据库名改为new_sakila
# MyISAM直接更改数据库目录下的文件即可
mysql -uroot -p123456 -e 'create database if not exists new_sakila'
list_table=$(mysql -uroot -p123456 -Nse "select table_name from information_schema.TABLES where TABLE_SCHEMA='sakila'")

for table in $list_table
do
    mysql -uroot -p123456 -e "rename table sakila.$table to new_sakila.$table"
done
```

这里用到了rename table,改表名的命令，但是如果新表名后面加数据库名，就会将老数据库的表移动到新的数据库，所以，这种方法即安全，又快速。 



## 表的管理命令

**查看库中已有的表**使用该命令前需要使用 use 命令来选择要操作的数据库

```mysql
show tables;
```

**创建表(指定字符集)**

```mysql
create table 表名(字段名1 数据类型，字段名2 数据类型)character set utf8；或charset=utf8;
```

**查看创建表的语句(字符集、存储引擎)**

```mysql
show create table 表名;
```

**查看表的结构**

```mysql
desc 表名;
或
SHOW COLUMNS FROM 数据表;
```

**删除表**

```mysql
drop table 表名1,表名2;
```

**表的重命名(rename)**

```mysql
alter table 原表名 rename 新表名;
```
**显示数据表的详细索引信息包括PRIMARY KEY（主键）**

```mysql
SHOW INDEX FROM 数据表;
```

**修改存储引擎：修改为myisam**

```mysql
alter table tableName engine=myisam;
```

**删除外键约束：keyName是外键别名**

```mysql
alter table tableName drop foreign key keyName;
```



## 表字段操作

```mysql
语法：alter table 表名 执行动作;
```

**添加字段(add)**

```mysql
alter table 表名 add 字段名 数据类型；(默认最后)
alter table 表名 add 字段名 数据类型 first；(加在第一列)
alter table 表名 add 字段名 数据类型 after 字段名；(在字段名后加)
```

**删除字段(drop)**

```mysql
alter table 表名 drop 字段名;
```

**修改数据类型(modify)**

```mysql
alter table 表名 modify 字段名 新数据类型;
```

**修改字段类型及名称(change)**

```mysql
alter table 表名 change 原字段名 新字段名 数据类型;
```

**修改字段的相对位置**

这里name1为想要修改的字段，type1为该字段原来类型，first和after二选一，这应该显而易见，first放在第一位，after放在name2字段后面

```mysql
alter table tableName modify name1 type1 first|after name2;
```



## 插入表记录(insert)

```mysql
insert into table_name ( field1, field2,...fieldN )
                       values
                       ( value1, value2,...valueN ),( value1, value2,...valueN ),...;
如果所有的列都要添加数据可以不规定列进行添加数据：
insert into 表名 values(value1, value2,...valueN),(value1, value2,...valueN),...;
```

**如果数据是字符型，必须使用单引号或者双引号，如："value"**

**如果添加过主键自增（PRINARY KEY AUTO_INCREMENT）第一列在增加数据的时候，可以写为0或者null，这样添加数据可以自增， 从而可以添加全部数据，而不用特意规定那几列添加数据。**



## 修改表记录(update)

```mysql
update 表名 set 字段1=值1,字段2=值2 where 条件;	(不加 where 表记录全改)
```



## 删除表记录(delete)

```mysql
delete from 表名 where 条件;   (不加 where 删除全部表记录 )
```



## 查询表记录(select)

```mysql
SELECT table_name1.field1[,table_name2.field2][,...]
FROM table_name1[,table_name2][,...]
[WHERE Clause...]
[GROUP BY field1, [field2...] WITH ROLLUP]
[HAVING Clause...]
[ORDER BY field1, [field2...] [ASC | DESC]]
[LIMIT count][ OFFSET start];
```

#### 查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割

>SELECT table_name1.field1[,table_name2.field2][,...]
>FROM table_name1[,table_name2][,...]

SELECT 命令可以读取一条或者多条记录。

你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据



#### WHERE 子句

 有条件地从表中选取数据

```mysql
where id between 100 and 200;
where 字段名 in(值1，值2，...);
where 字段名 is/is not  NULL;
```

##### binary 关键字

WHERE 子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

```mysql
select * from STUDENT where name='wei';
+------+------+------+------+
| id   | name | age  | sex  |
+------+------+------+------+
|    1 | wei  |   22 | 女   |
|    1 | WEI  |   33 | 男   |
+------+------+------+------+
select * from STUDENT where binary name='wei';
+------+------+------+------+
| id   | name | age  | sex  |
+------+------+------+------+
|    1 | wei  |   22 | 女   |
+------+------+------+------+
```

#### group by 分组

GROUP BY关键字可以将查询结果按照某个字段或多个字段进行分组。字段中值相等的为一组。

```mysql
GROUP BY field1, [field2...]  [HAVING 条件表达式] [WITH ROLLUP]
```

**在默认sql_mode=only_full_group_by模式下**

**SELECT list中的列必须为GROUP BY子句中的列或聚合列**：group by 后字段名必须要为select后的查询字段，如果SELECT list的表达式不是GROUP BY子句中的列，则必须对该字段进行聚合处理，所以聚合列的结果为一分组的该字段所有值的聚合结果

**多个字段进行分组:** 先按照第一个字段进行分组，遇到第一个字段的值相等的情况时，再把第一个值相等的记录按照第二个字段进行分组。

**聚合函数** 
    **av**g(字段) : 平均值**
    **max(字段) : 最大值**
    **min(字段) : 最小值**
    **sum(字段) : 和**
    count(字段) :  统计该字段记录的条数**

​		NULL不会被统计，count(*)可以统计	

**with rollup**可以实现在分组聚合的数据基础上再进行相同的聚合（SUM,AVG,COUNT…）

将会在所有记录的最后加上一条记录。加上的这一条记录是上面所有记录的聚合数据。

例如我们将以上的数据表按名字进行分组，再统计每个人登录的次数：

```
mysql> SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------+--------------+
| name   | singin_count |
+--------+--------------+
| 小丽 |            2 |
| 小明 |            7 |
| 小王 |            7 |
| NULL   |           16 |
+--------+--------------+
```

其中记录 NULL 表示所有人的登录次数。

我们可以使用 **coalesce** 来设置一个可以取代 NUll 的名称，coalesce 语法：

```
select coalesce(a,b,c);
```

参数说明：如果a\==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）。

以下实例中如果名字为空我们使用总数代替：

```
mysql> SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------------------------+--------------+
| coalesce(name, '总数') | singin_count |
+--------------------------+--------------+
| 小丽                   |            2 |
| 小明                   |            7 |
| 小王                   |            7 |
| 总数                   |           16 |
+--------------------------+--------------+
```



#### HAVING

**分组后的条件使用 HAVING 来限定，WHERE 是对原始数据进行条件限制,不能对聚合的字段限制**

​	having 语句通常与group by 联合使用
​        having 操作的是聚合函数生成的显示列

```mysql
SELECT name ,sum(*) as a FROM employee_tbl WHERE id<>1 GROUP BY name  HAVING a>5 ORDER BY sum(*) DESC;
```


#####  ORDER BY 

**使用 ORDER BY 子句将查询数据通过 field 排序后再返回数据 多级排序: 通过多个 field排序**

```mysql
select * from users order by age desc,id asc;
```

​           先通过 age 排序，age相同的再通过 id 排序

​	**DESC: 表示倒序，可替换成 ASC，表示升序**

####  LIMIT

你可以使用 LIMIT 属性来设定返回的记录数。

count: 查询的个数, limit N : 返回 N 条记录

limit N,M : 相当于 **limit M offset N** , 从第 N 条记录开始, 返回 M 条记录

你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

- start: 开始（升序第一条是0，降序最后一条是0）


- offset M : 跳过 M 条记录, 默认 M=0, 单独使用似乎不起作用

```mysql
/*websites  表名   NAME alexa url country  字段*/
SELECT * FROM websites;                      /* 查询表所有数据 */

SELECT NAME FROM websites;                   /* 查询表字段数据 */

SELECT * FROM websites where name = "广西";   /* 查询表字段下条件数据 */

SELECT * from websites where name like "_o%"; /* 模糊查询表下数据 */

SELECT * FROM websites where id BETWEEN "1" AND "5";    /* 查询表下字段范围数据 */

SELECT * FROM websites WHERE name in ("广西","百度");    /* 查询表字段下固定条件数据 */

SELECT DISTINCT country FROM Websites;                  /* 查询去重值 */

SELECT * FROM Websites WHERE country = "CN" AND alexa > 50;  /*查询表下范围条件数据*/

SELECT * FROM Websites WHERE country = "USA" OR country="sh"; /* 查询表下条件不同值 */

SELECT * FROM Websites ORDER BY alexa;                      /* 查询表下值排序结果 */

SELECT * FROM Websites ORDER BY alexa DESC;                 /* 查询表下排序结果降序 */

SELECT * FROM Websites LIMIT 2;      /* 查询表下范围数据 */

SELECT name as zzz from websites;    /*别名查询表下数据*/
```

### 记录去重处理

**distinct 关键字,不显示重复的查询记录**

​    **语法:  select distinct 字段1，字段2，... from 表名;**
可以去重之后聚合

```mysql
select count(distinct country) from sanguo;
```

​        注意：distinct和from之间所有字段的记录值都相同才会去重

### 不切换库 查看表

```mysql
select ...... from 库名.表名;
```

### 查询表记录时做运算

运算符  +  -   *   /   %

```mysql
select 字段*2 from 表名;  
```

函数运算

1. avg(字段) : 平均值

2. max(字段) : 最大值

3. min(字段) : 最小值

4. sum(字段) : 和

5. count(字段) :  统计该字段记录的条数   

      NULL不会被统计，count(*)可以统计

```mysql
select max(gongji) from table1;
select count(id),count(name) from table1;
```

### 给字段取别名 

```mysql
select 字段名 as y,字段名 as x from table;
或
select 字段名 y,字段名 x from table;
```



## 嵌套查询 (子查询)

​    定义：把内层的查询结果作为外层查询的条件
​    语法：

```mysql
select ... from 表名 where 字段名 运算符(select ...from 表名 where ...)
```

**子查询返回的值要与条件相匹配  一个值用 值比较(=,<)，多个值要用 in / not in**

**子查询返回多个值是以查询的字段元组的列表的形式[(id,name),(id,name),...] 所以条件字段也要是相匹配的字段元组**

主意: 多表查询用 join 效率更高,优先使用 join

eg: **重复记录查询**（多个字段）

```mysql
select * from vitae a
where (a.peopleId,a.seq) in  (select peopleId,seq from vitae group by peopleId,seq  having count(*) > 1);
```

删除表中多余的重复记录（多个字段），只留有rowid最小的记录

```mysql
delete from vitae a
where (a.peopleId,a.seq) in  (select peopleId,seq from vitae group by peopleId,seq having count(*) > 1)
and rowid not in (select min(rowid) from vitae group by peopleId,seq having count(*)>1);
```



## 行关联多表查询

以记录来拼接，可以单表多次查询拼接实现分类显示

### UNION 运算符 

UNION 操作符语法格式：	

```mysql
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```

expression1, expression2, ... expression_n: 要检索的列,每张表的列数必须一致,字段名以第一张表的字段显示

tables: 要检索的数据表。

**WHERE conditions:** 可选， 检索条件。

**DISTINCT:** 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响。

**ALL:** 可选，返回所有结果集，包含重复数据。

UNION 运算符通过组合其他两个结果表（例如 TABLE1 和 TABLE2）并消去表中任何重复行而派生出一个结果表
当 ALL 随 UNION一起使用时（即 UNION ALL），不消除重复行。两种情况下，派生表的每一行不是来自 TABLE1 就是来自 TABLE2。
UNION 语句：用于将不同表中相同列中查询的数据展示出来；（不包括重复数据）

UNION ALL 语句：用于将不同表中相同列中查询的数据展示出来；（包括重复数据）

**使用形式如下：**

​	SELECT 列名称 FROM 表名称 UNION SELECT 列名称 FROM 表名称 ORDER BY 列名称；
​	SELECT 列名称 FROM 表名称 UNION ALL SELECT 列名称 FROM 表名称 ORDER BY 列名称；

### EXCEPT 运算符 

EXCEPT 运算符通过包括所有在 TABLE1 中但不在 TABLE2 中的行并消除所有重复行而派生出一个结果表。
当 ALL 随 EXCEPT 一起使用时 (EXCEPT ALL)，不消除重复行

### INTERSECT 运算符

INTERSECT 运算符通过只包括 TABLE1 和 TABLE2 中都有的行并消除所有重复行而派生出一个结果表。
当 ALL 随 INTERSECT 一起使用时 (INTERSECT ALL)，不消除重复行。

```mysql
ysql> SELECT * FROM Websites;
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 7  | stackoverflow | http://stackoverflow.com/ |   0 | IND     |
+----+---------------+---------------------------+-------+---------+

mysql> SELECT * FROM apps;
+----+------------+-------------------------+---------+
| id | app_name   | url                     | country |
+----+------------+-------------------------+---------+
|  1 | QQ APP     | http://im.qq.com/       | CN      |
|  2 | 微博 APP | http://weibo.com/       | CN      |
|  3 | 淘宝 APP | https://www.taobao.com/ | CN      |
+----+------------+-------------------------+---------+

SELECT country FROM Websites
UNION
SELECT country FROM apps
ORDER BY country;
+---------+
|country	| 
+---------+
|  CN 		|
|  IND 		|
|  USA 		|
+---------+

eg2：
SELECT SNO,SNAME FROM STUDENT UNION SELECT CNO,GRADE FROM SC;
+------+---------+
| SNO  | SNAME   |
+------+---------+
|    1 | aaa     |
|    2 | bbb     |
|    3 | ccc     |
|    4 | ddd     |
|    5 | eee     |
|    6 | bbb     |
|    7 | liqiang |
|    8 | fff     |
|    9 | ggg     |
|    1 | 67      |
|    2 | 77      |
|    3 | 77      |
|    2 | 55      |
|    3 | 88      |
|    1 | 69      |
|    2 | 88      |
|    4 | 75      |
|    6 | 88      |
+------+---------+
eg3:
mysql> SELECT * FROM STUDENT WHERE SSEX="WO" UNION SELECT * FROM STUDENT WHERE SSEX="MAN";
+------+---------+------+------+
| SNO  | SNAME   | SAGE | SSEX |
+------+---------+------+------+
|    2 | bbb     |   23 | wo   |
|    3 | ccc     |   20 | wo   |
|    5 | eee     |   23 | wo   |
|    6 | bbb     |   20 | wo   |
|    9 | ggg     |   20 | wo   |
|    1 | aaa     |   22 | man  |
|    4 | ddd     |   26 | man  |
|    7 | liqiang |   24 | man  |
|    8 | fff     |   25 | man  |
+------+---------+------+------+

```



## 列拼接多表查询

​	**以列凭借的方式把多个表的查询结果合为一张表显示**

### 笛卡尔积查询，每一个值互相匹配，字段相加，记录相乘.

**不加 where 条件**

```mysql
select t1.name,t2.name from t1,t2;
```

如果a表和b表分别有10条记录，返回的结果就有100条记录，所以要注意

**加 where 条件**    合成表的基础上，显示条件匹配到的

```mysql
select  字段名列表   from 表1，表2 where 条件；
```



### join 连接查询

通过两个表中的某个字段把两个表关联起来显示(拼接在一起)
where 子句要写在最后,对合成表进行筛选
	select * from STUDENT inner join SC on STUDENT.SNO=SC.SNO where STUDENT.SSEX="wo";

#### 内连接inner join

(也可以省略 INNER 使用 JOIN，效果一样)   同加where的笛卡尔积查询，只显示两表相互比配的部分

![](https://www.runoob.com/wp-content/uploads/2014/03/img_innerjoin.gif)

   语法:

```mysql
select .. from 表1 inner join 表2 on 条件 inner join 表3 on 关联条件;
eg: 
	SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a 
	INNER JOIN tcount_tbl b
	ON a.runoob_author = b.runoob_author;
```

#### 外连接

**左连接(left join)**
     	左表显示全部查询结果，右表不匹配的字段用 null表示

![](https://www.runoob.com/wp-content/uploads/2014/03/img_leftjoin.gif)

**右连接(right join)**
     	右表显示全部查询结果，左表不匹配的字段用 null表示

![](https://www.runoob.com/wp-content/uploads/2014/03/img_rightjoin.gif)



## 事务

- 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
- 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
- 事务用来管理 insert,update,delete 语句

事务是必须满足4个条件（ACID）：

- **原子性：**一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。
- **一致性：**在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。
- **隔离性：**数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。
- **持久性：**事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

> 在 MySQL 命令行的默认设置下，事务都是自动提交的，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务务须使用命令 BEGIN 或 START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。

### 事务控制语句：

- BEGIN 或 START TRANSACTION 显式地开启一个事务；
- COMMIT 也可以使用 COMMIT WORK，不过二者是等价的。COMMIT 会提交事务，并使已对数据库进行的所有修改成为永久性的；
- ROLLBACK 也可以使用 ROLLBACK WORK，不过二者是等价的。回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；
- SAVEPOINT identifier，SAVEPOINT 允许在事务中创建一个保存点，一个事务中可以有多个 SAVEPOINT；
- RELEASE SAVEPOINT identifier 删除一个事务的保存点，当没有指定的保存点时，执行该语句会抛出一个异常；
- ROLLBACK TO identifier 把事务回滚到标记点；
- SET TRANSACTION 用来设置事务的隔离级别。InnoDB 存储引擎提供事务的隔离级别有READ UNCOMMITTED、READ COMMITTED、REPEATABLE READ 和 SERIALIZABLE。

### MYSQL 事务处理主要有两种方法：

1、用 BEGIN, ROLLBACK, COMMIT来实现

- **BEGIN** 开始一个事务
- **ROLLBACK** 事务回滚
- **COMMIT** 事务确认

2、直接用 SET 来改变 MySQL 的自动提交模式:

- **SET AUTOCOMMIT=0** 禁止自动提交
- **SET AUTOCOMMIT=1** 开启自动提交

**伪代码:**

```mysql
mysql> begin;  # 开始事务
mysql> insert into runoob_transaction_test value(5);
mysql> insert into runoob_transaction_test value(6);
mysql> commit; # 提交事务
mysql> begin;  # 开始事务 Query OK, 0 rows affected (0.00 sec)   
mysql> insert into runoob_transaction_test values(7);
mysql> insert into runoob_transaction_test value(6);
mysql> rollback;   # 回滚
```



### 使用保留点 SAVEPOINT

savepoint 是在数据库事务处理中实现“子事务”（subtransaction），也称为嵌套事务的方法。事务可以回滚到 savepoint 而不影响 savepoint 创建前的变化, 不需要放弃整个事务。

ROLLBACK 回滚的用法可以设置保留点 SAVEPOINT，执行多条操作时，回滚到想要的那条语句之前。

使用 SAVEPOINT

```mysql
SAVEPOINT savepoint_name;    // 声明一个 savepoint

ROLLBACK TO savepoint_name;  // 回滚到savepoint
```

删除 SAVEPOINT

保留点再事务处理完成（执行一条 ROLLBACK 或 COMMIT）后自动释放。

MySQL5 以来，可以用:

```mysql
RELEASE SAVEPOINT savepoint_name;  // 删除指定保留点
```



## SQL命令运行时间监测

**开启运行时间检测** 

```mysql
set profiling=1
```

**执行查询语句(没有索引)**

```mysql
select * from t1 where name="lucy1000000"
```

**在name字段创建索引**

```mysql
create index name on t1(name)
```

**再执行查询语句**

```mysql
select * from t1 where name="lucy1000000"
```

**对比**

```mysql
show profiles;
```



## 约束

**非空约束(not null)**
        不允许该字段的值为 NULL

**默认约束(default)**
    插入记录时，不给该字段赋值，则使用默认值

```mysql
cteate table t1(id int,name char(10) not null,
sex enum("man","F","s") default "s");
```



## 索引

​    **文件在: /var/lib/mysql/db3/** 
索引是对数据库表的一列或多列的值进行排序的一种结构(BTree方式)

优缺点： 优点是加快数据的检索速度(只对索引字段)
        	缺点是占用物理存储空间，当对表中数据更新时，索引需要动态维护
        	占用系统资源，降低系统维护速度。

把经常用来查询的字段设置为索引字段以加快搜索速度



### 普通索引	index

​	key 标志 :MUL

​        可以设置多个字段
​      	约束: 无约束

### 唯一索引(unique)

​	key 标志 :UNI

​	可以设置多个字段
  	约束 ：字段值不可重复，可为NULL 

**创建索引**：

1. 创建表时创建

```mysql
create table 表名(
......,
index(name),	#普通索引
index(age),
unique(phnumber),	#唯一索引
unique(cardnumber)
);
```

2. 已有表创建

```mysql
create [unique] index 索引名 on 表名(字段名);
```

**查看索引**

```mysql
desc 表名;  key 标志
或
show index from 表名\G;  \G 竖着显示每条记录
```

**删除索引**

```mysql
drop index 索引名 on 表名;
```





## 字段主外键关联

### 主键(primary key)  && 自增长(auto_increment)默认从0开始

​    使用规则:
​       1、只能有一个字段
​       2、约束：字段值不允许重复，且不能为NULL
​       3、key标志位 PRI
​       4、通常设置编号id为主键，能唯一锁定1条记录

1. 创建表时创建

```mysql
create table 表名(id int primary key [auto_increment],
...)  # 没有自增长要首动输入
auto_increment=10000 #指定从10000开始
;
```

有自增长主键索引的记录 删记录后，自增长值会保留，不会被使用。

2. 在已有表创建主键

```mysql
alter table 表名 add primary key(id) [auto_increment];
```

**设置主键自动起始**

```mysql
alter table 表名 auto_increment=10000;
例：
alter table userinfo add id int(3) zerofill 
primary key auto_increment first;
```

**删除主键**

```mysql
有自增长 先删自增长
   alter table 表名 modify id int;
没有自增长
   alter table 表名 drop primary key;
```
复合主键  以多个字段为一个主键，有一个字段不重复即可



### 外键(foreign key)

定义: 让当前表字段的值在另一个表的范围内选择
    语法：
        foreign key(参考字段名) references 主表(被参考字段名)
        on delete 级联动作{restrict | cascade |set null | on action | set default}
        on update 级联动作{restrict | cascade |set null | on action | set default}

**级联动作**

​    	cascade	跟随外键改动
​        	数据级联删除、更新(参考字段)同步 ，不提示

​	set NULL  设空值
​        	主表记录删除、更新
​        	从表有相关联记录，字段值设置为NULL

​	set default（设默认值）
​		主表记录删除、更新
​        	从表有相关联记录，字段值设置为NULL

​    	restrict	限制外表中的外键改动
​       		从表有相关联记录，不让主表删除、更新

​	no action  无动作，默认的

使用规则:
       主表、从表参考字段数据类型要一致
       主表被参考字段: 主键(主表要有主键从表才能设外键)

**创建外键**

1. 创建从表时创建

```mysql
create table bjtab(stu_id int,
-> name varchar(15),
-> money smallint,
-> foreign key(stu_id) references jftab(id)
-> on delete cascade
-> on update cascade
-> );
```

2. 已有表创建

```mysql 
alter table 表名 add constraint 外键名
-> foreign key(字段名) 
-> references 主表(主键)
-> on delete set NULL  主表删掉后外键给个NULL标记
-> on update cascade
);
```

**删除外键**

```mysql
alter table 子表名 drop foreign key 外键名;
```

fk_sno为外键ID名, 若不知，可查询建表明细（show create table 表名）。



## MySQL 序列

一张数据表只能有一个字段自增主键， 如果你想实现其他字段也实现自动增加，就可以使用MySQL序列来实现。 

使用序列的方法就是使用 **AUTO_INCREMENT** 来定义列 

### 创建序列

以下实例中创建了数据表 insect， insect 表中 id 无需指定值可实现自动增长。

```mysql
mysql> CREATE TABLE insect(id INT UNSIGNED NOT NULL AUTO_INCREMENT);
mysql> INSERT INTO insect (id) VALUES(NULL),(NULL),(NULL);
mysql> SELECT * FROM insect ORDER BY id;
+----+
| id |
+----+
|  1 |
|  2 |
|  3 | 
+----+
```

### 获取AUTO_INCREMENT值

在MySQL的客户端中你可以使用 SQL中的LAST_INSERT_ID( ) 函数来获取最后的插入表中的自增列的值。

### 重置序列

如果你删除了数据表中的多条记录，并希望对剩下数据的AUTO_INCREMENT列进行重新排列，那么你可以通过删除自增的列，然后重新添加来实现。 不过该操作要非常小心，如果在删除的同时又有新记录添加，有可能会出现数据混乱。操作如下所示：

```mysql
mysql> ALTER TABLE insect DROP id;
mysql> ALTER TABLE insect
    -> ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST,
    -> ADD PRIMARY KEY (id);
```

### 设置序列的开始值

一般情况下序列的开始值为1，但如果你需要指定一个开始值100，那我们可以通过以下语句来实现：

```mysql
mysql> CREATE TABLE insect
    -> (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    -> PRIMARY KEY (id),
    -> name VARCHAR(30) NOT NULL, 
    -> date DATE NOT NULL,
    -> origin VARCHAR(30) NOT NULL
)engine=innodb auto_increment=100 charset=utf8;
```

或者你也可以在表创建成功后，通过以下语句来实现：

```mysql
mysql> ALTER TABLE t AUTO_INCREMENT = 100;
```



## 锁

   加锁的目的：就是解决客户端并发访问的冲突问题

**锁类型**

1. 读锁(共享锁)

​        执行 select 语句时候，
​        别人可以查询，但不能更改(update)

2. 写锁(互斥锁、排他锁)

   ​    update: 加写锁之后，别人不能查也不能改

**锁粒度**
    1、行级锁  ：可加读锁、写锁
    2、表级锁  ：可加读锁、写锁



## 存储引擎(处理表的处理器)

1. 查看所有的存储引擎

```mysql
show engines; 
```

2. 查查看已有表的存储引擎

```mysql
show create table 表名;
```

创建表时指定

```mysql
create table 表名(....)  engine = 存储引擎;
```

已有表

```mysql
alter table 表名 engine = InnoDB;
```



**常用的存储引擎的特点**
    1、InnoDB :支持外键、行级锁、事物
               共享表空间
            存放地址 
                 表名.frm : 表结构和索引信息
                 表名.ibd : 表记录
    

2.MyISQM :支持表级锁、独享表空间

  	存放地址

​		表名.frm : 表结构
​		表名.MYD : 表记录
​		表名.ibd : 索引信息

3. MEMORY ：表结构存储在硬盘，表记录存储在内存

​            服务/主机重启后，表记录消失

​	执行查询操作多的表用MyISAM(使用InnoDB浪费资源)
​	执行写操作多的表用InnoDB



## 数据的备份(mysqldump,在Linux终端中操作)

**完全备份   增量备份**: 库表结构和记录数据全部备份

语法: 

```powershell
$:mysqldump -u用户名 -p******   源库名 > XXX.sql
```

源库名的表示方式
    --all-databases    	备份所有的库
    库名                		备份单个库
    -B 库1 库2 库3      	备份多个库
    库名 表1 表2 表3     	备份指定库的多个表

## 备份数据的恢复(Linux中操作)

​    语法：

```powershell
mysql -u用户名 -p 目标库名<xxx.sql
```

**库要手动创建**

**注意:**

​	恢复库时 会将表中数据覆盖，新增加表不会删除
​	恢复时，如果要恢复的库不存在，则先创建空库



## 数据的导入

​    **把文件系统的内容导入到数据库中**

**步骤**：

1. 创建表(字段，类型要一致)
2. 查看mysql文件搜索路径
3. 拷贝目标文件名到路径下
4. 导入

**导入语法:**

```mysql
load data infile "文件名"   #给绝对路径
into table 表名                 #没表先创建对应文件字段的表
fields terminated by "分隔符"  #确定字段  表格一般为","
lines terminated by "\n"     #确定记录
```

**查看搜索路径**

```mysql
show variables like "secure_file_priv";
```

**拷贝文件(终端)**

```powershell
sudo cp scoreTable.csv /var/lib/mysql-files/
```



## 数据导出

**把数据库中表记录导出到系统文件里**
**语法：**

```mysql
select ... from 表名 where 条件
into outfile "文件名"  #要在搜索目录下创建文件
fields terminated by "分隔符"
lines terminated by "\n"
```

例：

```mysql
select * from score where score>80 
into outfile "/var/lib/mysql-files/score.csv" 
fields terminated by "," 
lines terminated by "\n";
```



## 在mysql 里执行Linus 命令

```mysql
mysql> system sudo-i
sh: 1: sudo-i: not found
mysql> system sudo -i
[sudo] tarena 的密码： 
root@tedu:~# cat /var/lib/mysql-files/score.csv
root@tedu:~# exit
```



## E-R模型 (Entry-Relationship)

​      定义 ：实体-关系模型，数据模型，用于设计数据库
在关系数据库中，每一行记录就是一个实体(实例，对象)，每一列字段就是实体的一个属性
一般以一个能唯一标识的属性作为实体关键字(主属性，主码)

### 三个概念

​    **实体**：描述客观事物的概念
​        表示方式：矩形框
​    **属性**：实体具有的特性信息
​        表示方式：椭圆形
​    **关系**：各个实体之间的联系
​    分类：
​         一对一(1:1)：
​            A中的 1 个实体，在B中只能有一个与其关联
​            B中的 1 个实体，在A中只能有一个与其关联
​         一对多(1:n)：
​            A中的 1 个实体，在B中有n个与其关联
​            B中的 1 个实体，在A中只能有一个与其关联
​         多对多(n:n)：
​            A中 1 个实体，B中多个关联
​            B中 1 个实体，A中多个关联

### ER图绘制

​    1、矩形框代表实体，菱形框代表关系，椭圆形代表属性 

### 数据库三范式

​    后一个范式都是在前一个范式的基础上建立的。

   1、第一范式(1NF)   ：列不可拆分
        是关系型数据库的基础，是关系的基本保证。
        属性值要单一，不能再划分，避免重复的列。
   2、第二范式(2NF)   : 唯一标识
        每个实例必须被唯一区分，唯一标识作为主键(如 ID)，避免重复的行。
   3、第三范式(3NF)   : 引用主键
        一个表中不能包含已在另一个表中存在的非主键属性(列重复)，避免数据冗余。
        主键一般是主表与从表的关联的主从键，必须一致。



## python 交互

#### 模块安装

​	pymsql(第三方模块)

安装 pip3

```powershell
 sudo apt-get install python3-pip
```

1.在线安装
            sudo pip3 install pymsql[==版本号，默认最新的] 
2.离线安装
            安装包
            tar -zxvf 安装包
            cd 文件下
            python3 setup.py install

python2   MySQLdb

​    安装  sudo pip install mysql-python

### 流程：

**环境准备**

1. 创建库db5,utf8

```mysql
create database db5 charset utf8;
```

2. 创建表t1

```mysql
use db5;
create table t1(
id int primary key auto_increment,
name varchar(20),
score float(5,2)
)charset=utf8;
```

### python 程序

```python
#创建数据库连接对象
import pymysql
                            #连接对象的参数
my = pymysql.connect(host = "localhost",   #主机地址   
                            user = "root",         #用户名 
                            password = "123456",   #密码
                            database = "db5",      #指定操作库
                            charset = "utf8"      #指定字符集 
                            port = 3306)          # 应用程序端口号

#创建游标对象(利用数据库的对象)
cursor = my.cursor()

#执行SQL命令(利用游标对象)

#创建库
cdb = 'create database if not exists dbname charset utf8'
cursor.execute(cdb)
#创建表
ctb = 'create table ti(id int)'
cursor.execute("use dbname")
cursor.execute(ctb)
cursor.execute('insert into t1 values(4,"李商隐",100)')
#提交到数据库执行(commit())
my.commit()
#关闭游标对象
cursor.close()
#关闭数据库连接对象
db5.close() 


```

**数据库连接对象(my)方法**
    1.my.commit()   相对于“;”  提交到数据库执行
    2.my.rollback()   回滚
    3.my.close()     断开数据库连接
    4.my.cursor()    创建游标对象

**游标对象(cur)方法**
    1.cur.execute(SQL命令)   执行SQL命令
    2.cur.close()            关闭游标对象
    3.cur.fetchone()         取第一条(查询)
    4.cur.fetchmany(n)       取n条(查询)
    5.cur.fetchall()         取全部记录(查询)

#### 参数传递

```python
name = input()
score = input()
variable = "insert into t1(name,score) values(%s,%s);"
cursor.execute(variable,[name,score]) 
```



## ORM(Object Relation Mapping 对象关系映射)

​    定义： 
​        把对象模型映射到MySQL数据库中

### sqlalchemy框架

安装
    在线: sudo pip3 install sqlalchemy

离线:  $ tar -xf sql....tar.gz
      $ cd sqlalchemy
      $ sudo python3 setup.py install

