#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    return n*n

f = map(fun,range(5))

print(f)
pool = Pool()

r = pool.map(fun,range(5))

pool.close()
pool.join()
print(r)
for i in r:
    print(i)