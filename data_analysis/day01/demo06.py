# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
a = np.arange(1, 10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[::])
print(a[::3])
print(a[1::3])
print(a[2::3])
# a改为2维数组
a.resize(3, 3)
# 切出1 / 2行与0 / 1 / 2列
print(a[1:, :])
# 切出1 / 2行与1 / 2列
print(a[1:, 1:])
