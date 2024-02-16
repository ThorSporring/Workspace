#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:06:35 2021

@author: mads


This demo shows gamma transformation and gamma correction
"""


import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float
plt.gray()




gamma = 2.2

# Let's plot the gamma curve
plt.figure()
inputIntensity = np.linspace(0,1,100)
outputIntensity = inputIntensity**gamma
plt.figure()
plt.plot(inputIntensity,outputIntensity)
plt.xlabel('input intensity')
plt.ylabel('output intensity')
plt.legend(['gamma: '+str(gamma)])



# Let's apply the gamma correction to an image
im = data.camera()
#im = data.moon()
im = img_as_float(im) # convert to 0-1 interval
imGamma = im**gamma #Apply gamma transform
imGammaCorrection = imGamma**(1/gamma) #Apply gamma correction





# Display results
fig = plt.figure()
plt.subplot(1,3,1)
plt.imshow(im)
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(imGamma)
plt.title('gamma='+str(gamma))
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(imGammaCorrection)
plt.title('gamma=1/'+str(gamma))
plt.axis('off')

plt.show()