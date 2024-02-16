#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:55:36 2021

@author: Mads Dyrmann
"""

from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
import imageio
plt.gray()

rgb = imageio.imread('https://upload.wikimedia.org/wikipedia/commons/6/6e/Marstal-badehus.jpg')

# %% HUE-SATURATION-VALUE
fig, ax = plt.subplots(1, 3, constrained_layout=True, figsize=(10, 4))
fig.suptitle('RGB', fontsize=16)

plt.subplot(1, 3, 1)  # row 1, column 3, count 1
plt.imshow(rgb[:, :, 0])  # Red channel
plt.title('Red')
plt.axis('off')

plt.subplot(1, 3, 2)  # row 1, column 3, count 2
plt.imshow(rgb[:, :, 1])  # Green channel
plt.title('Green')
plt.axis('off')

plt.subplot(1, 3, 3)  # row 1, column 3, count 3
plt.imshow(rgb[:, :, 2])  # Blue channel
plt.title('Blue')
plt.axis('off')


# %% HUE-SATURATION-VALUE
hsv = rgb2hsv(rgb)

fig, ax = plt.subplots(1, 3, constrained_layout=True, figsize=(10, 4))
fig.suptitle('HSV', fontsize=16)

plt.subplot(1, 3, 1)  # row 1, column 3, count 1
plt.imshow(hsv[:, :, 0])  # Hue channel
plt.title('Hue')
plt.axis('off')

plt.subplot(1, 3, 2)  # row 1, column 3, count 2
plt.imshow(hsv[:, :, 1])  # Saturation channel
plt.title('Saturation')
plt.axis('off')

plt.subplot(1, 3, 3)  # row 1, column 3, count 3
plt.imshow(hsv[:, :, 2])  # Value channel
plt.title('Value')
plt.axis('off')
