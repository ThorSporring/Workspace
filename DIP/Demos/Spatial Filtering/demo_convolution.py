#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 2022

@author: Mads Dyrmann

Demo of Laplacian filter
"""

import matplotlib.pyplot as plt
from skimage.util import img_as_float
import numpy as np
from skimage import data
from scipy import ndimage
plt.gray()


# Read image and convert to float
im = img_as_float(data.camera())


# Create kernel
kernel = np.array([[0, 1,0],
                   [1,-4,1],
                   [0, 1,0]])


# Convolve
im_out = ndimage.convolve(im, kernel, mode='constant', cval=0.0)




# Display results
fig = plt.figure()
plt.subplot(1,2,1)
plt.imshow(im)
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(im_out)
plt.title('Laplacian')
plt.axis('off')


plt.show()