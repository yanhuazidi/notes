# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试联合间接排序
'''
import numpy as np

prices = np.array([
    92, 83, 71, 92, 40, 12, 64])
volumes = np.array([
    231, 38, 94, 56, 19, 61, 36])

indices = np.lexsort((volumes * -1, prices))
products = ['P1', 'P2', 'P3', 'P4',
            'P5', 'P6', 'P7']
for i in range(indices.size):
    print(products[indices[i]], end=' ')


# 测试插入排序

a = np.array([1, 2, 3, 5, 6, 8])
b = np.array([4, 7])
indices = np.searchsorted(a, b)
print(indices)
# 插入元素 向a中的indices位置插入b元素
d = np.insert(a, indices, b)
print(d)
