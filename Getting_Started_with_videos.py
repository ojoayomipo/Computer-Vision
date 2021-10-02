#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:49:07 2020

@author: Ojo Ayomipo
"""
"""
1. Capture Video from Camera/Webcam
"""
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #make each frame grey in color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
2. Playing Video from File

"""
import cv2
cap = cv2.VideoCapture('hymnopedia.mp4')

while True:
    ret, frame = cap.read()
    #make each frame grey in color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()


"""
3. Saving a Video

"""
import cv2
cap = cv2.VideoCapture(0)
#Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #Flip the frame
#        frame = cv2.flip(frame, 0)
        #Write the frame
        out.write(frame)
    #display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#When everything is done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()