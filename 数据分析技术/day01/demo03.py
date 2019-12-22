# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试数组的基本属性
'''
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# 测试数组的基本属性
print('a.shape:', a.shape)
# a.shape = (6, )
# print(a, 'a.shape:', a.shape)
print('a.size:', a.size)
print('len(a):', len(a))
# 数组元素的索引
ary = np.arange(1, 28)
ary.shape = (3, 3, 3)
print(ary, '; ary.shape:', ary.shape)
print('ary[0]:', ary[0])
print('ary[0][0]:', ary[0][0])
print('ary[0][0][0]:', ary[0][0][0])
print('ary[0,0,0]:', ary[0, 0, 0])
# 遍历三维数组
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k], end=' ')
