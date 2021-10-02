# -*- coding: utf-8 -*-
"""
i-TECH
Author: Ayomipo Ojo
"""

import urllib.request
import cv2
import numpy as np

url = 'http://10.62.228.40:8080/photo.jpg'
cv2.namedWindow("Feed", cv2.WINDOW_AUTOSIZE)

while True:
    imgResponse=urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    cv2.imshow("Feed", img)
    key = cv2.waitKey(5)
    if key==ord('q'):
        break

cv2.destroyAllWindows()
