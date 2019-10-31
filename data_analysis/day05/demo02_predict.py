# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
import pandas as pd
'''
demo02_predict: 线性预测
假设股价符合某种线性方程, 预测下一天的股价
'''


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

# 整理五元一次方程组, 最终预测一组股票的走势
N = 2
pred_prices = np.zeros(
    closing_prices.size - 2 * N + 1)
# 为预测值的每一个元素赋值
for i in range(pred_prices.size):
    a = np.zeros((N, N))
    # 整理5行5列的矩阵
    for j in range(N):
        a[j, ] = closing_prices[
            i + j:i + j + N]
    b = closing_prices[i + N:i + N * 2]
    # 根据a矩阵与b矩阵求解
    x = np.linalg.lstsq(a, b)[0]
    print(x)
    # b.dot(x) b与x执行矩阵相乘
    pred_prices[i] = b.dot(x)

# 把预测的结果绘制出来
# 向dates数组末尾在加一天 (工作日)
dates = np.append(
    dates, dates[-1] +
    pd.tseries.offsets.BDay())

mp.plot(dates[2 * N:], pred_prices,
        'o-', color='orangered',
        linewidth=2, label='Predict Price')

mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.show()
