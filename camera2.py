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
	#cv2.imshow('frame', frame)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# load the image, convert it to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	# find contours in the thresholded image
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	# compute the center of the contour
	M = cv2.moments(cnts[0])
	#cX = int(M["m10"] / M["m00"])
	#cY = int(M["m01"] / M["m00"])
	cv2.imshow("Image", frame)
	
	greenLower = (135, 180, 140)
	greenUpper = (160, 200, 150)
	maskG = cv2.inRange(hsv, greenLower, greenUpper)

	blueLower = (175, 75, 25)
	blueUpper = (290, 90, 40)
	maskB = cv2.inRange(frame, blueLower, blueUpper)
	
	mask = maskB + maskG
	#cv2.imshow('mask', mask)

	#cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()