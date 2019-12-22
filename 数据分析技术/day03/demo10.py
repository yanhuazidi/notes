# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试matplotlib的简单动画
1.随机生成100个泡泡
每个泡泡:
    位置:(x,x) 随机
    大小: x    随机
    速度: x    随机
    颜色:(1,1,1) 随机
2.把100个泡泡都绘制到窗口中
3.添加动画,每30毫秒更新泡泡的状态, 更新界面
'''
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

# 1.随机生成100个泡泡
# [((1,2), 30, 1, (0.2,0.2,0.2))]


n = 100
balls = np.zeros(n, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4)])
# 对着100个元素进行初始化 设置随机值
# uniform随机生成0-1的数填充n行2列的数组
balls['position'] = np.random.uniform(
    0, 1, (n, 2))
balls['size'] = np.random.uniform(
    60, 70, n)
balls['growth'] = np.random.uniform(
    10, 50, n)
balls['color'] = np.random.uniform(
    0, 1, (n, 4))

# 绘制这些球
mp.figure('Bubbles', facecolor='lightgray')
mp.title('Bubbles', fontsize=18)
mp.xticks([])
mp.yticks([])

sc = mp.scatter(balls['position'][:, 0],
                balls['position'][:, 1],
                balls['size'],
                color=balls['color'])


# 在update函数中更新球的状态
def update(number):
    balls['size'] += balls['growth']
    # 选择一个泡泡使之破裂
    boom_ind = number % n
    balls[boom_ind]['size'] = \
        np.random.uniform(67, 80, 1)
    balls[boom_ind]['position'] = \
        np.random.uniform(0, 1, (1, 2))
    # 重新绘制
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(
    mp.gcf(), update, interval=30)

mp.show()
