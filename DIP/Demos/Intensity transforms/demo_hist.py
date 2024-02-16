#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:25:39 2019

@author: mads
"""

#from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage.io import imshow, imread, imsave
from skimage.color import rgb2gray
plt.gray()



#Load image
# This image is also available in skimage
# it can be loaded using skimage.data.astronaut()
im = imread('../../Images/astronaut.png')


im = rgb2gray(im) #Convert to grayscale -> returns as float
im = skimage.img_as_ubyte(im) # convert to uint8

#Show image
plt.figure()
plt.imshow(im)
plt.show()

#Show histogram
plt.figure()
plt.hist(im.flatten(), bins=50)
plt.show()

#Show the datatype of the image
print(im.dtype,'Max value:', np.max(im))

#Convert the image to floats in the range [0,1]
imd = skimage.img_as_float(im)
print(imd.dtype, 'Max value:', np.max(imd))

#Show the image
plt.figure()
imshow(imd)
plt.show()

#show the histogram
plt.figure()
plt.hist(imd.flatten(), bins=50)
plt.show()