# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:46:34 2022

@author: Ahmed
"""

## test_vision_Canny :- a preliminary program to detect sutures in pre-captured images, using Canny edge detection

import cv2
import numpy as np

# fetching image path
path = r'C:\\Users\\ahmed\\Downloads\\Surgic\\Image Processing\\Testing\\IMG_0461.jpg'

# %% windows settings (NOTE: cv2.namedWindow creates window; copy/paste it under the display code block)
blurredWin = 'Blurred Image'
#cv2.namedWindow(blurredWin, cv2.WINDOW_NORMAL)
cannyWin = 'Canny Edge Detection'
#cv2.namedWindow(cannyWin, cv2.WINDOW_NORMAL)
sobelYWin = 'Sobel Y'
#cv2.namedWindow(sobelYWin, cv2.WINDOW_NORMAL)
sobelXYWin = 'Sobel XY using Sobel() function'
#cv2.namedWindow(sobelXYWin, cv2.WINDOW_NORMAL)
cv2.destroyAllWindows()

# %% loading image (in greyscale)
img_raw = cv2.imread(path, 0)
img_blur = cv2.GaussianBlur(img_raw,(15,15), sigmaX = 0, sigmaY = 0)

# displaying blurred image
cv2.namedWindow(blurredWin, cv2.WINDOW_NORMAL)
cv2.imshow(blurredWin, img_blur)
cv2.waitKey(0) #this is necessary to avoid Python kernel form crashing)
cv2.destroyAllWindows()

# %% Canny Edge Detection
img_canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) 

# displaying Canny Edge Detection Image
cv2.namedWindow(cannyWin, cv2.WINDOW_NORMAL)
cv2.imshow(cannyWin, img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% Displaying comparison
cmpH = np.concatenate((img_raw, img_canny), axis=1)

cv2.namedWindow('Before and After Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Before and After Edge Detection', cmpH)
cv2.waitKey(0)
cv2.destroyAllWindows()