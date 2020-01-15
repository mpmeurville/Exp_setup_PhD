#!/bin/bash

### This scripts aims at taking pictures from one cam and another, at different contrasts, and to name these pictures after the focus used to take it.
### It allows me to select the parameters easily than just by trying them all.

### In the terminal, run ls -ltrh /dev/video* to have an idea of detected cameras and their dev. 

#       key value
#cam.set(3 , 640  ) # width        
#cam.set(4 , 480  ) # height       
#cam.set(10, 120  ) # brightness     min: 0   , max: 255 , increment:1  
#cam.set(11, 50   ) # contrast       min: 0   , max: 255 , increment:1     
#cam.set(12, 70   ) # saturation     min: 0   , max: 255 , increment:1
#cam.set(13, 13   ) # hue         
#cam.set(14, 50   ) # gain           min: 0   , max: 127 , increment:1
#cam.set(15, -3   ) # exposure       min: -7  , max: -1  , increment:1
#cam.set(17, 5000 ) # white_balance  min: 4000, max: 7000, increment:1
#cam.set(28, 0    ) # focus          min: 0   , max: 255 , increment:5

import cv2
from datetime import datetime, date, time, timedelta
import time
import os
import numpy as np


interval = 5
#path1 = '/media/pi/My Passport/focus_ajustment/zero/'
#path2 = '/media/pi/My Passport/focus_ajustment/two/'

path1 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_contrast/cam_zero/"
path2 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_contrast/cam_two/"
#path3 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_focus/cam_three/" If want to test multiple devices


width = 1920 #1280 #Can't go upper in res when no USB3 and cams both on the Hub.
height = 1080 #720 #


contrast = [0, 5, 10, 15, 20, 25, 30,35, 40,45, 50,55, 60,65, 70,75, 80,85, 90,95 ,100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250] # 0 means infinite
    
for c in contrast:
    print (c)

    cap1 = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    cap2 = cv2.VideoCapture(4) # video capture source camera (Here webcam of laptop)
#    cap3 = cv2.VideoCapture(2)

    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #cap1.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    ret1,frame1 = cap1.read() # return a single frame in variable `frame`
    cap1.set(11,c)


    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #cap2.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    #cap2.set(cv2.CAP_PROP_BRIGHTNESS, 0)
    ret2,frame2 = cap2.read() # return a single frame in variable `frame`
    cap2.set(11,c)


#    cap3.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#    cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#    cap3.set(cv2.CAP_PROP_AUTOFOCUS, 0)
#    ret3,frame3 = cap3.read() # return a single frame in variable `frame`
#    cap3.set(cv2.CAP_PROP_FOCUS,f)

    while(True):
    
        filename1 = path1 + str(c)  + '.tiff'
        filename2 = path2 + str(c)  + '.tiff'
#        filename3 = path3 + str(f)  + '.tiff'


        print(filename1)
        print(cap1.get(cv2.CAP_PROP_CONTRAST))
        print(cap2.get(cv2.CAP_PROP_CONTRAST))


        #cv2.imshow('img1',frame1) #display the captured image
        #cv2.imshow('img2',frame2) #display the captured image
        
        
        #if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite(filename1,frame1)
        cv2.imwrite(filename2,frame2)
#        cv2.imwrite(filename3,frame3)

        
        cv2.destroyAllWindows()
        break
    time.sleep(interval)
    cap1.release()
    cap2.release()
#    cap3.release()


