#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:57:14 2020

@author: Ojo Ayomipo Israel
"""

"""
1. Face detection from loaded Pictures

"""
import cv2


#Load input image, resize it and change it to grayscale mode
original_img = cv2.imread('ayo2.jpg',1)
img = cv2.resize(original_img, (0,0), fx=0.2, fy = 0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Load Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Find face. If faces are found, the position of the detected faces ais returned as Rect(x,y,w,h)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    
cv2.imshow('img', img)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()

"""
2. Face detection from Video Stream
"""
import cv2
#Load Cascade
face_cascade = cv2.CascadeClassifier('/root/miniconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
#frame_count =0
while True:
    ret, frame = cap.read()
#    frame_count +=1
#    print(frame_count)
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
    cv2.imshow('feed', frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

        
