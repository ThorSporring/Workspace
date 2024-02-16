#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mads Dyrmann
"""

from pylab import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from skimage.morphology import disk
plt.gray()

#Create box in spatial domain
I = np.zeros((256,256))
I[110:146,120:136]=1

#Convert to frequency domain
fI = fftshift(fft2(I))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.imshow(I)
ax1.title.set_text('box in spatial')
ax2.imshow(log10(np.abs(fI)+1))
ax2.title.set_text('fourier spectrum')
plt.tight_layout()
plt.savefig('box2sinc_s2f.png')







# create disk


#Create box in spatial domain
r=20
I = np.zeros((255,255))
I[128-r:128+r+1,128-r:128+r+1] = disk(r)

#Convert to frequency domain
fI = fftshift(fft2(I))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.imshow(I)
ax1.title.set_text('box in spatial')
ax2.imshow(log10(np.abs(fI)+1))
ax2.title.set_text('fourier spectrum')
plt.tight_layout()
plt.savefig('circle_box.png')









# Now try to create a box in frequency domain and convert to spatial domain
fI = np.zeros((256,256))
fI[110:146,120:136]=1

#Convert to frequency domain
I = real(ifft2(fftshift(fI)))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.imshow(log10(np.abs(fI)+1))
ax1.title.set_text('box in frequency')
ax2.imshow(I)
ax2.title.set_text('inverse fourier')
plt.tight_layout()
plt.savefig('box2sinc_f2s.png')


