# 数据分析DAY03

## matplot基本功能详解

### 图形对象操作

#### 填充操作

以某种颜色自动填充两条曲线的闭合区域.

```python
mp.fill_between(
	x, 				# x轴水平坐标
    sinx,			# sinx曲线的y坐标
    cosx,			# cosx曲线的y坐标
    sinx < cosx,	# 填充条件为True时,执行填充操作
    color=''		# 颜色
    alpha=0.3		# 透明度
)
```

案例:绘制两条曲线: sinx=sin(x)   cosx=cos(x/2) / 2  [0-8π]

```python
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2

mp.figure("Fill", facecolor='lightgray')
mp.title("Fill", fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.plot(x, sinx, color='dodgerblue',
        label='y=sin(x)')
mp.plot(
    x, cosx, color='orangered',
    label=r'$y=\frac{cos(\frac{x}{2})}{2}$')
# 填充
mp.fill_between(
    x, sinx, cosx, sinx > cosx,
    color='dodgerblue', alpha=0.5)
mp.fill_between(
    x, sinx, cosx, sinx < cosx,
    color='orangered', alpha=0.5)


mp.tight_layout()
mp.legend()
mp.show()
```

#### 条形图(柱状图)

```python
mp.bar(
	x,			# 水平坐标数组
    y,			# 柱状图高度数组
    width,		# 柱子的宽度
    color='',	# 填充颜色
    label='',	#
    alpha=0.5	#
)
```

案例:绘制苹果12个月的销量,绘制橘子的销量.

```python
import numpy as np
import matplotlib.pyplot as mp

apples = [23, 19, 81, 22, 65, 34, 65, 23, 89, 56, 89, 39]
oranges = [56, 56, 74, 39, 64, 95, 63, 48, 56, 98, 65, 45]

mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=18)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')

x = np.arange(len(apples))
mp.bar(x - 0.2, apples, 0.4,
       color='dodgerblue', label='Apple')
mp.bar(x + 0.2, oranges, 0.4,
       color='orangered', label='Orange')

mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
```

#### 饼状图

```python
mp.pie(
	values,			# 值列表
    spaces,			# 扇形之间的间距列表
    labels, 		# 扇形的标签列表
    colors,			# 扇形的颜色列表
    '%d%%',			# 所占比例的格式
    shadow=True,	# 绘制阴影
    startangle=90,	# 逆时针绘制饼状图的起始角度
    radius=1		# 半径
)
```

案例:绘制饼状图显示5门语言的流行度.

```python
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=14)

values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
# 等轴比例绘制
mp.axis('equal')
mp.pie(values, spaces, labels, colors,
       '%d%%', shadow=True,
       startangle=90, radius=1)
mp.legend()
mp.show()

```

#### 等高线图

组成等高线需要网格点坐标矩阵,也需要每个点的高度.所以等高线的绘制是属于3D数学模型的范畴.

```python
#绘制等高图
mp.contourf(
    x, y, 	# 网格坐标矩阵
    z, 		# 坐标矩阵中每个点的值
    8, 		# 把整个模型的高度等分8份
    cmap='jet'	#颜色映射
)
#绘制等高线
mp.contour(x, y, z, 8, 
           colors='black',
           linewidths=0.5
)
# 设置等高线的标签文本
mp.clabel(cntr, inline_spacing=1,
          fmt='%.1f', fontsize=10)
```

#### 热成像图

用图形的方式显示矩阵及矩阵中值的大小.

```python
# origin
# 'upper': 默认值 y轴方向向下
# 'lower': y轴方向向上
mp.imshow(z, cmap='jet', origin='lower')
```

#### 3D图像绘制

matplotlib支持绘制三维曲面,但需要使用axes3d提供的3d坐标系进行绘制. 

```python
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')
# 使用ax3d对象绘制3维图形
ax3d.scatter()			# 3维散点图
ax3d.plot_surface()		# 3维平面图
ax3d.plot_wireframe()	# 3维线框图
```

**3维散点图的绘制**

```python
ax3d.scatter(
	x, y, z, 		# 点的位置坐标数组 x, y, z
    marker='',		#
    s=30,			#
    zorder=3,		#
    color='',		#
    edgecolor='',	# 边缘色
    facecolor='',	# 填充色
    c=v, 			# 设置颜色(使用cmap映射)
    cmap=''			
)
```

案例: 生成三维散点数组, 显示在三维坐标系中.

```python
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

mp.figure('3D Points', facecolor='gray')
mp.title('3D Points', fontsize=18)
# 获取3d坐标轴
ax = mp.gca(projection='3d')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
mp.tick_params(labelsize=8)
# v用于设置散点的颜色
v = np.sqrt(x**2 + y**2 + z**2)
ax.scatter(x, y, z, s=30, c=v, cmap='jet',
           alpha=0.5)
mp.show()
```

**绘制3d平面图**

```python
#如果n为1000, rstride为30,则图像将会被评分1000/33份,
#分别设置不同的渐变色.这意味着跨距越小,图像越细腻,资源消
#耗也越大.
ax3d.plot_surface(
	x, y, z,	# 与等高线图的xyz参数相同
    rstride=30,	# 行跨距
    cstride=30, # 列跨距
    cmap='jet'	# 颜色映射
)
```

**绘制3d线框图**

```python
ax3d.plot_wireframe(
    x, y, z, 		# 与等高线图的xyz参数相同
    rstride=30, 	# 行跨距
    cstride=30, 	# 列跨距
	linewidth=1,	
	color=''
)
```

#### 极坐标系

与笛卡尔坐标系不同,某些情况下极坐标系适合处理与角度有关的图像.极坐标系可以描述极径&rho;(rho)与极角&theta;(theta)之间的关系.

```python
mp.figure()
mp.gca(projection='polar')
# 再进行图像绘制时将会基于极坐标系进行绘制
```

案例:在极坐标系中绘制一条线 [0,4π]  y=0.8*x

```python
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 4 * np.pi, 1000)
y = 0.8 * x
sinx = 3 * np.sin(6 * x)
mp.figure('Polar', facecolor='lightgray')
mp.gca(projection='polar')  # 使用极坐标系
mp.title('Polar', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, label='y=0.8x')
mp.plot(x, sinx, label='y=3sin(6x)')
mp.legend()
mp.show()

```

#### 实现简单动画

动画是在一段时间内快速连续的重新绘制图像的过程.

matplotlib提供了方法用于处理简单动画的绘制.定义update函数用于实时更新图像.

```python
import matplotlib.animation ma
# 更新图像的函数,在该函数中实现图像更新业务
def update(number):
    pass
# 开始执行一段动画 (每隔10毫秒执行update更新界面)
# mp.gcf(): 获取当前窗体 getCurrentFrame() 
# update:	更新图像的函数,在该函数中实现图像更新业务
# interval: 周期时间
ma.FuncAnimation(mp.gcf(), update, interval=10)
```

案例:

```python
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

# 1.随机生成100个泡泡
# [((1,2), 30, 1, (0.2,0.2,0.2))]

n = 100
balls = np.zeros(n, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4)])
# 对着100个元素进行初始化 设置随机值
# uniform随机生成0-1的数填充n行2列的数组
balls['position'] = np.random.uniform(
    0, 1, (n, 2))
balls['size'] = np.random.uniform(
    60, 70, n)
balls['growth'] = np.random.uniform(
    10, 50, n)
balls['color'] = np.random.uniform(
    0, 1, (n, 4))

# 绘制这些球
mp.figure('Bubbles', facecolor='lightgray')
mp.title('Bubbles', fontsize=18)
mp.xticks([])
mp.yticks([])

sc = mp.scatter(balls['position'][:, 0],
                balls['position'][:, 1],
                balls['size'],
                color=balls['color'])


# 在update函数中更新球的状态
def update(number):
    balls['size'] += balls['growth']
    # 选择一个泡泡使之破裂
    boom_ind = number % n
    balls[boom_ind]['size'] = \
        np.random.uniform(67, 80, 1)
    balls[boom_ind]['position'] = \
        np.random.uniform(0, 1, (1, 2))
    # 重新绘制
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(
    mp.gcf(), update, interval=30)

mp.show()
```

使用生成器函数提供数据,实现动画的绘制

```python
import matplotlib.animation ma
# 更新图像的函数,在该函数中实现图像更新业务
def update(val):
    pass
# 生成器函数用于提供动画所需参数
def generator():
    # ...
    yield val
#执行动画时,将会先调用generator获取数据,然后带着数据调
#用update函数执行界面更新.(这个过程每10毫秒执行一次)
ma.FuncAnimation(mp.gcf(), update, 
                 generator,interval=10)
```

案例:模拟信号接收器 y=sin(2πt)*exp(sin(0.2πt))

```python
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=18)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle=':', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue',
             label='Signal')[0]
pl.set_data([], [])
# 接收生成器生成的(x,y),添加到绘制的
# 曲线坐标数组中,重新绘制界面


def update(data):
    t, v = data
    x, y = pl.get_data()
    # 把新的坐标点,添加到当前plot对象坐标数组中
    x.append(t)
    y.append(v)
    # 重新设置plot对象的数据集
    pl.set_data(x, y)
    # 移动坐标轴
    if(x[-1] > 10):
        mp.xlim(x[-1] - 10, x[-1])
    pass


x = 0
# 生成坐标点数据 yield返回
def generator():
    global x
    y = np.sin(2 * np.pi * x) * \
        np.exp(np.sin(0.2 * np.pi * x))
    yield (x, y)
    x += 0.05

# 执行动画
anim = ma.FuncAnimation(
    mp.gcf(), update, generator, interval=30)

mp.show()
```



## numpy与matplotlib应用

### 加载文件

读取aapl.csv文件, 在图标中绘制文件信息.

```python
#当numpy读取文件时,会把第一列的数据先经过func函数处理,
#然后交给dtype进行数据类型转换,最终赋值给dates变量.
def func(date):
    return '2011-10-10'

dates, opening_price = np.loadtxt(
	'../data/csv',			# 文件路径
    delimiter=',', 			# 文件的列分隔符(,)
    usecols=(1,3),			# 需要读取的列的下标
    unpack=True,			# 是否需要拆包
    dtype='U10,f8',			# 读取的每一列的类型	
    converters={1:func}		# 转换器函数字典
)
```

案例:读取文件,绘制股价图.

```python

```











































































