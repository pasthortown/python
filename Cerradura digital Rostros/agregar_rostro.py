import numpy as np
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)
contador = 0
print('Pulse la tecla C para capturar una nueva foto')
print('Pulse la tecla Q para salir')
while(True):
    rect, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('Entrenador', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        contador = contador + 1
        img_item = "Rostros/nuevo/a" + str(contador) + ".png"
        cv2.imwrite(img_item, frame)
        print('Captura Realizada')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()