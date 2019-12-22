# 数据分析DAY05

#### 布林带

布林带由3条线组成:

中轨线: 5日加权移动平均线

上轨线: 中轨 + 2*5日标准差 (这支股票顶部的压力)

下轨线: 中轨 - 2*5日标准差 (这支股票底部的支撑力)

布林带收窄代表趋于稳定, 如果布林带张开代表有较大的波动空间.

```python
sma53 = np.convolve(
    closing_prices, core, 'valid')
mp.plot(dates[4:], sma53, color='violet',
        linewidth=2, label='SMA-5(3)')

# 绘制5日均线的布林带
stds = np.zeros(sma53.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
# 底部支撑线 和 顶部压力线
lowers = sma53 - 2 * stds
uppers = sma53 + 2 * stds
# 绘制布林带
mp.plot(dates[4:], lowers,
        color='limegreen', label='Lower')
mp.plot(dates[4:], uppers,
        color='orangered', label='Upper')
mp.fill_between(
    dates[4:], lowers, uppers,
    uppers > lowers,
    color='dodgerblue', alpha=0.3)
```

#### 线性预测与线性拟合

**线性预测**

在二维世界(x,y),线性方程表示为一条直线; 在三维世界(x,y,z),线性方程表示为一个平面.再高的维度常人无法感受.但是线性方程依然存在.

假设一组数据符合一种线性规律, 那么就可以预测未来将会出现的数据.

```
a  b  c  d  e  f  ?

ax + by + cz = d
bx + cy + dz = e
cx + dy + ez = f
预测:
dx + ey + fz = ?
```

计算机如何解三元一次方程组?
$$
\left[ \begin{array}{ccc}
a & b & c \\
b & c & d \\
c & d & e \\
\end{array}
\right]
\times
\left[ \begin{array}{ccc}
x\\
y\\
z\\
\end{array}
\right]
=
\left[ \begin{array}{ccc}
d\\
e\\
f\\
\end{array}
\right]
$$

```python
# a矩阵为3*3的矩阵, b矩阵为等号右边的矩阵
# c即是[xyz]矩阵
c = np.linalg.lstsq(a, b)[0]
```

案例: 预测AAPL下一天的股价

```python
# 整理五元一次方程组, 最终预测一组股票的走势
N = 3
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
```

**线性拟合**

线性拟合可以寻求与一组数据的走势规律相适应的线性表达式方程.

```python
例如:
一组散点:[x1, y1][x2, y2][x3, y3] ... [xn, yn]

假设这组散点数据符合同一个线性方程, 那么:
kx1 + b = y1
kx2 + b = y2
kx3 + b = y3
...
kxn + b = yn 
```

$$
\left[ \begin{array}{ccc}
x_1 & 1 \\
x_2 & 1 \\
x_3 & 1 \\
x_n & 1 \\
\end{array}
\right]
\times
\left[ \begin{array}{ccc}
k\\
b\\
\end{array}
\right]
=
\left[ \begin{array}{ccc}
y_1\\
y_2\\
y_3\\
y_4\\
\end{array}
\right]
$$

由于样本数量非常多,没两组方程即可求得一组解. 

np.linalg.lstsq(a, b)可以通过最小二乘法求出拟合误差最小的k与b的值返回. 

案例:利用线性拟合画出股价的趋势线.

(股价趋势简单可以认为: 最高价/最低价/收盘价的均值)

```python
'''
1. 绘制每天的趋势点
2. 针对每天的趋势点去做线性拟合,得到直线方程.
3. 绘制趋势线
'''
# 通过 最高价最低价收盘价取得每天的趋势点
trend_points = (
    highest_prices + closing_prices +
    lowest_prices) / 3
# 绘制趋势点
mp.scatter(dates, trend_points,
           color='dodgerblue', alpha=0.8,
           zorder=4)
# 通过线性拟合,获取一条与趋势点匹配的拟合直线
days = dates.astype('M8[D]').astype('int32')
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, trend_points)[0]
# 获取趋势线  y=kx+b
trend_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, trend_line,
        color='dodgerblue', linewidth=3,
        label='Trend Line')

spreads = highest_prices - lowest_prices
# 绘制顶部压力线 (trend+(highest-lowest))
resistance_points = trend_points + spreads
mp.scatter(dates, resistance_points,
           color='orangered', alpha=0.8,
           zorder=4)
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, resistance_points)[0]
# 获取趋势线  y=kx+b
resistance_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, resistance_line,
        color='orangered', linewidth=3,
        label='resistance Line')


# 绘制底部支撑线 (trend-(highest-lowest))
support_points = trend_points - spreads
mp.scatter(dates, support_points,
           color='limegreen', alpha=0.8,
           zorder=4)
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, support_points)[0]
# 获取趋势线  y=kx+b
support_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, support_line,
        color='limegreen', linewidth=3,
        label='support Line')
```

#### 数组的裁剪压缩和累乘

数组的裁剪

```python
# 将调用数组中小于min的元素赋值为最小值
# 将调用数组中大于max的元素赋值为最大值
d = ndarray.clip(min=1, max=5)
```

数组的压缩

```python
# 返回调用数组中满足条件的元素组成的新数组
d = ndarray.compress(条件)
```

数组的累乘

```python
# 返回数组中所有元素的乘积
d = ndarray.prod()
# 返回调用数组中所有元素执行累乘的过程数组
d = ndarray.cumprod()
```

测试案例:

```python
import numpy as np
# 测试素组的裁剪
a = np.arange(1, 10)
b = a.clip(min=3, max=7)
print(a, b)

# 测试数组的压缩
c = a.compress((a > 5) & (a < 8))
print(a, c)

# 测试数组的累乘
d = a.prod()
print(a, d)
e = a.cumprod()
print(e)
```

#### 协方差/相关矩阵/相关系数

通过两组统计数据计算而得的协方差可以评估这两组统计数据的相似程度.

样本:

```
A = [a1, a2, a3, ..., an]
B = [b1, b2, b3, ..., bn]
```

平均值:

```
ave_a = (a1 + a2 +...+ an) / n
ave_b = (b1 + b2 +...+ bn) / n
```

离差:

```
dev_a = [a1, a2, a3, ..., an] - ave_a
dev_b = [b1, b2, b3, ..., bn] - ave_b
```

协方差:

```
cov_ab = ave(dev_a * dev_b) (ave即是取平均值)
cov_ba = ave(dev_b * dev_a) (ave即是取平均值)
```

案例: 评估bhp与vale两支股票的相似程度

```python
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
```

协方差可以简单的反应出两组样本的相关性. 值为正,则为正相关;若值为负则为负相关. 绝对值越大相关性越强.

**相关系数**

相关系数也体现了两组样本的相关性. 

相关系数=协方差 / 两组样本标准差的乘积.  这个结果处于[-1, 1]

```python
# 求出两组样本的相关系数
print(':', (cov_ab / (
            bhp_closing_prices.std() *
            vale_closing_prices.std())))
```

**相关矩阵**

numpy提供了相关矩阵的API, 可以方便的输出两组样本的相关系数.

```python
# d即为两组样本的相关矩阵
d = np.corrcoef(a, b)
print(d)
```

```python
# 调用corrcoef方法求得相关矩阵
d = np.corrcoef(bhp_closing_prices,
                vale_closing_prices)
print(d)
```

#### 多项式运算与多项式拟合

多项式方程的一般形式
$$
y = p_0x^n + p_1x^{n-1} + p_2x^{n-2}+ ...+ p_n
$$


多项式运算相关API:

```python
# 已知一组多项式系数数组: P = [4, 3, 0, 1]
# 则多项式为: y = 4x^3 + 3x^2 + 1
# 根据多项式系数与自变量x的值,求出多项式的结果
y = np.polyval(P, x)
# 根据多项式的系数,求得该多项式导函数的系数
Q = np.polyder(P)  #-> [12, 6, 0]
# 根据多项式的系数,求多项式的根 (一般针对二次函数)
# 返回x的值
xs = np.roots(Q) 
```

案例: 求多项式y=4x<sup>3</sup> + 3x<sup>2</sup> -1000x + 1曲线拐点坐标.

```python
'''
1. 对多项式求导函数  Q = []
2. 求导函数的根 --> 得到y为0时x的坐标值
3. 把x带入原函数求得y坐标
4. 绘制多项式曲线, 并且标注拐点
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4 * x**3 + 3 * x**2 - 1000 * x + 1
# 多项式求导
Q = np.polyder([4, 3, -1000, 1])
# 导函数求根
xs = np.roots(Q)
# x带入原函数求y
ys = np.polyval([4, 3, -1000, 1], xs)
print(xs, ys)
mp.figure('PolyLine', facecolor='lightgray')
mp.title('PlyLine', fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.plot(x, y, color='dodgerblue',
        linewidth=3, label='Poly Line')
# 绘制拐点
mp.scatter(xs, ys, color='red', marker='D',
           zorder=3, label='Points')
mp.legend()
mp.show()

```

**多项式拟合**

假设得到的多项式如下:
$$
f(x) = p_0x^n + p_1x^{n-1} + p_2x^{n-2}+ ...+ p_n
$$
那么拟合的多项式与原函数的差方:
$$
loss = (y_1-f(x_1))^2 + (y_2-f(x_2))^2 + ... + (y_n-f(x_n))^2 
$$
多项式拟合的意义在于求取一组p<sub>0</sub>-p<sub>n</sub>,使得loss的值最小.

numpy提供的多项式拟合的API:

```python
# x, y 样本数组的xy坐标 (告诉numpy原函数的数据)
# n 最高次幂 (告诉numpy拟合结果的多项式的最高次幂)

# 返回 P :拟合结果多项式的系数数组
P = np.polyfit(x, y, n)
```

案例: 使用多项式拟合两只股票(bhp, vale)收盘价的差价函数:

```python
'''
1. 读取文件,求得bhp与vale的收盘价的差价
2. 绘制差价的散点图
3. 基于多项式拟合,拟合得到一个多项式方程(系数)
4. 绘制多项式方程的曲线
'''
```




































































