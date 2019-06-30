#!/usr/bin/env python
#coding:utf-8

import multiprocessing as mp
import time

def fun():
    # time.sleep(3)
    global a
    print("子进程事件")
    a = 100
    print()

a = 1
p = mp.Process(target=fun)

p.start()

time.sleep(2)
print("父进程事件")

print(a)
p.join()