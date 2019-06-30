# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
生成三维散点数组, 显示在三维坐标系中.'
'''
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

mp.figure('3D Points', facecolor='gray')
mp.title('3D Points', fontsize=18)
# 获取3d坐标轴
ax = mp.gca(projection='3d')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
mp.tick_params(labelsize=8)
# v用于设置散点的颜色
v = np.sqrt(x**2 + y**2 + z**2)
ax.scatter(x, y, z, s=30, c=v, cmap='jet',
           alpha=0.5)
mp.show()
