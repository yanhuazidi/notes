# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
绘制刻度网格线
'''
import numpy as np
import matplotlib.pyplot as mp

y = [1, 10, 100, 1000, 100, 10, 1]

mp.figure('GridLine', facecolor='lightgray')

mp.subplot(1, 2, 1)
mp.title('GridLine', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    mp.MultipleLocator())
ax.xaxis.set_minor_locator(
    mp.MultipleLocator(0.1))
ax.grid(which='major', axis='both',
        linewidth=0.75, color='orange')
ax.grid(which='minor', axis='both',
        linewidth=0.25, color='orange')
mp.plot(y, 'o-', c='dodgerblue', label='p')
mp.legend()

mp.subplot(1, 2, 2)
mp.title('GridLine', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    mp.MultipleLocator())
ax.xaxis.set_minor_locator(
    mp.MultipleLocator(0.1))
ax.grid(which='major', axis='both',
        linewidth=0.75, color='orange')
ax.grid(which='minor', axis='both',
        linewidth=0.25, color='orange')
mp.semilogy(y, 'o-', c='dodgerblue', label='p')
mp.legend()

mp.show()
