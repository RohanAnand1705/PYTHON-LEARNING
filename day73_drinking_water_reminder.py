import time
import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")

text = ("Drink Water or I'll beat the shit out of you")
while True:
    speaker.Speak(text)
    time.sleep(5)