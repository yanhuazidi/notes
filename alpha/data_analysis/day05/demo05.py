# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
1. 对多项式求导函数  Q = []
2. 求导函数的根 --> 得到y为0时x的坐标值
3. 把x带入原函数求得y坐标
4. 绘制多项式曲线, 并且标注拐点
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4 * x**3 + 3 * x**2 - 1000 * x + 1
# 多项式求导
Q = np.polyder([4, 3, -1000, 1])
# 导函数求根
xs = np.roots(Q)
# x带入原函数求y
ys = np.polyval([4, 3, -1000, 1], xs)
print(xs, ys)
mp.figure('PolyLine', facecolor='lightgray')
mp.title('PlyLine', fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.plot(x, y, color='dodgerblue',
        linewidth=3, label='Poly Line')
# 绘制拐点
mp.scatter(xs, ys, color='red', marker='D',
           zorder=3, label='Points')
mp.legend()
mp.show()
