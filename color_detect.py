import cv2
import numpy as np

def getthresholdedimg(hsv):
    red = cv2.inRange(hsv,np.array((160,20,70)),np.array((190,255,255)))
    yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((30,255,255)))
    green = cv2.inRange(hsv,np.array((36,0,0)),np.array((70,255,255)))
    blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((120,255,255)))
    both = cv2.add(yellow,yellow)
    return both

c = cv2.VideoCapture(0)
width,height = c.get(3),c.get(4)

while(True):
    rect,frame = c.read()
    frame = cv2.flip(frame,1)
    blur = cv2.medianBlur(frame,5)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    both = getthresholdedimg(hsv)
    erode = cv2.erode(both,None,iterations = 3)
    dilate = cv2.dilate(erode,None,iterations = 10)

    im2,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
        if 20 < hsv.item(int(cy),int(cx),0) < 30:
            cv2.rectangle(frame,(x,y),(x+w,y+h),[0,0,255],2)
        elif 100 < hsv.item(int(cy),int(cx),0) < 120:
            cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)

    cv2.imshow('img',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
c.release()