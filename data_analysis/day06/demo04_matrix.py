# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
martix.py 测试矩阵
'''
import numpy as np

a = np.array([1, 2, 3, 7, 6, 5, 8, 7, 6])
a = a.reshape(3, 3)
# 使用第一种方式创建矩阵对象
m = np.matrix(a)
m[0, 0] = 999
print(a)
print(m, type(m))

# 使用第二种方式创建矩阵对象
m2 = np.mat(a)
m2[0, 0] = 999
print(m2, a, sep='\n')

# 使用第三种方式创建矩阵对象
m3 = np.mat('1 2 3;6 7 8;4 5 6')
print(m3)

# 测试矩阵的乘法
e = np.mat('1 2 6; 3 5 7; 4 8 9')
f = np.mat('3; 4; 5')
print(f)
print(e * f)

g = np.mat('2 2 6; 4 5 7; 5 8 9')
print(e * g)
print(g * e)
print(g.T * e.T)

print('-' * 40)

e = np.mat('2 2 6; 4 5 7; 5 8 9')
#e = np.mat('2 3 4; 5 6 7; 8 9 10')
print(e)
print(e.I)
print(e * e.I)

# 解应用题
prices = np.mat('3 3.5; 3.2  3.6')
total = np.mat('118.4 135.2')
print(total * prices.I)

# 使用矩阵求斐波那契数列
n = 35
print((np.mat('1 1; 1 0') ** (n - 1))[0, 0])
