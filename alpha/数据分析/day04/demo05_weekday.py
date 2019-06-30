# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
统计每周一/二/三...五
的收盘价的平均值, 并输出.
'''
import numpy as np
import datetime as dt


def dmy2wdays(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    # 返回一周中的天
    wday = date.weekday()
    return wday

# 读取收盘价
wdays, closing_prices = np.loadtxt(
    '../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    converters={1: dmy2wdays})

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = \
        closing_prices[wdays == wday].mean()

print(ave_closing_prices)
