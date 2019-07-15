# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
'''
测试协方差
绘制两支股票的趋势图, 比较相似程度
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

# 计算两只股票收盘价的相关程度(协方差)
# 两组样本的均值
ave_bhp = bhp_closing_prices.mean()
ave_vale = vale_closing_prices.mean()
# 两组样本的离差
dev_bhp = bhp_closing_prices - ave_bhp
dev_vale = vale_closing_prices - ave_vale
# 两组样本的协方差
cov_ab = np.mean(dev_bhp * dev_vale)
print(cov_ab)
# 求出两组样本的相关系数
print(':', (cov_ab / (
            bhp_closing_prices.std() *
            vale_closing_prices.std())))

# 调用corrcoef方法求得相关矩阵
d = np.corrcoef(bhp_closing_prices,
                vale_closing_prices)
print(d)


# 绘制收盘价的折线图
mp.figure('BHP VS VALE', facecolor='lightgray')
mp.title('BHP VS VALE', fontsize=18)
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
mp.plot(dates, bhp_closing_prices,
        color='dodgerblue', linewidth=3,
        linestyle=':', label='bhp_closing_price',
        alpha=0.8)
mp.plot(dates, vale_closing_prices,
        color='orangered', linewidth=3,
        linestyle=':', label='vale_closing_price',
        alpha=0.8)

mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.tight_layout()
mp.show()
