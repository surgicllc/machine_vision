# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:30:53 2022

@author: Ahmed
"""

# live_analysis : a live video with user modifiable paramteres to analyze edge
# and color detection

# import the libraries
import cv2
import numpy as np
#'optional' argument is required for trackbar creation parameters
def nothing():
    pass
  
  
# define a video capture object
vid = cv2.VideoCapture(0, cv2.CAP_V4L2)
 
#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
cl= 'Canny lower Threshold'
cu= 'Canny Upper Threshold'
wnd = 'Colorbars'

cv2.namedWindow('Colorbars') # Create a window named 'Colorbars'
#Begin Creating trackbars for each
cv2.createTrackbar(hl, wnd,0,179,nothing)
cv2.createTrackbar(hh, wnd,0,179,nothing)
cv2.createTrackbar(sl, wnd,0,255,nothing)
cv2.createTrackbar(sh, wnd,0,255,nothing)
cv2.createTrackbar(vl, wnd,0,255,nothing)
cv2.createTrackbar(vh, wnd,0,255,nothing)
cv2.createTrackbar(cl, wnd,0,255,nothing) # canny thresholding recommends cu = cl*3
cv2.createTrackbar(cu, wnd,0,255,nothing)



  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame_raw = vid.read()
    
    frame_blur = cv2.GaussianBlur(frame_raw, (5,5), 0)
    frame_hsv = cv2.cvtColor(frame_raw, cv2.COLOR_BGR2HSV)
    
    #read trackbar positions for each trackbar
    hul=cv2.getTrackbarPos(hl, wnd)
    huh=cv2.getTrackbarPos(hh, wnd)
    sal=cv2.getTrackbarPos(sl, wnd)
    sah=cv2.getTrackbarPos(sh, wnd)
    val=cv2.getTrackbarPos(vl, wnd)
    vah=cv2.getTrackbarPos(vh, wnd)
    cThreshold1=cv2.getTrackbarPos(cl, wnd)
    cThreshold2=cv2.getTrackbarPos(cu, wnd)

    
    #make array for final values
    HSVLOW = np.array([hul,sal,val])
    HSVHIGH = np.array([huh,sah,vah])
    # This creates a mask of the range of colors chosen of
    # objects found in the frame.
    mask = cv2.inRange(frame_hsv, HSVLOW, HSVHIGH)
  
    # The bitwise and of the frame and mask is done so 
    # that only the blue coloured objects are highlighted 
    # and stored in res
    res = cv2.bitwise_and(frame_blur, frame_blur, mask = mask) # dst(I)=sur1(I) ^ sur2(I), if mask(I) != 0, where ^ represents the 'and' operator
    
    # Canny Edge Detection
    frame_canny = cv2.Canny(image = frame_blur, threshold1 = cThreshold1, threshold2 = cThreshold2) 

    # Closing then Opening with a wide kernel
    kernel = np.ones((5,5),np.uint8)
    kernel2 = np.ones((2,6),np.uint8)
    frame_close = cv2.morphologyEx(frame_canny, cv2.MORPH_CLOSE, kernel)
    frame_open =  cv2.morphologyEx(frame_close, cv2.MORPH_OPEN, kernel2)
#=============================================================================   
    # HOUGH TRANSFORM https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 50  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments
    frame_line = np.copy(frame_raw) * 0  # creating a blank to draw lines on
    frame_line_color = np.copy(frame_raw) * 0  # creating a blank to draw lines on
    
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(frame_close, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(frame_line,(x1,y1),(x2,y2),(0,0,255),5)
            
    # Draw the lines on the  image
    lines_edges = cv2.addWeighted(frame_raw, 0.8, frame_line, 1, 0)
#=============================================================================

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines_color = cv2.HoughLinesP(mask, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)
    
    for line_color in lines_color:
        for x1,y1,x2,y2 in line:
            cv2.line(frame_line_color,(x1,y1),(x2,y2),(0,0,255),5)
            
    # Draw the lines on the  image
    lines_edges_color = cv2.addWeighted(frame_raw, 0.8, frame_line_color, 1, 0)
    
#=============================================================================

    
    

        
    # Split into channels
    (B, G, R) = cv2.split(frame_blur)
    (H, S, V) = cv2.split(frame_hsv)

    # Display Opened and Closed Canny Image
    # cv2.namedWindow('Close after Canny', cv2.WINDOW_NORMAL)
    # cv2.imshow('Close after Canny', frame_close)

    # cv2.namedWindow('Open after Close', cv2.WINDOW_NORMAL)
    # cv2.imshow('Open after Close', frame_open)

    # Display the rest
    # cv2.namedWindow('frame_raw', cv2.WINDOW_NORMAL)
    # cv2.imshow('frame_raw', frame_raw)
    
    # cv2.namedWindow('frame_blur', cv2.WINDOW_NORMAL)
    # cv2.imshow('frame_blur', frame_blur)

    # cv2.namedWindow('frame_hsv', cv2.WINDOW_NORMAL)
    # cv2.imshow('frame_hsv', frame_hsv) # cv2.imshow() expects a BGR array
    
    # cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    # cv2.imshow('mask', mask)
    
    # cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    # cv2.imshow('res', res)
    
    cv2.namedWindow('lines_edges_color', cv2.WINDOW_NORMAL)
    cv2.imshow('lines_edges_color', lines_edges_color)

    hsv_split = np.concatenate((frame_hsv, H, S, V, mask, res),axis=1)
    cv2.namedWindow('hsv_split', cv2.WINDOW_NORMAL)
    cv2.imshow('hsv_split', hsv_split)

    edges_detected = np.concatenate((frame_raw, frame_canny, frame_close, frame_open, lines_edges),axis=1)
    cv2.namedWindow('edges_detected', cv2.WINDOW_NORMAL)
    cv2.imshow('edges_detected', edges_detected)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Destroy all the windows
vid.release()
cv2.destroyAllWindows()