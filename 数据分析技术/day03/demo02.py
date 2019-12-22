# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试柱状图, 绘制水果销量
'''
import numpy as np
import matplotlib.pyplot as mp

apples = [23, 19, 81, 22, 65, 34, 65, 23, 89, 56, 89, 39]
oranges = [56, 56, 74, 39, 64, 95, 63, 48, 56, 98, 65, 45]

mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=18)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')

x = np.arange(len(apples))
mp.bar(x - 0.2, apples, 0.4,
       color='dodgerblue', label='Apple')
mp.bar(x + 0.2, oranges, 0.4,
       color='orangered', label='Orange')

mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
