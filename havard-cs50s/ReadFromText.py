import pyttsx3
from time import sleep

engine = pyttsx3.init()
user = str(input('Type to text to speech: '))
sleep(1)
engine.say(user)
engine.runAndWait()
