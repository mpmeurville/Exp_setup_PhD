import cv2

cap = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop)
x=1920
y=1080


cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))
print(str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

