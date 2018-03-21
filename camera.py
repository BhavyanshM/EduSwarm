import cv2
import numpy as np

cap = cv2.VideoCapture(0);

def click_pos(event, x, y, flags, param):
	global mouseX , mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		mouseX, mouseY = x, y
		print(frame[y,x])

while True:
	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
	global frame
	ret, frame = cap.read()

	greenLower = (135, 175, 115)
	greenUpper = (175, 225, 155)

	# print(frame.shape)
	# frame = frame[100:400, 100:600]
	cv2.imshow('frame', frame)
	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(frame, greenLower, greenUpper)
	cv2.imshow('mask', mask)
	cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()