#Source: CodingEntrepreneurs

#### README ####

# This script aims at taking a video in grayscales over a defined time, while taking a picture every xxx second. 
# Ideally works for upper and lower camera, for behavioural monitoring. It indicates the time at which the picture was taken.

#### TO DO ####

# Save videos & pictures on external drive: 
# Adjust focus manually: Done
# Register video for 10 seconds and then stop -> start another one immediatly etc:
# Change with frames per second: Done
# Check if OK with red filter: 
# Test day / night cycles image quality: 
# Try on a big colony:
# Try in the final physical device: 
# Find a way to select the camera we want to use: 
# Add light control: synchronized flash only: 
# Add timestamp on video: DONE
# Add timestamp on picture: DONE




import numpy as np
import cv2
import os
from datetime import datetime, date, time, timedelta
import time


### Parameters ###
                        # VIDEO -> PiCAM
NOW = datetime.now() # Do not touch
d=NOW.strftime("%d-%m-%y_%H-%M-%S") # Do not touch

frame_per_seconds = 24.0 # Can be changed. Can slow the device

my_res = '720p' # Can be either 480p, 720p, 1080p or 4K, depends on what you want (higher = slower!) and on the device. 

seconds_duration = 120 # Time over which the video will be recorded

filename_video =  '/home/pi/setup/opencv-python/videos/' + d  + '.avi' # name of the file. Extension matters here!


# Timestamp on both videos and pictures: Now it is set to have it bottom-left -> Do not touch or I eat you!
font = cv2.FONT_HERSHEY_SIMPLEX # Font of the time on the video
position_v = (1,700) # Position at which the writting has to start
position_c = (1,1000)
fontsize = 0.5



finish_time = NOW + timedelta(seconds=seconds_duration) # Do not touch



                        # CAPTURE -> WEBCAM
interval = 10 # Time between captures, in seconds

path_capture = '/home/pi/setup/opencv-python/pictures/' # Where to save the images
#focus = 0.28 # 0 means infinite
width = 1920 # Picture resolution
height = 1080 # Picture resolution

### Parameters collected from the F_B_C.txt file
file = "/home/pi/setup/opencv-python/params/F_B_C.txt"
f = open(file, "r")
lines = f.readlines()[-2:]
f.close()

split1 = lines[0].strip().split(' ')
split2 = lines[1].strip().split(' ')

dev1, focus1, brightness1, contrast1 = split1
dev2, focus2, brightness2, contrast2 = split2


### Functions definition ###

# Change resolution of video capture
def change_res(cap, width, height):
        cap.set(3,width) # 3 for width
        cap.set(4, height) # 4 for height

# Standard video dimensions sizes
STD_DIMENSIONS = {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
}

def get_dims(cap, res='1080p'):
        width, height = STD_DIMENSIONS['480p']
        if res in STD_DIMENSIONS: 
                width, height = STD_DIMENSIONS[res]
        change_res(cap, width, height)
        return width, height


# Change the size of the frame when recording
def rescale_frame(frame, percent=75):
        scale_percent = 75
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)


# Video encoding, might require additional installs
## fourcc.org/codecs to see what types of video formats are available for my system
VIDEO_TYPE =  {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
        filename, ext = os.path.splitext(filename) # We define the video type we want by giving the extension
        if ext in VIDEO_TYPE:
                return VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']


if dev1 == "L" and dev2 == "U":
    ### Video recording ###

    # Call the camera device 0.Default camera is used if 0. Otherwise, need 1 or 2.
    cap_v = cv2.VideoCapture(0)

    # Define video type we want
    video_type_cv2 = get_video_type(filename_video)

    # Define the resolution we want to record
    dims = get_dims(cap_v, my_res) # video

    # Creation of the video file
    out = cv2.VideoWriter(filename_video, video_type_cv2, frame_per_seconds, dims, isColor=False )

    # Creation of a counter that will define when pictures are taken.
    t_int = datetime.now()


    while datetime.now() < finish_time:

        # Capture frame-by-frame
        ret_v, frame_v = cap_v.read()

        if (ret_v):
            # The frame is in grays
            frame_v = cv2.cvtColor(frame_v,cv2.COLOR_BGR2GRAY)

            # Adding the time on each frame

            cv2.putText(frame_v,datetime.now().strftime("%d-%m-%y_%H-%M-%S"), position_v , font, fontsize ,(255,255,255),2) 

            # Display the resulting frame
            cv2.imshow('Video', frame_v)
        out.write(frame_v)

        if datetime.now() >= t_int:
            # Call the camera device 1.
            cap_c = cv2.VideoCapture(1)

            # Define the resolution we want for the pictures.
            cap_c.set(3, width) # capture
            cap_c.set(4, height) # capture

            print ('Picture taken at: ' , datetime.now())

                # Set the focus. If autofocus activated, prints the autofocus value
            #cap_c.set(cv2.CAP_PROP_FOCUS,focus)
            print (cap_c.get(cv2.CAP_PROP_FOCUS))

                # Capture frame-by-frame
            ret_c, frame_c = cap_c.read()
            cv2.putText(frame_c,datetime.now().strftime("%d-%m-%y_%H-%M-%S"), position_c , font, fontsize ,(255,255,255),2) 

                # Display the resulting frame
            cv2.imshow('Pictures', frame_c)

            # Define the picture name based on date and time
            TIME_SAVE = datetime.now()
            d = TIME_SAVE.strftime("%d-%m-%y_%H-%M-%S")
            filename_capture = path_capture + d  + '.tiff'

            # Save capture
            cv2.imwrite(filename_capture, frame_c)
            t_int = t_int + timedelta(seconds=interval)
            cap_c.release()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap_v.release()
    cv2.destroyAllWindows()



if dev1 == "U" and dev2 == "L":
    ### Video recording ###

    # Call the camera device 0.Default camera is used if 0. Otherwise, need 1 or 2.
    cap_v = cv2.VideoCapture(1)

    # Define video type we want
    video_type_cv2 = get_video_type(filename_video)

    # Define the resolution we want to record
    dims = get_dims(cap_v, my_res) # video

    # Creation of the video file
    out = cv2.VideoWriter(filename_video, video_type_cv2, frame_per_seconds, dims, isColor=False )

    # Creation of a counter that will define when pictures are taken.
    t_int = datetime.now()


    while datetime.now() < finish_time:

        # Capture frame-by-frame
        ret_v, frame_v = cap_v.read()

        if (ret_v):
            # The frame is in grays
            frame_v = cv2.cvtColor(frame_v,cv2.COLOR_BGR2GRAY)

            # Adding the time on each frame

            cv2.putText(frame_v,datetime.now().strftime("%d-%m-%y_%H-%M-%S"), position_v , font, fontsize ,(255,255,255),2) 

            # Display the resulting frame
            cv2.imshow('Video', frame_v)
        out.write(frame_v)

        if datetime.now() >= t_int:
            # Call the camera device 1.
            cap_c = cv2.VideoCapture(0)

            # Define the resolution we want for the pictures.
            cap_c.set(3, width) # capture
            cap_c.set(4, height) # capture

            print ('Picture taken at: ' , datetime.now())

                # Set the focus. If autofocus activated, prints the autofocus value
            #cap_c.set(cv2.CAP_PROP_FOCUS,focus)
            print (cap_c.get(cv2.CAP_PROP_FOCUS))

                # Capture frame-by-frame
            ret_c, frame_c = cap_c.read()
            cv2.putText(frame_c,datetime.now().strftime("%d-%m-%y_%H-%M-%S"), position_c , font, fontsize ,(255,255,255),2) 

                # Display the resulting frame
            cv2.imshow('Pictures', frame_c)

            # Define the picture name based on date and time
            TIME_SAVE = datetime.now()
            d = TIME_SAVE.strftime("%d-%m-%y_%H-%M-%S")
            filename_capture = path_capture + d  + '.tiff'

            # Save capture
            cv2.imwrite(filename_capture, frame_c)
            t_int = t_int + timedelta(seconds=interval)
            cap_c.release()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap_v.release()
    cv2.destroyAllWindows()
    
    
#else:
#    print("Problem!")