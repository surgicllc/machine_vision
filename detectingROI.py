# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:19:30 2022

@author: Ahmed
"""

## detectingROI :- a preliminary program to crop pre-captured images [WIP]

import cv2
import numpy as np
  
path = r'C:\\Users\\ahmed\\Downloads\\Surgic\\Image Processing\\Testing\\IMG_0461.jpg'

# Read image
img_raw = cv2.imread(path)
img_hsv = cv2.cvtColor(img_raw, cv2.COLOR_BGR2HSV)

# Split into channels
(B, G, R) = cv2.split(img_raw)
(H, S, V) = cv2.split(img_hsv)


# Display
cv2.namedWindow('img_raw', cv2.WINDOW_NORMAL)
cv2.imshow('img_raw', img_raw)
cv2.waitKey(0)

cv2.namedWindow('img_hsv', cv2.WINDOW_NORMAL)
cv2.imshow('img_hsv', img_hsv) # cv2.imshow() expects a BGR array
cv2.waitKey(0)

hsv_split = np.concatenate((H, S, V),axis=1)
cv2.namedWindow('hsv_split', cv2.WINDOW_NORMAL)
cv2.imshow('hsv_split', hsv_split)
cv2.waitKey(0)

cv2.destroyAllWindows()