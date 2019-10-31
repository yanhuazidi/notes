#!/usr/bin/env python
#coding:utf-8

import threading
from time import sleep,time
import os

a = time()

num = 1
def music():
    for i in range(5):
        sleep(2)
        print("播放学猫叫",os.getpid())
    global num
    num = int(input("输入:"))

t = threading.Thread(target=music)
t.start()

for i in range(3):
    sleep(3)
    print("播放卡路里",os.getpid())


t.join()

print(num)

c = time() - a
print(int(c))
