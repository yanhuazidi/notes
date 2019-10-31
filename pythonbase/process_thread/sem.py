#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Semaphore,Process
from time import sleep
import os

sem = Semaphore(3)

def fun():
    print("%d 想执行事件"%os.getpid())
    sem.acquire()
    print("%d　执行事件"%os.getpid())
    sleep(3)
    print("%d　执行事件完毕"%os.getpid())

jobs = []

for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in range(3):
    sleep(5)
    sem.release()

for i in jobs:
    i.join()

print(sem.get_value())