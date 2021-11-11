import pyttsx3
import keyboard

def onWord(name, location, length):
   print ('word', name, location, length)
   if keyboard.is_pressed("esc"):
      engine.stop()
      
engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('have fun, i love you.')
engine.runAndWait()