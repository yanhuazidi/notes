# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试刻度定位器
'''
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',
            'mp.AutoLocator()',
            'mp.MultipleLocator()',
            'mp.LogLocator(base=2)']

mp.figure('Locators', facecolor='lightgray')

for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    mp.xlim(0, 10)
    mp.ylim(-10, 10)
    mp.yticks([])

    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))

    ax.xaxis.set_major_locator(eval(locator))
    ax.xaxis.set_minor_locator(
        mp.MultipleLocator(0.1))
    mp.plot(np.arange(11), np.zeros(11), c='none')
    mp.text(5, 0.3, locator,
            ha='center', size=12)
    mp.tight_layout()

mp.show()
