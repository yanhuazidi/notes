# 数据分析DAY07

### 矩阵的特征值与特征向量

对于n阶方阵,如果存在数a和非零n维列向量x, 使得Ax=ax, 则称a是矩阵A的一个特征值, x是矩阵A属于特征值a的特征向量.

```python
# 已知n阶方阵A, 求特征值与特征向量
# eigvals: 找到的所有特征值数组
# eigvecs: 找到的与特征值对应的特征向量数组
eigvals, eigvecs = np.linalg.eig(A)
# 已知特征值与特征向量,逆向求原方阵
A = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * 
	np.mat(eigvecs).I
```

案例: 读取图片的亮度矩阵, 提取特征值与特征向量, 保留部分特征值, 重新生成新的亮度矩阵所描述的图片, 并绘制在窗体中.

```python
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm

# 使用sm的方法读取一张图片 得到图片像素矩阵
# True  黑白亮度矩阵
# False 完整图像
img = sm.imread('../data/lily.jpg', True)
# 提取图片的特征值与特征向量
eigvals, eigvecs = np.linalg.eig(img)
#print(eigvals.shape, eigvecs.shape)
eigvals[512:] = 0
nimg = np.mat(eigvecs) *  \
    np.mat(np.diag(eigvals)) * \
    np.mat(eigvecs).I
nimg = nimg.real

mp.figure('Lily', facecolor='lightgray')
mp.subplot(1, 2, 1)
mp.xticks([])
mp.yticks([])
mp.imshow(img, cmap='gray')
mp.tight_layout()

mp.subplot(1, 2, 2)
mp.xticks([])
mp.yticks([])
mp.imshow(nimg, cmap='gray')
mp.tight_layout()

mp.show()
```

#### 奇异值分解

有一个矩阵M, 可以分解为3个矩阵U, S, V, 使得U x S x V等于M.

U与V都是正交矩阵(自己乘以自己的转置结果为单位矩阵). 那么S矩阵主对角线上的元素成为矩阵M的奇异值, 其他元素均为0.

```python
# 调用svd方法完成对M矩阵的奇异值分解, 得到U sv V
# 其中sv存储了矩阵M的奇异值
U, sv, V = np.linalg.svd(M)
# 通过U sv V逆向求取原矩阵:
M2 = U * np.diag(sv) * V
```

案例: 读取图片的亮度矩阵, 提取奇异值, 保留部分奇异值, 重新生成新的亮度矩阵所描述的图片, 并绘制在窗体中.

```python
# 奇异值分解
print(img.dtype)
U, sv, V = np.linalg.svd(img)
sv[50:] = 0
img3 = U * np.mat(np.diag(sv)) * V

mp.subplot(2, 2, 3)
mp.xticks([])
mp.yticks([])
mp.imshow(img3, cmap='gray')
mp.tight_layout()
```

## 快速傅里叶变换模块(FFT)

什么是傅里叶变换?

傅里叶定理指出,任何一条周期曲线,无论多么跳跃或不规则,都能表示成一组光滑正弦曲线叠加之和.

傅里叶变换的过程即是把这条周期曲线拆解成多个光滑正弦曲线的过程. 傅里叶变换的目的是将时域(时间域)上的信号转变为频域(频率域信号), 随着域的不同, 对一个事物的了解角度也会随之改变.因此某些在时域中不好处的地方, 在频域中就可以简单的处理.这样可以大量的减少处理信号的存储量.

**傅里叶变换相关函数**

```python
import numpy.fft as nf

# 通过采样数量/采样周期
# 求得傅里叶变换分解所得曲线的频率序列
freqs = np.fft.fftfreq(采样数量, 采样周期)
# fft.fft()方法 通过原函数做快速傅里叶变换
# 得到拆解出来所有的函数参数
# 目标函数值序列(复数序列[实部,虚部]), 
# 复数的模代表振幅,复数的幅角代表相位角
目标复数序列 = np.fft.fft(原函数值序列)

#逆向傅里叶变换
原函数值序列 = np.fft.ifft(目标复数序列)
```

**案例:基于傅里叶变换的频域滤波**

含噪声音信号是高能信号与低能噪声信号叠加的信号. 可以通过傅里叶变换实现简单降噪. 

过程: 

1. 通过FFT使含噪信号转换为含噪频谱.  
2. 把能量较小的频率信号去除.
3. 留下高能频谱后再通过IFFT生成新的声音信号(高能信号).

**实现步骤**

1. 读取音频文件, 获取音频文件的基本信息: 采样个数, 采样周期,与每个采样的声音信号值. 绘制音频的时域图像.

```python
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf
import numpy.fft as nf

sample_rate, noised_sigs = \
    wf.read('../data/noised.wav')
print(sample_rate, noised_sigs.shape)
# 声音在存储时放大了2**15, 所以处理时先除去
noised_sigs = noised_sigs / 2**15
# 绘制声音图像
times = np.arange(
    len(noised_sigs)) / sample_rate
mp.figure('Filter', facecolor='lightgray')

mp.subplot(221)
mp.title('Noised', fontsize=16)
mp.xlabel('Times', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],
        color='dodgerblue', label='Signal')
mp.legend()
mp.show()
```

2. 基于傅里叶变换, 获取音频频率信息, 绘制音频频域的频率/能量图像

```python
# 通过采样个数与周期 得到频率数组
freqs = nf.fftfreq(times.size,
                   1 / sample_rate)
# 获取每个频率对应的能量值
noised_fft = nf.fft(noised_sigs)
noised_pow = np.abs(noised_fft)
mp.subplot(222)
mp.title('Frequency', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(
    freqs[freqs > 0], noised_pow[freqs > 0],
    color='orangered', label='Frequency')

```

3. 将低频噪声去除后绘制音频频率的:频率/能量图像.

```python
# 将低频噪声去除后绘制音频频率的:频率/能量图
fund_freq = freqs[noised_pow.argmax()]
# 找到不是高能信号的噪声信号
noised_inds = np.where(freqs != fund_freq)
# 把fft得到的复数数组中所有噪声信号的值
# 改为0
filter_fft = noised_fft.copy()
filter_fft[noised_inds] = 0
filter_pow = np.abs(filter_fft)
mp.subplot(224)
mp.title('Filter Frequency', fontsize=16)
mp.xlabel('Filter Frequency', fontsize=12)
mp.ylabel('Filter Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(
    freqs[freqs > 0], filter_pow[freqs > 0],
    color='orangered', label='Filter Frequency')

```

4. 基于逆向傅里叶变换,生成新的音频信号,绘制音频的时域图:时间/位移图像.

```python
# 第四步
filter_sigs = nf.ifft(filter_fft).real
mp.subplot(223)
mp.title('Filter', fontsize=16)
mp.xlabel('Times', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],
        color='dodgerblue', label='Signal')
mp.tight_layout()
mp.legend()

```

5 生成音频文件

```python
# 第五步
wf.write(
    '../data/filter.wav', sample_rate,
    (filter_sigs * 2**15).astype('int16'))
```

### 随机数模块(random)

**二项分布(binomial)**

二项分布就是重复n次的伯努利试验. 在每次实验中只有两种可能性:成功/失败. 两种结果相互对立, 相互独立, 事件发生与否的概率在每一次独立实验中都保持不变.

```python
#产生size个随机数, 每个随机数来自n次尝试中的成功次数, 其
#中每次尝试成功的概率为p
np.random.binomial(n, p, size)
```

案例: 

某人投篮命中率0.3, 投10次, 进5个的概率大概多少?

```python
n = 10
p = 0.3
s = np.random.binomial(n, p, 10000)
print(s)
print(sum(s == 5) / 10000)
```

**超几何分布(hypergeometric)**

超几何分布是"无放回模型".

```python
# 产生size个随机数, 每个随机数为在样本中随机抽取samples
# 个样本后好样本的个数.
# 其中总样本由ngood个好样本 和 nbad个坏样本组成.
s = np.random.hypergeometric(
    ngood, nbad, samples, size)
```

案例:

```python
print('-' * 40)
a = np.random.hypergeometric(9, 1, 3, 10)
print(a)

```

**正态分布**

```python
# loc代表期望值, scale为标准差
# 最终随机到的数字呈标准正态分布(loc=0,scale=1)
np.random.normal(loc=0, scale=1, size)
```

### 杂项功能

#### 排序

**联合间接排序**

联合间接排序支持为待排序列排序,若待排序列值相同,则利用参考序列作为参考继续排序.最终返回排序过后的有序索引序列.

```python
indices = np.lexsort((参考序列, 待排序列))
```

案例: 先按价格排序, 然后再按销售量排序.

```python
import numpy as np

prices = np.array([
    92, 83, 71, 92, 40, 12, 64])
volumes = np.array([
    231, 38, 94, 56, 19, 61, 36])

indices = np.lexsort((volumes * -1, prices))
products = ['P1', 'P2', 'P3', 'P4',
            'P5', 'P6', 'P7']
for i in range(indices.size):
    print(products[indices[i]], end=' ')

```

**复数数组排序**

按照实部升序排列, 对于实部相同的元素,参考虚部升序排列,返回排序后的结果数组.

```python
np.sort_complex(复数数组)
```

**插入排序**

若有需求向有序数组中插入元素, 而后使数组依然有序, numpy提供了searchsorted方法查询并返回可插入位置数组.

```python
indices = np.searchsorted(有序序列, 待插入序列)
```

调用numpy的insert方法将待插入序列中的元素插入到指定位置,返回数据插入后的结果.

```python
np.insert(被插入序列, 位置序列, 待插入序列)
```

```python
# 测试插入排序

a = np.array([1, 2, 3, 5, 6, 8])
b = np.array([4, 7])
indices = np.searchsorted(a, b)
print(indices)
# 插入元素 向a中的indices位置插入b元素
d = np.insert(a, indices, b)
print(d)

```

**插值**

scipy提供了常见的插值算法可以通过一系列的散点值设计出符合一定规律的插值器函数.我们可以使用matplotlib绘制插值器函数的图像.

```python
import scipy.interpolate as si
#返回插值器函数, 可以通过插值器函数绘制插值器的图像
func = si.interp1d(
	散点x坐标,
    散点y坐标,
    kind='插值器算法'  (默认:kind线性插值器)
)
```

案例:

```python
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 原始数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 20)
dis_y = np.sinc(dis_x)

# 绘制原曲线
mp.figure('Interpolate')
mp.title('Interpolate')
mp.grid(linestyle=':')
mp.plot(dis_x, dis_y, 'o-',
        color='dodgerblue', label='y=sinc(x)')
mp.legend()

# 通过一系列散点 基于线性插值器 求得曲线函数
linear = si.interp1d(dis_x, dis_y)
x = np.linspace(min_x, max_x, 1000)
y = linear(x)
mp.figure('linear')
mp.title('linear')
mp.grid(linestyle=':')
mp.plot(x, y, color='dodgerblue',
        label='y=sinc(x)')
mp.legend()

# 通过一系列散点 基于三次样条插值器 求得曲线函数
cubic = si.interp1d(dis_x, dis_y,
                    kind='cubic')
y = cubic(x)
mp.figure('cubic')
mp.title('cubic')
mp.grid(linestyle=':')
mp.plot(x, y, color='dodgerblue',
        label='y=sinc(x)')
mp.legend()
mp.show()
```

##### 积分

直观说, 对于一个给定的正实值函数, 在一个实数区间上的定积分可以理解为坐标平面由曲线/直线以及轴围城的曲边梯形的面积值.

```python
import scipy.integrate as si
# f: 函数
# [a, b]: 定积分的区间
# quad方法返回值为一个元组, (积分值, 误差)
area = si.quad(f, a, b)[0]
```

案例: 利用微元法求y=x<sup>2</sup>+3x+4在[-5,5]区间的定积分.

```python
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc
import scipy.integrate as si


def f(x):
    return 2 * x**2 + 3 * x + 4

a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)

mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x1, y1, color='dodgerblue',
        linewidth=6, alpha=0.5,
        label=r'$y=x^2+3x+4$')

# 利用微元法绘制函数在区间中的小梯形
n = 150
x2 = np.linspace(a, b, n + 1)
y2 = f(x2)

# 求积分
area = 0
for i in range(n):
    area += (y2[i] + y2[i + 1]) * \
        (x2[i + 1] - x2[i]) / 2
print(area)

# 使用API求积分
area = si.quad(f, a, b)[0]
print(area)

for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [x2[i], 0], [x2[i], y2[i]],
        [x2[i + 1], y2[i + 1]],
        [x2[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))

mp.legend()
mp.show()
```

#### 简单图像处理

scipy.ndimage中提供了一些简单的图像处理函数,如高斯模糊, 任意角度旋转, 边缘识别等功能.

```python
import scipy.misc as sm
import scipy.ndimage as sn
# 把图像读取为亮度矩阵 (使用灰度颜色映射后将会变为黑白图)
img = sm.imread('url', True)
# 高斯模糊 21可以简单理解为模糊程度
img = sn.median_filter(img, 20)
# 图像旋转45度
img = sn.rotate(img, 45)
# 边缘识别
img = sn.prewitt(img)
```

案例:

```python
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import matplotlib.pyplot as mp

img = sm.imread('../data/lily.jpg', True)
mp.figure('Image', facecolor='lightgray')
mp.subplot(221)
mp.axis('off')  # 关闭坐标轴
mp.imshow(img, cmap='gray')

# 高斯模糊
img1 = sn.median_filter(img, 21)
mp.subplot(222)
mp.axis('off')  # 关闭坐标轴
mp.imshow(img1, cmap='gray')

# 角度旋转
img2 = sn.rotate(img, 45)
mp.subplot(223)
mp.axis('off')  # 关闭坐标轴
mp.imshow(img2, cmap='gray')

# 边缘识别
img3 = sn.prewitt(img)
mp.subplot(224)
mp.axis('off')  # 关闭坐标轴
mp.imshow(img3, cmap='gray')

mp.show()
```

#### 金融相关API

```python
import numpy as np

# 将1000元以1%的年利率存银行5年, 每年加
# 存100元, 到期后本息一共多少钱?
# 求金融终值 fv
fv = np.fv(0.01, 5, -100, -1000)
print(fv)

# 将多少钱以1%的年利率存入银行5年, 每年
# 加存100元,到期后本息合计fv元.
# 求金融现值 pv
pv = np.pv(0.01, 5, -100, fv)
print(pv)

# 净现值
# 将1000元以1%的年利率存入银行5年, 每年加存
# 100元, 相当于现在要一次性存入多少钱
npv = np.npv(0.01, [-1000, -100,
                    -100, -100, -100, -100])
print(npv)

# 每期支付
# 以1%的利率从银行贷款1000元, 分5年还清.
# 平均每年还多少钱?
pmt = np.pmt(0.01, 5, 1000)
print(pmt)
pmt = np.pmt(0.0441 / 12, 360, 1000000)
print(pmt)

# 以4.41%/12的利率从银行贷款100万元,
# 平均每期还pmt元, 多少年还清?
nper = np.nper(0.0441 / 12, pmt, 1000000)
print(nper)
```









































