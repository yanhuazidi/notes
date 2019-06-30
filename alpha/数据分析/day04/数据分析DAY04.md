# 数据分析DAY04

### 算数平均值

```
S = [s1, s2, s3, s4 .. sn]
m = (s1 + s2 + s3 +..+ sn)/n
```

算数平均值表示对真值的无偏估计.

```python
<1>: np.mean(array)
<2>: ndarray.mean()
```

案例: 计算收盘价的算数平均值

```python
# 计算收盘价的算数平均值
m = np.mean(closing_prices)
mp.hlines(m, dates[0], dates[-1],
          color='orangered', label='AVG',
          linestyle='--')
```

### 加权平均值

算数平均值的每个样本对均值的影响权重是相同的, 但实际业务中每个样本对真值的估计重要性是不同的.

```
S = [s1, s2, s3, s4 .. sn]
W = [w1, w2, w3, w4 .. wn]
m = (s1w1 + s2w2 + s3w3 +..+ snwn)/(w1+w2+..+wn)
```

np提供了API很方便的计算加权平均值:

```python
# array 样本数组
# weight_array  每个样本权重值的数组
np.average(array, weights=weight_array)
```

**(VWAP)成交量加权平均价格**

成交量加权平均值体现了市场对当前交易价格的认可度,VWAP将会更接近这支股票的真实价格.

```python
# 计算成交量加权平均值
vwap = np.average(closing_prices,
                  weights=volumes)
mp.hlines(vwap, dates[0], dates[-1],
          color='limegreen',
          label='VWAP', linestyle='--')
```

**(TWAP)时间加权平均价格**

时间加权平均价格中时间权重越高, 参考意义越大. (越接近当前时间股价的时间权重应该越高)

```python
# 计算时间加权平均值
wprices = dates.astype('M8[D]').astype('int32')
twap = np.average(closing_prices,
                  weights=wprices)
mp.hlines(twap, dates[0], dates[-1],
          color='violet',
          label='TWAP', linestyle='--')
```

### 最值

```python
np.max(array)	# 求数组中的最大值
np.min(array)	# 求数组中的最小值
np.ptp(array)	# 求数组中元素的极差 (max-min)
```

```python
np.argmax(array)	# 求数组最大值的索引位置(下标)
np.argmin(array)	# 求数组最小值的索引位置(下标)
```

```python
# 返回一个新数组. 每个元素从a与b数组中进行选取,选择
# 相应位置较大的值,作为新数组的元素.
np.maximum(a, b)	
# 返回一个新数组. 每个元素从a与b数组中进行选取,选择
# 相应位置较小的值,作为新数组的元素.
np.minimum(a, b)
```

### 中位数

将多个样本按照顺序排列,取中间位置的元素. 

若样本数为奇数,中位数是最中间的元素;若样本数为偶数,中位数是中间两个元素的平均值.

```python
a = [1, 2, 3, 4, 5, 1000]
np.median(a)
# 中位数的算法公式:(a[(size-1)/2] + a[size/2]) / 2
```

案例:

```python
# 获取中位数
median = np.median(sorted_prices)
median2 =   \
    (sorted_prices[int((size - 1) / 2)] +
     sorted_prices[int((size / 2))]) / 2
print(median)
print(median2)
```

### 标准差

```
S = [s1, s2, s3, ... , sn]				#样本
m = (s1 + s2 + .. + sn) / n 			#平均值
D = [d1, d2, d3, ... , dn]; di=si-m  	#离差
Q = [q1, q2, q3, ... , qn]; qi=di^2  	#离差方
V = (q1 + q2 + q3 +...+ qn)/n			#总体方差
S = sqrt(V)	 #总体标准差
V' = (q1 + q2 + q3 +...+ qn)/n-1		#样本方差
S' = sqrt(V')	 #样本标准差
```

方差与标准差可以表示一组数据相对于这组数据的均值的离散程度. 方差和标准差越大越离散, 越小越收敛.

```python
#求出array这组数据的标准差
np.std(array)
```

案例:

```python
import numpy as np
# 读取收盘价
closing_prices = np.loadtxt(
    '../data/aapl.csv', delimiter=',',
    usecols=(6,), unpack=True)
print(closing_prices)
# 计算标准差
print(np.std(closing_prices))
# ddof为修正值  ddof=1时
# 求标准差时的分母将会是n-1
print(np.std(closing_prices, ddof=1))

# 手动计算标准差
mean = np.mean(closing_prices)  # 算数均值
devs = closing_prices - mean  # 离差数组
dsqs = devs ** 2  # 离差方数组
pvar = np.sum(dsqs) / dsqs.size  # 总体方差
pstd = np.sqrt(pvar)  # 总体标准差
print('pstd:', pstd)
# 样本方差
svar = np.sum(dsqs) / (dsqs.size - 1)
sstd = np.sqrt(svar)  # 样本标准差
print('sstd:', sstd)
```

### 时间数据处理

案例: 统计每周一/二/三...五的收盘价的平均值, 并输出.

```python
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
```

#### 数据的轴向汇总

案例: 汇总每周的最高价,最低价,开盘价,收盘价

```python
def func(data):
    pass
# 针对二维数组, 沿着某个轴向统一处理一组数据
# func: 处理函数
# axis: 轴向 [0, 1]
# array: 源数据二维数组
np.apply_along_axis(func, axis, array)
```

案例:

```python
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
```

#### 移动平均线

收盘价5日移动均线: 从第五天开始,计算最近五天的收盘价平均值所构成的一条线. 移动均线可以实现简单的数据降噪功能. 去除信号的噪声影响,更好的体现数据的趋势.

移动均线算法:

```python
a b c d e f g .... 
(a + b + c + d + e) / 5
(b + c + d + e + f) / 5
(c + d + e + f + g) / 5
...
```

案例:绘制收盘价的5日均线

```python
# 整理5日均线的数据并且绘制5日移动平均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i + 5].mean()

mp.plot(dates[4:], sma5, color='orangered',
        linewidth=2, label='SMA-5')
```

#### 卷积运算

卷积运算可以简单的对一组数据实现降噪功能. 

```
一组数据a:   [1, 2, 3, 4, 5]
卷积核数组b:  [8,7,6]

使用b卷积核数组对a数组执行卷积运算的过程如下:

                44  65  86         有效卷积 valid
            23  44  65  86  59     同维卷积 same
         8  23  44  65  86  59  30 完全卷积 full
 0   0   1   2   3   4   5   0   0
 6   7   8
     6   7   8
         6   7   8
             6   7   8
                 6   7   8
                     6   7   8
                         6   7   8
```

使用卷积运算实现5日均线:

```
[234, 523, 532, 532, 453, 245, ..    245 ]
[1/5, 1/5, 1/5, 1/5, 1/5]
     [1/5, 1/5, 1/5, 1/5, 1/5]
     	...
     			[1/5, 1/5, 1/5, 1/5, 1/5]
```

numpy提供的卷积运算的API:

```python
# array 源数组
# core_array 卷积核数组
# type	卷积类型
#	'valid'	有效卷积
#	'same'	同维卷积
#	'full'	完全卷积
np.convolve(array, core_array, type)
```

案例: 使用卷积实现收盘价的5日移动平均线

```python
# 使用卷积绘制5日均线
core = np.ones(5) / 5
sma52 = np.convolve(
    closing_prices, core, 'valid')

mp.plot(dates[4:], sma52, color='red',
        linewidth=5, label='SMA-5(2)',
        alpha=0.2)

# 使用卷积绘制10日均线
core = np.ones(10) / 10
sma10 = np.convolve(
    closing_prices, core, 'valid')

mp.plot(dates[9:], sma10, color='limegreen',
        linewidth=5, label='SMA-10',
        alpha=0.8)
```

#### 加权卷积运算

案例:绘制加权卷积实现的5日均线

```python

```





















































