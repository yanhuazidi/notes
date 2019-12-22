# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
插值器演示
'''
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 原始数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 20)
dis_y = np.sinc(dis_x)

# 绘制原曲线
mp.figure('Interpolate')
mp.title('Interpolate')
mp.grid(linestyle=':')
mp.plot(dis_x, dis_y, 'o-',
        color='dodgerblue', label='y=sinc(x)')
mp.legend()

# 通过一系列散点 基于线性插值器 求得曲线函数
linear = si.interp1d(dis_x, dis_y)
x = np.linspace(min_x, max_x, 1000)
y = linear(x)
mp.figure('linear')
mp.title('linear')
mp.grid(linestyle=':')
mp.plot(x, y, color='dodgerblue',
        label='y=sinc(x)')
mp.legend()

# 通过一系列散点 基于三次样条插值器 求得曲线函数
cubic = si.interp1d(dis_x, dis_y,
                    kind='cubic')
y = cubic(x)
mp.figure('cubic')
mp.title('cubic')
mp.grid(linestyle=':')
mp.plot(x, y, color='dodgerblue',
        label='y=sinc(x)')
mp.legend()
mp.show()
