#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process,Array
import time

# shm = Array('i',[1,2,3,4,5])  #将列表放入共享内存
# shm = Array('i',5)      #开辟五个整型空间
shm = Array('c',b'12345')   # 存入字符类型


def fun():
    for i in shm:
        print(i)
    shm[2] = b'x'

p = Process(target=fun)

p.start()
p.join()
for i in shm:
    print(i,end = ' ')
print()
print(shm.value)