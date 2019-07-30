from adjust_F_B_C import adjust
from vid_cap_func import vid_cap
import cv2
import numpy as np
import os


os.remove("/home/pi/setup/opencv-python/params/F_B_C.txt")

pos = False
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(1)
 
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
    p = input ("Is it L(OWER) or U(PPER) cam?    ")
    pos = True

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

adjust(p, 1, 1024, 768)


pos = False
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
 
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
    p = input ("Is it LOWER or UPPER cam?    ")
    pos = True
    
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()


adjust(p, 0, 1024, 768)

### Here, parse the F_B_C.txt to assess the values!!!
#
#if choice1 == "UPPER" and choice2 == "LOWER":
#
#    vid_cap( seconds_duration = 120, cam_device_v = 0, cam_device_c = 1, f_v = adjust(0)[0], b_v = adjust(0)[1], c_v = adjust(0)[2], f_c = adjust(1)[0], b_c = adjust(1)[1], c_c = adjust(1)[2], interval = 10 )
#
#if choice2 == "UPPER" and choice1 == "LOWER":
#
#        vid_cap( seconds_duration = 120, cam_device_v = 0, cam_device_c = 1, f_v = adjust(1)[0], b_v = adjust(1)[1], c_v = adjust(1)[2], f_c = adjust(0)[0],  b_c = adjust(0)[1], c_c = adjust(0)[2], interval = 10 )
#


