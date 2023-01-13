import cv2 
import os 
from PIL import Image
import time

cap = cv2.VideoCapture(0)
start = False
data_type = "train"
current_class = "yID"
dir_ = f"data/{data_type}/{current_class}"

available_samples = len(os.listdir(dir_))
total_samples_gen = 500


x, y, w, h =  400, 100, 400, 500

while not start:
	ret, frame = cap.read()
	if not ret:
		continue
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

	cv2.putText(frame,
				f"press s to start",
				(x, y - 10),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (255, 0, 0), 1)
	cv2.imshow('SmartID', frame)
	if cv2.waitKey(10)== ord('s'):
		start = True
	if cv2.waitKey(10)==ord('q'):
		break

