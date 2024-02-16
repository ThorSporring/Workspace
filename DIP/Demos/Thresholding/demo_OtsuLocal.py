#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:03:52 2021

@author: Mads Dyrmann
"""

import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu, rank
from skimage.morphology import disk
from skimage import data

img = data.page()

radius = 15
selem = disk(radius)
local_otsu = rank.otsu(img, selem)
threshold_global_otsu = threshold_otsu(img)
global_otsu = img >= threshold_global_otsu

fig, ax = plt.subplots(2, 2, figsize=(8, 5), sharex=True, sharey=True)
ax0, ax1, ax2, ax3 = ax.ravel()
plt.tight_layout()

ax0.imshow(img, cmap=plt.cm.gray)
ax0.set_title('Original')
ax0.axis('off')

ax1.imshow(local_otsu, cmap=plt.cm.gray)
ax1.set_title('Local Otsu (radius=%d)' % radius)
ax1.axis('off')

ax2.imshow(img >= local_otsu, cmap=plt.cm.gray)
ax2.set_title('Original >= Local Otsu' % threshold_global_otsu)
ax2.axis('off')

ax3.imshow(global_otsu, cmap=plt.cm.gray)
ax3.set_title('Global Otsu (threshold = %d)' % threshold_global_otsu)
ax3.axis('off')

plt.show()