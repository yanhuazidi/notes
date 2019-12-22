# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试ndarray对象的创建
'''
import numpy as np
# 创建二维数组
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)
# np.arange(起始值, 结束值, 步长)
b = np.arange(1, 10, 1)
print(b)
# np.zeros(数组元素个数, dtype='')
c = np.zeros(10)
print(c, '; c.dtype:', c.dtype)
# np.ones(数组元素个数, dtype='')
d = np.ones(10, dtype='int64')
print(d, '; d.dtype:', d.dtype)
