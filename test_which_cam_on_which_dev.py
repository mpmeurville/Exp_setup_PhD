import numpy as np
import cv2
import os
from datetime import datetime, date, time, timedelta
import time
    

### In the terminal, run v4l2-ctl --list-devices  or run ls -ltrh /dev/video* to have an idea of detected cameras and their dev. 

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)
cap.set(cv2.CAP_PROP_CONTRAST,80)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)



print(cap.get(cv2.CAP_PROP_AUTOFOCUS))

vid_cod = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("/home/pi/setup/device/test/test.avi", vid_cod, 20.0, (640,480))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    out.write(gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

            

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()