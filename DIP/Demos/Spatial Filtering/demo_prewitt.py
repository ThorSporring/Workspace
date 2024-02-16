#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:49:52 2021

@author: mads

Demo of prewitt filter
"""

import matplotlib.pyplot as plt
from skimage import data
plt.gray()


from skimage import filters
im = data.camera()
edges = filters.prewitt(im)



# Display results
fig = plt.figure()
plt.subplot(1,2,1)
plt.imshow(im)
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(edges)
plt.title('Prewitt')
plt.axis('off')


plt.show()