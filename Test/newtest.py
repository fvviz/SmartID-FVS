import cv2

cam = cv2.VideoCapture(0)
x, y, w, h =  400, 30, 600,600
text = "Not wearing ID"
while True:
	res, frame= cam.read()
	cv2.imshow('frame',frame)
	cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)

	font = cv2.FONT_HERSHEY_SIMPLEX
	fontscale = 2
	thickness= 3
	color= (255,255,255)
	cv2.rectangle(frame, (x, y + h + 50), (x + 150, y + h + 80+10), (0, 0, 0), -1)

	cv2.putText(frame,text,(x,y+h+30),font,
		1,color,2,cv2.LINE_AA)

	cv2.putText(frame, "Accuracy: 96.3%", (x ,y + h + 80), font,
				0.5, (0,0,255), 1, cv2.LINE_AA)

	cv2.imshow('SmartID',frame)
	if cv2.waitKey(10) == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
