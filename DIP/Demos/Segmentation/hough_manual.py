#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:46:32 2021

@author: Mads Dyrmann
"""

from pylab import *
from skimage.util import img_as_float
from matplotlib.pyplot import imshow
from scipy import ndimage as ndi
import skimage
import imageio

from skimage import feature
plt.gray()

#Load the cameraman 
im = skimage.data.camera()
im = img_as_float(im)
imb = ndi.gaussian_filter(im, 2) # blur image

# Compute the Canny filter
iEdge = feature.canny(imb)

# The Hough space should have a height equal to twice the diagonal (see GW p 739)
diagonal = int(sqrt(sum(array(im.shape)**2)))

# Hough-image 1.index in degrees, 2. index dist from origo 1==dist_equal_0
H = zeros((2*diagonal, 180))

for r in range(iEdge.shape[0]):
    for s in range(iEdge.shape[1]):
        if iEdge[r, s] == 1:  # if point in image -> draw line i Hough-space
            for theta in range(180): 
                rho = round((r*cos(pi*theta/180) + s *
                             sin(pi*theta/180))+diagonal)
                
                H[rho, theta] = H[rho, theta]+1

# Normalize Hough-space
H = H / np.max(H)


#Threshold hough-space to find lines
[rho, theta] = np.where(H > .55)  # Try to use 0.55 => gives the tripod...

#Draw the lines
im_lines = zeros(im.shape)
for k in range(len(theta)):
    for s in range(im.shape[1]):
        # Notice sign of rho is gone, may result in displaced line
        r = round(-tan(pi*theta[k]/180)*s +
                  (rho[k]-diagonal)/cos(pi*theta[k]/180))
        if((1 < r) and (r < im.shape[0])):
            im_lines[r, s] = 1





# Generating plots
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
ax = axes.ravel()

ax[0].imshow(im, cmap=cm.gray)
ax[0].set_title('Input image')
ax[0].set_axis_off()

ax[1].imshow(np.log(1 + H), cmap=cm.gray, aspect=0.1)
ax[1].set_title('Hough transform')
ax[1].set_xlabel('Angles (degrees)')
ax[1].set_ylabel('Distance (pixels)')
#ax[1].axis('image')

ax[2].imshow(np.clip(im_lines+im,0,1), cmap=cm.gray)
ax[2].set_axis_off()
ax[2].set_title('Original with lines')
#plt.tight_layout()
plt.savefig('hough_manual.png',dpi=600)
plt.show()


