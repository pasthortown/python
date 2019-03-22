import cv2
import numpy as np

def getthresholdedimg(hsv):
    red = cv2.inRange(hsv,np.array((160,20,70)),np.array((190,255,255)))
    yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((30,255,255)))
    green = cv2.inRange(hsv,np.array((36,0,0)),np.array((70,255,255)))
    blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((120,255,255)))
    both = cv2.add(red,red)
    return both

c = cv2.VideoCapture(0)
width,height = c.get(3),c.get(4)

while(True):
    rect,frame = c.read()
    frame = cv2.flip(frame,1)
    blur = cv2.medianBlur(frame,5)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    both = getthresholdedimg(hsv)
    circles = cv2.HoughCircles(both,cv2.HOUGH_GRADIENT,1.2,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
    	    cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
c.release()