#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:25:37 2021

@author: mads
"""

from pylab import *
from skimage.util import img_as_float
from skimage.color import rgb2gray
from matplotlib.pyplot import imshow
from scipy import ndimage as ndi

from skimage import feature
import imageio
plt.gray()

#load cameraman
im = imageio.imread('1200px-Aarhus_Universitets_hovedbygning_set_fra_parken.jpg')
im = img_as_float(rgb2gray(im))

imn = ndi.gaussian_filter(im, 2)

# Compute the Canny filter for two values of sigma
imC = feature.canny(imn)


# Generating figure 1
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ax = axes.ravel()

ax[0].imshow(im)
ax[0].set_title('Input image')
ax[0].set_axis_off()


ax[1].imshow(imC)
ax[1].set_title('Canny filtered')
ax[1].set_axis_off()

plt.tight_layout()
plt.savefig('canny.png', dpi=600)
plt.show()