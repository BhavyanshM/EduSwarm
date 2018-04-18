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
	# frame = frame[100:400, 100:600]
	copy = frame.copy()

	cv2.imshow('frame', frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 20)

	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")

		for (x, y, r) in circles:
			cv2.circle(copy, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(copy, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	# greenLower = (150, 190, 140)
	# greenUpper = (140, 210, 160)
	# maskG = cv2.inRange(frame, greenLower, greenUpper)

	# bgreenLower = (125, 180, 130)
	# bgreenUpper = (155, 200, 150)
	# bmaskG = cv2.inRange(frame, bgreenLower, bgreenUpper)

	# blueLower = (160, 80, 50)
	# blueUpper = (190, 110, 80)
	# maskB = cv2.inRange(frame, blueLower, blueUpper)
	
	# mask = maskB + maskG + bmaskG
	#cv2.imshow('copy', copy)
	
	cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()