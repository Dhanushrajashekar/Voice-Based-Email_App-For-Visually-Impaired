import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
#import datetime
import time
from datetime import datetime
import MySQLdb
from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import Register as r
import time


from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import time

mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='vmail')
conn = mydb.cursor()

uidd=""
uname=""
password=""
name=""
email=""
epassword=""
mobile=""
n=0
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
def TakeImages(uid,unames):
    co=['Id']
    df=pd.read_csv("StudentDetails\StudentDetails.csv",names=co)
    
    namess = df['Id']
    ides=[]

    #print'Id:'
    #print namess
    
    Id=uid
    
    ides=Id
    #print 'Id='
    #print ides
    name=unames
    estest=0
    if ides in namess:
        estest=1
    else:
        estest=0
    #print estest
    if (estest==0):
        if(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>200:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name
            row = [Id , name]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            
        else:
            if(is_number(Id)):
                res = "Enter Alphabetical Name"
                print("Res",res)
                
            if(name.isalpha()):
                res = "Enter Numeric Id"
                print("Res",res)
                
        
    else:
        res = "Already Id Exist"
        print("Res",res)
        tts = gTTS(text="Userid Already Exists", lang='en')
        ran=random.randint(0,999)
        ttsname=("id"+str(ran)+".mp3")
        tts.save(ttsname)
        playsound(ttsname)
        os.remove(ttsname)

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids
# function to be called when button-2 of mouse is pressed 
def pressed2(event): 
        print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y)) 

# function to be called when button-3 of mouse is pressed 
def pressed3(event):
        global n
        print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y)) 
        print("usename",uname)
        print("password",password)
        print("name",name)
        print("email",email)
        print("epassword",epassword)
        print("mobile",mobile)
        print("uid",uidd)
        
        cmd="SELECT * FROM login WHERE uname='"+str(uname)+"'"
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()
        isRecordExist=0
        for row in cursor:
                isRecordExist=1
        if (isRecordExist==1):
                tts = gTTS(text="Username Already Exists", lang='en')
                ran=random.randint(0,999)
                ttsname=("name"+str(ran)+".mp3")
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)

                
        else:
                print("insert")
                cmd="INSERT INTO login(uid,uname,pass,name,email,epasssword,mobileno) Values('"+str(uidd)+"','"+str(uname)+"','"+str(password)+"','"+str(name)+"','"+str(email)+"','"+str(epassword)+"','"+str(mobile)+"')"
                print(cmd)
                tts = gTTS(text="Inserted Successfully", lang='en')
                ran=random.randint(0,999)
                ttsname=("name"+str(ran)+".mp3")
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
                conn.execute(cmd)
                mydb.commit()
                conn.close() 
                tts = gTTS(text="Kindly sit straight system will take your image for face based authentication", lang='en')
                ran=random.randint(0,999)
                ttsname=("an"+str(ran)+".mp3")
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
                TakeImages(uidd,uname)
                tts = gTTS(text="System captured Your face", lang='en')
                ran=random.randint(0,999)
                ttsname=("ans"+str(ran)+".mp3")
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)
                TrainImages()
                
                n=1
                
        
        


def process():
        global uidd,uname,password,name,email,epassword,mobile
        bgcolor="#ECFDB0"
        fgcolor="black"
        window = tk.Tk()
        window.title("Voice based Email System")
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.bind('<Button-2>', pressed2) 
        window.bind('<Button-3>', pressed3) 

                
        message1 = tk.Label(window, text="Voice based Email System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=10)             
    
        
        lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=300, y=250)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=600, y=265)

        lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=300, y=300)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=600, y=315)

        lbl2 = tk.Label(window, text="Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=300, y=350)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=600, y=365)

        lbl3 = tk.Label(window, text="Email",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=300, y=400)
        
        txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=600, y=415)


        lbl4 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=300, y=450)
        
        txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt4.place(x=600, y=465)
        
        lbl5 = tk.Label(window, text="Mobile",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl5.place(x=300, y=500)

        txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt5.place(x=600, y=515)
        
        lbl6 = tk.Label(window, text="Uid",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl6.place(x=300, y=550)

        txt6 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt6.place(x=600, y=565)


        uid,sym,sym1,sym2,sym3,sym4,sym5=r.process()
                
        txt.insert('end',sym)
        txt1.insert('end',sym1)
        txt2.insert('end',sym2)
        txt3.insert('end',sym3)
        txt4.insert('end',sym4)
        txt5.insert('end',sym5)
        txt6.insert('end',uid)


        uname=txt.get()
        password=txt1.get()
        name=txt2.get()
        email=txt3.get()
        epassword=txt4.get()
        mobile=txt5.get()
        uidd=txt6.get()
        print("uiddd==",uidd)
        
        
        window.update()
        
        while True:
                time.sleep( 1 )
                uname=txt.get()
                password=txt1.get()
                name=txt2.get()
                email=txt3.get()
                epassword=txt4.get()
                mobile=txt5.get()
                uidd=txt6.get()

                print(uname)
                print("eswar-- uid test",uidd)
                print(password)
                print(name)
                print(email)
                print(epassword)
                print(mobile)
                print(n)

                if n==1:
                        window.destroy()
                        break
                window.update()

        window.mainloop()
        
#TrainImages()
