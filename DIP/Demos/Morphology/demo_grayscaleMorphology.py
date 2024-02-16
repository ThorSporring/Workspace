#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Mads Dyrmann
"""


from pylab import *
from skimage.util import img_as_float
from imageio import imread, imsave
from skimage.morphology import disk, erosion, dilation, opening, closing
from skimage.color import rgb2gray


im = imread('Eaqgv.jpg')
se = disk(5)

imshow(im,cmap='gray')
title('input')
show()

#Perform gray-scale dilation
imdil = dilation(im,selem=se)
imshow(imdil, cmap='gray')
title('Dilation')
imsave('dilation.png', imdil)
show()

#Perform gray-scale erosion
imero = erosion(im,selem=se)
imshow(imero, cmap='gray')
title('Erosion')
imsave('erosion.png', imero)
show()

#Perform gray-scale opening
imopen = opening(im,selem=se)
imshow(imopen, cmap='gray')
title('Opening')
imsave('Opening.png', imopen)
show()

#Perform gray-scale closing
imclose = closing(im,selem=se)
imshow(imclose, cmap='gray')
title('Closing')
imsave('Closing.png', imclose)
show()