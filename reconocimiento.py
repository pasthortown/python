import numpy as np
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)
contador = 0

while(True):
    rect, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        contador = contador + 1
        img_item = "a" + str(contador) + ".png"
        cv2.imwrite(img_item, frame)
        print('C')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()