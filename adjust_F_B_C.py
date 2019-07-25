import cv2
import numpy as np
import time
import os



#### AIM OF THIS SCRIPT ####
# I want to be able to take pictures from a camera, and to adjust contrast, brightness and focus easily, before taking real images. 
# The idea is to iteratively ask the user to set a value for these 3 parameters, 
# and once the user is happy with it, to remember the values, and pass them as an argument for the actual recording. 


# Default parameters
f = 0.32
b = 0.7
c = 0.5


main = input ('Do you want to set parameters? (Yes, Default, Auto) :	') # When python3, change to input


if main == 'Auto':

	val = False

	cap  = cv2.VideoCapture(0)

	cap.set(3, 1920)
	cap.set(4, 1080)


	if not cap.isOpened():
        	raise Exception("Could not open video device")

	while True:
		ret, frame = cap.read()
		cv2.imshow('Auto Settings', frame)

		if val == False:
			print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'	', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '	', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))
			val = True
		if cv2.waitKey(20) & 0xFF == ord('q'):

			break
	cv2.destroyAllWindows()

if main == 'Default':

	val = False

	cap  = cv2.VideoCapture(0)

	cap.set(3, 1920)
	cap.set(4, 1080)

	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

	if not cap.isOpened():
		raise Exception("Could not open video device")

	while True:

		ret, frame = cap.read()

		cap.set(cv2.CAP_PROP_FOCUS,f)
		cap.set(cv2.CAP_PROP_BRIGHTNESS,b)
		cap.set(cv2.CAP_PROP_CONTRAST,c)

		cv2.imshow('Default Settings', frame)

		if val == False:
			print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))
			val = True

		if cv2.waitKey(20) & 0xFF == ord('q'):

			break
	cv2.destroyAllWindows()


if main == 'Yes':

	val = False

	f = input ('F :    ')
	b = input ('B :    ')
	c = input ('C :    ')


	cap  = cv2.VideoCapture(0)

	cap.set(3, 640)
	cap.set(4, 480)

	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

	if not cap.isOpened():
		raise Exception("Could not open video device")

	while True:

		ret, frame = cap.read()

		cap.set(cv2.CAP_PROP_FOCUS, float(f))
		cap.set(cv2.CAP_PROP_BRIGHTNESS, float(b))
		cap.set(cv2.CAP_PROP_CONTRAST, float(c))

		cv2.imshow('User Settings', frame)

		if val == False:
			print ('F: ', cap.get(cv2.CAP_PROP_FOCUS),'     ', 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), '    ', 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))
			val = True
			print ('Quit: hit Q. Change parameters: hit C.')
		if cv2.waitKey(20) & 0xFF == ord('q'):

			break

		if cv2.waitKey(20) & 0xFF == ord('c'):

			cv2.destroyAllWindows()

			if not cap.isOpened():
				raise Exception("Could not open video device")

			f = input ('F :    ')
			b = input ('B :    ')
			c = input ('C :    ')


	cv2.destroyAllWindows()
