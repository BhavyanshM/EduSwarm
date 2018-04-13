import cv2
import imutils
import numpy as np

#func for getting color of click pos
def click_pos(event, x, y, flags, param):
	global mouseX , mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		mouseX, mouseY = x, y
		print(frame[y,x])

#The camera
cap = cv2.VideoCapture(1);

while True:
	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
	global frame
	ret, frame = cap.read()
	frame = frame[100:400, 100:600]
	cv2.imshow('frame', frame)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	greenLower = (140, 185, 120)
	greenUpper = (150, 205, 145)
	maskG = cv2.inRange(hsv, greenLower, greenUpper)

	blueLower = (175, 75, 25)
	blueUpper = (290, 90, 40)
	maskB = cv2.inRange(frame, blueLower, blueUpper)
	
	mask = maskB + maskG
	cv2.imshow('mask', mask)
	

	# img = cv2.imread('frame')
	# ret,thresh = cv2.threshold(img,127,255,0)
	# _,contours,hierarchy = cv2.findContours(thresh, 1, 2)
	# cnt = contours[0]
	# M = cv2.moments(cnt)

	cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()