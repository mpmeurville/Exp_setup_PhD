#!/bin/bash

### This scripts aims at taking pictures from one cam and another, at different brightnesses, and to name these pictures after the focus used to take it.
### It allows me to select the parameters easily than just by trying them all.

### In the terminal, run v4l2-ctl --list-devices or ls -ltrh /dev/video* to have an idea of detected cameras and their dev. 

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

path1 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_default_params/upper/upper_red_light_3-on-9_int_blue_water/"
path2 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_default_params/lower/lower_red_light_3-on-9_int_blue_water/"
#path3 = "/home/marie-pierre/Documents/PhD/ants_trophallaxis/exp_setup/setup_output/tests_focus/cam_three/" If want to test multiple devices


width = 1920 #1280 #Can't go upper in res when no USB3 and cams both on the Hub.
height = 1080 #720 #


brightness = [ 70, 80, 90, 100] # 1 means dark
focus = [35, 60, 65 ] # 1 means no contrast?
contrast = [ 100, 110, 120, 130] # 0 means infinite
saturation = [0, 55, 60]

    
for b in brightness:
    #print (b)
    for f in focus:
        #print(f)
        
        for c in contrast:
            #print(c)
            for s in saturation:
                #print(s)
            
                cap1 = cv2.VideoCapture(5) # video capture source camera (Here webcam of laptop)
                cap2 = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
            #    cap3 = cv2.VideoCapture(2)

            #print("A")



                cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                cap1.set(cv2.CAP_PROP_AUTOFOCUS,0) #Disable autofocus
            
                ret1,frame1 = cap1.read() # return a single frame in variable `frame`
            
                cap1.set(cv2.CAP_PROP_BRIGHTNESS,b)
                cap1.set(cv2.CAP_PROP_CONTRAST,c)
                cap1.set(cv2.CAP_PROP_FOCUS,f)
                cap1.set(cv2.CAP_PROP_SATURATION,s)


            

                cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                cap2.set(cv2.CAP_PROP_AUTOFOCUS,0)#Disable autofocus


                ret2,frame2 = cap2.read() # return a single frame in variable `frame`
                cap2.set(cv2.CAP_PROP_BRIGHTNESS,b)
                cap2.set(cv2.CAP_PROP_CONTRAST,c)
                cap2.set(cv2.CAP_PROP_SATURATION, s)

#    cap3.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#    cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#    cap3.set(cv2.CAP_PROP_AUTOFOCUS, 0)
#    ret3,frame3 = cap3.read() # return a single frame in variable `frame`
#    cap3.set(cv2.CAP_PROP_FOCUS,f)

                while(True):
    
                    #filename1 = path1 + 'f'+ str(cap1.get(cv2.CAP_PROP_FOCUS)) + 'c'+ str(cap1.get(cv2.CAP_PROP_CONTRAST)) + 'b' + str(cap2.get(cv2.CAP_PROP_BRIGHTNESS))  + '.tiff'
                    #filename2 = path2 + 'f'+ str(cap2.get(cv2.CAP_PROP_FOCUS)) + 'c'+ str(cap2.get(cv2.CAP_PROP_CONTRAST)) + 'b' + str(cap2.get(cv2.CAP_PROP_BRIGHTNESS))  + '.tiff'
                    #filename3 = path3 + str(f)  + '.tiff'
                    filename1 = path1 + 'f'+ str(f) + 'c'+ str(c) + 'b' + str(b)  + 's' + str(cap1.get(cv2.CAP_PROP_SATURATION)) + '.tiff'
                    filename2 = path2 + 'f'+ str(f) + 'c'+ str(c) + 'b' + str(b)  + 's' + str(cap1.get(cv2.CAP_PROP_SATURATION)) + '.tiff'
                
                    print(filename1)
                    print(filename2)
                    #print(f)
                    print(cap1.get(cv2.CAP_PROP_SATURATION))
                    #print(cap2.get(cv2.CAP_PROP_FOCUS))
                    print(b)
                


                #cv2.imshow('img1',frame1) #display the captured image
                #cv2.imshow('img2',frame2) #display the captured image
        
        
                #if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
                    cv2.imwrite(filename1,frame1)
                    cv2.imwrite(filename2,frame2)
#               cv2.imwrite(filename3,frame3)

        
                    cv2.destroyAllWindows()
                    break
                time.sleep(interval)
                cap1.release()
                cap2.release()
#    cap3.release()


