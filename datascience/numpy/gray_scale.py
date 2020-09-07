#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# formula
# Y' = 0.299 R + 0.587 G + 0.114 B 

def rgb2gray(rgb):

    print(rgb[...,:3].shape)
    # print(rgb.size)
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('sid.jpg')     
gray_img = rgb2gray(img)    

plt.imshow(gray_img, cmap=plt.get_cmap('gray'))
plt.show()
