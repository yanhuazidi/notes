#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print('当前时间 '+ctime()[11:19])

p = Process(target = tm,name='tarena')
# p.daemon = True

p.start()

print('Process name',p.name)
print("Process pid",p.pid)
print("Process alive",p.is_alive())

p.join()
    