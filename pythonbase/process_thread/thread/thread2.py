#!/usr/bin/env python
#coding:utf-8

import threading
from time import sleep,time

a = time()
def fun(sec,name):
    print("线程参数传递")
    sleep(sec)
    print("%s 线程执行完毕"%name)

thread = []
for i in range(3):
    t = threading.Thread(target=fun,args=(2,),\
    kwargs={'name':"t%d"%i})
    thread.append(t)
    t.start()

for i in thread:
    i.join()
c = time() - a
print(int(c))
