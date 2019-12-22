#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process,Pipe
import os,time

fd1,fd2 = Pipe(False)

def fun(name):
    time.sleep(3)
    fd2.send(name)

jobs = []
for i in range(5):
    p = Process(target = fun, args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()