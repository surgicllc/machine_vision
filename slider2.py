# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:34:19 2022

@author: Ahmed

slider2.py - Demonstrating a user of trackbars on OpenCV windows
Author: Tim Poulsen, github.com/skypanther
License: MIT
2018-10-15
Example usage:
python3 slider2.py -i path/to/image.jpg
"""

import cv2
import numpy as np

edge_params = {
    'min_val': 200,
    'max_val': 300,
    'aperture_size': 3
}
gray = None


def main():
    global edge_params, gray
    file_name = r"C:\Users\ahmed\SURGIC\opencv_frame_0.png"

    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Original')
    cv2.createTrackbar('Min', 'Original', 0, 800, min_change)
    cv2.createTrackbar('Max', 'Original', 100, 800, max_change)
    cv2.imshow('Original', image)
    redraw_edges()

    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            exit()


def min_change(new_val):
    change_params('min_val', new_val)


def max_change(new_val):
    change_params('max_val', new_val)


def change_params(name, value):
    global edge_params
    edge_params[name] = value
    print(edge_params)
    redraw_edges()


def redraw_edges():
    edges = cv2.Canny(gray,
                      edge_params['min_val'],
                      edge_params['max_val'],
                      edge_params['aperture_size'])
    
    # Closing then Opening with a wide kernel
    kernel = np.ones((5,5),np.uint8)
    kernel2 = np.ones((2,6),np.uint8)
    img_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    img_opened =  cv2.morphologyEx(img_closed, cv2.MORPH_OPEN, kernel2)
    
    images = np.concatenate((edges, img_closed, img_opened),axis=1)
    cv2.namedWindow('images', cv2.WINDOW_NORMAL)
    cv2.imshow('images', images)

if __name__ == '__main__':
    main()

