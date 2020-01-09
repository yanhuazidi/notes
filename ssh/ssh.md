[TOC]



## 概述

SSH是一种网络协议，用于计算机之间的加密登录。本文针对的实现是OpenSSH，它是自由软件，应用非常广泛

SSH连接是CS模型（客户端-服务器），客户端发出连接申请，服务器对客户端进行验证，再考虑是否接受连接申请。
SSH的安全加密方式的理论基础是非对称加密体系

SSH有**两种方式**的用户登录认证



## 管理SSH

### 安装

如果你用的是redhat，fedora，centos等系列linux发行版，那么敲入以下命令：

```shell
sudo yum install sshd 
# 或
sudo yum install openssh-server
```

如果你使用的是debian，ubuntu，linux mint等系列的linux发行版，那么敲入以下命令：

```shell
sudo apt-get install sshd
# 或
sudo apt-get install openssh-server
```



### 运行服务

```shell
sshd [-46DdeiqTt] [-C connection_spec] [-c host_certificate_file] [-E log_file] [-f config_file] [-g login_grace_time] [-h host_key_file][-o option] [-p port] [-u len]

```

`sshd `监听来自客户端的连接。它通常在从`/etc/init.d/ssh`启动时自动启动。它为每个传入连接派生一个新的守护进程。分叉守护进程处理密钥交换、加密、身份验证、命令执行和数据交换。

**手动启动**

```shell
service sshd start | restart | stop |status
```



sshd可以使用命令行选项或配置文件（默认情况下为`sshd_config(5)`）；命令行选项覆盖配置文件中指定的值。sshd在接收到挂断信号SIGHUP时重新读取其配置文件，方法是使用名称和启动选项执行自己，例如`/usr/sbin/sshd`

**选项如下：**

- **-4**    强制sshd仅使用IPv4地址

- **-6**    强制sshd仅使用IPv6地址

- **-C connection_spec**    指定要用于-T扩展测试模式的连接参数。如果提供，配置文件中应用于指定用户、主机和地址的任何匹配指令都将在配置写入标准输出之前设置。连接参数将作为关键字=值对提供。关键字是“user”、“host”、“laddr”、“lport”和“addr”。所有这些都是必需的，可以按任意顺序提供，可以是多个-C选项，也可以是逗号分隔的列表

- **-c host_certificate_file**   指定在密钥交换期间标识sshd的证书文件的路径。证书文件必须与主机密钥文件规范匹配

  使用-h选项或HostKey配置指令验证

- **-D**   指定此选项时，sshd不会分离，也不会成为守护进程。这样可以方便地监视sshd

- **-d**  调试模式。服务器将详细的调试输出发送到标准错误，而不将自己放在后台。服务器也不会分叉，只处理一个连接。此选项仅用于调试服务器

- **-E log_file**  将调试日志附加到日志文件，而不是系统日志

- **-e**   将调试日志写入标准错误而不是系统日志

- **-f config_file**    指定配置文件的名称。默认为`/etc/ssh/sshd_config`。如果没有配置文件，sshd将拒绝启动

-  **-g login_grace_time**   为客户端验证自身提供宽限时间（默认为120秒）。如果客户端在这段时间内无法验证用户，服务器断开并退出。值为零表示没有限制。

-  **-h host_key_file**   指定从中读取主机密钥的文件。如果sshd不是以根用户身份运行（因为除了根用户以外，其他用户通常都无法读取正常的主机密钥文件），则必须提供此选项。默认为`/etc/ssh/ssh_host_rsa_key`、`/etc/ssh/ssh_host_ecdsa_key`和`/etc/ssh/ssh_host_ed25519_key`。对于不同的主机密钥算法，可能有多个主机密钥文件

- **-i**     指定sshd是从inetd（8）运行的。

- **-p  prot**   指定服务器侦听连接的端口（默认22）。允许多端口选项。当指定命令行端口时，配置文件中使用Port选项指定的端口将被忽略。使用`ListenAddress`选项指定的端口覆盖命令行端口。

- **-q**  静音模式。不会向系统日志发送任何内容。通常记录每个连接的开始、身份验证和终止。

- **-T**   扩展测试模式。检查配置文件的有效性，将有效配置输出到STDUT，然后退出。或者，可以通过使用一个或多个-C选项指定连接参数来应用匹配规则。

- **-t**   测试模式。只检查配置文件的有效性和密钥的健全性。这对于可靠地更新sshd很有用，因为配置选项可能会改变。

  

### 卸载

如果你用的是redhat，fedora，centos等系列linux发行版，那么敲入以下命令：

```shell
yum remove sshd
```


如果你使用的是debian，ubuntu，linux mint等系列的linux发行版，那么敲入以下命令：

```shell
sudo apt-get –purge remove sshd
```



## 密码登录

只要你知道自己帐号和口令，就可以登录到远程主机。所有传输的数据都会被加密，但是不能保证你正在连接的服务器就是你想连接的服务器。可能会有别的服务器在冒充真正的服务器，也就是受到“中间人”这种方式的攻击。

**大致流程：**

1. 客户端发起ssh请求，服务器会把自己的公钥发送给用户
2. 用户会根据服务器发来的公钥对密码进行加密
3. 加密后的信息回传给服务器，服务器用自己的私钥解密，如果密码正确，则用户登录成功

### 中间人攻击

SSH之所以能够保证安全，原因在于它采用了公钥加密。在重复下密码登录的方式

（1）远程主机收到用户的登录请求，把自己的公钥发给用户。

（2）用户使用这个公钥，将登录密码加密后，发送回来。

（3）远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录。

这个过程本身是安全的，但是实施的时候存在一个风险：如果有人截获了登录请求，然后冒充远程主机，将伪造的公钥发给用户，那么用户很难辨别真伪。因为不像https协议，SSH协议的公钥是没有证书中心（CA）公证的，也就是说，都是自己签发的。可以设想，如果攻击者插在用户与远程主机之间（比如在公共的wifi区域），用伪造的公钥，获取用户的登录密码。再用这个密码登录远程主机，那么SSH的安全机制就荡然无存了。这种风险就是著名的”中间人攻击”（Man-in-the-middle attack）。SSH协议是如何应对的呢？就是通过基于密钥的登录方式登录。



### ssh命令基本用法

假设非第一次登录

假定你要以用户名user，登录远程主机192.168.0.100

```shell
laopi@debian:~$ ssh user@192.168.0.100
#或
laopi@debian:~$ ssh -l user 192.168.0.100
# 如果本地用户名与远程用户名一致，登录时可以省略用户名
laopi@debian:~$ ssh 192.168.0.100
```

SSH的默认端口是22，也就是说，你的登录请求会送进远程主机的22端口。使用p参数，可以修改这个端口。

```shell
laopi@debian:~$ ssh -p 2222 user@192.168.0.100

laopi@debian:~$ ssh -p 2222 -l user 192.168.0.100

laopi@debian:~$ ssh -I private_key.file -p 2222 -l user 192.168.0.100
```





### 查看远程主机公钥指纹

事先在远程的服务器上通过下面的命令查看

`ssh-keygen -E md5 -lf /etc/ssh/ssh_host_rsa_key.pub`

```shell
ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub
ea:a6:60:d4:51:c3:44:fc:7b:9c:6e:4b:1b:6f:5b:89.
```

上面生成的密钥对都是通过RSA算法生成的，有的发行版也许算法不是 RSA ，而是 DSA或ECDSA 之类的，寻找对应公钥文件的时候需要注意一下，默认情况下密钥对都在/etc/ssh/目录下，包括不同算法的公钥，私钥



### 通过ssh命令第一次登录对方主机

第一次登录，客户端发起ssh请求，服务器会把自己的公钥发送给用户，因为第一次登录对方，无法确认host主机的真实性，只知道它的公钥指纹，终端会询问是否继续链接

```shell
# 客户机为 CentOS5.9系统
:~$ ssh root@192.168.1.82
The authenticity of host '192.168.1.82 (192.168.1.82)' can't be established.
# 无法建立主机“192.168.1.82（192.168.1.82）”的真实性
RSA key fingerprint is ea:a6:60:d4:51:c3:44:fc:7b:9c:6e:4b:1b:6f:5b:89.
# RSA密钥指纹是 ea:a6:60:d4:51:c3:44:fc:7b:9c:6e:4b:1b:6f:5b:89.
Are you sure you want to continue connecting (yes/no)?
# 是否确实要继续连接（是/否）？
```

**公钥指纹**  ：  因为公钥采用RSA算法，长达2048位，很难对比，所以客户机会对公钥进行摘要计算(`SHA256`或 `MD5` ),  上例中是ea:a6:60:d4:51:c3:44:fc:7b:9c:6e:4b:1b:6f:5b:89，通过`MD5`计算



决定接受这个远程主机的公钥输入yes回车，回车后不要输入密码登录，而是按`Ctrl+C`组合键中止会话，这时候也会生成`~/.ssh/known_hosts`s文件，我们可以通过`known_hosts`文件得到对应的指纹，因为远程服务器的公钥已经保存在这个文件中，命令如下：

```shell
:~/.ssh$ ssh-keygen -E md5 -lf known_hosts
```

通过和远程主机的公钥相同摘要算法计算的指纹对比，就能确认主机的身份



#### 登录主机

当我们决定接受这个远程主机的公钥的时候输入yes回车：

```shell
:~$ ssh root@192.168.1.82
The authenticity of host '192.168.1.82 (192.168.1.82)' can't be established.
RSA key fingerprint is SHA256:x+yJlwiVM1tzFvSmHFMwiWX7s6Jhf8CZE37pq6/FHrw.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.82' (RSA) to the list of known hosts.
root@192.168.1.82's password: 
```

上面出现的一句提示，表示host主机已经得到认可，然后，会要求输入密码。如果密码正确，就可以登录了。



#### 保存远程主机公钥

当远程主机的公钥被接受以后，它就会被保存在用户主目录下的`.ssh`目录中的`known_hosts`文件中。下次再连接这台主机，系统就会认出它的公钥已经保存在本地了，从而跳过警告部分，直接提示输入密码。

每个SSH用户都有自己的`known_hosts`文件，此外系统层也有一个这样的文件，通常是`/etc/ssh/ssh_known_hosts`，保存对本机所有用户都可信赖的远程主机的公钥



#### 查看公钥文件

`known_hosts`可以保存多个公钥文件，每个访问过计算机的公钥(public key)都记录在`~/.ssh/known_hosts`文件中

**查看公钥指纹：**

```shell
laopi@debian:~/.ssh$ ssh-keygen -E md5 -lf known_hosts 
2048 MD5:ea:a6:60:d4:51:c3:44:fc:7b:9c:6e:4b:1b:6f:5b:89 192.168.1.82 (RSA)
256 MD5:64:d6:56:fa:48:78:2c:27:2c:a4:27:9c:70:31:13:98 192.168.1.80 (ECDSA)
```

通过上面的方法可以查看每个公钥的指纹，并且可以知道每个公钥的加密方式，上面两个公钥分别是通过RSA 2048位加密和ECDSA 256位加密。

**查看公钥：**

```shell
laopi@debian:~/.ssh$ cat known_hosts       
192.168.1.82 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA159Qo8XpaqG6WAC7r33wIInBCGWeux/Bun7LYu28U/Vt2CrSSbqoakTUBdS7Gsn8Kj9ZQ55qW/dSwkBMthTaAd3W5X+jtLKymjfSWTLxzlBaX52q64YHop/mA2o88KgVZt/aNOS3iMrD5PI2xXcnUSms2CK6Ps1rWR83QEWorqrY3A/SRWNU0mwNAMOXX55KBQjS06kdbpmnv5csIBxODJi0C5hjfCuWxfXyibZlra4VXW4JAI4Fxo+v9nYK2DWd6bfGS3FRYPuoy0hzAI1WqmzSb+3M4RF81JjZOMZT0yT5BR1RlwX9+32WerO9v2T2PceYdBGY3dtxMLvwouLz7Q==
192.168.1.80 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBATw5wuZnAwuiX6XrwcHcgHnrha9xPqt739GKTl5cSjkn4mxr7STy4bimus/Wd7lOcEZ1C0SlzmZOINQ3TtICuQ=
```

通过上面的方法是直接查看`known_hosts`文件的内容，可以看到两个主机的IP地址和公钥密文



#### 清理过期的公钥

如果远程的服务器重新安装系统，或其他原因使公钥消失，而本地公钥信息还在，公钥不同，连接就会出现错误

1. 在文件中直接删除对应ip的相关rsa公钥信息或其他公钥信息

   ```shell
   vi ~/.ssh/known_hosts
   ```

2. 通过命令删除对应ip的相关rsa公钥信息或其他公钥信息

   ```shell
   ssh-keygen -R 192.168.0.100
   ```



## 密钥登录

需要依靠密匙，也就是你必须为自己创建一对密匙，并把公用密匙放在需要访问的服务器上。但是，与密码登录相比，密钥登录不需要在网络上传送口令。

密钥登录不仅加密所有传送的数据，而且“中间人”这种攻击方式也是不可能的（因为他没有你的私人密匙）。但是整个登录的过程会比基于passwd认证稍长，可能需要10秒

**大致流程：**

1. 首先在客户端生成一对密钥
2. 并将客户端的公钥ssh-copy-id拷贝到服务器端
3. 当客户端再次发送一个连接请求，包括ip、用户名
4. 服务端得到客户端的请求后，会到`authorized_keys`中查找，如果有响应的IP和用户，服务器就会发出“质询”（challenge），表现为一串随机字符，如：abcd。
5. 服务端将使用客户端拷贝过来的公钥对“质询”进行加密，然后发送给客户端
6. 得到服务端发来“质询”后，客户端会使用私钥进行解密，然后将解密后的字符串发送给服务端
7. 服务端接受到客户端发来的字符串后，跟之前的字符串进行对比，如果一致，就允许免密码登录



### 创建SSH密钥

SSH有专门创建SSH密钥的工具**ssh-keygen**，

进入Linux系统的用户目录下的`.ssh`目录下，root用户是`/root/.ssh`，普通用户是/home/您的用户名/.ssh，我们以root用户为例：

```shell
cd /root/.ssh
ssh-keygen -t rsa   #执行ssh-keygen命令创建密钥对
```

执行密钥生成命令，基本上是一路回车既可以了

但是需要注意的是：执行命令的过程中是会提示输入密钥的密码的, 不需要密码直接回车就行



密钥生成后会在当前目录下多出两个文件，id_rsa和id_rsa.pub，其中id_rsa是私钥，id_rsa.pub这个是公钥，



### 配置公钥

把公钥拷贝到需要登录的远程服务器或Linux系统上，这里可以使用ssh-copy-id自动完成，也可以手动追加秘钥到远程服务器。

**使用ssh-copy-id自动完成**

```shell
ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.100.10
```

执行命令了会要求输入远程机器的密码，输入密码即可。

注：ssh-copy-id默认端口是22，如果您的SSH端口不是22，也就是远程服务器端口修改成其他的了，那就要得加上 -p +端口。



**手动追加秘钥**

进入远程服务器需要SSH登录的用户的目录下，这里仍然用root用户，执行ls看看目录下是否有authorized_keys文件没有的话则执行以下命令创建：

```shell
cd /root/.ssh
touch authorized_keys   #创建空authorized_keys文件
chmod 600 /root/.ssh/authorized_keys  #授予600权限（注意：此处权限必须是600）

```



如果已经有了authorized_keys文件，这直接执行以下的密钥追加工作。

将上面生成的公钥id_rsa.pub追加到authorized_keys文件中：

```shell
cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
```



密钥准备好了接下来就可以使用密钥登录了

```shell
ssh -i ./id_rsa root@192.168.100.39
```



## OpenSSH配置文件

OpenSSH常用配置文件有两个`/etc/ssh/ssh_config` 和 `/etc/ssh/sshd_config`
ssh_config 为客户端配置文件，sshd_config 为服务端配置文件，此外/etc/ssh/目录中还有一些其他文件，对这些文件进行下说明：

- moduli            # 配置用于构建安全传输层 所必须的密钥组    

- ssh_host_ecdsa_key            #SSH2版本所使用的ecdsa私钥
- ssh_host_ecdsa_key.pub        #SSH2版本所使用的ecdsa公钥
- ssh_host_ed25519_key          #SSH2版本所使用的ed25519私钥
- ssh_host_ed25519_key.pub      #SSH2版本所使用的ed25519公钥
- ssh_host_rsa_key              #SSH2版本所使用的RSA私钥
- ssh_host_rsa_key.pub          #SSH2版本所使用的RSA公钥

 

### SSH客户端配置文件

`/etc/ssh/ssh_config`

配置文件概要
ssh 按以下顺序从以下源获取配置数据：
1、命令行选项
2、用户的配置文件（〜/.ssh/config）
3、系统范围的配置文件（/etc/ssh/ssh_config）
对于每个参数，将使用第一个获得的值。配置文件包含按Host 规范分隔的部分，该部分仅适用于与规范中给出的模式之一匹配的主机。匹配的主机名通常是命令行中给出的主机名。
由于使用了每个参数的第一个获取值，因此应在文件开头附近给出更多特定于主机的声明，并在结尾处给出一般默认值。
该文件包含关 键字和参数，每行一个。、
部分的关键字及其含义如下（请注意，关键字不区分大小写，参数区分大小写）：



详细的参数可以查看官方文件说明：https://man.openbsd.org/ssh_config

```shell
Host *        #选项“Host”只对能够匹配后面字串的计算机有效。“*”表示所有的计算机。

ForwardAgent no     #设置连接是否经过验证代理（如果存在）转发给远程计算机。

ForwardX11 no        #设置X11连接是否被自动重定向到安全的通道和显示集（DISPLAY set）

RhostsAuthentication no     #设置是否使用基于rhosts的安全验证。

RhostsRSAAuthentication no     #设置是否使用用RSA算法的基于rhosts的安全验证。

RSAAuthentication yes           #设置是否使用RSA算法进行安全验证。

PasswordAuthentication yes     #设置是否使用口令验证。

FallBackToRsh no               #设置如果用ssh连接出现错误是否自动使用rsh。

UseRsh no                      #设置是否在这台计算机上使用“rlogin/rsh”。

BatchMode no                   #如果设为“yes”，passphrase/password（交互式输入口令）的提示将被禁止。当不能交互式输入口令的时候，这个选项对脚本文件和批处理任务十分有用。

CheckHostIP yes               #设置ssh是否查看连接到服务器的主机的IP地址以防止DNS欺骗。建议设置为“yes”。

StrictHostKeyChecking no     #如果设置成“yes”，ssh就不会自动把计算机的密匙入“$HOME/.ssh/known_hosts”文件，并且一旦计算机的密匙发生了变化， 就拒绝连接。

IdentityFile ~/.ssh/identity       #设置从哪个文件读取用户的RSA安全验证标识。

Port 22                             #设置连接到远程主机的端口。

Protocol 2,1　　              # 选择的 SSH 协议版本，可以是 1 也可以是 2 ，如果要同时支持两者，就必须要使用 2,1 这个分隔了！

GSSAPIAuthenticationno       #是否允许使用基于GSSAPI 的用户认证.默认值为"yes".仅用于SSH-2

Cipher blowfish           #设置加密用的密码。

EscapeChar ~             #设置escape字符。
```



### SSH服务端守护程序配置文件

`/etc/ssh/sshd_config`

配置文件概要
sshd从 `/etc/ssh/sshd_config`（或-f在命令行中指定的文件）读取配置数据。该文件包含 关键字和参数，每行一个。对于每个关键字，将使用第一个获得的值。以' #'和空行开头的行被解释为注释。参数可以可选地用双引号（“）括起来，以表示包含空格的参数。
可能的关键字及其含义如下（请注意，关键字不区分大小写，参数区分大小写）：



详细的参数可以查看官方文件说明：https://man.openbsd.org/sshd_config

```shell
AddressFamily any  #指定 sshd 应当使用哪种地址族。取值范围是："any"(默认)、"inet"(仅IPv4)、"inet6"(仅IPv6)。 any表示二者均有。

AuthorizedKeysFile  .ssh/authorized_keys   # 指定包含用于用户身份验证的公钥的文件 

AllowGroups   #这个指令后面跟着一串用空格分隔的组名列表(其中可以使用"*"和"?"通配符)。默认允许所有组登录。如果使用了这个指令，那么将仅允许这些组中的成员登录，而拒绝其它所有组。这里的"组"是指"主组"(primary group)，也就是/etc/passwd文件中指定的组。这里只允许使用组的名字而不允许使用GID。相关的 allow/deny 指令按照下列顺序处理：DenyUsers, AllowUsers, DenyGroups, AllowGroups

AllowUsers    #这个指令后面跟着一串用空格分隔的用户名列表(其中可以使用"*"和"?"通配符)。默认允许所有用户登录。如果使用了这个指令，那么将仅允许这些用户登录，而拒绝其它所有用户。如果指定了 USER@HOST 模式的用户，那么 USER 和 HOST 将同时被检查。这里只允许使用用户的名字而不允许使用UID。相关的 allow/deny 指令按照下列顺序处理：DenyUsers, AllowUsers, DenyGroups, AllowGroups

Banner   #将这个指令指定的文件中的内容在用户进行认证前显示给远程用户。这个特性仅能用于SSH-2，默认什么内容也不显示。"none"表示禁用这个特性。

Compression yes　#是否可以使用压缩指令？

ChallengeResponseAuthentication yes #是否允许质疑-应答(challenge-response)认证。默认值是"yes"。所有 login.conf 中允许的认证方式都被支持。规定的认证方式，均可适用！

DenyGroups    #这个指令后面跟着一串用空格分隔的组名列表(其中可以使用"*"和"?"通配符)。默认允许所有组登录。 如果使用了这个指令，那么这些组中的成员将被拒绝登录。 这里的"组"是指"主组"(primary group)，也就是/etc/passwd文件中指定的组。这里只允许使用组的名字而不允许使用GID。相关的 allow/deny 指令按照下列顺序处理： DenyUsers, AllowUsers,DenyGroups,AllowGroups，

DenyUsers    #这个指令后面跟着一串用空格分隔的用户名列表(其中可以使用"*"和"?"通配符)。默认允许所有用户登录。 如果使用了这个指令，那么这些用户将被拒绝登录。 如果指定了 USER@HOST 模式的用户，那么 USER 和 HOST 将同时被检查。 这里只允许使用用户的名字而不允许使用UID。相关的 allow/deny 指令按照下列顺序处理： DenyUsers, AllowUsers, DenyGroups, AllowGroups

ForceCommand    #强制执行这里指定的命令而忽略客户端提供的任何命令。这个命令将使用用户的登录shell执行(shell -c)。这可以应用于 shell 、命令、子系统的完成，通常用于 Match 块中。这个命令最初是在客户端通过 SSH_ORIGINAL_COMMAND 环境变量来支持的。

HostKey /etc/ssh/ssh_host_key　

SSH version 1 #使用的私钥

HostKey /etc/ssh/ssh_host_rsa_key　

SSH version 2 #使用的 RSA 私钥

HostKey /etc/ssh/ssh_host_dsa_key　

SSH version 2 #使用的 DSA 私钥

HostbasedAuthentication no      #在开启 HostbasedAuthentication 的情况下， 指定服务器在使用 ~/.shosts ~/.rhosts /etc/hosts.equiv 进行远程主机名匹配时，是否进行反向域名查询。 "yes"表示 sshd 信任客户端提供的主机名而不进行反向查询。默认值是"no"。

IgnoreRhosts yes　 #是否在 RhostsRSAAuthentication 或 HostbasedAuthentication 过程中忽略 .rhosts 和 .shosts 文件。不过 /etc/hosts.equiv 和 /etc/shosts.equiv 仍将被使用。推荐设为默认值"yes"。

IgnoreUserKnownHosts no　   #是否在 RhostsRSAAuthentication 或 HostbasedAuthentication 过程中忽略用户的 ~/.ssh/known_hosts 文件。默认值是"no"。为了提高安全性，可以设为"yes"。

KeyRegenerationInterval 3600　 　　#由前面联机的说明可以知道， version 1 会使用 server 的 Public Key ，每隔一段时间来重新建立一次！时间为秒！

ListenAddress 0.0.0.0　    #监听的主机适配卡！举个例子来说，如果您有两个 IP，分别是 192.168.0.100 及 192.168.2.20 ，那么只想要开放 192.168.0.100 时， 就可以写如同下面的样式： ListenAddress 192.168.0.100 只监听来自 192.168.0.100 这个IP 的SSH联机。如果不使用设定的话，则预设所有接口均接受 SSH，即：0.0.0.0表示本机的所有地址  

ListenAddress ::    #指明监听的IPV6的所有地址格式。

LoginGraceTime 600　   #当使用者连上 SSH server 之后，会出现输入密码的画面，在该画面中，在多久时间内没有成功连上 SSH server ，就断线！时间为秒！

LogLevel INFO　　　#指定 sshd 的日志等级(详细程度)   

MaxAuthTries  6     #指定每个连接最大允许的认证次数。默认值是 6 。 如果失败认证的次数超过这个数值的一半，连接将被强制断开，且会生成额外的失败日志消息。  

Maxsessions  10      #同一地址的最大连接数,也就是同一个IP地址最大可以保持多少个链接

MaxStartups  10:30:100    #同时允许几个尚未登入的联机画面,所谓联机画面就是在你ssh登录的时候,没有输入密码的阶段。

Port 22　　　　       #SSH 预设使用 22 这个 port，您也可以使用多的 port ！

Protocol 2,1　　    #选择的 SSH 协议版本，可以是 1 也可以是 2 ，如果要同时支持两者，就必须要使用 2,1 这个分隔了！

PidFile /var/run/sshd.pid　　　#可以放置 SSHD 这个 PID 的档案！左列为默认值

PermitRootLogin no　　#是否允许 root 用户直接登录，如果想root直接登录设置为yes，安全方面的考虑最好设置成no

PubkeyAuthentication yes　  #是否允许公钥认证。仅可以用于SSH-2

PasswordAuthentication yes       #是否允许使用基于密码的认证

PermitEmptyPasswords no　　 #上面那一项如果设定为 yes 的话，这一项就最好设定为 no ，这项为是否允许密码为空的用户远程登录

PAMAuthenticationViaKbdInt yes     #是否启用其它的 PAM 模块！启用这个模块将会导致 PasswordAuthentication 设定失效！

PrintMotd no                #指定 sshd 是否在每一次交互式登录时打印 /etc/motd 文件的内容。

PrintLastLog yes　　　　 #指定 sshd 是否在每一次交互式登录时打印最后一位用户的登录时间。

RSAAuthentication yes　　   #是否使用纯的 RSA 认证！？仅针对 version 1 ！

RhostsAuthentication no　　   #本机系统不使用 .rhosts ， .rhosts 不安全！

RhostsRSAAuthentication no   #是否使用强可信主机认证(通过检查远程主机名和关联的用户名进行认证)。仅用于SSH-1。这是通过在RSA认证成功后再检查 ~/.rhosts 或 /etc/hosts.equiv 进行认证的。 出于安全考虑，建议使用默认值"no"。

Subsystem   #配置一个外部子系统(例如，一个文件传输守护进程)。仅用于SSH-2协议。 值是一个子系统的名字和对应的命令行(含选项和参数)。

ServerKeyBits 1024 　#Server key 的长度！

SyslogFacility AUTH　　　#配置sshd发送到syslog所使用的日志类型，当有人使用ssh登录系统的时候，SSH会记录信息，信息保存在/var/log/secure里面

SyslogFacility AUTHPRIV     #默认日志类型为AUTHPRIV

StrictModes yes　　　　#指定是否要求 sshd在接受连接请求前对用户主目录和相关的配置文件进行宿主和权限检查。 强烈建议使用默认值"yes"来预防可能出现的低级错误。

UserLogin no　　　#在 SSH 底下本来就不接受 login 这个程序的登入！

UsePrivilegeSeparation yes  #是否让 sshd 通过创建非特权子进程处理接入请求的方法来进行权限分离。默认值是"yes"。认证成功后，将以该认证用户的身份创建另一个子进程。这样做的目的是为了防止通过有缺陷的子进程提升权限，从而使系统更加安全。

UseDNS yes            #指定 sshd是否应该对远程主机名进行反向解析，以检查此主机名是否与其IP地址真实对应

UseLogin   #是否在交互式会话的登录过程中使用 login 。默认值是"no"。如果开启此指令，那么 X11Forwarding 将会被禁止，因为 login不知道如何处理 xauth cookies 。需要注意的是，login 是禁止用于远程执行命令的。如果指定了 UsePrivilegeSeparation ，那么它将在认证完成后被禁用。

UsePAM yes   #利用 PAM 管理使用者认证有很多好处，可以记录与管理。所以这里我们建议你使用 UsePAM 且 ChallengeResponseAuthentication 设定为 no 

X11DisplayOffset   #指定 sshd X11 转发的第一个可用的显示区(display)数字。默认值是 10 。这个可以用于防止 sshd 占用了真实的 X11 服务器显示区，从而发生混淆。

X11Forwarding   #是否允许进行 X11 转发。默认值是"no"，设为"yes"表示允许。如果允许X11转发并且sshd 代理的显示区被配置为在含有通配符的地址(X11UseLocalhost)上监听。那么将可能有额外的信息被泄漏。由于使用X11转发的可能带来的风险，此指令默认值为"no"。需要注意的是，禁止X11转发并不能禁止用户转发X11通信，因为用户可以安装他们自己的转发器。如果启用了 UseLogin ，那么X11转发将被自动禁止。

X11UseLocalhost   #sshd 是否应当将X11转发服务器绑定到本地loopback地址。默认值是"yes"。sshd 默认将转发服务器绑定到本地loopback地址并将 DISPLAY 环境变量的主机名部分设为"localhost"。这可以防止远程主机连接到 proxy display 。不过某些老旧的X11客户端不能在此配置下正常工作。为了兼容这些老旧的X11客户端，你可以设为"no"。

```

通常只配置上面的加粗字体选项就可以，端口号，是否允许密码登录，是否允许root直接登录。



## ssh-keygen

```shell
 -a trials   #在使用 -T 对 DH-GEX 候选素数进行安全筛选时需要执行的基本测试数量。
 
 -E fingerprint_hash  # 指定显示密钥指纹时使用的哈希算法。有效选项是：“md5”和“sha256”。默认值是“sha256”。
 
 -B     # 显示指定的公钥/私钥文件的 bubblebabble 摘要。
 
 -b bits  #指定密钥长度。对于RSA密钥，最小要求768位，默认是2048位。DSA密钥必须恰好是1024位(FIPS 186-2 标准的要求)。
 
 -C comment #提供一个新注释
 
 -c      # 要求修改私钥和公钥文件中的注释。本选项只支持 RSA1 密钥。程序将提示输入私钥文件名、密语(如果存在)、新注释。
 
 -D reader  #下载存储在智能卡 reader 里的 RSA 公钥。
 
 -e      # 读取OpenSSH的私钥或公钥文件，并以 RFC 4716 SSH 公钥文件格式在 stdout 上显示出来。该选项能够为多种商业版本的 SSH 输出密钥。
 
 -F hostname  #在 known_hosts 文件中搜索指定的 hostname ，并列出所有的匹配项。这个选项主要用于查找散列过的主机名/ip地址，还可以和 -H 选项联用打印找到的公钥的散列值。
 
 -f filename # 指定密钥文件名
 
 -l    # 显示公钥文件的指纹数据。它也支持 RSA1 的私钥。对于RSA和DSA密钥，将会寻找对应的公钥文件，然后显示其指纹数据。
 
 -G output_file   # 为 DH-GEX 产生候选素数。这些素数必须在使用之前使用 -T 选项进行安全筛选。
 
 -g     #在使用 -r 打印指纹资源记录的时候使用通用的 DNS 格式。
 
 -H     #对 known_hosts 文件进行散列计算。这将把文件中的所有主机名/ip地址替换为相应的散列值。原来文件的内容将会添加一个".old"后缀后保存。这些散列值只能被 ssh 和 sshd 使用。这个选项不会修改已经经过散列的主机名/ip地址，因此可以在部分公钥已经散列过的文件上安全使用。
 
 -i      # 读取未加密的SSH-2兼容的私钥/公钥文件，然后在 stdout 显示OpenSSH兼容的私钥/公钥。该选项主要用于从多种商业版本的SSH中导入密钥。
 
 
 -M memory  # 指定在生成 DH-GEXS 候选素数的时候最大内存用量(MB)。
 
 -N new_passphrase  # 提供一个新的密码
 
 -P passphrase   # 提供(旧)密码。
 
 -p      #要求改变某私钥文件的密码而不重建私钥。程序将提示输入私钥文件名、原来的密语、以及两次输入新密语。
 
 -q      # 安静模式。用于在 /etc/rc 中创建新密钥的时候
 
 -R hostname  # 从 known_hosts 文件中删除所有属于 hostname 的密钥。这个选项主要用于删除经过散列的主机(参见 -H 选项)的密钥。
 
 -r hostname  #打印名为 hostname 的公钥文件的 SSHFP 指纹资源记录。
 
 -S start  #指定在生成 DH-GEX 候选模数时的起始点(16进制)。
 
 -T output_file # 测试 Diffie-Hellman group exchange 候选素数(由 -G 选项生成)的安全性。
 
 -t type # 指定要创建的密钥类型。可以使用："rsa1"(SSH-1) "rsa"(SSH-2) "dsa"(SSH-2)
 
 -U reader   # 把现存的RSA私钥上传到智能卡 reader
 
 -v     #详细模式。ssh-keygen 将会输出处理过程的详细调试信息。常用于调试模数的产生过程。重复使用多个 -v 选项将会增加信息的详细程度(最大3次)。
 
 -W generator  #指定在为 DH-GEX 测试候选模数时想要使用的 generator
 
 -y      #读取OpenSSH专有格式的公钥文件，并将OpenSSH公钥显示在 stdout 上。
```


## ssh-copy-id的参数有：

```shell
-i # 指定密钥文件
-p # 指定端口，默认端口号是22
-o <ssh -o options> user@]hostname #用户名@主机名
-f  #强制模式   复制密钥而不尝试检查它们是否已安装
-n  #试运行   实际上没有密钥被复制
```



