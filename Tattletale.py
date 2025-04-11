'''
This is our code for the tattletale project, 
which tracks irises and helps determine if a user 
is looking away or distracted enough from their computer and sends an alert.

Members:
Onella Moitra
Chanti Boschetti
Kaitlyn Hull
Rebecca Murphy
William Rocha 
Anthony Beuke 

'''
import cv2
import numpy as np

cap = cv2.VideoCapture("eye_recording.flv")

while True:
  ret, frame = cap.read()
  roi = frame[269: 795, 537: 1416]
  cv2.imshow("Roi", frame)
  key = cv2.waitKey(30)
  if key == 27:
    break

cv2.destroyAllWindows()





