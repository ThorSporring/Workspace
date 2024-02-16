#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:57:38 2021

@author: mads

Demo of gaussian filter
"""

import matplotlib.pyplot as plt
from skimage import data
plt.gray()


from skimage import filters
im = data.camera()


#Plot image with different sigma-values
sigma_values=[0.1, 0.5, 1, 2, 5, 10, 20]


fig = plt.figure(figsize=(10,10*len(sigma_values)))
plt.subplot(1,len(sigma_values),1)
plt.imshow(im)
plt.title('Original')
plt.axis('off')

for ix, sigma in enumerate(sigma_values):

    im_blur = filters.gaussian(im, sigma=sigma)


    # Display results     
    plt.subplot(1,len(sigma_values),ix+1)
    plt.imshow(im_blur)
    plt.title('sigma='+str(sigma))
    plt.axis('off')


plt.show()