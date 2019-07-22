#!/bin/bash

import cv2
from datetime import datetime, date, time, timedelta
import time
import os
import numpy as np


seconds_duration = 30
NOW = datetime.now()
print(NOW)

d=NOW.strftime("%d-%m-%y_%H-%M-%S")

finish_time = NOW + timedelta(seconds=seconds_duration)
print(finish_time)

interval = 10

#path = '/mnt/mydisk/live_record/pictures/'
path = '/home/pi/setup/opencv-python/pictures/'
focus = 0.74 # 0 means infinite
width = 1920
height = 1080


cap  = cv2.VideoCapture(0)

# Enable (1) or disable (0) autofocus. 
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

cap.set(3, width)
cap.set(4, height)
ret, frame = cap.read()
cnt = 0


while datetime.now() < finish_time:
	NOW = datetime.now()
	print(NOW)

	cap.set(cv2.CAP_PROP_FOCUS,focus)
	print (cap.get(cv2.CAP_PROP_FOCUS))

	d=NOW.strftime("%d-%m-%y_%H-%M-%S")
	filename = path + d  + '.tiff'

	ret, frame = cap.read()


#	cv2.imshow('frame', frame)
	cv2.imwrite(filename, frame)
	cnt = cnt + 1
	print(cnt)
	time.sleep(interval)

# When it is done, release the capture
cap.release()
cv2.destroyAllWindows()

