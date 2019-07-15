# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as mp

x = [1, 2, 3, 4, 5]
y = [7, 8, 9, 2, 3]
mp.plot(x, y)
# 绘制水平线与垂直线
mp.vlines(5, 0, 10)
mp.hlines(3, 0, 10)
# 绘制一条抛物线  在[-10,10]区间均分10个点
x = np.linspace(-10, 10, 1000)
print(x)
y = x ** 2
mp.plot(x, y)

mp.show()
