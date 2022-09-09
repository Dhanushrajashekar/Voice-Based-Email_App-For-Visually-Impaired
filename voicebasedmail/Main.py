from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import SignUp as s
import Login as l

def process():
	#fetch project name

	tts = gTTS(text="Welcome to Voice based Email System", lang='en')
	ran=random.randint(0,999)
	ttsname=("name"+str(ran)+".mp3") 
	tts.save(ttsname)

	playsound(ttsname)
	os.remove(ttsname)

	#choices
	print ("1.Register.")
	tts = gTTS(text="option 1. Register.", lang='en')
	ran=random.randint(0,999)

	ttsname=("hello"+str(ran)+".mp3") 
	tts.save(ttsname)

	playsound(ttsname)
	os.remove(ttsname)

	print ("2.Login")
	tts = gTTS(text="option 2. Login", lang='en')
	ran=random.randint(0,999)

	ttsname=("hello1"+str(ran)+".mp3")
	tts.save(ttsname)

	playsound(ttsname)
	os.remove(ttsname)

	#this is for input choices
	tts = gTTS(text="Your choice ", lang='en')
	ran=random.randint(0,999)

	ttsname=("hello2"+str(ran)+".mp3") 
	tts.save(ttsname)

	playsound(ttsname)
	os.remove(ttsname)
	
	text=""
	while(text==""):
		#voice recognition part
		r = sr.Recognizer()
		m = sr.Microphone()
			#set threhold level
		with m as source: r.adjust_for_ambient_noise(source)#recognize
		with sr.Microphone() as source:
			print ("Your choice:")
			audio=r.listen(source)
			print ("ok done!!")

		try:
			text=r.recognize_google(audio)
			print ("You said : "+text)
	
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		 
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

		if text=="":
			tts = gTTS(text="Error in Message.Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("err"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)


	#choices details
	if text == '1' or text == 'One' or text == 'one':
		print("Register")
		s.process()
		#sMail.process(uname)	
	if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text == 'Do'or text == 'do' :
		print("Login")
		l.process()
		#rMail.process(uname)
		
		
process()		
