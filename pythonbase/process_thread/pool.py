#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

pool = Pool()

result = []
for i in range(10):
    msg = 'hello %d'%i
    r = pool.apply_async(func = worker,args = (msg,))
    # r = pool.apply(func = worker,args = (msg,))
    result.append(r)
pool.close()
pool.join()
print(result)
for i in result:
    # print(i)
    print(i.get())