[TOC]



## pip 的使用

pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。 

目前如果你在 [python.org](https://www.python.org/) 下载最新版本的安装包，则是已经自带了该工具。

​	Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。

**pip 官网：**<https://pypi.org/project/pip/>

## 安装pip

你可以通过以下命令来判断是否已安装：

```powershell
pip --version
```

如果你还未安装，则可以使用以下方法来安装：

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
```

> **注意：**用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：
>
> ```
> $ sudo python3 get-pip.py    # 运行安装脚本。
> ```
>
> 一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。

 Linux 发行版可直接用包管理器安装 pip，如 Debian 和 Ubuntu：

```powershell
sudo apt-get install python-pip	#python2.*
或
sudo apt-get install python3-pip #python3.*
```



## 常用命令 

**安装包**

```powershell
sudo pip3 install [package]
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
```

**查看安装的python包 :**

```powershell
pip3 list
```

**搜索python包 :**

```powershell
pip3 search [package]
```

**升级软件包 :** 

```powershell
pip3 install --upgrade [package]
pip install --upgrade SomePackage
升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
```

**查看软件包的信息 :**

```powershell
pip3 show [package]
查看指定包的详细信息
pip show -f SomePackage
```

**卸载软件包  :**

```powershell
pip3 uninstall [package]
```

**导出软件包环境  :**

```powershell
pip3 freeze > [requirements.txt]
```

**安装软件环境 :**

```powershell
pip3 install -r [requirements.txt] #在目标主机
```

**显示版本和路径**

```
pip --version
```

**获取帮助**

```
pip --help
```

**升级 pip**

```
pip install -U pip
```

如果这个升级命令出现问题 ，可以使用以下命令：

```
sudo easy_install --upgrade pip
```

**查看可升级的包**

```
pip list -o
```

### 注意事项

如果 Python2 和 Python3 同时有 pip，则使用方法如下：

Python2：

```
python2 -m pip install XXX
```

Python3:

```
python3 -m pip install XXX
```