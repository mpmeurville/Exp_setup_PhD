
import cv2
import numpy as np
import time
import os



#### AIM OF THIS SCRIPT ####
# I want to be able to take pictures from a camera, and to adjust contrast, brightness and focus easily, before taking real images. 
# The idea is to iteratively ask the user to set a value for these 3 parameters, 
# and once the user is happy with it, to remember the values, and pass them as an argument for the actual recording. 
#This script contains a function that is called when  using our devices.


def Auto(p, cam_device, width = 1920, height = 1080): # Never give pos a value!
    val = False
    cap  = cv2.VideoCapture(cam_device)

    cap.set(3, width)
    cap.set(4, height)
    


    if not cap.isOpened():
        raise Exception("Could not open video device")

    while (cap):
        ret, frame = cap.read()
        cv2.imshow('Auto Settings', frame)
            
        f = cap.get(cv2.CAP_PROP_FOCUS)
        b = cap.get(cv2.CAP_PROP_BRIGHTNESS)
        c = cap.get(cv2.CAP_PROP_CONTRAST)

        if val == False:
            print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))
            val = True
             
        if cv2.waitKey(20) & 0xFF == ord('q'):
       
            res = input ("Are you happy with the result? (Y,N):     ")
    
            if res == "Y":
                print('EXIT')
                file = open ('/home/pi/setup/opencv-python/params/F_B_C.txt', "a+")
                file.write("%s: %f %f %f\n" %(p,f,b,c))
                file.close()
                cap.release()
                cv2.destroyAllWindows()
                
                break
        
            if res == "N":
                cap.release()
                cv2.destroyAllWindows()
                
                User_params(p, cam_device, width, height)
                

    cv2.destroyAllWindows()
    
def Default(p, cam_device, width = 1920, height = 1080):

    # Default parameters
    f = 0.32
    b = 0.7
    c = 0.5

    val = False
    
    cap  = cv2.VideoCapture(cam_device)

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

        cv2.imshow('Default Settings', frame)
        
        
        f = cap.get(cv2.CAP_PROP_FOCUS)
        b = cap.get(cv2.CAP_PROP_BRIGHTNESS)
        c = cap.get(cv2.CAP_PROP_CONTRAST)


    
        if val == False:
            print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST)) 
            val = True

        if cv2.waitKey(20) & 0xFF == ord('q'):
       
            res = input ("Are you happy with the result? (Y,N):     ")
    
            if res == "Y":
                print('EXIT')
                file = open ('/home/pi/setup/opencv-python/params/F_B_C.txt', "a+")
                file.write("%s: %f %f %f\n" %(p,f,b,c))
                file.close()
                cap.release()
                cv2.destroyAllWindows()

                break
        
            if res == "N":
                cap.release()
                cv2.destroyAllWindows()
                
                User_params(p, cam_device, width, height)
                

    cv2.destroyAllWindows()
    

def User_params(p, cam_device, width = 1920, height = 1080):

    val = False

    f = input ('F :    ')
    b = input ('B :    ')
    c = input ('C :    ')
    
    f = float(f)
    b = float(b)
    c = float(c)

    cap  = cv2.VideoCapture(cam_device)

    cap.set(3, width)
    cap.set(4, height)

    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    if not cap.isOpened():
        raise Exception("Could not open video device")

    while True:

        ret, frame = cap.read()

        cap.set(cv2.CAP_PROP_FOCUS, f)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, b)
        cap.set(cv2.CAP_PROP_CONTRAST, c)

        cv2.imshow('User Settings', frame)
            

        if val == False:
            print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))     
            val = True
            print ('Quit: hit Q. Change parameters: hit C.')



        if cv2.waitKey(20) & 0xFF == ord('q'):
            print('EXIT')
            file = open ('/home/pi/setup/opencv-python/params/F_B_C.txt', "a+")
            file.write("%s: %f %f %f\n" %(p,f,b,c))
            file.close()
            
            break
        

        elif cv2.waitKey(200) & 0xFF == ord('c'):
            cap.release()
            cv2.destroyAllWindows()

            User_params(p, cam_device, width, height)
            


    cap.release()

    cv2.destroyAllWindows()
    
    
def adjust(p, cam_device, path, width = 1920, height = 1080):

    main = input ('Do you want to set parameters? (Yes, Default, Auto) :    ') # When python3, change to input


    if main == 'Auto':

        Auto(p, cam_device, width, height)
        print("Exit")

    cv2.destroyAllWindows()

    if main == 'Default':

        Default(p, cam_device, width, height)

    cv2.destroyAllWindows()

    if main == 'Yes':

        User_params(p, cam_device, width, height)

    cv2.destroyAllWindows()



