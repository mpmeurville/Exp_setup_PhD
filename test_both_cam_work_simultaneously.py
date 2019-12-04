import numpy as np
import cv2
import os
from datetime import datetime, date, time, timedelta
import time
    


cap1 = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(0)

cap1.set(cv2.CAP_PROP_AUTOFOCUS, 0.8)
cap1.set(cv2.CAP_PROP_BRIGHTNESS, 0.4)
cap1.set(cv2.CAP_PROP_CONTRAST,0.5)

cap2.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap2.set(cv2.CAP_PROP_BRIGHTNESS, 0.4)
cap2.set(cv2.CAP_PROP_CONTRAST,0)


vid_cod = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter("/home/pi/setup/device/test/test.avi", vid_cod, 20.0, (640,480))
out2 = cv2.VideoWriter("/home/pi/setup/device/test/test.avi", vid_cod, 20.0, (640,480))


while(True):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Our operations on the frame come here
    #gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame1',frame1)
    out1.write(frame1)
    
    cv2.imshow('frame2', frame2)
    out2.write(frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

            

# When everything done, release the capture
cap1.release()
out1.release()
cap2.release()
out2.release()
cv2.destroyAllWindows()
