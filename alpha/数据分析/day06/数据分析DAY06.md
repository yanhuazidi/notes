# 数据分析DAY06

### 数据平滑处理

在做数据分析时, 由于数据的噪声太多, 需要对数据进行数据平滑处理. 通常包含有降噪/拟合等操作. 降噪的功能在于去除额外的影响因素. 拟合的目的在于数学模型化,可以通过更多的数学方法识别曲线特征.

降噪手段: 卷积运算

```python
# 通常卷积核的选取API
con_core = np.hanning(8)
con_core /= con_core.sum()
# 卷积API
np.convolve(samples, con_core, 'valid')
```

数学模型化: 多项式拟合

```python
# 通过原函数曲线(x,y)/最高次数 得到 拟合多项式系数
P = np.polyfit(x, y, n)
# 通过多项式系数与x的值,求对应的多项式函数值.
y = np.polyval(P, x)
# 通过原函数求导函数
Q = np.polyder(P)
# 求多项式的根
X = np.roots(Q)
# 求两个多项式函数的差函数. 可以通过该方法求取两个多项式
# 函数的交点
Q = np.polysub(P1, P2)
```

### 符号数组

sign函数可以把样本数组变成对应的符号数组, 所有正数变为1, 负数变为-1, 0还是0.

```python
ary = np.sign(源数组)
```

绘制 净额成交量(OBV)

若相比上一天的收盘价上涨,则为正成交量; 若比上一天的收盘价下跌,则为负成交量.

成交量可以反映市场对某支股票的人气, 成交量是一支股票上涨的能量. 一般情况下股票上涨往往需要较大的成交量,而下跌时则不然.

案例: 绘制OBV柱状图

```python
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
```

**数组预处理函数**

```python
# array 源数组
# 条件序列:  [a<60, a==60, a>60]
# 取值序列:  [-1,   0,     1   ]
np.piecewise(array, 条件序列, 取值序列)
```

测试:

```python
a = np.array([23, 94, 65, 23, 84, 56, 23])
d = np.piecewise(
    a,
    [(20 < a) & (a < 60), a == 60, a > 60],
    [-1, 0, 1])
print(d)
```

### 矢量化

矢量化指的是用数组代理标量来操作数组里的每个元素.

numpy提供了vectorize函数, 可以把处理标量的函数矢量化. 经过vectorize函数矢量化处理过后将会返回一个矢量函数, 该函数可以直接处理ndarray数组.

案例:

```python
import numpy as np
import math as m

def foo(x, y):
    return m.sqrt(x**2 + y**2)

x, y = 3, 4
print(foo(x, y))
x = np.array([3, 4, 5, 6])
y = np.array([4, 5, 6, 7])
# z = foo(x, y)  错误
# 把foo函数矢量化处理
foo_v = np.vectorize(foo)
print(foo_v(x, y))
```

numpy提供了frompyfunc函数, 也可以完成vectorize相同的功能

```python
# 使用frompyfunc方法矢量化函数
# foo需要2个参数, 最终将会有1个返回值
foo_f = np.frompyfunc(foo, 2, 1)
print(foo_f(x, y))
```

### 矩阵

numpy.matrix类型用来描述矩阵. 该类继承自numpy.ndarray. 任何多维数组的操作,对矩阵同样有效. 但是作为子类矩阵又结合了自身的特点,做了必要的扩充,比如乘法计算/矩阵求逆等等.

#### 矩阵的创建

```python
# ary: 任何可以被解释为矩阵的二维容器
# copy: 如果copy的值为True(缺省), 所得到的矩阵对象与参
# 数中源容器各自拥有独立的数据拷贝.否则,共享同一份数据
numpy.matrix(ary, copy=True)
```

```python
# ary: 任何可以被解释为矩阵的二维容器
# 默认copy=False
numpy.mat(ary)
```

```python
# str: 字符串矩阵拼块规则
#      '1 2 3;4 5 6;7 8 9'
np.mat(str)
```

#### 矩阵的乘法运算

```python
'''
a * b
矩阵的乘法:a矩阵的每一行分别乘以b矩阵的每一列
结果矩阵的行数与a的行数一致, 结果矩阵的列数与b的列数一致
'''
e = np.mat('1 2 6; 3 5 7; 4 8 9')
print(e * e)
```

#### 矩阵的逆矩阵

若两个矩阵A/B满足: AB = BA = E (单位矩阵),则 A/B互为逆矩阵.

*单位矩阵: 矩阵的主对角线值为1, 其他位置值为0的矩阵.*

```python
e = np.mat(..)
print(e.I)  #逆矩阵
```

案例 : 春游, 去程做大巴, 小孩票价3元, 家长票价3.2元, 一共花了118.4; 回程做火车, 小孩3.5, 家长3.6, 花了135.2; 求小孩与家长的人数.
$$
\left[ \begin{array}{ccc}
x & y
\end{array} \right]
\times
\left[ \begin{array}{ccc}
3  & 3.5 \\
3.2 & 3.6 \\
\end{array} \right]
=
\left[ \begin{array}{ccc}
118.4 & 135.2
\end{array} \right]
$$
**斐波那契数列**

```
1 1 2 3 5 8 13 ...

     1 1  1 1  1 1  1 1
  X  1 0  1 0  1 0  1 0 
---------------------------------------------
1 1  2 1  3 2  5 3
1 0  1 1  2 1  3 2  ...
```

### numpy通用函数

#### 加法通用函数

```python
np.add(a, b)			# 两数组相加
np.add.reduce(a)		# a数组元素的累加和
np.add.accumulate(a)	# a数组元素累加和的过程
np.add.outer([10,20,30], a)	#外和
```

案例:

```python
a = np.arange(1, 7)
print(a)
print(np.add(a, a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.add.outer(a, [10, 20, 30]))

```

#### 除法通用函数

```python
# 真除
a / b
np.true_divide(a, b)
np.divide(a, b)
# 地板除
np.floor_divide(a, b)
np.ceil(a / b)	# 天花板除
np.trunc(a / b) # 截断除
```

```python
import numpy as np

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
print(a)
print(b)
# 开始测试
print(np.true_divide(a, b))
print(np.divide(a, b))

print(np.floor_divide(a, b))
print(np.ceil(a / b))
print(np.trunc(a / b))
```

#### 三角函数通用函数

```python
np.sin()  np.cos()
```

傅里叶定理

傅里叶说过, 任何周期函数都可以由多个不同振幅/频率/相位的正弦函数叠加而成.

**合成方波**

一个方波由如下参数的正弦波叠加而成:
$$
y = 4\pi \times sin(x) \\
y = \frac{4}{3}\pi \times sin(3x) \\
y = \frac{4}{5}\pi \times sin(5x) \\
y = \frac{4}{7}\pi \times sin(7x) \\
... \\
y = \frac{4}{2n-1}\pi \times sin((2n-1)x) \\
$$
案例:

```python
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# 根据公式搞出来3条曲线
y1 = 4 * np.pi * np.sin(x)
y2 = 4 / 3 * np.pi * np.sin(3 * x)
y3 = 4 / 5 * np.pi * np.sin(5 * x)

# 使用循环控制叠加波的数量
n = 1000
y = np.zeros(1000)
for i in range(1, n + 1):
    y += 4 / (2 * i - 1) * np.pi * \
        np.sin((2 * i - 1) * x)

mp.figure('SIN', facecolor='lightgray')
mp.title('SIN', fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)

mp.plot(x, y1, label='y1')
mp.plot(x, y2, label='y2')
mp.plot(x, y3, label='y3')
mp.plot(x, y, label='y')

mp.legend()
mp.show()
```

**位运算通用函数**

**位异或**

```python
c = a ^ b
c = np.bitwise_xor(a, b)
```

按位异或可以很方便的判断两个数据是否同号

```python
a = np.array([4, -6, 7, -3, -4, 2])
b = np.array([-2, -8, 2, -5, 3, -4])

print(a)
print(b)
print(a ^ b)
print(np.bitwise_xor(a, b))
# where找到符合条件的元素下标 (异号)
print(np.where((a ^ b) < 0)[0])

```

**位与**

```python
e = a & b
e = np.bitwise_and(a, b)
```

利用位与运算计算某个数字是否是2的幂

```python
'''
1  2^0  00001    0  00000
2  2^1  00010    1  00001
4  2^2  00100    3  00011
8  2^3  01000    7  00111
'''
print('-' * 40)
d = np.arange(1, 20)
print(d)
e = np.bitwise_and(d, d - 1)
print(e)

```

**位或 / 位反 / 移位**

```python
# 位或操作
np.bitwise_or(a, b)
# 位反操作 (1变0, 0变1)
np.bitwise_not(a)
# 移位操作
np.left_shift(array, 1)		#每个元素左移1位 (乘2)
np.right_shift(array, 1)	#每个元素右移1位 (除2)

```

### numpy提供的线性代数模块(linalg)

#### 逆矩阵和广义逆矩阵

如果一个方阵A与方阵B的乘积是单位矩阵,则AB互为逆矩阵.

```python
np.linalg.inv(A)  # 返回A方阵的逆矩阵
```

如果A不是方阵, A的逆矩阵则称为广义逆矩阵.

```python
np.linalg.pinv(A) # 返回矩阵A的广义逆矩阵
```

```python
d = A.I # 既可以返回逆矩阵也可以返回广义逆矩阵
```

#### 线性方程求解与线性拟合

```python
# 求解线性方程组
c = np.linalg.solve(a, b)
# 线性拟合(求出误差最小的结果矩阵)
c = np.linalg.lstsq(a, b)[0]
```

$$
\begin{cases}
x -2y+z=0\\
2y-8z=8\\
-4x+5y+9z=-9
\end{cases}
$$

```python

```





































