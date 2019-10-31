# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
绘制3D平面图
'''
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x**5 + y**3) * \
    np.exp(-x**2 - y**2)

mp.figure('Hot', facecolor='lightgray')
mp.title('Hot', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)

ax3d.plot_surface(x, y, z, rstride=10,
                  cstride=10, cmap='jet')

mp.show()
