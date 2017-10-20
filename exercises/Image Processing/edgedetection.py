import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
	ret, frame = cap.read()
	cv2.imshow('Edges',cv2.Canny(frame,130,210))
	if cv2.waitKey(5) == 27:
        	cap.release()
		cv2.destroyAllWindows()
		break
