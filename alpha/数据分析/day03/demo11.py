# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
模拟信号接收器
y=sin(2πt)*exp(sin(0.2πt))
'''
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=18)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle=':', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue',
             label='Signal')[0]
pl.set_data([], [])
# 接收生成器生成的(x,y),添加到绘制的
# 曲线坐标数组中,重新绘制界面


def update(data):
    t, v = data
    x, y = pl.get_data()
    # 把新的坐标点,添加到当前plot对象坐标数组中
    x.append(t)
    y.append(v)
    # 重新设置plot对象的数据集
    pl.set_data(x, y)
    # 移动坐标轴
    if(x[-1] > 10):
        mp.xlim(x[-1] - 10, x[-1])
    pass


x = 0
# 生成坐标点数据 yield返回


def generator():
    global x
    y = np.sin(2 * np.pi * x) * \
        np.exp(np.sin(0.2 * np.pi * x))
    yield (x, y)
    x += 0.05

# 执行动画
anim = ma.FuncAnimation(
    mp.gcf(), update, generator, interval=30)

mp.show()
