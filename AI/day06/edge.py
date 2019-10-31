# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
original = cv.imread(
    '../../data/chair.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Original', original)
edge = cv.Canny(original, 50, 240)
cv.imshow('Edge', edge)
cv.waitKey()
