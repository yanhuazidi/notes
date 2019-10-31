#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 上午11:16 
# @Author : yrh
# @Site :  
# @File : demo2.py 
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x=[[1,1],[0,0],[0,1]]
y=[1,0,0]

for lbl,dt in zip(y,x):
    plt.plot(dt[0],dt[1],'o' if lbl else '^',mec='r' if lbl else 'b')
plt.show()

x=np.array(x)
weights=np.random.normal(0,0.001,size=[x.shape[1],1])
bias=np.random.normal(0,0.001,size=1)
print(weights)
print(bias)

linear_r=np.sum(np.dot(x,weights))+bias
print(linear_r)
# 激活函数
def f(input_x):
    return 1 if input_x>0 else 0
# 预测输出
def predict(vec,theta,b):
    return f(np.dot(vec,theta)+b)
print('预测输出')
for v in x:
    print(predict(v,weights,bias))


def update_weights(theta,vec,output,lbls,b):
    loss=lbls-output
    theta=list(map(lambda x:x[0]+x[1]*0.1*loss,list(zip(theta,vec))))
    b+=loss*0.1


