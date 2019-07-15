# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
