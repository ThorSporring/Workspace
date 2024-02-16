#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:38:08 2021

@author: Mads Dyrmann
"""

from pylab import *
from skimage.util import img_as_float
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np
import imageio
plt.gray()


f = imageio.imread('news-120712d-lg.png')
f = img_as_float(f)

# Vi laver et periodisk st�j-signal
A = .075  # Amplitude
[M, N] = f.shape
l1 = 100;   k1 = 0
l2 = 71;    k2 = 71
l3 = 0;     k3 = 100
l4 = 71;    k4 = -71

n1 = np.empty(f.shape)  # allocate noise images
n2 = np.empty(f.shape)  # allocate noise images
n3 = np.empty(f.shape)  # allocate noise images
n4 = np.empty(f.shape)  # allocate noise images

for r in range(M):
    for s in range(N):
        n1[r, s] = A*sin(2*pi/M*(l1*r) + 2*pi/N*(k1*s))
        n2[r, s] = A*sin(2*pi/M*(l2*r) + 2*pi/N*(k2*s))
        n3[r, s] = A*sin(2*pi/M*(l3*r) + 2*pi/N*(k3*s))
        n4[r, s] = A*sin(2*pi/M*(l4*r) + 2*pi/N*(k4*s))

n = n1+n2+n3+n4  # noise
fn = f+n  # image+ noise

figure(), imshow(n), title('Periodisk støj')
figure(), imshow(fn), title('Periodisk støj i billede')

imageio.imwrite('noisy_spaceman.png', fn)
