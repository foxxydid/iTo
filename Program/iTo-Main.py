import time
import serial
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import tkinter as tk
from tkinter import *
from tkinter import font
from time import strftime
import random

#setup tkinter
root = Tk()
#root.attributes("-fullscreen",True)
root.title('iTo-EID')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

#setup image
backgr = PhotoImage(file='/home/EID_Raspi/Program/Image/iTo-Background.png')
but_1 = PhotoImage(file='/home/EID_Raspi/Program/Image/Button-Pull_Send.png')

#setup sensor
sens_1 = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sens_1, GPIO.IN)
#smoke_1 = GPIO.input(sens_1)

def main1():
    smoke_2 = random.randint(0,10)
    print(smoke_2)
    smoke.configure(text=smoke_2)
    root.after(1000,main1)

background = Label(root, image=backgr)
background.place(x=-1, y=-1)

smoke = Label(root,text=sens_1, font='arial')
smoke.place(x=400, y=400)

btn = tk.Button(root, bg="black", bd=0, highlightthickness=0, image=but_1, command=main1)
btn.place(x=200,y=200)

val = Entry(root, font=('arial', 15, 'bold'))
val.focus()
val.place(x=60, y=160)

root.after(1000, lambda: root.wm_attributes('-fullscreen', 'true'))
root.mainloop()