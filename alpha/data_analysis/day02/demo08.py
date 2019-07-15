# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
随机生成100个人的身高体重, 绘制散点图
'''
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)

mp.figure('Persons', facecolor='gray')
mp.title('Persons', fontsize=18)
mp.xlabel('Height', fontsize=14)
mp.ylabel('Weight', fontsize=14)
mp.tick_params(labelsize=12)

d = (x - 172)**2 + (y - 60)**2

mp.scatter(x, y, c=d, cmap='jet_r', s=40)

mp.tight_layout()
mp.savefig("exercice_2.png",dpi=72)	
mp.show()
