#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
from time import ctime,sleep

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    def run(self):
        for i in range(5):
            print("The time is {}".format(ctime()[11:19]))
            sleep(self.value)
    
p = ClockProcess(2)
p.start()
p.join()