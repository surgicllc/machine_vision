# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:36:42 2022

@author: Ahmed
"""

## MeasuringLength:- a preliminary program to measure line length from Hough [NOT LIVE]

import cv2
import numpy as np
  
path = r'C:\Users\ahmed\SURGIC\opencv_frame_0.png' # change this to the image-to-be-analyzed

# Read image
img_raw = cv2.imread(path, 0)
img_blur = cv2.GaussianBlur(img_raw,(5, 5), sigmaX = 0, sigmaY = 0)

# %% Canny Edge Detection
img_canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) 

# Closing then Opening with a wide kernel
kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((2,6),np.uint8)
img_close = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel)
img_open =  cv2.morphologyEx(img_close, cv2.MORPH_OPEN, kernel2)

# %% HOUGH TRANSFORM
rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img_raw) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(img_close, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
        
# Draw the lines on the  image
lines_edges = cv2.addWeighted(img_raw, 0.8, line_image, 1, 0)

# %% Display   
img_cat = np.concatenate((img_raw, img_canny, img_close, img_open, lines_edges),axis=1)
cv2.namedWindow('img_cat', cv2.WINDOW_NORMAL)
cv2.imshow('img_cat', img_cat)
cv2.waitKey(0)
cv2.destroyAllWindows()