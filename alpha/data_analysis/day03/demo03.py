# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
饼状图显示语言流行度
'''
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=14)

values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
# 等轴比例绘制
mp.axis('equal')
mp.pie(values, spaces, labels, colors,
       '%d%%', shadow=True,
       startangle=90, radius=1)
mp.legend()
mp.show()
