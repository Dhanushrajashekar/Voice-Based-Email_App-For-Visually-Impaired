import speech_recognition as sr
import smtplib
# import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os
from imap_tools import MailBox, Q
from playsound import playsound
import sendMail as sMail
import sendmaila as smaila
import readMail as rMail
import random

def process(uname):
        #choices
        print ("1. composed a mail.")
        tts = gTTS(text="option 1. composed a mail.", lang='en')
        ran=random.randint(0,999)

        ttsname=("hello"+str(ran)+".mp3") 
        tts.save(ttsname)

        playsound(ttsname)
        os.remove(ttsname)

        print ("2. Check your inbox")
        tts = gTTS(text="option 2. Check your inbox", lang='en')
        ran=random.randint(0,999)

        ttsname=("hello1"+str(ran)+".mp3")
        tts.save(ttsname)

        playsound(ttsname)
        os.remove(ttsname)

        print ("3. Exit")
        tts = gTTS(text="option 3. Exit", lang='en')
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
                print("Choice one")
                print ("1. With Attachment")
                tts = gTTS(text="option 1. With Attachment.", lang='en')
                ran=random.randint(0,999)

                ttsname=("hello"+str(ran)+".mp3") 
                tts.save(ttsname)

                playsound(ttsname)
                os.remove(ttsname)

                print ("2. Simple Mail")
                tts = gTTS(text="option 2. Simple mail", lang='en')
                ran=random.randint(0,999)

                ttsname=("hello1"+str(ran)+".mp3")
                tts.save(ttsname)

                playsound(ttsname)
                os.remove(ttsname)
                tts = gTTS(text="Your choice ", lang='en')
                ran=random.randint(0,999)

                ttsname=("hello2"+str(ran)+".mp3") 
                tts.save(ttsname)

                playsound(ttsname)
                os.remove(ttsname)
                
                text1=""
                while(text1==""):
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
                                text1=r.recognize_google(audio)
                                print ("You said : "+text)
                
                        except sr.UnknownValueError:
                                print("Google Speech Recognition could not understand audio.")
                         
                        except sr.RequestError as e:
                                print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

                        if text1=="":
                                tts = gTTS(text="Error in Message.Please Give Input Again ", lang='en')
                                ran=random.randint(0,999)
                                ttsname=("err"+str(ran)+".mp3") 
                                tts.save(ttsname)
                                playsound(ttsname)
                                os.remove(ttsname)
                if text1 == '1' or text1 == 'One' or text1 == 'one':
                        smaila.process(uname)
                if text1 == '2' or text1 == 'tu' or text1 == 'two' or text1 == 'Tu' or text1 == 'to' or text1 == 'To' or text1 == 'do' or text1 == 'Do' :
                        sMail.process(uname)
        if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text == 'do' or text == 'Do' :
                print("Choice two")
                rMail.process(uname)
        if text == '3' or text == 'th' or text == 'thr' or text == 'Th' or text == 'thre' or text == 'Three' :
                print("Choice three")
                exit()  
