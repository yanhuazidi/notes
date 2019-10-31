# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
import matplotlib.pyplot as mp
original = cv.imread('../../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Star特征点检测器
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = original.copy()
cv.drawKeypoints(original, keypoints, mixture,
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
# SIFT特征描述器
sift = cv.xfeatures2d.SIFT_create()
_, desc = sift.compute(gray, keypoints)
mp.matshow(desc.T, cmap='jet', fignum='SIFT')
mp.title('SIFT', fontsize=20)
mp.xlabel('Sample', fontsize=14)
mp.ylabel('Feature', fontsize=14)
mp.tick_params(which='both', top=False, labeltop=False,
               labelbottom=True, labelsize=10)
mp.tight_layout()
mp.show()
