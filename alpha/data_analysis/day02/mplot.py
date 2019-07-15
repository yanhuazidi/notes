# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
mplot.py   测试matplot基本绘图
'''
import numpy as np
import matplotlib.pyplot as mp
# 准备数据
x = np.linspace(-np.pi, np.pi, 1000)
cos_x = np.cos(x) / 2
sin_x = np.sin(x)

# 设置坐标轴范围
# mp.xlim(-np.pi, np.pi)
# mp.ylim(-1, 1)

#设置坐标刻度 [-π, -π/2, 0, π/2, π]
x_val_list = [-np.pi, -np.pi / 2, 0,
              np.pi / 2, np.pi]
x_text_list = [r'$-\pi$',
               r'$-\frac{\pi}{2}$', '0',
               r'$\frac{\pi}{2}$',
               r'$\pi$']
mp.xticks(x_val_list, x_text_list)

# 设置坐标轴的颜色与位置
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 绘制两个特殊点
point_x = np.pi / 2
point_cos_x = np.cos(point_x) / 2
point_sin_x = np.sin(point_x)
mp.scatter(point_x, point_cos_x,
           facecolor='limegreen', s=60,
           marker='D', zorder=3)
mp.scatter(point_x, point_sin_x,
           facecolor='limegreen', s=60,
           marker='h', zorder=3)

# 为特殊点添加备注
mp.annotate(r'$(\frac{\pi}{2}, 1)$',
            xycoords='data',
            xy=(np.pi / 2, 1),
            textcoords='offset points',
            xytext=(40, 10),
            fontsize=14,
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='angle3'))


mp.annotate(r'$(\frac{\pi}{2}, 0)$',
            xycoords='data',
            xy=(np.pi / 2, 0),
            textcoords='offset points',
            xytext=(-50, -50),
            fontsize=14,
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='angle3'))


# 绘制这两条线
mp.plot(x, cos_x, linestyle='--',
        linewidth=1, color='dodgerblue',
        label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_x, linestyle=':',
        linewidth=2, color='orangered',
        label=r'$y=sin(x)$')
mp.legend(loc='best')
mp.show()
