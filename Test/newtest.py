import cv2

cam = cv2.VideoCapture(0)
x, y, w, h =  400, 100, 400, 500
text = "wearing ID"
while True:
	res, frame= cam.read()
	cv2.imshow('frame',frame)
	cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)

	font = cv2.FONT_HERSHEY_SIMPLEX
	fontscale = 2
	thickness= 3
	color= (0,255,0)

	cv2.putText(frame,text,(x+20,y+h+50),font,
		fontscale,color,thickness,cv2.LINE_AA)
	cv2.imshow('SmartID',frame)
	if cv2.waitKey(10) == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
