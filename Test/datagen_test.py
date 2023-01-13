import cv2 
import os 
from PIL import Image
import time
from numpy import asarray

cap = cv2.VideoCapture(0)
start = False
data_type = "train"
current_class = "nID"
dir_ = f"data/{data_type}/{current_class}"

available_samples = len(os.listdir(dir_))
total_samples_gen = 100


x, y, w, h =  400, 30, 600,600

while not start:
	ret, frame = cap.read()
	if not ret:
		continue
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

	cv2.putText(frame,
				f"press s to start",
				(x, y - 10),
				cv2.FONT_HERSHEY_DUPLEX,
				1, (0, 255, 255), 1)

	cv2.putText(frame,
				f"class:{current_class}",
				(x, y + h + 25),
				cv2.FONT_HERSHEY_DUPLEX,
				1, (255, 255, 255), 1)

	cv2.putText(frame,
				f"type:{data_type}",
				(x, y + h + 55),
				cv2.FONT_HERSHEY_DUPLEX,
				1, (255, 255, 255), 1)

	cv2.putText(frame,
				f"samples available:{available_samples}/{total_samples_gen}",
				(x, y + h + 85),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.7, (255, 255, 255), 1)


	cv2.imshow('SmartID', frame)
	if cv2.waitKey(10)== ord('s'):
		start = True
	if cv2.waitKey(10)==ord('q'):
		break

for i in range(available_samples, total_samples_gen):
	ret, shot = cap.read()
	print(i,"/",total_samples_gen)
	if not ret:
		continue

	cv2.rectangle(shot, (x, y), (x + w, y + h), (0, 0, 255), 1)
	cv2.putText(shot,
				f"Capturing {current_class}", (x, y - 5),
				cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
	cv2.putText(shot,
				f"class:{current_class}",
				(x, y + h + 10),
				cv2.FONT_HERSHEY_DUPLEX,
				0.4, (255, 0, 0), 1)
	cv2.putText(shot,
				f"type:{data_type}",
				(x, y + h + 20),
				cv2.FONT_HERSHEY_DUPLEX,
				0.4, (255, 0, 0), 1)
	cv2.putText(shot,
				f"samples captured:{i}/{total_samples_gen}",
				(x, y + h + 30),
				cv2.FONT_HERSHEY_DUPLEX,
				0.4, (255, 0, 0), 1)

	roi = shot[y:y+h,x:x+w]
	cv2.imwrite(f"{dir_}/{i}.png",roi)
	cv2.imshow('SmartID-datagen', shot)
	if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
		break

cap.release()
cv2.destroyAllWindows()