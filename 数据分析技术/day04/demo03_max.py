# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 定义函数,转换日期格式


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    s = date.strftime("%Y-%m-%d")
    return s

# 加载文件
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = \
    np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})


# 观察最高价与最低价的波动范围,分析这支股票
# 是否坚挺.
hptp = np.ptp(highest_prices)
lptp = np.ptp(lowest_prices)
print('hptp:', hptp)
print('lptp:', lptp)

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(a, b, sep='\n')
print(np.maximum(a, b))
print(np.minimum(a, b))


# 求收盘价的中位数
# 对样本数据进行排序 np.msort()
sorted_prices = np.msort(closing_prices)
size = sorted_prices.size
# 获取中位数
median = np.median(sorted_prices)
median2 =   \
    (sorted_prices[int((size - 1) / 2)] +
     sorted_prices[int((size / 2))]) / 2
print(median)
print(median2)
