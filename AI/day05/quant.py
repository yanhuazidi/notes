# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp
image1 = sm.imread(
    '../../data/lily.jpg', True).astype(np.uint8)
x = image1.reshape(-1, 1)
model = sc.KMeans(n_clusters=4)
model.fit(x)
centers = model.cluster_centers_.squeeze()
y = model.labels_
image2 = centers[y].reshape(image1.shape)
model = sc.KMeans(n_clusters=3)
model.fit(x)
centers = model.cluster_centers_.squeeze()
y = model.labels_
image3 = centers[y].reshape(image1.shape)
model = sc.KMeans(n_clusters=2)
model.fit(x)
centers = model.cluster_centers_.squeeze()
y = model.labels_
image4 = centers[y].reshape(image1.shape)
mp.figure('Image Quantization', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(image1, cmap='gray')
mp.subplot(222)
mp.title('4 Colors', fontsize=16)
mp.axis('off')
mp.imshow(image2, cmap='gray')
mp.subplot(223)
mp.title('3 Colors', fontsize=16)
mp.axis('off')
mp.imshow(image3, cmap='gray')
mp.subplot(224)
mp.title('2 Colors', fontsize=16)
mp.axis('off')
mp.imshow(image4, cmap='gray')
mp.tight_layout()
mp.show()
