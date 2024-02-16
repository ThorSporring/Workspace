#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:25:37 2021

@author: mads
"""

from pylab import *
from skimage.util import img_as_float
from matplotlib.pyplot import imshow
import skimage
plt.gray()

#load cameraman
im = skimage.data.camera()
im = img_as_float(im)
imshow(im)


# Filter with prewitt kernels
imH = skimage.filters.prewitt_h(im)
imV = skimage.filters.prewitt_v(im)
imM = skimage.filters.prewitt(im)


# Generating figure 1
fig, axes = plt.subplots(1, 4, figsize=(20, 6))
ax = axes.ravel()

ax[0].imshow(im)
ax[0].set_title('Input image')
ax[0].set_axis_off()


ax[1].imshow(imH)
ax[1].set_title('Horizontal gradient')
ax[1].set_axis_off()

ax[2].imshow(imV)
ax[2].set_title('Vertical gradient')
ax[2].set_axis_off()


ax[3].imshow(imM)
ax[3].set_title('Gradient Magnitude')
ax[3].set_axis_off()




plt.tight_layout()
plt.savefig('prewitt.png', dpi=600)
plt.show()