# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
数据的轴向汇总
np.apply_along_axis(func, axis, array)
'''
import numpy as np


def func(data):
    print(data)

a = np.arange(1, 10).reshape(3, 3)
np.apply_along_axis(func, 1, a)
