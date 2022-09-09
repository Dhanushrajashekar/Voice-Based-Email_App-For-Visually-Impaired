import smtplib
import email
import imaplib
import os
from imap_tools import MailBox, Q
import bs4
from gtts import gTTS
from playsound import playsound
import re
import random
import speech_recognition as sr
import smtplib
import MySQLdb
import Start as s


username=""
password=""
mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='vmail')
conn = mydb.cursor()



mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security


def cleanhtml(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext
        
        
def numunreadMessage():
        unseen = mail.search(None, 'UnSeen') # unseen count
        print(unseen)
        b=unseen[1]
        print ("Number of UnSeen1 mails :"+str(len(b[0])))
        n=len(b[0])
        print ("Number of Un mails :"+ str(n))
        try:
                num=n
        except:
                num=0
        return num
        
def readMessage():
        unseen = mail.search(None, 'UnSeen') # unseen count
        b=unseen[1]
        ret=unseen[0]
        print(ret)
        i=0
        if ret=="OK":
                num=b[0].split()
                typ, data = mail.fetch(num[0],'(RFC822)')
                raw_email = data[0][1].decode("utf-8") #decode
                email_message = email.message_from_string(raw_email)
                print ("From: "+email_message['From'])
                print ("Subject: "+str(email_message['Subject']))
                stat, total1 = mail.select('Inbox')
                stat, data1 = mail.fetch(num[0], "(UID BODY[TEXT])")
                data2=data1[0]
                soup = bs4.BeautifulSoup(str(data2[1]), "html")
                div = soup.find("div")  
                res=cleanhtml(str(div))
                print(res)

                print ("From: "+email_message['From'])
                tts = gTTS(text="From: "+email_message['From'], lang='en')
                ran=random.randint(0,999)
                ttsname=("From"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)

                print ("Subject: "+str(email_message['Subject']))
                tts = gTTS(text="Subject: "+str(email_message['Subject']), lang='en')
                ran=random.randint(0,999)
                ttsname=("sub"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)

                print ("Body Of Message : "+res)
                tts = gTTS(text="Body Of Message : "+res, lang='en')
                ran=random.randint(0,999)
                ttsname=("body"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)

  
def process(sym):
        #conn= sqlite3.connect("Email")
        cmd="SELECT email,epasssword FROM login WHERE uname='"+str(sym)+"'"
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()


        for row in cursor:
                print(row[0])
                username=row[0]
                password=row[1]
                
        mail.login(username,password)  #login           

        stat, total = mail.select('Inbox')  #total number of mails in inbox
        print ("Number of mails in your inbox :"+str(total))
        num=numunreadMessage()  
        if num>0:
                print("Do you want read It")
                tts = gTTS(text="Do you want read It", lang='en')
                ran=random.randint(0,999)
                ttsname=("totalmail"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
                text=""
                while(text==""):
                        #voice recognition part
                        r = sr.Recognizer()
                        m = sr.Microphone()
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
                        #text="yes"
                        if text=="":
                                print("Empty")
                                tts = gTTS(text="Error in Message.Please Give Input Again ", lang='en')
                                ran=random.randint(0,999)
                                ttsname=("err"+str(ran)+".mp3") 
                                tts.save(ttsname)
                                playsound(ttsname)
                                os.remove(ttsname)
                        

                #choices details
                if text == 's' or text == 'yes' or text == 'ye':
                        print("Choice yes")
                        text=""
                        readMessage()
                        num1=numunreadMessage()
                        try:
                                while num1>0:
                                        print("Do you want read Another Mail")
                                        tts = gTTS(text="Do you want read Another Mail", lang='en')
                                        ran=random.randint(0,999)
                                        ttsname=("totalmail"+str(ran)+".mp3") 
                                        tts.save(ttsname)
                                        playsound(ttsname)
                                        os.remove(ttsname)
                                        #voice recognition part
                                        r = sr.Recognizer()
                                        m = sr.Microphone()
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
                                                print("Empty")
                                                tts = gTTS(text="Error in Message.Please Give Input Again ", lang='en')
                                                ran=random.randint(0,999)
                                                ttsname=("err"+str(ran)+".mp3")
                                                tts.save(ttsname)
                                                playsound(ttsname)
                                                os.remove(ttsname)
                                        else:
                                                if text == 's' or text == 'yes' or text == 'ye':
                                                        readMessage()
                                                        text=""
                                                        num1=num1-1
                                                if text == 'n' or text == 'no' or text == 'o':
                                                        text=""
                                                        num1=-1
                                                        break

                        except:
                                pass
        else:
                print("No Unread Message")
                tts = gTTS(text="No Unread Message", lang='en')
                ran=random.randint(0,999)
                ttsname=("totalmails"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
                s.process(sym)
                
#process("thiru")
