import numpy as np
import cv2

cap = cv2.VideoCapture(0)
rect, frame = cap.read()
frame = cv2.flip(frame,1)
cv2.imwrite('captura.png',frame)
cap.release()
cv2.destroyAllWindows()