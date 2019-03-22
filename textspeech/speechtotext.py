import speech_recognition as sr                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Hable:")                                                                                   
    audio = r.listen(source)   

try:
    print("Dijiste " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("No pude entender")
except sr.RequestError as e:
    print("No pude entender; {0}".format(e))