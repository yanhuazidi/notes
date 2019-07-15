# 数据分析DAY02

## matplotlib概述

matplotlib是python的一个绘图库,使用它可以很方便的绘制出版质量级别的图形.

### matplotlib的基本功能

1. 基本绘图

   1. 绘制坐标系中连续的线,设置线型/线宽/颜色
   2. 设置坐标轴的范围
   3. 设置坐标刻度
   4. 设置坐标轴
   5. 显示图例
   6. 绘制特殊点
   7. 为图像添加备注.

2. 高级绘图

   1. 绘制子图
   2. 刻度定位器
   3. 刻度网格线
   4. 半对数坐标
   5. 散点图
   6. 图像填充
   7. 条形图
   8. 饼图


## matplotlib基本功能详解

### 基本绘图

绘制一条线的相关API:

```python
import numpy as ap
import matplotlib.pyplot as mp
#xarray: 散点的x坐标数组
#yarray: 散点的y坐标数组
mp.plot(xarray, yarray)
mp.show()
```

绘制水平线与垂直线相关API:

```python
#绘制一条垂直x轴的线, 需要给x坐标值value,指定y坐标范围
mp.vlines(value, ymin, ymax, ..)
#绘制一条垂直y轴的线, 需要给y坐标值value,指定x坐标范围
mp.hlines(value, xmin, xmax, ..)
```

#### 线型/线宽/颜色

```python
#linestyle: 线型
	# - or solid 直线
    # -- or dashed 虚线
    # -. or dashdot 点虚线
    # : or dot 点线 
#linewidth: 线宽 (数字代表n倍线宽)
#color: 英文的颜色单词 或 常见颜色单词的首字母 或
        #abcdef 或 (1, 1, 0.7) 或 (1, 1, 1, 1)
#alpha: 设置透明度 0~1  0为完全透明  

mp.plot(xarray, yarray, 
       linestyle='',	# 线型
       linewidth=1,		# 线宽
       color='', 		# 颜色
       alpha=0.5		# 透明度
)
```

#### 设置坐标轴范围

设置图像的可视区域.

```python
#x_lim_min: 可视区域x的最小值
#x_lim_max: 可视区域x的最大值
mp.xlim(x_lim_min, x_lim_max)
#同上
mp.ylim(y_lim_min, y_lim_max)
```

#### 设置坐标刻度

```python
#设置x轴的坐标刻度
#x_val_list: 坐标值列表
#x_text_list: 坐标刻度列表
mp.xticks(x_val_list, x_text_list)
mp.yticks(y_val_list, y_text_list)
```

*刻度文本的特殊语法 -- LaTex排版语法规范* (参考附录)
$$
x^2 + y^2 = z^2, -\frac{\pi}{2}
$$

#### 设置坐标轴

坐标轴包含四个: left / right / bottom / top

```python
# getCurrentAxis 获取当前坐标轴对象
ax = mp.gca()
axl = ax.spines['left']
axr = ax.spines['right']
...
# 设置坐标轴的颜色
axl.set_color() 
# 设置坐标轴的位置  
# ('data', 0) 以坐标值作为定位参考, 设置坐标轴到0位置
axl.set_position((type, val))
```

#### 显示图例

```python
# 自动在窗口中某个位置添加图例
# 添加图例需要在调用mp.plot()绘制曲线时设置label参数
mp.plot(..., label='y=sin(x)')
# 通过loc参数设置图例的位置
# ===============   =============
# Location String   Location Code
# ===============   =============
# 'best'            0
# 'upper right'     1
# 'upper left'      2
# 'lower left'      3
# 'lower right'     4
# 'right'           5
# 'center left'     6
# 'center right'    7
# 'lower center'    8
# 'upper center'    9
# 'center'          10
===============   =============
mp.legend(loc='')
```

#### 绘制特殊点

```python
# xarray与yarray是坐标序列
mp.scatter(xarray, yarray,
          marker='',	#点型
          s=3,			#大小
          edgecolor='', #边缘色
          facecolor='', #填充色
          zorder=3		#绘制顺序
)
```

*marker点型详见附录*

#### 添加备注文本

```python
mp.annotate(
	'', 				# 备注内容
    xycoords='', 		# 备注目标点使用的坐标系
    xy=(x, y),			# 备注目标点的坐标
    textcoords='',		# 备注文本使用的坐标系
    xytext=(x, y),		# 备注文本的坐标
    fontsize=14,		# 备注文本字体大小
    arrowprops=dict()	# 指示箭头的属性
)
```

arrowprops参数使用字典定义指向目标点的箭头样式

```python
arrowprops=dict(
	arrowstyle='',		# 定义箭头样式
    connectionstyle=''	# 定义连接线的样式
)
```

*arrowstyle参见 help(mp.annotate)*

### 高级图形窗口对象操作

一次绘制两个窗口

```python
mp.figure(
	'',				# 窗口标题
    figsize=(4, 3),	# 窗口大小
    facecolor=''	# 窗口颜色
)
mp.show()
```

mp.figure()方法可以创建多个窗口, 每个窗口的标题不同. 后续调用mp的方法进行绘制时将作用于当前窗口. 如果希望修改以前已经创建过的窗口,可以通过相同的窗口标题调用mp.figure()方法把该窗口置为当前窗口.

**设置当前窗口的常用参数**

```python
#设置图表的标题
mp.title('', fontsize=18)
#设置窗口中x坐标轴的文本即y坐标轴的文本
mp.xlabel('', fontsize=12)		
mp.ylabel('', fontsize=12)
#设置刻度参数(刻度字体大小)
mp.tick_params(labelsize=8)
#设置图表网格线
mp.gird(linestyle=':')
#设置紧凑布局
mp.tight_layout()
```

#### 绘制子图

**矩阵式布局**

```python
mp.figure('')
# 开始绘制一个子图
# 通过参数rows与cols拆分当前窗口, 每个子窗口都将分配一
# 个序号, 1~x
mp.subplot(rows, cols, 1)
mp.title()
mp.grid()
mp.subplot(2, 3, 2)
mp.subplot(233)
mp.show()
```

案例:绘制九宫格子图, 每个子图写一个文本.

```python
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Sub Layout', facecolor='gray')
for i in range(1, 10):
    mp.subplot(3, 3, i)
    mp.text(0.5, 0.5, i, ha='center',
            va='center', size=36, alpha=0.8)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()
mp.show()
```



**网格式布局**

```python
import matplotlib.gridspec as mg
mp.figure('')
# 该方法将会返回子图的二维数组
gs = mg.GridSpec(3, 3)
# 通过subplot对子图进行合并  
# gs[0, :2]->合并0行中的0/1列作为1个子图进行绘制
mp.subplot(gs[0, :2])
mp.show()
```

**自由布局**

```python
mp.figure('')
# left_bottom_x:子图左下角点的横坐标
# left_bottom_y:子图左下角点的纵坐标
# w: 宽度
# h: 高度
mp.axes([left_bottom_x, left_bottom_y,w, h])
mp.show()
```

#### 刻度定位器

```python
# 获取当前坐标轴
ax = mp.gca()
# 设置x轴的主刻度定位器为NullLocator()
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置x轴的次刻度定位器为MultipleLocator()
ax.xaxis.set_minor_locator(mp.MultipleLocator())
```

案例: 画个数轴

```python
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',
            'mp.AutoLocator()',
            'mp.MultipleLocator()',
            'mp.LogLocator(base=2)']

mp.figure('Locators', facecolor='lightgray')

for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    mp.xlim(0, 10)
    mp.ylim(-10, 10)
    mp.yticks([])

    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))

    ax.xaxis.set_major_locator(eval(locator))
    ax.xaxis.set_minor_locator(
        mp.MultipleLocator(0.1))
    mp.plot(np.arange(11), np.zeros(11), c='none')
    mp.text(5, 0.3, locator,
            ha='center', size=12)
    mp.tight_layout()

mp.show()

```

#### 刻度网格线

```python
ax = mp.gca()
ax.grid(
	which='',		#'major' / 'minor'	
    axis='',		#'x' / 'y' / 'both'
    linewidth=1,	# 线宽
    linestyle='',	# 线型
    color='',		
    alpha=0.5
)
```

#### 半对数坐标系

y轴将会以指数方式递增.

```python
mp.figure()
mp.semilogy(x, y, ....)
mp.show()
```

#### 绘制散点图

```python
mp.scatter(
	xarray, 
    yarray,
    marker='',
    s=10,
    color='',
    edgecolor='',
    facecolor='',
    zorder=3
)
```

使用numpy.random的normal函数生成符合二项分布的随机数.

```python
n = 100
# 172: 期望值
# 20:  标准差
# n:   数字生成数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)
```

设置点的颜色

```python
# d的值是一个大于0的数
# 若所有点计算出的d处于[0-1000]区间
# 那么绘制该点时所使用的颜色,可以根据d的值去jet颜色映射
# 表中取值(即如果d取值为500,则使用jet颜色映射表中最中心
# 的颜色值)
d = (x-172)**2 + (y-60)**2
mp.scatter(x, y, c=d, cmap='jet')
```



## 附录

![matplotlib_colors](images\matplotlib_colors.png)

LaTex语法字符串

![laTex_](images\laTex_.png)



![LaTeX_eg](images\LaTeX_eg.gif)



![matplotlib_markers](images\matplotlib_markers.png)



