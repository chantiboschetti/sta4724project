'''
This is our code for the tattletale project, which trachs irises and helps determine if a user is looking away or distracted enough form their computer and sends an alert.

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

#Threshold Code (I'm a bit lost hehe)

_, _, contour, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv.2CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)

#Period !!
