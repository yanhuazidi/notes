# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
original = cv.imread('../../data/sunrise.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
eq_gray = cv.equalizeHist(gray)
cv.imshow('Eq-Gray', eq_gray)
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
eq_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Eq-Color', eq_color)
cv.waitKey()
