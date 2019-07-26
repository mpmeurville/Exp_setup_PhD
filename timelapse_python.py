#!/bin/bash 

#source CodingForEntrepreneurs https://github.com/codingforentrepreneurs/OpenCV-Python-Series
from datetime import datetime, date, time, timedelta
import time
import os
import numpy as np
import cv2

from classVideo import CFEVideoConf


cap = cv2.VideoCapture(0) #default webcam


save_path = '/mnt/mydisk/live_record/pictures/'
frames_per_seconds = 5
config = CFEVideoConf(cap, filepath=save_path, res='1080p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
seconds_duration = 120
timelapse_img_dir = "/home/pi/webcam/timelapse/opencv_python/opencv_timelapse/saved-media"
seconds_between_shots = 10



if not os.path.exists(timelapse_img_dir):
	os.mkdir(timelapse_img_dir)


# Set 2 counters for file naming. s = the time of the previous picture, counter is the number of pictures taken during this second so far.
counter=0
s=0


NOW = datetime.now()
print(NOW)

finish_time = NOW + timedelta(seconds=seconds_duration)
print(finish_time)




i=0 #Number of iterations for the name.



while datetime.now() < finish_time:
	T=time.strftime("%Y%m%d-%H:%M:%S")

	#capture frame by frame
	ret, frame = cap.read()


	# Name files / pictures according to the date / time, adding a number afterwards if multiple ones in 1 second
	if s == T:
		filename =  '/home/pi/webcam/timelapse/opencv_python/opencv_timelapse/saved-media/' + str(T) + '-' + str(counter) + '.jpg'
		counter = counter + 1

	else:
		counter = 0
		filename =  '/home/pi/webcam/timelapse/opencv_python/opencv_timelapse/saved-media/' + str(T) + '-' + str(counter) + '.jpg'
  

	s=T
	i += 1
	cv2.imwrite(filename, frame) # Create the image
	time.sleep(seconds_between_shots)
	#frame = cv2.cvtColor(frame, cv2, COLOR_BGR2GRAY)
	#out.write(frame) #For video

	#Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# When it is done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
