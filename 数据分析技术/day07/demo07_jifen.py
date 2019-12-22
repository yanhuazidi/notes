# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
微元法求定积分
'''
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc
import scipy.integrate as si


def f(x):
    return 2 * x**2 + 3 * x + 4

a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)

mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x1, y1, color='dodgerblue',
        linewidth=6, alpha=0.5,
        label=r'$y=x^2+3x+4$')

# 利用微元法绘制函数在区间中的小梯形
n = 150
x2 = np.linspace(a, b, n + 1)
y2 = f(x2)

# 求积分
area = 0
for i in range(n):
    area += (y2[i] + y2[i + 1]) * \
        (x2[i + 1] - x2[i]) / 2
print(area)

# 使用API求积分
area = si.quad(f, a, b)[0]
print(area)

for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [x2[i], 0], [x2[i], y2[i]],
        [x2[i + 1], y2[i + 1]],
        [x2[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))

mp.legend()
mp.show()
