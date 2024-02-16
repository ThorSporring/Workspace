#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Mads Dyrmann
"""

from skimage.util import img_as_float
from skimage.io import imshow
from imageio import imread, imwrite
import matplotlib.pyplot as plt
from skimage.morphology import disk, erosion, dilation
plt.gray()

#read image
plt.figure()
I = img_as_float(imread('sugarbeet.JPG'))
plt.imshow(I)

#Create a grayscale image by weighting the color channels
plt.figure()
Ig = 2*I[:,:,1] - I[:,:,0] - I[:,:,2]
plt.imshow(Ig, cmap='gray')

#Threshold the image
plt.figure()
Ibw = Ig>0.11
plt.imshow(Ibw, cmap='gray')


# Let's try removing some noise using erosion
strel = disk(2)
Iero = erosion(Ibw, strel)
plt.figure()
imshow(Iero,  cmap='gray')



# Let's try som dilation to make objects go back to their normal size
Idil = dilation(Iero, strel)
plt.figure()
plt.imshow(Idil,  cmap='gray')