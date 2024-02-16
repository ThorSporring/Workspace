#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Mads Dyrmann
"""


#from pylab import *
import numpy as np
from skimage.util import img_as_float
from skimage.io import imshow, imread, imsave
from skimage.morphology import disk, erosion, dilation
import matplotlib.pyplot as plt
plt.gray()


# Create image
I = np.zeros((100,100))

for i in range(0,100,10):
    I[i,:]=1
    I[:,i]=1
    pass

# Add some noise
I = np.logical_or(I, np.random.rand(*I.shape)>0.9)


#Show the image
plt.figure()
plt.imshow(I)


# Let's try removing some lines and noise
strel = np.array([[1,1,1,1,1,]])

I_horizontal = erosion(I, strel)
plt.figure()
plt.imshow(I_horizontal)

