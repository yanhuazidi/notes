# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试除法通用函数
'''
import numpy as np

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
print(a)
print(b)
# 开始测试
print(np.true_divide(a, b))
print(np.divide(a, b))

print(np.floor_divide(a, b))
print(np.ceil(a / b))
print(np.trunc(a / b))
