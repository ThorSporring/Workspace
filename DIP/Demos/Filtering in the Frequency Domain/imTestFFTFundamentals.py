#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mads Dyrmann
"""

from pylab import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



N = 16
n = np.linspace(0, N-1, N)
k = 2
x = np.sin((2*pi)/N*k*n)


# We see the sinoid corresponds to a pair of non-zero values in the frequnecy domian
print(fft(x))

ix = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
x = ifft(ix)  # We could also get these using ifft
stem(x)
title('ifft("point pair") = sine')

# Let's try this in 2 dimensions
M = 256
N = 256
l = 10
k = 5

I = np.empty((M, N))
for r in range(M):
    for s in range(N):
        I[r, s] = .5*sin(2*pi/M*(l*r)+2*pi/N*(k*s))+.5



figure()
imshow(I, cmap='gray')

title('Sine wave')  # Note the wave vector (l,k) is ortogonal to the wave

fI = fftshift(fft2(I))
fig = figure()
plt.imshow(abs(fI) > .001)
title('Spectrum of the sine wave')  # Only two points != 0 + DC
