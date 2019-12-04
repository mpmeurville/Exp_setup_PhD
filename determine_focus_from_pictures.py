#!/bin/bash



### This scripts aims at taking pictures from one cam and another, at different focuses, and to name these pictures after the focus used to take it.
### It allows me to select the parameters easily than just by trying them all.


import cv2
from datetime import datetime, date, time, timedelta
import time
import os
import numpy as np


interval = 5
path1 = '/media/pi/My Passport/focus_ajustment/zero/'
path2 = '/media/pi/My Passport/focus_ajustment/two/'

width = 1920
height = 1080


focus = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95] # 0 means infinite
    
for f in focus:
    print (f)

    cap1 = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    cap2 = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop)

    cap1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    ret1,frame1 = cap1.read() # return a single frame in variable `frame`
    cap1.set(cv2.CAP_PROP_FOCUS,f)
    
    cap2.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    ret2,frame2 = cap2.read() # return a single frame in variable `frame`
    cap2.set(cv2.CAP_PROP_FOCUS,f)
    
    while(True):
    
        filename1 = path1 + str(f)  + '.tiff'
        filename2 = path2 + str(f)  + '.tiff'

        print(filename1)
        print(cap1.get(cv2.CAP_PROP_FOCUS))

        cv2.imshow('img1',frame1) #display the captured image
        cv2.imshow('img2',frame2) #display the captured image

        #if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite(filename1,frame1)
        cv2.imwrite(filename2,frame2)

        cv2.destroyAllWindows()
        break
    time.sleep(interval)
    cap1.release()
    cap2.release()
