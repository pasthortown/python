from gtts import gTTS
import os    

tts = gTTS(text="Hablo español", lang='es')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")