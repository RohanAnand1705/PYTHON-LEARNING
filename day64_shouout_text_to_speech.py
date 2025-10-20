import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")
l = ["A", "B", "C", "D"]
for item in l:
    text = (f"shoutout to {item}")
    print(text)
    speaker.Speak(text)