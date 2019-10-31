[TOC]

## inspect模块主要提供了四种用处：

1. 对是否是模块、框架、函数进行类型检查
2. 获取源码
3. 获取类或者函数的参数信息
4. 解析堆栈



## 类型检查

1. `inspect.ismodule(object)`： 是否为模块
2. `inspect.isclass(object)`：是否为类
3. `inspect.ismethod(object)`：是否为方法（bound method written in python）
4. `inspect.isfunction(object)`：是否为函数(python function, including lambda expression)
5. `inspect.isgeneratorfunction(object)`：是否为python生成器函数
6. `inspect.isgenerator(object)`:是否为生成器
7. `inspect.istraceback(object)`： 是否为traceback
8. `inspect.isframe(object)`：是否为frame
9. `inspect.iscode(object)`：是否为code
10. `inspect.isbuiltin(object)`：是否为built-in函数或built-in方法
11. `inspect.isroutine(object)`：是否为用户自定义或者built-in函数或方法
12. `inspect.isabstract(object)`：是否为抽象基类
13. `inspect.ismethoddescriptor(object)`：是否为方法标识符
14. `inspect.isdatadescriptor(object)`：是否为数据描述符，数据描述符有`__get__` 和`__set__属性； 通常也有__name__和__doc__属性`
15. `inspect.isgetsetdescriptor(object)`：是否为getset descriptor
16. `inspect.ismemberdescriptor(object)`：是否为member descriptor