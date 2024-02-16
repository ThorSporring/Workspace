#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:12:27 2021

@author: Mads Dyrmann

Npt yet finished
"""

from pylab import *
import numpy as np
from skimage.util import img_as_ubyte, img_as_float
from imageio import imread

import matplotlib.pyplot as plt
plt.gray()

#Transforms in frequency plane -- Ideal Low-pass

#Load image and show
dI=img_as_float(imread('cameraman.tif'))


figure()
imshow(dI)
title('Original image')

#Lets calculate the Fourier Transform (goto Frequnecy Domain)
FI=fft2(dI);
FI=fftshift(FI);
M,N = FI.shape

#Do the Low pass filtering
D0=25 # cut-off frequency


for u in range(FI.shape[0]):
    for v in range(FI.shape[1]):
        Duv = sqrt((u-M//2)**2+(v-N//2)**2) #calculate distance from DC
        
        FI[u,v] = FI[u,v] * e**(-(Duv**2)/(2*D0**2))



logabsFI=log10(abs(FI)+1);
figure()
imshow(logabsFI/np.max(logabsFI[:]))
title('Fourier of cutted frequences')

#Lets return to the spatial domain
FI = fftshift(FI)
idJ = ifft2(FI)
idJ = real(idJ) #Remove numeric errors causing a insignificant complex number
figure()
imshow(idJ/np.max(idJ))
title('Gaussian Lowpass filtered image')