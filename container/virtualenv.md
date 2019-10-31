

[TOC]



## 安装virtualenv

```powershell
pip install virtualenv
```



## 创建虚拟环境

安装完成之后，可以通过以下命令创建该博客的虚拟环境：

```powershell
virtualenv myblog
```



## 指定Python版本的虚拟环境(win==linux)

virtualenv -p 已经安装的指定版本的python执行文件 env

### 安装Python2.7版本的虚拟环境env-py2:

```powershell
virtualenv -p C:\Python27\python.exe env-py2
```

### 安装Python3.6版本的虚拟环境env-py3:

```powershell
virtualenv -p C:\Python36\python.exe env-py3
```



## 激活虚拟环境

### win中，定位到myblog/scripts中，执行activate.bat

```
activate.bat
```



### Linux 中

```
$ source venv/bin/activate
```



当前虚拟环境的名字会显示在提示符左侧（比如说 `(venv)您的电脑:您的工程 用户名$）以让您知道它是激活的。从现在起，任何您使用pip安装的包将会放在 ``venv` 文件夹中， 与全局安装的Python隔绝开。

像平常一样安装包，比如：

```
$ pip install requests
```



## 退出虚拟环境

Linux 中

```
deactivate
```

### win中，定位到myblog/scripts中，执行deactivate.bat

```
deactivate.bat
```



这将会回到系统默认的Python解释器，包括已安装的库也会回到默认的。

要删除一个虚拟环境，只需删除它的文件夹。（要这么做请执行 `rm -rf venv` ）



运行带 `--no-site-packages` 选项的 `virtualenv` 将不会包括全局安装的包。 这可用于保持包列表干净，以防以后需要访问它。（这在 `virtualenv` 1.7及之后是默认行为）



## freeze环境包当前的状态

**为了保持您的环境的一致性**

在虚拟环境中执行:

```powershell
$ pip freeze > requirements.txt
```

这将会在当前目录下创建一个 `requirements.txt` 文件，其中包含了当前环境中所有包及各自的版本的简单列表。



您可以使用 `pip list` 在不产生requirements文件的情况下， 查看已安装包的列表。

重新创建这样的环境,在虚拟环境中执行 :

```powershell
$ pip install -r requirements.txt
```

这能帮助确保安装、部署和开发者之间的一致性。

**最后，记住在源码版本控制中排除掉虚拟环境文件夹，可在ignore的列表中加上它。 **

