#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 2022

@author: Mads Dyrmann

Demo of Laplacian filter
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import data
plt.gray()


im = data.camera()

kernelsize = 3
a = kernelsize//2
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])




im_out = np.zeros(im.shape)
# run through rows
for r in range(a,im_out.shape[0]-a):
    # run through columns
    for c in range(a,im_out.shape[1]-a):
        
        # Run through filter
        im_out[r,c] = np.sum(im[r-a:r+a+1,c-a:c+a+1]*kernel[::-1,::-1])
        




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