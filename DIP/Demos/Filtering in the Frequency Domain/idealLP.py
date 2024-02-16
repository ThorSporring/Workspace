#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mads Dyrmann
"""

from pylab import *
import numpy as np
from skimage.util import img_as_ubyte, img_as_float
from imageio import imread


#Transforms in frequency plane -- Ideal Low-pass

#Load image and show
dI = img_as_float(imread('cameraman.tif'))
#dI = img_as_float(skimage.data.camera()) # Load image of cameraman


figure()
imshow(dI, cmap='gray')
title('Original image')

#Lets calculate the Fourier Transform (goto Frequnecy Domain)
FI=fft2(dI);
FI=fftshift(FI);

M,N = FI.shape
Mc, Nc = M//2, N//2 # Center of image

#Do the Low pass filtering
D0=25
for u in range(FI.shape[0]):
    for v in range(FI.shape[1]):
        if ((u-Mc)**2+(v-Nc)**2 > D0**2): #if distance from DC is grater than cutt-off freq...
            FI[u,v]=0

logabsFI=log10(abs(FI)+1);
figure()
imshow(logabsFI/np.max(logabsFI[:]), cmap='gray')
title('Fourier of cutted frequences')

#Lets return to the spatial domain
FI = fftshift(FI)
idJ = ifft2(FI)
idJ = real(idJ) #Remove numeric errors causing a insignificant complex number
figure()
imshow(idJ/np.max(idJ), cmap='gray')
title('Ideal Lowpass filtered image')