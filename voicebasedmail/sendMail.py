
import speech_recognition as sr
import smtplib
import email
import imaplib
from gtts import gTTS
import pyglet
import os
from imap_tools import MailBox, Q
from playsound import playsound
import random
import MySQLdb

import tkinter as tk
from tkinter import Message ,Text
import time
import Start as s

remail=""
subject=""
bom=""
sender_email=""
password=""
n=0
mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='vmail')
conn = mydb.cursor()

# function to be called when button-2 of mouse is pressed 
def pressed2(event): 
        print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y)) 

# function to be called when button-3 of mouse is pressed 
def pressed3(event):
        global n
        print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y)) 
        n=1
        
        header = 'To:' + remail + '\n' + 'From: ' + sender_email + '\n' + 'Subject: ' + subject + '\n'
        msg = header + bom
        
        print("header",header)
        print("msg",msg)
                
        mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
        mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
        mail.starttls() #security connection
        mail.login(sender_email,password) #login part
        mail.sendmail(sender_email,remail,msg) #send part
        print ("Congrates! Your mail has send. ")
        tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
        ttsname=("send.mp3") 
        tts.save(ttsname)
        playsound(ttsname)
        os.remove(ttsname)
        mail.close()   


def display(uname):
        global remail,subject,bom,sender_email,password,n
        bgcolor="#ECFDB0"
        fgcolor="black"
        window = tk.Tk()
        window.title("Voice based Email System")
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.bind('<Button-2>', pressed2) 
        window.bind('<Button-3>', pressed3) 

                
        message1 = tk.Label(window, text="Voice based Email System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=10)

   
        
        lbl = tk.Label(window, text="Receiver Email",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=300, y=300)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=600, y=315)

        lbl1 = tk.Label(window, text="Subject",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=300, y=400)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=600, y=415)
        

        lbl2 = tk.Label(window, text="Message",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=300, y=500)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=600, y=515)
        
        print("remail in display",remail)

        txt.insert('end',remail)
        txt1.insert('end',subject)
        txt2.insert('end',bom)

        window.update()
        
        while True:
                time.sleep( 1 )
                remail=txt.get()
                subject=txt1.get()
                bom=txt2.get()
                print(remail)
                print(subject)
                print(bom)

                print(n)
                if n==1:
                        window.destroy()
                        s.process(uname)
                        break
                window.update()

        #window.after(30000, window.destroy)
        window.mainloop()


def process1(sym):
        global remail,subject,bom,sender_email,password
        
        cmd="SELECT email,epasssword FROM login WHERE uname='"+str(sym)+"'"
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()
        sender_email=""
        password=""

        for row in cursor:
                print(row[0])
                sender_email=row[0]
                password=row[1]

        receiver_email="dmindsoftblore@gmail.com"
        
        
        r = sr.Recognizer()
        m = sr.Microphone()
        #set threhold level
        with m as source: r.adjust_for_ambient_noise(source)#recognize

        tts = gTTS(text="Enter Receiver Email. ", lang='en')
        ttsname=("sub1.mp3") 
        tts.save(ttsname)
        playsound(ttsname)
        os.remove(ttsname)

        receiver_email1=""
        while(receiver_email1==""):
                with sr.Microphone() as source:
                        print ("Your Receiver Email :")
                        audio=r.listen(source)
                        print ("ok done!!")
                try:
                        receiver_email1=r.recognize_google(audio)
                        print ("You Receiver Email : "+receiver_email1)
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

                if receiver_email1=="":
                        tts = gTTS(text="Error in Receiver Email.Please Give Input Again ", lang='en')
                        ran=random.randint(0,999)
                        ttsname=("err"+str(ran)+".mp3") 
                        tts.save(ttsname)
                        playsound(ttsname)
                        os.remove(ttsname)
                        
        words=receiver_email1.split()
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

        receiver_email=modified_mail
        
        
        
        sub=""
        msg=""
        
        while(sub==""):
                print(receiver_email)
                tts = gTTS(text="Your Subject. ", lang='en')
                ttsname=("sub.mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)


                with sr.Microphone() as source:
                        print ("Your Subject :")
                        audio=r.listen(source)
                        print ("ok done!!")
                try:
                        sub1=r.recognize_google(audio)
                        print ("You Subject : "+sub1)
                        sub = sub1
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

                if sub=="":
                        tts = gTTS(text="Error in Subject.Please Give Input Again ", lang='en')
                        ran=random.randint(0,999)
                        ttsname=("err"+str(ran)+".mp3") 
                        tts.save(ttsname)
                        playsound(ttsname)
                        os.remove(ttsname)

        while(msg==""):
                tts = gTTS(text="Body of the Message. ", lang='en')
                ran=random.randint(0,999)
                ttsname=("sub"+str(ran)+".mp3") 
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)


                with sr.Microphone() as source:
                        print ("Body of the Message :")
                        audio=r.listen(source)
                        print ("ok done!!")
                try:
                        text1=r.recognize_google(audio)
                        print ("You said : "+text1)
                        msg = text1
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))   
                
                if msg=="":
                        tts = gTTS(text="Error in Body of Message.Please Give Input Again ", lang='en')
                        ran=random.randint(0,999)
                        ttsname=("err"+str(ran)+".mp3") 
                        tts.save(ttsname)
                        playsound(ttsname)
                        os.remove(ttsname)
                
        return receiver_email,sub,msg
                
 

def process(sym):
        global remail,subject,bom,sender_email,password
        remail,subject,bom=process1(sym)
        print("remail in process",remail)

        display(sym)
