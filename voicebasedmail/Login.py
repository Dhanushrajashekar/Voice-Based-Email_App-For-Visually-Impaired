import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import MySQLdb
import cv2,os
import shutil
import pandas as pd
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import LoginPage as LP

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import time
import Start as s
import time
from datetime import datetime
    
uname=""
password=""
n=0
mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='vmail')
conn = mydb.cursor()
cam = cv2.VideoCapture(0)

# function to be called when button-2 of mouse is pressed 
def pressed2(event): 
        print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y)) 

def TrackImages(dbuid):
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    co=['name']
    attendance = pd.DataFrame(columns = col_names)
    namess=""

    for index, row in df.iterrows():
        namess+= row['Name']+" "
    aa=""


    
    attendance1 = pd.DataFrame(columns = co)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print("id==",Id)
            print("conf==",conf)
            if(conf < 50):
                    print("outside if")
                    tt=str(Id)
                    print("dbuid=",dbuid)
                    if dbuid!=tt:
                            print("Inside if")
                            return False
                    else:
                            print("inside else")
                            return True
               
                
                
                
            else:
                Id='Unknown'                
                tt=str(Id)
                return False
            break
            
                #cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
          
        cv2.imshow('im',im)
        if (cv2.waitKey(1)==ord('q')):
            cam.release()
            cv2.destroyAllWindows()
        
        

# function to be called when button-3 of mouse is pressed 
def pressed3(event):
        global n
        print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y)) 
        print("usename",uname)
        print("password",password)
        
        cmd="SELECT uid,uname,pass FROM login WHERE uname='"+str(uname)+"' and pass='"+str(password)+"'"
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()
        uid=""
        #print(cursor.fetchall())
        isRecordExist=0
        for row in cursor:
                uid=row[0]
                #print("uid==",uid)
                isRecordExist=1
        if(isRecordExist==1):
                              
                if TrackImages(uid):
                        cam.release()
                        cv2.destroyAllWindows()
                        tts = gTTS(text="Login Succesfully", lang='en')
                        ran=random.randint(0,999)
                        ttsname=("name"+str(ran)+".mp3")
                        tts.save(ttsname)
                        playsound(ttsname)
                        os.remove(ttsname)
                        n=1
                else:
                        tts = gTTS(text="Face is not matched", lang='en')
                        ran=random.randint(0,999)
                        ttsname=("name"+str(ran)+".mp3")
                        tts.save(ttsname)
                        playsound(ttsname)
                        os.remove(ttsname)
                        
                
        else:
                tts = gTTS(text="Check Username and Password", lang='en')
                ran=random.randint(0,999)
                ttsname=("name"+str(ran)+".mp3")
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
        
        
    



def process():
        global uname,password,n 
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

   
        
        lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=300, y=300)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=600, y=315)

        lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=300, y=400)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=600, y=415)


        sym,sym1=LP.process()

        txt.insert('end',sym)
        txt1.insert('end',sym1)

        uname=txt.get()
        password=txt1.get()

        window.update()
        
        while True:
                time.sleep( 1 )
                uname=txt.get()
                password=txt1.get()
                print(uname)
                print(password)
                print(n)
                if n==1:
                        window.destroy()
                        s.process(uname)
                        break
                window.update()

        #window.after(30000, window.destroy)
        window.mainloop()
        
#process()
