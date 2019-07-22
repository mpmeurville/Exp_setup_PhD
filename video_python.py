#Source: CodingEntrepreneurs

#### TO DO ####

# Save videos: Done
# Adjust focus manually: Done
# Register video for 10 seconds and then stop -> start another one immediatly etc.
# When video captured, store it on the external drive
# Change with frames per second: Done
# Check if OK with red filter
# Try on a big colony



import os
from datetime import datetime, date, time, timedelta
import time
import numpy as np
import cv2


### Parameters ###
NOW = datetime.now()
d=NOW.strftime("%d-%m-%y_%H-%M-%S")
print(d)


frame_per_seconds = 15.0
my_res = '720p'
focus = 0.28 # Focus between 0 and 255, 5 by 5. 
seconds_duration = 30
filename =  '/home/pi/setup/opencv-python/videos/' + d  + '.avi'

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


### Video recording ###

# Default camera is used
cap = cv2.VideoCapture(0)

# Enable (1) or disable (0) autofocus. 
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# Define the resolution we want to record
dims = get_dims(cap, my_res)

# Define video type we want
video_type_cv2 = get_video_type(filename)

# Creation of the file
out = cv2.VideoWriter(filename, video_type_cv2, frame_per_seconds, dims, isColor=False )


while datetime.now() < finish_time :

	# Capture frame by frame
	ret, frame = cap.read()
	if ret == True:

		# Set the focus values and print it
		cap.set(cv2.CAP_PROP_FOCUS,focus)
		print (cap.get(cv2.CAP_PROP_FOCUS))

		# The frame is in grays
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		# Write on the movie file
		out.write(frame)

		# Displays the video as it is saved
		cv2.imshow('frame', frame)

		# Keyboard interrupt in case of emergency !!!
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break


# When all done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
