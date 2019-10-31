# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
数据的轴向汇总
np.apply_along_axis(func, axis, array)
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
wdays, opening_prices, highest_prices,\
    lowest_prices, closing_prices = np.loadtxt(
        '../data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        converters={1: dmy2wdays})

print(wdays)
# 获取第一个周一与最后一个周五的数组下标
# where方法返回值是一个元组, 真实数据存储在
# 元组的第一个元素中
first_mon = np.where(wdays == 0)[0][0]
last_fri = np.where(wdays == 4)[0][-1]
print(first_mon, ';', last_fri)

indices = np.arange(first_mon, 16).reshape(3, 5)
print(indices)

# 处理每一周数据


def func(indices):
    # 周一的开盘价 即是一周的开盘价
    open_price = opening_prices[indices[0]]
    # 周五的收盘价 即是一周的收盘价
    closing_price = closing_prices[
        indices[-1]]
    # 一周的最高价  一周的最低价
    highest_price =	\
        highest_prices[indices].max()
    lowest_price =	\
        lowest_prices[indices].min()
    return open_price, highest_price, \
        lowest_price, closing_price

r = np.apply_along_axis(func, 1, indices)
print(r)
