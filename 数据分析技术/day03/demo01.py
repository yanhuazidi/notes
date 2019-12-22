# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
绘制填充
sinx=sin(x)   cosx=cos(x/2) / 2  [0-8π]
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2

mp.figure("Fill", facecolor='lightgray')
mp.title("Fill", fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.plot(x, sinx, color='dodgerblue',
        label='y=sin(x)')
mp.plot(
    x, cosx, color='orangered',
    label=r'$y=\frac{cos(\frac{x}{2})}{2}$')
# 填充
mp.fill_between(
    x, sinx, cosx, sinx > cosx,
    color='dodgerblue', alpha=0.5)
mp.fill_between(
    x, sinx, cosx, sinx < cosx,
    color='orangered', alpha=0.5)


mp.tight_layout()
mp.legend()
mp.show()
