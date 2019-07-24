import cv2
import numpy as np
import time
import os



 #### AIM OF THIS SCRIPT ####
# I want to be able to take pictures from a camera, and to adjust contrast, brightness and focus easily, before taking real images. 
# The idea is to iteratively ask the user to set a value for these 3 parameters, 
# and once the user is happy with it, to remember the values, and pass them as an argument for the actual recording. 



cap  = cv2.VideoCapture(0)


main = raw_input ('Do you want to set parameters? (Y, N, A)') # When python3, change to input

if main == 'A':
	cap.set(3, width)
	cap.set(4, height)
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	print ('F: ', cap.get(cv2.CAP_PROP_FOCUS), 'B: ',cap.get(cv2.CAP_PROP_BRIGHTNESS), 'C: ', cap.get(cv2.CAP_PROP_CONTRAST))

	if cv2.waitKey(20) & 0xFF == ord('q'):
		print("Q")
		#break




# Enable (1) or disable (0) autofocus. 
#cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
#cap.set(cv2.CAP_PROP_AUTOEXPOSURE, 0)


#cap.set(3, width)
#cap.set(4, height)

#foc_ok = False
#bri_ok = False
#con_ok = False

#while (ret):
#	if foc_ok == False:
#		foc = input('What value for FOCUS?')
#
#	if bri_ok == False:
#		bri = input('What value for BRIGHTNESS?')
#
#	if con_ok = False:
#		con = input('What value for CONTRAST?')
#
#	cap.set(cv2.CAP_PROP_FOCUS, foc)
#	cap.set(cv2.CAP_PROP_BRIGHTNESS, bri)
#	cap.set(cv2.CAP_PROP_CONTRAST, con)
#
#	ret, frame = cap.read()
#
#	F = input('Is FOCUS ok?')
#	B = input ('Is BRIGHTNESS ok?')
#	C = input ('Is CONTRAST ok?')
#
#	# Keyboard interrupt in case of emergency !!!
#	if cv2.waitKey(20) & 0xFF == ord('q'):
#                       break

#cap.release()
#cv2.destroyAllWindows()


