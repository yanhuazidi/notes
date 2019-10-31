

[TOC]



## 启动/停止odoo服务器

odoo使用客户机/服务器体系结构，其中客户机是通过RPC访问odoo服务器的Web浏览器。

为了启动服务器，只需在shell中调用命令odoo bin，必要时添加文件的完整路径：

```shell
odoo-bin
```

通过在终端上按两次`ctrl-c`或终止相应的操作系统进程来停止服务器。



## 命令行界面: odoo-bin

**python odoo-bin option**



## -c <configfile>或--config <configfile>

**提供备用配置文件**



## -d <databasename> 或 --database <databasename>

**安装或更新模块时指定使用的数据库。 提供以逗号分隔的列表限制对列表中提供的数据库的访问。**



## -i <modules> 或 --init <modules> 

**在运行服务器之前要安装的以逗号分隔的模块列表（需要-d）。**



## -u <modules> 或 --update <modules> 

**在运行服务器之前要更新的以逗号分隔的模块列表（需要-d）。**



## --addons-path <directories> 

**以逗号分隔的目录列表，其中存储了模块。 扫描这些目录的模块（nb：何时以及为什么？）**



## --workers <count> 

**如果count不为0（默认值），则启用多处理并设置指定数量的HTTP worker（处理HTTP和RPC请求的子进程）。**
**多处理模式仅适用于基于Unix的系统**

**许多选项允许限制和回收worker：**

### --limit-request <limit> 
在回收和重新启动之前，worker 将处理的请求数。默认为8196。

### --limit-memory-soft <limit> 
每个worker 允许的最大虚拟内存 如果超出限制，则worker 将在当前请求结束时被终止并回收。默认为2048MiB。

### --limit-memory-hard <limit> 
阻止worker 为每个请求使用超过<limit> CPU秒数。 如果超过限制，worker 将被杀死。默认为60。

### --limit-time-real <limit> 
防止工作者花费超过<limit>秒来处理请求。 如果超过限制，worker 将被杀死。与--limit-time-cpu不同之处在于这是一个“进程运行的时间总量 ”限制，包括例如 SQL查询。默认为120。

### --max-cron-threads <count> 

致力于cron工作worker 的数量。 默认为2. worker 是多线程模式下的线程，并且是多处理模式下的进程。
对于多处理模式，这是HTTP工作进程的补充。



## -s 或 --save 

**将服务器配置保存到当前配置文件（默认情况下为$ HOME / .odoorc，可以使用-c覆盖）**



##--proxy-mode 

**通过Werkzeug的代理支持，可以使用X-Forwarded- *headers头。不得在反向代理方案之外启用代理模式**



## --test-enable 

**安装模块后运行测试**



## --test-tags  'tag_1,tag_2,...,-tag_n' 

**选择要使用标记运行的测试**



## --dev <feature,feature,...,feature> 

all：以下所有功能都已激活
xml：直接从xml文件读取模板qweb而不是数据库。 在数据库中修改模板后，在下一次更新/初始化之前，不会从xml文件中读取该模板。
reload ：更新python文件时重新启动服务器（根据使用的文本编辑器可能无法检测到）
qweb：当节点包含t-debug ='debugger'时，打破qweb模板的评估
（i）p（u）db：在记录并返回错误之前，当引发意外错误时，在代码中启动所选的python调试器。





## database

### -r <user>, --db_user <user> 

数据库用户名，用于连接PostgreSQL。

### -w <password>, --db_password <password> 

数据库密码，如果使用密码验证。

### --db_host <hostname>

数据库服务器的主机

- Windows上的localhost
- 否则是UNIX套接字

### --db_port <port> 

数据库侦听的端口，默认为5432

### --db-filter <filter> 

隐藏与<filter>不匹配的数据库。 过滤器是一个正则表达式，增加了：

- `%h` 由请求所在的整个主机名替换。

- `%d` 由请求所在的子域替换，但www除外（因此域odoo.com和www.odoo.com都匹配数据库odoo）。

  这些操作区分大小写。 添加选项（？i）以匹配所有数据库（因此域odoo.com使用（？i）％d匹配数据库Odoo）。



从版本11开始，还可以使用-database参数并指定以逗号分隔的数据库列表来限制对给定数据库的访问组合这两个参数时，db-filter取代了逗号分隔的数据库列表以限制数据库列表，而逗号分隔列表用于执行请求的操作，如模块升级。

```python
odoo-bin --db-filter ^11.*$
#限制对名称以11开头的数据库的访问
odoo-bin --database 11firstdatabase,11seconddatabase
#限制只能访问两个数据库，11firstdatabase和11seconddatabase
odoo-bin --database 11firstdatabase,11seconddatabase -u base
#限制只访问两个数据库，11firstdatabase和11seconddatabase，并在一个数据库上更新基本模块：11firstdatabase如果数据库11seconddatabase不存在，则创建数据库并安装基本模块
odoo-bin --db-filter ^11.*$ --database 11firstdatabase,11seconddatabase -u base
#限制对名称以11开头的数据库的访问，并在一个数据库上更新基本模块：11firstdatabase如果数据库11seconddatabase不存在，则创建数据库并安装基本模块
```



### --db-template <template> 

从数据库管理屏幕创建新数据库时，请使用指定的模板数据库。 默认为template0。


### --no-database-list 

禁止列出系统上可用的数据库

### --db_sslmode 

控制Odoo和PostgreSQL之间连接的SSL安全性。值应该是

‘disable’, ‘allow’, ‘prefer’, ‘require’, ‘verify-ca’ or ‘verify-full’ Default value is ‘prefer’ 

'禁用'，'允许'，'首选'，'需要'，'验证-ca'或'验证完整'之一，默认值是'首选'



## 国际化Internationalisation

使用这些选项将Odoo翻译成另一种语言。 请参阅用户手册的i18n部分。 选项'-d'是强制性的。 在输入的情况下，选项'-l'是强制性的

### --load-language <languages> 

指定要加载的翻译的语言（以逗号分隔）

### -l, --language <language> 

指定翻译文件的语言。 与-i18n-export或-i18n-import一起使用

### --i18n-export <filename> 

将要翻译的所有句子导出为CSV文件，PO文件或TGZ存档并退出。

### --i18n-import <filename> 

导入包含翻译的CSV或PO文件并退出。 '-l'选项是必需的。

### --i18n-overwrite 

覆盖更新模块或导入CSV或PO文件的现有翻译术语。

### --modules

指定要导出的模块。 与-i18n-export结合使用



## 内置HTTP		built-in HTTP

### --no-http 

不要启动HTTP或长轮询worker（可能仍然启动cron worker）
如果设置了--test-enable，则无效，因为测试需要可访问的HTTP服务器

### --http-interface <interface> 

HTTP服务器侦听的TCP / IP地址，默认为0.0.0.0（所有地址）

### --http-port <port> 

HTTP服务器侦听的端口，默认为8069。

### --longpolling-port <port> 

用于多处理或gevent模式下的长轮询连接的TCP端口，默认为8072.未在默认（线程）模式下使用。



## logging

默认情况下，Odoo显示除工作流日志记录（仅警告）之外的所有级别信息日志记录，并将日志输出发送到stdout。 有多种选项可用于将日志记录重定向到其他目标并自定义日志记录输出量

### --logfile <file> 

将日志记录输出发送到指定的文件而不是stdout。 在Unix上，该文件可以通过外部日志轮换程序进行管理，并在替换时自动重新打开

### -logrotate 

每天启用日志轮换，保留30个备份。 日志轮换频率和备份数量不可配置。

内置日志轮换在多工作方案中不可靠，可能会导致严重的数据丢失。 强烈建议使用外部日志轮换实用程序或使用系统记录器（-syslog）。

### --syslog 

记录到系统的事件记录器：unices上的syslog和Windows上的事件日志。

两者都不可配置

### --log-db <dbname> 

记录到指定数据库的ir.logging模型（ir_logging表）。 数据库可以是“当前”PostgreSQL中的数据库的名称，或者是例如PostgreSQL的URI。 日志聚合

### --log-handler <handler-spec> 

LOGGER：LEVEL，在提供的LEVEL上启用LOGGER，例如： odoo.models：DEBUG将在模型中启用DEBUG级别或更高级别的所有日志消息。

冒号：是强制性的
可以省略记录器来配置根（默认）处理程序
如果省略级别，则记录器设置为INFO
可以重复该选项以配置多个记录器，例如

```powershell
$ odoo-bin --log-handler :DEBUG --log-handler werkzeug:CRITICAL --log-handler odoo.fields:WARNING
```

### --log-request 

为RPC请求启用DEBUG日志记录，相当于--log-handler=odoo.http.rpc.request:DEBUG 

### --log-response 

enable DEBUG logging for RPC responses, equivalent to --log-handler=odoo.http.rpc.response:DEBUG

### --log-web

启用DEBUG记录HTTP请求和响应，相当于--log-handler=odoo.http:DEBUG

### --log-sql 

 启用SQL查询的DEBUG日志记录，相当于 --log-handler=odoo.sql_db:DEBUG

### --log-level <level> 

可以更轻松地在特定记录器上设置预定义级别的快捷方式。 在odoo和werkzeug记录器上设置“真实”级别(`critical`, `error`, `warn`, `debug`) （除了仅在odoo上设置的`debug`）。



Odoo还提供适用于不同记录器集的调试伪级别：

debug_sql 	将SQL记录器设置为debug	相当于--log-sql

debug_rpc  	设置odoo和HTTP请求记录器进行调试	相当于--log-level debug --log-request

debug_rpc_answer  设置odoo和HTTP请求和响应记录器进行调试   相当于--log-level debug --log-request --log-response

如果--log-level和--log-handler之间发生冲突，则使用后者



##emails

### --email-from <address> 

当Odoo需要发送邮件时用作<FROM>的电子邮件地址

### --smtp <server> 

要连接的SMTP服务器的地址以便发送邮件

###### `--smtp-port <port>`

###### `--smtp-ssl`

如果设置，odoo应使用SSL / STARTSSL SMTP连接

### --smtp-user <name> 

用于连接SMTP服务器的用户名

### --smtp-password <password> 

用于连接SMTP服务器的密码



## Scaffolding  

脚手架是自动创建骨架结构以简化引导（在Odoo的情况下，新模块）。 虽然没有必要，但它避免了设置基本结构和查找所有起始要求的乏味。

可以通过odoo-bin scaffold子命令获得脚手架

`python .\odoo-bin scaffold openacademy public`

### -t <template> 

一个模板目录，文件通过jinja2传递，然后复制到目标目录

### name 

要创建的模块的名称，可以用各种方式来生成程序名称（例如模块目录名称，型号名称......）

### destination目标目录

在其中创建新模块的目录，默认为当前目录



## 配置文件

大多数命令行选项也可以通过配置文件指定。 大多数情况下，他们使用类似的名称，前缀 - 删除和其他 - 被_替换为 --db-template变为db_template。

某些转化与模式不符：

--db-filter变为dbfilter
--no-http对应于http_enable布尔值
记录预设（除了--log-handler和--log-db之外的所有以--log-开头的选项）只是将内容添加到log_handler，直接在配置文件中使用
--smtp存储为smtp_server
--database存储为db_name
--i18n-import和--i18n-export根本不可用于配置文件

默认配置文件是$ HOME / .odoorc，可以使用--config覆盖它。 指定--save会将当前配置状态保存回该文件。











