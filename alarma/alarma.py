import smtplib
import cv2
import numpy as np
import os
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from PIL import Image
import requests

def send_mail(username, password, send_from, send_to, subject, message, files=[]):
    use_tls=True
    server='smtp.gmail.com'
    port=587
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(os.path.basename(path)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

def capture(path, max):
    cap = cv2.VideoCapture(0)
    count = 1
    toReturn = []
    while(count<=max):
        rect, frame = cap.read()
        frame = cv2.flip(frame,1)
        fileOut = path + 'captura' + str(count) + '.png'
        cv2.imwrite(fileOut, frame)
        count = count + 1
        toReturn.append(fileOut)
        time.sleep(1);
    cap.release()
    cv2.destroyAllWindows()
    return toReturn

def recordVideo(filename):
    frames_per_second = 24.0
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    dims = (640, 480)
    video_type_cv2 = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, video_type_cv2, frames_per_second, dims)
    startTime = time.time()
    continueRecording = True
    while(continueRecording):
        rect, frame = cap.read()
        frame = cv2.flip(frame,1)
        out.write(frame)
        if(time.time() - startTime > 10):
            continueRecording = False
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return [filename]

def registerEvent(tiempo, idEstadoSirena, asunto):
    response = requests.post('http://alarmaedificio.000webhostapp.com/server/evento/crear',data={'tiempo': tiempo, 'idEstadoSirena': idEstadoSirena, 'AsuntoEmail': asunto})
    data = response.json()
    return data

response = requests.get('http://alarmaedificio.000webhostapp.com/server/estadosirena/leer')
data = response.json()
print(data)
now = datetime.datetime.now()
captured = capture(str(now.strftime('D:\\Proyectos\\python\\alarma\\%Y-%m-%d %Hh %Mm foto')),5)
userName = 'lsystemsecuador@gmail.com'
password = '1509Charles*'
fromMail = 'El presi'
toMails = ['balvarez@yavirac.edu.ec', 'pastorchessmaster@gmail.com', 'luissalazarvaca1986@gmail.com']
subject = str(now.strftime('Evento %Y-%m-%d %I:%M %p'))
bodyMail = str(now.strftime('Evento registrado el %d del mes %m del %Y a las %I:%M %p'))
send_mail(userName, password, fromMail, toMails, subject, bodyMail, captured)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('c'):
        now = datetime.datetime.now()
        captured = recordVideo(str(now.strftime('D:\\Proyectos\\python\\alarma\\video %Y-%m-%d %I:%M %p.mp4')))
        userName = 'alarmaedificiojimenez@gmail.com'
        password = '1509Charles*'
        fromMail = 'ALARMA EDIFICIO'
        toMails = ['pastorchessmaster@gmail.com']
        subject = str(now.strftime('Evento %Y-%m-%d %I:%M %p'))
        bodyMail = str(now.strftime('Evento registrado el %d del mes %m del %Y a las %I:%M %p'))
        send_mail(userName, password, fromMail, toMails, subject, bodyMail, captured)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;