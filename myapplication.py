import pyttsx3
import os
import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

pyttsx3.speak("Welcome to this application ! I'm PyCom. ")

while True:
    print("Talk to me with your requirement : ", end=" ")
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognising...")
        data = r.recognize_google(audio)
        print(data)
    if (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("write" in data)) and (
            ("notepad" in data) or ("editor" in data) or ("document" in data) or ("file" in data)):
        pyttsx3.speak("Opening Notepad")
        os.system("notepad")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("play" in data)) and (
            ("vlc" in data) or ("player" in data) or ("music" in data) or ("song" in data)):
        pyttsx3.speak("Opening Windows Media Player")
        os.system("vlc")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("click" in data)) and (
            ("cam" in data) or ("camera" in data) or ("webcam" in data) or ("photo" in data)):
        pyttsx3.speak("Opening Camera")
        os.system("start microsoft.windows.camera:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("solve" in data)) and (
            ("calculator" in data) or ("calc" in data) or ("operation" in data) or ("calculation" in data)):
        pyttsx3.speak("Opening Calculator")
        os.system("start calc")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("change" in data)) and (
            ("settings" in data) or ("setting" in data)):
        pyttsx3.speak("Opening Settings")
        os.system("start ms-settings:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("notebook" in data) or ("jupyter notebook" in data) or ("jupyter" in data)):
        pyttsx3.speak("Opening Jupyter")
        os.system("jupyter notebook")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("excel" in data) or ("ms excel" in data) or ("msexcel" in data) or ("microsoft excel" in data) or (
            "spreadsheet" in data) or ("database" in data)):
        pyttsx3.speak("Opening M S Excel")
        os.system("start excel")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("make" in data)) and (
            ("powerpoint" in data) or ("ms powerpoint" in data) or ("mspowerpoint" in data) or ("microsoft powerpoint" in data) or (
            "presentation" in data)):
        pyttsx3.speak("Opening M S Powerpoint")
        os.system("start powerpnt")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("see" in data)) and (
            ("applications" in data) or ("apps" in data)):
        pyttsx3.speak("Opening Applications")
        os.system("start shell:appsfolder")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("draw" in data)) and (
            ("diagram" in data) or ("paint" in data) or ("ms paint" in data) or ("mspaint" in data)):
        pyttsx3.speak("Opening M S Paint")
        os.system("mspaint")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("write" in data)) and (
            ("Word" in data) or ("word" in data) or ("msword" in data) or ("ms word" in data)):
        pyttsx3.speak("Opening M S Word")
        os.system("start winword")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("write" in data)) and ("wordpad" in data):
        pyttsx3.speak("Opening Wordpad")
        os.system("write")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("file explorer" in data) or ("explorer" in data)):
        pyttsx3.speak("Opening File Explorer")
        os.system("start explorer")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("controlpanel" in data) or ("control panel" in data) or ("cpanel" in data) or ("control" in data)):
        pyttsx3.speak("Opening Control Panel")
        os.system("control")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("cmd" in data) or ("commandprompt" in data) or ("command prompt" in data)):
        pyttsx3.speak("Opening Command Prompt")
        os.system("start cmd")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and ("calendar" in data):
        pyttsx3.speak("Opening Calendar")
        os.system("start outlookcal:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("launch" in data)) and (
            ("msedge" in data) or ("microsoft edge" in data)):
        pyttsx3.speak("Opening Microsoft Edge")
        os.system("start microsoft-edge:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("change" in data)) and (
            ("settings" in data) or ("setting" in data)):
        pyttsx3.speak("Opening Settings")
        os.system("start ms-settings:")

    elif ("exit" in data) or ("quit" in data):
        break
    else:
        pyttsx3.speak("This application is not supported yet!")
        print("not supported till now")
pyttsx3.speak("Thank you for using me ! ")
print("Thank you ! ")
