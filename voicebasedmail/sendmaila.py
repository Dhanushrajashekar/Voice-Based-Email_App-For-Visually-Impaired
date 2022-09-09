import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from playsound import playsound
import speech_recognition as sr
import random
import MySQLdb

import tkinter as tk
from tkinter import Message ,Text
import time
import Start as s
from gtts import gTTS
import pyglet
import os

remail=""
subject=""
bom=""
sender_email=""
password=""
fname=""
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
    
    fromaddr = sender_email
    toaddr = remail

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = bom

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = fname
    attachment = open(fname, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
def display(uname):
	global remail,subject,bom,sender_email,password,n,fname
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
	lbl3 = tk.Label(window, text="Filename",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=300, y=600)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=600, y=615)
	
	print("remail in display",remail)

	txt.insert('end',remail)
	txt1.insert('end',subject)
	txt2.insert('end',bom)
	txt3.insert('end',fname)

	window.update()
	
	while True:
		time.sleep( 1 )
		remail=txt.get()
		subject=txt1.get()
		bom=txt2.get()
		fname=txt3.get()
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
    global remail,subject,bom,sender_email,password,fname
    #conn= sqlite3.connect("Email")
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
    fname=""
    
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
    while(fname==""):
            tts = gTTS(text="File name with extension ", lang='en')
            ran=random.randint(0,999)
            ttsname=("sub"+str(ran)+".mp3") 
            tts.save(ttsname)
            playsound(ttsname)
            os.remove(ttsname)


            with sr.Microphone() as source:
                    print ("File name with extension :")
                    audio=r.listen(source)
                    print ("ok done!!")
            try:
                    text1=r.recognize_google(audio)
                    print ("You said : "+text1)
                    fname = text1
            except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))   
            
            if fname=="":
                    tts = gTTS(text="Error in File name with extension.Please Give Input Again ", lang='en')
                    ran=random.randint(0,999)
                    ttsname=("err"+str(ran)+".mp3") 
                    tts.save(ttsname)
                    playsound(ttsname)
                    os.remove(ttsname)
    words1=fname.split()
    modified_fname=str()
    for word1 in words1:
            if word == 'dot':
                    modified_fname=modified_fname+'.'
            
            else:
                    modified_fname=modified_fname+word1

    fname=modified_fname
		
    return receiver_email,sub,msg,fname
def process(sym):
	global remail,subject,bom,sender_email,password,fname
	remail,subject,bom,fname=process1(sym)
	print("remail in process",remail)

	display(sym)
#process("eswar")
