import numpy as np
import cv2
import pickle
import time

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
cap = cv2.VideoCapture(0)

def analizar_captura():
    rect, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        color = (255, 0, 0)
        stroke = 2
        id_, conf = recognizer.predict(roi_gray)
        if conf>=35:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 0, 0)
            stroke = 2
            cv2.putText(frame, name, (x,y-5), font, 1, color, stroke, cv2.LINE_AA)
            print('Acceso Autorizado a Luis Salazar')
        start_cord = x+w
        end_cord = y+h
        cv2.rectangle(frame, (x,y), (start_cord, end_cord), color, stroke)
    cv2.imshow('Cerradura con Rostros', frame)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    analizar_captura()
        
cap.release()
cv2.destroyAllWindows()