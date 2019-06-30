# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
位操作
'''
import numpy as np

a = np.array([4, -6, 7, -3, -4, 2])
b = np.array([-2, -8, 2, -5, 3, -4])

print(a)
print(b)
print(a ^ b)
print(np.bitwise_xor(a, b))
# where找到符合条件的元素下标 (异号)
print(np.where((a ^ b) < 0)[0])


print('-' * 40)
d = np.arange(1, 20)
print(d)
e = np.bitwise_and(d, d - 1)
print(e)
