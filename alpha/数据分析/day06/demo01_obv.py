# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
obv.py 绘制净额成交量柱状图
'''
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    s = date.strftime("%Y-%m-%d")
    return s

# 加载文件
dates, closing_prices, volumes = np.loadtxt(
    '../data/bhp.csv', delimiter=',',
    usecols=(1, 6, 7), unpack=True,
    dtype='M8[D], f8, f8',
    converters={1: dmy2ymd})

# 获取相比上一天股价是否上涨
diff_closing_prices = np.diff(closing_prices)
# 获取相对应的符号数组
sign_closing_prices = np.sign(diff_closing_prices)
# 绘制每天的成交量
obvs = volumes[1:] * sign_closing_prices

# 绘制净额成交量柱状图
mp.figure('OBV', facecolor='lightgray')
mp.title('OBV', fontsize=18)
mp.xlabel('Dates', fontsize=14)
mp.ylabel('Volumes', fontsize=14)
# 整理x轴刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
ax.xaxis.set_minor_locator(md.DayLocator())

mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')
dates = dates[1:].astype(md.datetime.datetime)

mp.bar(dates, obvs, 1.0, color='dodgerblue',
       edgecolor='white', label='OBV')

mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
