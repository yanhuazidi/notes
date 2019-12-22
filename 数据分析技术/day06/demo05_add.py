# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试加法的通用函数
'''
import numpy as np

a = np.arange(1, 7)
print(a)
print(np.add(a, a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.add.outer(a, [10, 20, 30]))
