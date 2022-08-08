# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:23:28 2022

@author: Ahmed
"""

## test_vision_sobel :- a preliminary program to detect sutures in pre-captured images, using Canny edge detection

import cv2
import numpy as np

# getting image
path = r'C:\\Users\\ahmed\\Downloads\\Surgic\\Image Processing\\Testing\\IMG_0461.jpg'

# %% windows settings (NOTE: cv2.namedWindow creates window; copy/paste it under the display code block)
blurredWin = 'Blurred Image'
#cv2.namedWindow(blurredWin, cv2.WINDOW_NORMAL)
sobelXWin = 'Sobel X'
#cv2.namedWindow(sobelXWin, cv2.WINDOW_NORMAL)
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

# %% Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=5, dy=0, ksize=11) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=5, ksize=11) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=5, dy=5, ksize=11) # Combined X and Y Sobel Edge Detection

# Display Sobel Edge Detection Images
cv2.namedWindow(sobelXWin, cv2.WINDOW_NORMAL)
cv2.imshow(sobelXWin, sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow(sobelYWin, cv2.WINDOW_NORMAL)
cv2.imshow(sobelYWin, sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow(sobelXYWin, cv2.WINDOW_NORMAL)
cv2.imshow(sobelXYWin, sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()