# Run this in pycharm IDE or Jupiter Notebook (It will work)

import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ == "__main__":
    print("Welcome to RoboSpeaker. This is created by Ammar")
    while True:
        x = input("What you want me to speak: ")
        if x == "q":
            text = "Ok bye, will talk to you later"
            speak.Speak(text)
            break
        text = x
        speak.Speak(text)
