


import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md



def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')
    date=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    str_ = date.strftime('%Y-%m-%d')
    return str_

dates,opening_prices,highest_prices,lowest_prices,closing_prices,volumes= np.loadtxt('aapl.csv',#文件路径
				delimiter=',',					#文件的列分隔符
				usecols=(1,3,4,5,6,7),			#需要读取的列的下标
				unpack = True,				#是否需要拆包(不拆返回二维数组，拆返回每列的元组)
				dtype='M8[D],f8,f8,f8,f8,f8',	    #读取的每每一列的类型
				converters={1:dmy2ymd}		#转换器函数字典	
				)


mp.figure('AAPL',facecolor='lightgray')
mp.title('AAPL',fontsize=18)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Price',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_minor_locator(md.DayLocator())

dates = dates.astype(md.datetime.datetime)
mp.plot(dates,closing_prices,color='dodgerblue',
		linewidth=3,linestyle=':',label='closing_prices',alpha=0.4)

#整理蜡烛图的所需的颜色
rise = closing_prices > opening_prices
color = np.array([('white' if x else 'green') for x in rise])
ecolor = np.array([('red' if x else 'green') for x in rise])

#绘制K线图的影线

mp.bar(dates,highest_prices - lowest_prices,0.1,lowest_prices,edgecolor=ecolor,color=color)

#绘制K线图的实体
mp.bar(dates,closing_prices - opening_prices,0.8,opening_prices,edgecolor=ecolor,color=color)



#计算收盘价的平均值
m = np.mean(closing_prices)
mp.hlines(m,dates[0],dates[-1],color='orangered',label='AVG',linestyles='--')

#交易量加权平均值
vwap = np.average(closing_prices,weights=volumes)
mp.hlines(vwap,dates[0],dates[-1],color='red',label='vwapAVG',linestyles='--')

#时间加权平均值
wprices=dates.astype('M8[D]').astype('i4')
twap = np.average(closing_prices,weights=wprices)
mp.hlines(vwap,dates[0],dates[-2],color='blue',label='twapAVG',linestyles='--')

mx = np.max(closing_prices)
mxy = np.argmax(closing_prices)
mp.scatter(dates[mxy],mx,marker='^',s=30,edgecolor='#000000',facecolor='#000000',zorder=3)
mi = np.min(closing_prices)
miy = np.argmin(closing_prices)
mp.scatter(dates[miy],mi,marker='P',s=30,edgecolor='#000000',facecolor='#000000',zorder=3)


mp.legend()		
mp.gcf().autofmt_xdate()#自动格式化日期,斜着放
mp.show()










