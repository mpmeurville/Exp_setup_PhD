from adjust_F_B_C import adjust
from vid_cap_func import vid_cap
import cv2
import numpy as np
import os
from datetime import datetime, date, time, timedelta
import time
from both_cap_vid import change_res 
from both_cap_vid import get_dims
from both_cap_vid import rescale_frame
from both_cap_vid import get_video_type
from both_cap_vid import get_cap_vid



# Create the divices we will use
dev1 = 1
dev2 = 0


try:
    os.remove("/media/pi/My Passport/params/F_B_C.txt")
    
except OSError:
    pass 
    
pos = False
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name

cap = cv2.VideoCapture(dev1)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()

      break
    
if pos == False:
    po1 = input ("Is it L(OWER) or U(PPER) cam?    ")
    pos = True

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()


# p is the info on whether we talk about upper or lower camera
# cam_device indicates how the device is called by the pi -> Do not touch!
# path is the path to the external drive (where parameters are stored)
# width and height is the resolution of the frames displayed for parameters setting

adjust(dev = dev1, p = po1, path = "/media/pi/My Passport", width = 1024, height = 768)


pos = False
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(dev2)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
if pos == False:
    po2 = input ("Is it LOWER or UPPER cam?    ")
    pos = True
    
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

 #p is the info on whether we talk about upper or lower camera
 #cam_device indicates how the device is called by the pi -> Do not touch!
 #path is the path to the external drive (where parameters are stored)
 #width and height is the resolution of the frames displayed for parameters setting

adjust( dev = dev2, p = po2,  path = "/media/pi/My Passport", width = 1024, height = 768)


next1 = input ("Do you want to start recording? (Y, N)     ")

if next1 == "Y":

    # RECORD
    s = input("How long in s?    ")
    i = input("Interval in s?    ")
    foo = input ("What folder name?    ")
    
    s = int(s)
    i = int(i)


    if not os.path.exists("/media/pi/My Passport/%s" %(foo)):
        os.mkdir("/media/pi/My Passport/%s" %(foo))
        os.mkdir("/media/pi/My Passport/%s/videos" %(foo))
        os.mkdir("/media/pi/My Passport/%s/pictures" %(foo))


    N = datetime.now() # Do not touch
    d=N.strftime("%d-%m-%y_%H-%M-%S") # Do not touch

# CREATE folders architecture. 

    f_video =  '/media/pi/My Passport/' + foo +'/video/' + d  + '.avi' # name of the file. Extension matters here! Will have to be ,odified / put in a loop for updating d.
    p_capture = '/media/pi/My Passport/' + foo + '/picture/'

    print(f_video)
    print(p_capture)


    get_cap_vid(NOW = N, seconds_duration = s, interval = i, path_capture = p_capture, filename_video = f_video, percent = 30, file_params = "/media/pi/My Passport/params/F_B_C.txt", my_res = '720p', width = 1920, height = 1080 ,frame_per_seconds = 24.0)

elif next1 == "N":
    print("Bye!")
