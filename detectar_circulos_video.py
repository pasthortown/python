import cv2
import numpy as np
c = cv2.VideoCapture(0)
while(True):
    rect,frame = c.read()
    frame = cv2.flip(frame,1)
    blur = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 20, minRadius=25)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
    	    cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
c.release()