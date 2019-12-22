#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process,Value
import time
import random

v = Value('i',10000)


def man():
    for i in range(30):
        time.sleep(0.2)
        v.value +=random.randint(1,1000)

def woman():
    for i in range(30):
        time.sleep(0.1)
        v.value -=random.randint(100,900)

m = Process(target=man)
w = Process(target=woman)

m.start()
w.start()

m.join()
w.join()

print(v.value)