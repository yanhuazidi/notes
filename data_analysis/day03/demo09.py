# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试极坐标系
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 4 * np.pi, 1000)
y = 0.8 * x
sinx = 3 * np.sin(6 * x)
mp.figure('Polar', facecolor='lightgray')
mp.gca(projection='polar')  # 使用极坐标系
mp.title('Polar', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, label='y=0.8x')
mp.plot(x, sinx, label='y=3sin(6x)')
mp.legend()
mp.show()
