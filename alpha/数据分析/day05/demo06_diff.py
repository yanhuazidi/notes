# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
'''
1. 读取文件,求得bhp与vale的收盘价的差价
2. 绘制差价的散点图
3. 基于多项式拟合,拟合得到一个多项式方程(系数)
4. 绘制多项式方程的曲线
'''


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    s = date.strftime("%Y-%m-%d")
    return s

# 加载文件
dates, bhp_closing_prices = np.loadtxt(
    '../data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8',
    converters={1: dmy2ymd})

vale_closing_prices = np.loadtxt(
    '../data/vale.csv', delimiter=',',
    usecols=(6), unpack=True)

# 1. 读取文件,求得bhp与vale的收盘价的差价
diff_prices = \
    bhp_closing_prices - vale_closing_prices


# 绘制收盘价的折线图
mp.figure('BHP DIFF VALE', facecolor='lightgray')
mp.title('BHP DIFF VALE', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置刻度定位器, x轴需要显示时间信息
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

# 2. 绘制差价的散点图
mp.xlim(dates[0], dates[-1])
mp.scatter(dates, diff_prices, alpha=0.8,
           color='dodgerblue', s=60)


# 3. 基于多项式拟合,拟合得到一个多项式方程(系数)
days = dates.astype('M8[D]').astype('int32')
P = np.polyfit(days, diff_prices, 4)
# 4. 绘制多项式方程的曲线
ys = np.polyval(P, days)
mp.plot(dates, ys, color='orangered',
        linewidth=3, alpha=0.8)

mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.tight_layout()
mp.show()
