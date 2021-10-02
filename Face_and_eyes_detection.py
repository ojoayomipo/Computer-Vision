#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:57:14 2020

@author: Ojo Ayomipo
"""
import cv2

#Load input image in grayscale mode
original_img = cv2.imread('ayo2.jpg',1)
img = cv2.resize(original_img, (0,0), fx=0.2, fy = 0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Load Cascade
face_cascade = cv2.CascadeClassifier('/root/miniconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/root/miniconda3/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')

#Find face. If faces are found, the position of the detected faces ais returned as Rect(x,y,w,h)
#We can then create a ROI for the face and apply eye detection on this ROI

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img', img)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()
