# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
验证傅里叶定理, 生成方波
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# 根据公式搞出来3条曲线
y1 = 4 * np.pi * np.sin(x)
y2 = 4 / 3 * np.pi * np.sin(3 * x)
y3 = 4 / 5 * np.pi * np.sin(5 * x)

# 使用循环控制叠加波的数量
n = 1000
y = np.zeros(1000)
for i in range(1, n + 1):
    y += 4 / (2 * i - 1) * np.pi * \
        np.sin((2 * i - 1) * x)

mp.figure('SIN', facecolor='lightgray')
mp.title('SIN', fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)

mp.plot(x, y1, label='y1')
mp.plot(x, y2, label='y2')
mp.plot(x, y3, label='y3')
mp.plot(x, y, label='y')

mp.legend()
mp.show()
