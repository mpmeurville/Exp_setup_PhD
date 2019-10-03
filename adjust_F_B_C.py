
import cv2
import numpy as np
import time
import os



#### AIM OF THIS SCRIPT ####
# I want to be able to take pictures from a camera, and to adjust contrast, brightness and focus easily, before taking real images. 
# The idea is to iteratively ask the user to set a value for these 3 parameters, 
# and once the user is happy with it, to remember the values, and pass them as an argument for the actual recording. 
#This script contains a function that is called when  using our devices.


def Auto(dev, path, p, width = 1280, height = 720): # Never give pos a value!

    path_to_params = "%s/params/F_B_C.txt" %(path)

    val = False
    cap  = cv2.VideoCapture(dev)

    cap.set(3, width)
    cap.set(4, height)
    
    try:
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    
    except OSError:
        pass 


    if not cap.isOpened():
        raise Exception("Could not open video device")

    while (cap):
        
        
        ret, frame = cap.read()
        
        if p == "U":
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
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
    
def Default(dev, path, p, width = 1280, height = 720):
    
    path_to_params = "%s/params/F_B_C.txt" %(path)

    # Default parameters
    f = 0.7
    b = 0.7
    c = 0.7

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
    

def User_params(dev, path, p, width = 1280, height = 720):
    
    path_to_params = "%s/params/F_B_C.txt" %(path)

    val = False

    f = input ('F :    ')
    b = input ('B :    ')
    c = input ('C :    ')
    
    f = float(f)
    b = float(b)
    c = float(c)

    cap  = cv2.VideoCapture(dev)

    cap.set(3, width)
    cap.set(4, height)

    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    if not cap.isOpened():
        raise Exception("Could not open video device")

    while True:

        ret, frame = cap.read()

        try:
            cap.set(cv2.CAP_PROP_FOCUS, f)
    
        except OSError:
            pass 

        cap.set(cv2.CAP_PROP_BRIGHTNESS, b)
        cap.set(cv2.CAP_PROP_CONTRAST, c)

        #if p == "U":
        #    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
        cv2.imshow('User Settings', frame)
            

        if val == False:
            print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))     
            val = True
            #print ('Quit: hit Q. Change parameter hit C.')

        elif cv2.waitKey(0) & 0xFF == ord('q'):
       
            res = input ("Are you happy with the result? (Y,N):     ")
    
            if res == "Y":
                print('EXIT')
                file = open (path_to_params, "a+")
                file.write("%s %i %f %f %f\n" %(p, dev,f,b,c))
                file.close()
                print( "Parameters saved at %s" %(path_to_params))

                #cap.release()
                #cv2.destroyAllWindows()
                
                break
            
            if res == 'N':
                cap.release()
                cv2.destroyAllWindows()

                User_params(dev, path, p, width, height)
    
        

        elif cv2.waitKey(0) & 0xFF == ord('c'):
            cap.release()
            cv2.destroyAllWindows()

            User_params(dev, path, p,  width, height)
            


    cap.release()

    cv2.destroyAllWindows()
    
    
def adjust(dev, p, path, width = 1920, height = 1080):

    main = input ('Do you want to set parameters? (Y(es), D(efault), A(uto) ) :    ') # When python3, change to input
    

    if main == 'A':

        Auto(dev, path, p, width, height)
        #print("Exit")

    cv2.destroyAllWindows()

    if main == 'D':

        Default(dev, path, p, width, height)

    cv2.destroyAllWindows()

    if main == 'Y':

        User_params(dev, path, p, width, height)

    cv2.destroyAllWindows()



