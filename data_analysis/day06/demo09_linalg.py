# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试线性代数模块相关API
'''
import numpy as np

A = np.mat('1 2 3; 7 8 5; 7 6 5')
print(A)
B = np.linalg.inv(A)
print(B)
print(A * B)
print(A.I)
print('-' * 40)

A = np.mat('11 12 13; 21 22 23')
print(A)
B = np.linalg.pinv(A)
B = A.I
print(B)
print(A * B)

# 求解方程组

a = np.mat('1 -2 1;0 2 -8;-4 5 9')
b = np.mat('0; 8; -9')
c = np.linalg.solve(a, b)
c2 = np.linalg.lstsq(a, b)[0]
print(c)
print(c2)
