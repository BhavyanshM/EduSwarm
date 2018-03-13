import cv2
import numpy as np

cap = cv2.VideoCapture(1);

while True:
	cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
	ret, frame = cap.read()
	# print(frame.shape)
	frame = frame[100:400, 100:600]
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()