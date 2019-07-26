import cv2
import os
from datetime import datetime, date, time, timedelta
import time


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
## fourcc.org/codecs to see what types of video formats are avai$
VIDEO_TYPE =  {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
        filename, ext = os.path.splitext(filename) # We define t$
        if ext in VIDEO_TYPE:
                return VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']


def vid_cap(interval, seconds_duration, cam_device_v, cam_device_c, f_v,b_v,c_v,  f_c,b_c,c_c, frame_per_second= 24, my_res = "720p", path_v = '/home/pi/setup/opencv-python/videos/', ext_v = '.avi', path_c = '/home/pi/setup/opencv-python/pictures/' , width = 1920, height = 1080, ext_c = '.tiff'):

	font = cv2.FONT_HERSHEY_SIMPLEX # Font of the time on the video
	position_v = (1,700) # Position at which the writting has to start
	position_c = (1,1000)
	fontsize = 0.5

	NOW = datetime.now() # Do not touch
	d=NOW.strftime("%d-%m-%y_%H-%M-%S") # Do not touch
	finish_time = NOW + timedelta(seconds=seconds_duration) # Do not touch
	filename_video = path_v + d  + ext_v # name of the file. Extension matters here!



	# Call the camera device 0.Default camera is used if 0. Otherwis$
	cap_v = cv2.VideoCapture(cam_device_v)

	# Define video type we want
	video_type_cv2 = get_video_type(filename_video)

	# Define the resolution we want to record
	dims = get_dims(cap_v, my_res) # video

	# Creation of the video file
	out = cv2.VideoWriter(filename_video, video_type_cv2, frame_per_second, dims, isColor=False )


	# Creation of a counter that will define when pictures are taken.
	t_int = datetime.now()

	# Enable (1) or disable (0) the autofocus
	cap_v.set(cv2.CAP_PROP_AUTOFOCUS, 0)

	while datetime.now() < finish_time:

		# Capture frame-by-frame
		ret_v, frame_v = cap_v.read()

		# Set parameters for FOCUS, BRIGHTNESS, CONTRAST
		cap_v.set(cv2.CAP_PROP_FOCUS,f_v)
		cap_v.set(cv2.CAP_PROP_BRIGHTNESS,b_v)
		cap_v.set(cv2.CAP_PROP_CONTRAST,c_v)


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
			cap_c = cv2.VideoCapture(cam_device_c)
			cap_c.set(cv2.CAP_PROP_AUTOFOCUS, 0)

			# Define the resolution we want for the pictures.
			cap_c.set(3, width) # capture
			cap_c.set(4, height) # capture
			print ('Picture taken at: ' , datetime.now())

			# Set the focus. If autofocus activated, prints the autofocus value
			cap_c.set(cv2.CAP_PROP_FOCUS,f_c)
			cap_c.set(cv2.CAP_PROP_BRIGHTNESS,b_c)
			cap_c.set(cv2.CAP_PROP_CONTRAST,c_c
)
			print ("F: ", cap_c.get(cv2.CAP_PROP_FOCUS))
			print ("B: ", cap_c.get(cv2.CAP_PROP_BRIGHTNESS))
			print ("C: ", cap_c.get(cv2.CAP_PROP_CONTRAST))

			# Capture frame-by-frame
			ret_c, frame_c = cap_c.read()
			cv2.putText(frame_c,datetime.now().strftime("%d-%m-%y_%H-%M-%S"), position_c , font, fontsize ,(255,255,255),2) 

			# Display the resulting frame
			cv2.imshow('Pictures', frame_c)

			# Define the picture name based on date and time
			TIME_SAVE = datetime.now()
			d = TIME_SAVE.strftime("%d-%m-%y_%H-%M-%S")
			filename_capture = path_c + d  + ext_c

			# Save capture
			cv2.imwrite(filename_capture, frame_c)
			t_int = t_int + timedelta(seconds=interval)
			cap_c.release()

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything is done, release the capture
	cap_v.release()
	cv2.destroyAllWindows()


# Function debug
#vid_cap( seconds_duration = 120, cam_device_v = 0, cam_device_c = 1, f_v = 0.4, b_v = 0.7, c_v = 0.7, f_c = 0.4, b_c = 0.3, c_c = 0.7, interval = 10 )
