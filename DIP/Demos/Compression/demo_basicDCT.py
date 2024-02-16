#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:00:40 2021

@author: Mads Dyrmann
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import dctn, idctn
import skimage
plt.gray()

# Create image
im = skimage.data.camera()

# set blocksize
bz = 8


# %% Allocate space for encoded image
dctCoeff = np.empty(im.shape)

# Encode blocks
for r in range(0, im.shape[0], bz):
    for c in range(0, im.shape[1], bz):

        # Find end coordinates of block. Make sure we dont exceed image size
        rs = min(im.shape[0], r+bz)
        cs = min(im.shape[0], c+bz)

        # Calculate DCT coefficients
        dctCoeff[r:rs, c:cs] = dctn(im[r:rs, c:cs], type=2, norm='ortho')

plt.figure()
plt.imshow(dctCoeff)
plt.title('DCT coded image')

# allocate space for decoded image
imrestore = np.empty(im.shape)

# %% Decode blocks
for r in range(0, im.shape[0], bz):
    for c in range(0, im.shape[1], bz):

        # Find end coordinates of block. Make sure we dont exceed image size
        rs = min(im.shape[0], r+bz)
        cs = min(im.shape[0], c+bz)

        # Calculate DCT coefficients
        imrestore[r:rs, c:cs] = idctn(dctCoeff[r:rs, c:cs], type=2, norm='ortho')

plt.figure()
plt.imshow(imrestore)
plt.title('Decoded image')
