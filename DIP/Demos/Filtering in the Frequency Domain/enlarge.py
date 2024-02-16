#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:36:02 2021

@author: mads
"""

from pylab import *
from skimage.util import img_as_float
from imageio import imread, imwrite
from matplotlib.pyplot import imshow

# load cameraman
#im = img_as_float(imread('cameraman.tif'))
im = img_as_float(imread('small_cameraman.png'))


imshow(im, cmap='gray', vmin=0, vmax=1)


pad = 300
amp = (1+2.0*pad/im.shape[0])**2


imfft = fft2(im)    # fourier
imfftsh = fftshift(imfft)   # Shift so that DC is centered

# Show Fourier spectrum
figure(), imshow(log10(abs(imfftsh)+1), cmap='gray')

imfftpad = np.pad(amp*imfftsh, ((pad, pad), (pad, pad)))    # add padding around

# Show padded Fourier spectrum
figure(), imshow(log10(abs(imfftpad)+1), cmap='gray')

bigger = ifft2(fftshift(imfftpad))      # inverse fft of padded array
figure(), imshow(real(bigger), cmap='gray', vmin=0, vmax=1)

imwrite('enlarge_orig_fourier.png', log10(abs(imfftsh)+1))
imwrite('enlarge_padded_fourier.png', log10(abs(imfftpad)+1))
imwrite('enlarged_cameraman.png', real(bigger))

