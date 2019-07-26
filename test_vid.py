import os
from datetime import datetime, date, time, timedelta
import time
import numpy as np
import cv2

frame_per_seconds = 24.0
my_res = '480p'
seconds_duration = 10
NOW = datetime.now()
finish_time = NOW + timedelta(seconds=seconds_duration)


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



cap = cv2.VideoCapture(0)

# Define the resolution we want to record
dims = get_dims(cap, my_res)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_grey.avi',fourcc, frame_per_seconds, dims, isColor=False)

while datetime.now() < finish_time :
	ret, frame = cap.read()
	if ret==True:
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		# write the flipped frame
		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
    
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
