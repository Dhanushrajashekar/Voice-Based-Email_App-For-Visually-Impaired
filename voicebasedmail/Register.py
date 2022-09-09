from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random

import os


def process():


	uname=""
	uid=""
	password=""
	name=""
	email=""
	epass=""
	email1=""
	mobile=""


	r = sr.Recognizer()
	m = sr.Microphone()
	#set threhold level
	with m as source: r.adjust_for_ambient_noise(source)#recognize
	while(uid==""):
		tts = gTTS(text="Enter User id", lang='en')
		ran=random.randint(0,999)
		ttsname=("uid"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)


		with sr.Microphone() as source:
			print ("Your User id :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			uid=r.recognize_google(audio)
			print ("You userid : "+uid)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if uid=="":
			tts = gTTS(text="Error in User id .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("unameerrid"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)



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


	while(name==""):
		tts = gTTS(text="Enter Name", lang='en')
		ran=random.randint(0,999)
		ttsname=("name"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		with sr.Microphone() as source:
			print ("Your Name :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			name=r.recognize_google(audio)
			print ("You Name : "+name)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if name=="":
			tts = gTTS(text="Error in Name .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("nameerr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)


	while(email1==""):

		tts = gTTS(text="Enter Email", lang='en')
		ran=random.randint(0,999)
		ttsname=("email"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		with sr.Microphone() as source:
			print ("Your email :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			email1=r.recognize_google(audio)
			print ("You email : "+email1)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    


		
		if email1=="":
			tts = gTTS(text="Error in email .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("emailerr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)


	words=email1.split()
	modified_mail=str()
	for word in words:
		if word == 'underscore':
			modified_mail=modified_mail+'_'
		elif word == 'dot':
			modified_mail=modified_mail+'.'
		elif word == 'at':
			modified_mail=modified_mail+'@'
		else:
			modified_mail=modified_mail+word

	email=modified_mail

	while(epass==""):

		tts = gTTS(text="Enter Email Password", lang='en')
		ran=random.randint(0,999)
		ttsname=("epss"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		with sr.Microphone() as source:
			print ("Your Eamil Password :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			epass=r.recognize_google(audio)
			print ("You Email Password : "+epass)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if epass=="":
			tts = gTTS(text="Error in Email Password .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("passerr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)

	while(mobile==""):

		tts = gTTS(text="Enter Mobile Number", lang='en')
		ran=random.randint(0,999)
		ttsname=("enum"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		with sr.Microphone() as source:
			print ("Your Mobile Number :")
			audio=r.listen(source)
			print ("ok done!!")
		try:
			mobile=r.recognize_google(audio)
			print ("Mobile Number : "+mobile)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))    

		
		if epass=="":
			tts = gTTS(text="Error in Mobile Number .Please Give Input Again ", lang='en')
			ran=random.randint(0,999)
			ttsname=("moberr"+str(ran)+".mp3") 
			tts.save(ttsname)
			playsound(ttsname)
			os.remove(ttsname)


	print(uname)
	print(password)
	print(name)
	print(email)	
	print(epass)
	print(mobile)
	return uid,uname,password,name,email,epass,mobile
	

#process()
