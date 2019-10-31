#!/usr/bin/env python
#coding:utf-8

import os

def cop1(filename):
    size = os.path.getsize(filename)
    with open(filename,'rb') as f:
        n = size //2
        with open('1.jpg','wb') as f1:
            while True:
                if n < 1024:
                    data = f.read(n)
                    f1.write(data)
                    break
                data = f.read(1024)
                f1.write(data)
                n -=1024

def cop2(filename):
    size = os.path.getsize(filename)
    with open(filename,'rb') as f:
        f.seek(size//2,0)
        with open('2.jpg','wb') as f1:
            while True:
                data = f.read(1024)
                if not data:
                    break
                f1.write(data)
filename = input("文件名:")
pid = os.fork()
if pid < 0:
    print("创建进程失败")
elif pid == 0:
    cop2(filename)
else:
    cop1(filename)