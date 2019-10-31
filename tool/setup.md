

[TOC]

LICENSE,README.md,setup.py

# 使用Setuptools构建和分发包

https://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools

`Setuptools`是Python的增强功能集合`distutils` ，允许开发人员更轻松地构建和分发Python包，尤其是那些依赖于其他包的包。

使用`setuptools`基于的普通Python包对用户进行构建和分发的包`distutils`。您的用户无需安装甚至不需要了解setuptools即可使用它们，并且您不必在发行版中包含整个setuptools包。通过仅包含一个[引导程序模块](https://bootstrap.pypa.io/ez_setup.py)（12K .py文件），`setuptools`如果用户从源代码构建程序包并且尚未安装合适的版本，则程序包将自动下载并安装。



### 安装`setuptools`

要安装最新版本的setuptools，请使用：

```shell
pip install -U setuptools
```



### 基本用法

- setup.py是 setuptools的构建脚本，它告诉setuptools你的包的相关信息（如包名称、版本等）

对于setuptools的基本使用，只需从setuptools而不是distutils导入东西。这是使用setuptools的最小设置脚本：

**setup.py**

```python
from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
)
```

在项目文件夹中运行该脚本，以及您开发的Python包。



生成源代码分发，只需调用：

```shell
python setup.py sdist
```



在将项目发布到PyPI之前，您需要向设置脚本添加更多信息，以帮助人们查找或了解您的项目。也许你的项目将在那时增长，包括一些依赖项，也许还有一些数据文件和脚本：

**文件结构**

test/
​	|-test/
​		|-\__init__.py
​		|-test.py
​	|-setup.py
​	|-README.md
​	|-LICENSE


```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="HelloWorld",#模块名称
    version="0.1",
    packages=find_packages(),
    license=license,
    scripts=['setup/odoo'],
    # Project使用RestructuredText，因此请确保在目标计算机上安装或升级docutils
    install_requires=['docutils>=0.3',],
    python_requires='>=3.5',
    extras_require={
        'SSL': ['pyopenssl'],
    },
    tests_require=[
        'mock',
    ],
    package_data={
        # 如果任何包包含*.txt或*.rst文件，请包括这些文件：
        '': ['*.txt', '*.rst'],
        # 还包括在“hello”包中找到的任何*.msg文件：
        'hello': ['*.msg'],
    },

    # 要在PYPI上显示的元数据
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]

    # 还可以包括长描述、下载网址等。
)
```

- name，version，author，author_email，description，url根据名称的含义参考你的模块功能进行填写即可，没有特别要注意的地方。（注：name参数在上传到internet上要求必须是唯一的，不能有重复，否则无法上传）
- long_description为读取README.md的内容，encoding="utf-8"设置是为了README.md的内容支持中文，long_description_content_type执定long_description内容格式为markdown。
- packages通过setuptools.find_packages(where*='.', *exclude*=(), *include*=('*',))它默认在和setup.py同一目录下搜索各个含有 \__init\__.py的包。避免手工输入的麻烦。
- classifiers提供一些额外的模块信息，是一个列表格式。
- install_requires 依赖的模块列表，回自动安装



LICENSE是规定了你使用哪种协议发布自己的模块，如下MIT license的内容。如果你只是学习如何发布，直接copy如下内容即可，不用特别关注。

```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



README.md的内容也就是对模块的详细说明，示例如下



\__init__.py仅一行代码，提供模块名称信息

```bash
name = "example_pkg_zx1"
```



### 构建发布文件

接下来就是要构建发布文件了，会用到setuptools和wheel两个工具，终端下执行如下命令确保已经安装了最新版本

> python -m pip install --user --upgrade setuptools wheel



接着在setup.py文件所在目录下执行如下命令开始构建

> python setup.py sdist bdist_wheel

构建完成后会创建多个文件及目录，其中dist目录下会生成.whl和.tar.gz两个文件



### 上传模块到PyPI

测试平台来给大家来练习，Test PyPI就是提供这样的功能，让你随意上传自己的模块进行测试和实验，首先你需要在[注册Test PypI页面](https://test.pypi.org/account/register/)上注册一个账户并登陆邮箱验证。上传发布包需要用到twine这个工具，首先需要通过下面的命令进行安装。

> python -m pip install --user --upgrade twine

安装成功后，在test目录下使用下面的命令上传你的发布包

> twine upload --repository-url https://test.pypi.org/legacy/ dist/*

> 说明：
> 1.你的模块名称及子目录名称（示例为test）不能有重复，否则上传会失败，提示HTTPError: 403 Client Error: The user 'xxxx' isn't allowed to upload to project 'example-pkg'错误，遇到这种情况需要修改子目录example_pkg_zx1及setup.py中的name，然后重新尝试上传直到成功。

提示上传成功后，登陆Test PypI页面Your projects下查看应该就能看到你上传的模块了。



### 从PyPI安装自己的模块

你可以使用pip从Test PyPI上安装你的模块来验证是否能工作，example_pkg_zx1为模块名称

> python -m pip install --index-url https://test.pypi.org/simple/ example_pkg_zx1

> 注意上面的命令不要在example_pkg目录下执行，否则会提示模块已经存在而不执行安装，随意cd到其他的目录下执行



### 最后的提示

如果你已经准备好了正式发布自己的模块到PyPI（**与Test PyPI不同哦**），你需要首先在[https://pypi.org](https://pypi.org/)上注册正式的账户并验证邮箱，twine上传命令直接使用"twine upload dist/*"命令即可，不用再指定url；同样从PyPI安装模块直接使用命令"pip install your-package-name"进行安装，也不用指定url。



### MANIFEST.in（无静态文件可以不用创建） 文件

**MANIFEST.in 文件里输入要打包的 静态文件/文件夹**

recursive  递归

```
include requirements.txt
include LICENSE
include README.md
include odoo/addons/mail/static/scripts/odoo-mailgate.py
recursive-include font *
recursive-include Images *
recursive-include sounds *
recursive-include odoo *.css
recursive-include odoo *.csv
recursive-include odoo *.doc
recursive-include odoo *.docx
recursive-include odoo *.eml
recursive-include odoo *.eot
recursive-include odoo *.gif
recursive-include odoo *.html
recursive-include odoo *.ico
recursive-include odoo *.jpeg
recursive-include odoo *.jpg
recursive-include odoo *.js
recursive-include odoo *.md
recursive-include odoo *.mp3
recursive-include odoo *.ogg
recursive-include odoo *.ods
recursive-include odoo *.odt
recursive-include odoo *.otf
recursive-include odoo *.pdf
recursive-include odoo *.png
recursive-include odoo *.po
recursive-include odoo *.pot
recursive-include odoo *.rml
recursive-include odoo *.rng
recursive-include odoo *.rst
recursive-include odoo *.scss
recursive-include odoo *.sql
recursive-include odoo *.svg
recursive-include odoo *.template
recursive-include odoo *.txt
recursive-include odoo *.ttf
recursive-include odoo *.woff
recursive-include odoo *.woff2
recursive-include odoo *.wsdl
recursive-include odoo *.xls
recursive-include odoo *.xsd
recursive-include odoo *.xsl
recursive-include odoo *.xlsx
recursive-include odoo *.xml
recursive-include odoo *.yml
recursive-include odoo *.zip
recursive-include odoo/addons/l10n_mx_edi *.xslt *.key *.cer *.txt
recursive-include odoo/addons/l10n_mx_reports *.xslt
recursive-exclude * *.py[co]
recursive-exclude * *.hg*
```



# **Python 包和模块的打包和发布（setup.py、MANIFEST.in）**

使用MANIFEST.in
设置include_package_data=True

**在需要打包的包目录下创建 setup.py 文件 和 MANIFEST.in（无静态文件可以不用创建） 文件**

**setup.py 里输入**

```
# 引入构建包信息的模块
from distutils.core import setup

# 定义发布的包文件的信息
setup(
    name="plane_01",  # 发布的包的名称
    version="1.00.001",  # 发布包的版本序号
    description="",  # 发布包的描述信息
    author="桔子",  # 发布包的作者信息
    author_email="1847562860@qq.com",  # 作者的联系邮箱
    py_modules=['__init__', 'ariplane']  # 发布包中的模块文件列表
)
```

**MANIFEST.in 文件里输入要打包的 静态文件/文件夹**

```
recursive-include font *
recursive-include Images *
recursive-include sounds *
```

**打开当前目录命令行：**

**输入**

```
python setup.py sdist
```

打包成功，在目录下生成 dist文件夹 

**包的网络发布：**

**首先，进入 https://pypi.org 网站上，注册一个账号;**

**然后打开cmd命令行输入以下命令 安装 twine 第三方模块**



```
pip install twine
```

**装好后，进入打包目录的命令行输入以下命名 上传网络**



```
twine upload dist/*
```



**setup函数各参数详解：**>>python setup.py --help
  --name              包名称
  --version (-V)      包版本
  --author            程序的作者
  --author_email      程序的作者的邮箱地址
  --maintainer        维护者
  --maintainer_email  维护者的邮箱地址
  --url               程序的官网地址
  --license           程序的授权信息
  --description       程序的简单描述
  --long_description  程序的详细描述
  --platforms         程序适用的软件平台列表
  --classifiers       程序的所属分类列表
  --keywords          程序的关键字列表
  --packages  需要打包的目录列表
  --py_modules  需要打包的python文件列表
  --download_url  程序的下载地址
  --cmdclass 
  --data_files  打包时需要打包的数据文件，如图片，配置文件等
  --scripts  安装时需要执行的脚步列表

**setup.py打包命令各参数详解：**
\>>python setup.py --help-commands
  --python setup.py build     编译建造模块
  --python setup.py sdist      生成压缩包(zip/tar.gz).在当前目录下生成了一个模块名加版本的模块压缩包
  --python setup.py bdist_wininst  生成NT平台安装包(.exe)
  --python setup.py bdist_rpm 生成rpm包 
  --python setup.py install    解压压缩包，进入到有setup.py目录路径里安装模块到python安装目录的lib下，在Python里面能够直接调用



## setup.cfg

setup.cfg提供一种方式，可以让包的开发者提供命令的默认选项，同时为用户提供修改的机会。对setup.cfg的解析，是在setup.py之后，在命令行执行前。







## [reStructuredText](https://github.com/WeiTianHua/CheatSheet/blob/master/files/reStructuredText-Quick-Syntax.md)






