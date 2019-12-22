#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃法")
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())

things = [th1,th2,th3]
process = []
for th in things:
    p = Process(target = th)
    process.append(p)
    p.start()

print("父进程")

for i in process:
    i.join()