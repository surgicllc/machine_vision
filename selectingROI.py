# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:37:25 2022

@author: Ahmed
"""

## selectingROI :- a preliminary program to manually crop pre-captured images

import cv2
import numpy as np
  
path = r'C:\\Users\\ahmed\\Downloads\\Surgic\\Image Processing\\Testing\\IMG_0461.jpg'

# Read image
img_raw = cv2.imread(path, 0)
  
# Select ROI
cv2.namedWindow("select the area", cv2.WINDOW_NORMAL)
r = cv2.selectROI("select the area", img_raw)
  
# Crop and blur image
img_cropped = img_raw[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]
img_blur = cv2.GaussianBlur(img_cropped,(5, 5), sigmaX = 0, sigmaY = 0)
  
# Display cropped, blurred image
cv2.namedWindow("Cropped and blurred image", cv2.WINDOW_NORMAL)
cv2.imshow("Cropped and blurred image", img_blur)
cv2.waitKey(0)

# Canny Edge Detection
img_canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) 

# displaying Canny Edge Detection Image
cv2.namedWindow('Canny Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Canny Edge Detection', img_canny)
cv2.waitKey(0)

# Closing then Opening with a wide kernel
kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((2,6),np.uint8)
img_close = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel)
img_open =  cv2.morphologyEx(img_close, cv2.MORPH_OPEN, kernel2)

# Display Opened/Closed Canny Image
cv2.namedWindow('Close after Canny', cv2.WINDOW_NORMAL)
cv2.imshow('Close after Canny', img_close)
cv2.waitKey(0)

cv2.namedWindow('Open after Close', cv2.WINDOW_NORMAL)
cv2.imshow('Open after Close', img_open)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # %% Displaying comparison
# cmpH = np.concatenate((img_raw, img_canny), axis=1)

# cv2.namedWindow('Before and After Edge Detection', cv2.WINDOW_NORMAL)
# cv2.imshow('Before and After Edge Detection', cmpH)d
# cv2.waitKey(0)
# cv2.destroyAllWindows()
 
