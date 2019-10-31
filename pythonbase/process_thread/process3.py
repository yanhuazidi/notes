#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")
    
# p = Process(target = worker,args = (2,'Levi'))
p = Process(target = worker,kwargs = {'sec':2,'name':'Levi'})

p.start()
p.join(4)
print('='*20)