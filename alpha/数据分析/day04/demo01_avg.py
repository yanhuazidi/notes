# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
demo01_avg.py  测试均值
'''
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
    lowest_prices, closing_prices, \
    volumes = np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6, 7),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8, f8',
        converters={1: dmy2ymd})

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
#设置刻度定位器, x轴需要显示时间信息
ax = mp.gca()
# x轴主刻度为每周一
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d'))
# x轴次刻度为每天
ax.xaxis.set_minor_locator(
    md.DayLocator())
# 把日期数组元素类型改为md可识别的类型
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices,
        color='dodgerblue', linewidth=3,
        linestyle=':', label='closing_price')

# 计算收盘价的算数平均值
m = np.mean(closing_prices)
mp.hlines(m, dates[0], dates[-1],
          color='orangered', label='AVG',
          linestyle='--')

# 计算成交量加权平均值
vwap = np.average(closing_prices,
                  weights=volumes)
mp.hlines(vwap, dates[0], dates[-1],
          color='limegreen',
          label='VWAP', linestyle='--')

# 计算时间加权平均值
wprices = dates.astype('M8[D]').astype('int32')
twap = np.average(closing_prices,
                  weights=wprices)
mp.hlines(twap, dates[0], dates[-1],
          color='violet',
          label='TWAP', linestyle='--')

mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.show()
