from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os

def process():

	uname=""
	password=""


	r = sr.Recognizer()
	m = sr.Microphone()
	#set threhold level
	with m as source: r.adjust_for_ambient_noise(source)#recognize


	while(uname==""):
		tts = gTTS(text="Enter UserName", lang='en')
		ran=random.randint(0,999)
		ttsname=("unams"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)


		with sr.Microphone() as source:
			print ("Your User Name :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			uname=r.recognize_google(audio)
			print ("You UserName : "+uname)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if uname=="":
			tts = gTTS(text="Error in User Name .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("unameerr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)


	while(password==""):
		tts = gTTS(text="Enter Password", lang='en')
		ran=random.randint(0,999)
		ttsname=("pss"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		with sr.Microphone() as source:
			print ("Your Password :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			password=r.recognize_google(audio)
			print ("You Password : "+password)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if password=="":
			tts = gTTS(text="Error in Password .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("passerr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)



	print(uname)
	print(password)
	return uname,password
	