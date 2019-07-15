# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试ndarray的API
数组的裁剪 clip
数组的压缩 compress
数组的累乘 prod  cumprod
'''
import numpy as np
# 测试素组的裁剪
a = np.arange(1, 10)
b = a.clip(min=3, max=7)
print(a, b)

# 测试数组的压缩
c = a.compress((a > 5) & (a < 8))
print(a, c)

# 测试数组的累乘
d = a.prod()
print(a, d)
e = a.cumprod()
print(e)
