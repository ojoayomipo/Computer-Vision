#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:34:49 2020

@author: Ojo Ayomipo
"""
import cv2

image_path = 'microB3.png'
#Load an image
image = cv2.imread(image_path, 1)

"""
To load an image in grayscale, use
image = cv2.imread(image_path, 0)
"""

#Display the image
cv2.imshow('image', image)

k = cv2.waitKey(0)
"""
    If you are using a 64-bit machine, you'll modify line 22 to:
        k = cv2.waitKey(0) & 0xFF
        
        """
if k == 27: #wait for ESC key to exit
    cv2.destroyAllWindows()
    
#Let's try to save the image when the 's' key is pressed
    
elif k == ord('s'):
    cv2.imwrite('MicroB.jpg', image)
    cv2.destroyAllWindows()
    print('saved successfully')

"""
Plot using Matplotlib
"""
from matplotlib import pyplot as plt
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image2)

#To hide the x and y tick values
plt.xticks([]), plt.yticks([])













