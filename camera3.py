# import cv2
# import imutils
# import numpy as np

# #func for getting color of click pos
# def click_pos(event, x, y, flags, param):
# 	global mouseX , mouseY
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		mouseX, mouseY = x, y
# 		print(frame[y,x])

# def draw_pos(event, x, y, flags, param):
# 	global mouseX , mouseY
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		mouseX, mouseY = x, y
# 		cv2.circle(frame, (mouseX, mouseY), 100, (255, 255, 255), -1)


# #The camera
# cap = cv2.VideoCapture(1);

# while True:
# 	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# 	global frame
# 	ret, frame = cap.read()
# 	frame = frame[100:400, 100:600]
# 	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	

# 	cv2.setMouseCallback('frame', click_pos)
# 	cv2.setMouseCallback('frame', draw_pos)
# 	cv2.imshow('frame', frame)

# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break

# cap.release()
# cv2.destroyAllWindows()



import cv2
from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture(1) #Webcam Capture

while(True):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	names = ['bot1.png', 'bot2.png', 'bot3.png']

	for i in range(3):
		template = cv2.imread(names[i],0)
		w, h = template.shape[::-1]
		res = cv2.matchTemplate(gray,template,cv2.TM_SQDIFF)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		top_left = min_loc
		bottom_right = (top_left[0] + w, top_left[1] + h)
		cv2.rectangle(frame,top_left, bottom_right, 255, 1)
		cv2.putText(frame, names[i], (top_left[0],top_left[1]-10), 
				cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
	cv2.imshow('Test',frame)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()