#!/usr/bin/env python
#coding:utf-8

import threading


def fun():
    print("线程属性测试")
    print('----',threading.currentThread().getName())

t = threading.Thread(target=fun,name='haha')
t.start()
print(t.is_alive())
print(t.name)
print(t.getName())
t.setName("gogo")
print(t.name)
t.join()
print(t.is_alive())
