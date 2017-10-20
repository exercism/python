import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _,frame= cap.read()
    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    obj = cv2.HoughCircles(frame,cv2.cv.CV_HOUGH_GRADIENT,1, 260, param1=30, param2=65, minRadius=0, maxRadius=0)
    if obj is not None:
        obj = np.round(obj[0,:]).astype('int')
        for (x,y,z) in circles:
            cv2.circle(output,(x,y),z,(0,255,0),4)
        cv2.imshow("Video",frame)
        if cv2.waitKey(5) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break
