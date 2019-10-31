# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试自由坐标系布局
'''
import matplotlib.pyplot as mp

mp.figure('Free Layout', facecolor='gray')
mp.axes([0.4, 0.2, 0.5, 0.5])
mp.text(0.5, 0.5, 1,va='center',
        ha='center', size=36)
mp.show()
