import cv2
import numpy as np
import time
import os

### This script aims at either setting or directly using the default parameters
### The params file should be located above the folder where we collect data
### but I also want it to be copied within the folder of results, so we have a record on
### the parameters used for each result collected

def Default(f, b,c, dev, path, p, width = 1024, height = 768):
    
    path_to_params = "%s/params/F_B_C.txt" %(path)

    # Default parameters
    #f = 0.2
    #b = 0.5
    #c = 0.5

    val = False
    
    cap  = cv2.VideoCapture(dev)

    cap.set(3, width)
    cap.set(4, height)

    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    if not cap.isOpened():

        raise Exception("Could not open video device")

    while True:

        ret, frame = cap.read()

        cap.set(cv2.CAP_PROP_FOCUS,f)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, b)
        cap.set(cv2.CAP_PROP_CONTRAST,c)

        if p == "U":
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('Default Settings', frame)
        
        
        try:
            cap.set(cv2.CAP_PROP_FOCUS, f)
    
        except OSError:
            pass
        
        b = cap.get(cv2.CAP_PROP_BRIGHTNESS)
        c = cap.get(cv2.CAP_PROP_CONTRAST)


    
        if val == False:
            print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST)) 
            val = True

        if cv2.waitKey(20) & 0xFF == ord('q'):
       
            res = input ("Are you happy with the result? (Y,N):     ")
    
            if res == "Y":
                print('EXIT')
                file = open (path_to_params , "a+")
                file.write("%s %i %f %f %f\n" %(p, dev,f,b,c))
                file.close()
                print( "Parameters saved at %s" %(path_to_params))

                cap.release()
                cv2.destroyAllWindows()

                break
        
            if res == "N":
                cap.release()
                cv2.destroyAllWindows()
                
                User_params(dev, path, p, width, height)
                

    cv2.destroyAllWindows()
    