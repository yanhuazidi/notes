

[TOC]



## base64

介绍
经常听到有人说“base64加密”，其实base64并不能用于数据加密，它也不是为了纯粹的数据加密而生的，
它的出现是为了解决不可见字符串的网络传输和数据保存问题。因为，用base64对数据进行转换的过程不
能成为“加密”与“解密”，只能成为“编码”与“解码”。下面我们也会用到它，所以这里顺便做下简单的介绍。



### base64的作用

Base64是一种用64个字符来表示任意二进制数据的方法，它是一种通过查表对二进制数据进行编码的方法，
不能用于数据加密。base64最初的出现时为了能够正确的传输邮件数据，因为邮件中的附件（比如图片）
的二进制数中可能存在不可见字符（ascii码中128-255之间的值是不可见字符），比如我们尝试用记事本或
其他文本编辑器打开一个图片时，通常都会看到一大堆乱码，这些乱码就是不可见字符。由于早期的一些网络
设备和网络协议是无法正确识别这些字符的，这就可能在数据传输时出现各种无法预知的问题。base64的作用
就是把含有不可见字符的信息用可见字符来表示（Ascii码中0-127之间的值是可见字符），从而解决这个问题。

关于base64的介绍及实现原理可以看看这几篇文章：

http://www.cnblogs.com/wellsoho/archive/2009/12/09/1619924.html
https://www.zhihu.com/question/36306744/answer/
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001399413803339f4bbda5c01fc479cbea98b1387390748000



### base64的常见应用场景

base64适用于小段内容的编码，比如数字证书的签名、URL、Cookie信息
等需要通过网络进行传输的小段数据。关于base64在数字签名中的应用会
在本文后面讲解pycrypto模块使用实例时有具体的应用示例。



### base64模块介绍及简单使用示例

Python中有一个内置的base64模块可直接用来进行base64的编码和解码
工作--即提供 “二进制数据” 与 “可打印（可见）的ASCII字符”之间
的转换功能。常用的函数有以下几个：



下面来看个简单的示例：

```python
import base64

data = 'hello, 世界'.encode()
based_data1 = base64.b64encode(data)
print(based_data1.decode())
plain_data1 = base64.b64decode(based_data1)
print(plain_data1.decode())
based_data2 = base64.urlsafe_b64encode(data)
print(based_data2.decode())
plain_data2 = base64.urlsafe_b64decode(based_data2)
print(plain_data2.decode())

#输出结果：
aGVsbG8sIOS4lueVjO+8gQ==
hello, 世界！
aGVsbG8sIOS4lueVjO-8gQ==
hello, 世界！

```



## 常用编码

`base64.b64encode(s, altchars=None)`

对二进制数据（字节串）s通过base64进行编码，返回编码后的字节串

`base64.b64decode(s, altchars=None, validate=False)`

对通过base64编码的字节对象或ASCII字符串s进行解码，返回解码后的字节串



参数s代表需要编码/解码的数据。其中b64encode的参数s的类型必须是字节包（bytes）。b64decode的参数s可以是字节包（bytes），也可以是字符串（str）。

由于Base64编码后的数据中可能会含有’+’或者’/’两个符号，如果编码后的数据用于url或者文件系统的路径中，就可能会导致Bug。所以base64模块提供了将编码后的数据中’+’和’/’进行替换的方法。

参数altchars必须是长度为2的字节包，这两个符号会用于替换编码后数据中的’+’和’/’。这个参数默认是None。

参数validate默认为False。如果它为True时，base64模块在进行解码前会先检查s中是否有非base64字母表中的字符，如果有的话则抛出错误`binascii.Error: Non-base64 digit found`。

如果数据的长度不正确则会抛出错误`binascii.Error: Incorrect padding`。



## 超文本链接，文件名安全编码

`base64.urlsafe_b64encode(s)`

与b64encode()函数不同的是，它会把标准Base64编码结果中的字符'+'和字符'/'分别替换成字符'-'和字符'_'。

`base64.urlsafe_b64decode(s)`

解码通过`base64.urlsafe_b64encode()`函数编码的字节对象或ASCII字符串s。

提示： URL中有一些有特殊意义的字符,也就是保留字符:';', '/', '?', ':', '@', '&', '=', '+', '$' 和 ',' ，在URL的参数值中应该避免这些字符的出现。



## 二进制文件编码

`base64.encode(input, output)` | `base64.decode(input, output)`

函数输入输出都是二进制，不能是字符串，补码的‘ = ’可以多，不能少，少了报错。

```python
import base64

with open('wei.jpg','rb') as f,open('wei2.jpg','wb') as f1:
    base64.encode(f,f1)

with open('wei2.jpg','rb') as f,open('wei1.jpg','wb') as f1:
    base64.decode(f,f1)

```



## 字节串编码

`base64.encodebytes(b)` 

将字节串编码为包含多行base-64数据的bytes对象

`base64.decodebytes(b)`

将base-64数据的bytestring解码为bytes对象。



`encodebytes`和`b64encode`在内部都是调用的`binascii`模块的`b2a_base64`，只不过`encodebytes`调用`b2a_base64`时`newline`参数使用默认值True。也就是说，`encodebytes`在输出数据的时候，每76个字节会添加一个换行符`b'\n'`。

`decodebytes`和默认参数下的`b64decode`基本一致。只有参数类型的检查不一样，`decodebytes`只支持`bytes`类型的数据。

