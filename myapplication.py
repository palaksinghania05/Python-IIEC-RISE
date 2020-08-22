import pyttsx3
import os

pyttsx3.speak("Welcome to this application ! I'm *****. ")

while(True):
	print("Talk to me with your requirement : " , end="")
	p=input()
	if((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("search" in p)) and (("chrome" in p) or ("browser" in p) or ("google" in p))):
		pyttsx3.speak("Opening Chrome")	
		os.system("chrome")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("write" in p)) and (("notepad" in p) or ("editor" in p) or ("document" in p) or ("file" in p))):
		pyttsx3.speak("Opening Notepad")
		os.system("notepad")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("play" in p)) and (("vlc" in p) or ("player" in p) or ("music" in p) or ("song" in p))):
		pyttsx3.speak("Opening Windows Media Player")
		os.system("vlc")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("click" in p)) and (("cam" in p) or ("camera" in p) or ("webcam" in p) or ("photo" in p))):
		pyttsx3.speak("Opening Camera")
		os.system("start microsoft.windows.camera:")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("solve" in p)) and (("calculator" in p) or ("calc" in p) or ("operation" in p) or ("calculation" in p))):
		pyttsx3.speak("Opening Calculator")
		os.system("start calc")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("change" in p)) and (("settings" in p) or ("setting" in p))):
		pyttsx3.speak("Opening Settings")
		os.system("start ms-settings:")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("notebook" in p) or ("jupyter notebook" in p) or ("jupyter" in p))):
		pyttsx3.speak("Opening Jupyter")
		os.system("jupyter notebook")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("excel" in p) or ("ms excel" in p) or ("msexcel" in p) or ("microsoft excel" in p) or ("spreadsheet" in p) or ("database" in p))):
		pyttsx3.speak("Opening M S Excel")
		os.system("start excel")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("make" in p)) and (("powerpoint" in p) or ("ms powerpoint" in p) or ("mspowerpoint" in p) or ("microsoft powerpoint" in p) or ("presentation" in p))):
		pyttsx3.speak("Opening M S Powerpoint")
		os.system("start powerpnt")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("see" in p)) and (("applications" in p) or ("apps" in p))):
		pyttsx3.speak("Opening Applications")
		os.system("start shell:appsfolder")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("draw" in p)) and (("diagram" in p) or ("paint" in p) or ("ms paint" in p) or ("mspaint" in p))):
		pyttsx3.speak("Opening M S Paint")
		os.system("mspaint")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("write" in p)) and (("Word" in p) or ("word" in p) or ("msword" in p) or ("ms word" in p))):
		pyttsx3.speak("Opening M S Word")
		os.system("start winword")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("write" in p)) and ("wordpad" in p)):
		pyttsx3.speak("Opening Wordpad")
		os.system("write")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("file explorer" in p) or ("explorer" in p))):
		pyttsx3.speak("Opening File Explorer")
		os.system("start explorer")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("controlpanel" in p) or ("control panel" in p) or ("cpanel" in p) or ("control" in p))):
		pyttsx3.speak("Opening Control Panel")
		os.system("control")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("cmd" in p) or ("commandprompt" in p) or ("command prompt" in p))):
		pyttsx3.speak("Opening Command Prompt")
		os.system("start cmd")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and ("calendar" in p)):
		pyttsx3.speak("Opening Calendar")
		os.system("start outlookcal:")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and (("msedge" in p) or ("microsoft edge" in p))):
		pyttsx3.speak("Opening Microsoft Edge")
		os.system("start microsoft-edge:")
	elif((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("change" in p)) and (("settings" in p) or ("setting" in p))):
		pyttsx3.speak("Opening Settings")
		os.system("start ms-settings:")

	elif(("exit" in p) or ("quit" in p)):
		break
	else:
		pyttsx3.speak("This application is not supported yet!")
		print("not supported till now")
pyttsx3.speak("Thank you for using me ! ")
print("Thank you ! ")
