import time
import serial
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import tkinter as tk
from tkinter import *
from tkinter import font
from time import strftime
from gpiozero import MCP3002
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
toggle_on = PhotoImage(file='/home/EID_Raspi/Program/Image/Toggle_on-Kemuri.png')
toggle_off = PhotoImage(file='/home/EID_Raspi/Program/Image/Toggle_off-Kemuri.png')
toggle2_on = PhotoImage(file='/home/EID_Raspi/Program/Image/Toggle_on-Kemuri.png')
toggle2_off = PhotoImage(file='/home/EID_Raspi/Program/Image/Toggle_off-Kemuri.png')
indi_1on = PhotoImage(file='/home/EID_Raspi/Program/Image/iTo-Indicator-On.png')
indi_1off = PhotoImage(file='/home/EID_Raspi/Program/Image/iTo-Indicator-Off.png')
indilog_1on = PhotoImage(file='/home/EID_Raspi/Program/Image/iTo-Smoke_Icon-On.png')
indilog_1off = PhotoImage(file='/home/EID_Raspi/Program/Image/iTo-Smoke_Icon-Off.png')

#setup sensor
sens_1 = MCP3002(0)
sens_2 = 10
sens_3 = 10
sens_4 = 10
lamp = 24
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
#smoke_1 = GPIO.input(sens_1)
GPIO.setup(lamp, GPIO.OUT)

state = 0

def main1():
    global sens_1
    sensor = 100 - (sens_1.value * 100)
    sense = "%.1f" % sensor
    print(sens_1.value, sensor, sense)
    smoke.configure(text=sense)
    root.after(500,main1)
    btn.configure(image=toggle_on)
    if sens_1.value <= 0.8:
        #print ("smokedetect")
        #indicator.configure(text='alarm')
        lampind_1.configure(image=indi_1on)
        smoke_1.configure(image=indilog_1on)
    else:
        #print("clr")
        #indicator.configure(text='OK')
        lampind_1.configure(image=indi_1off)
        smoke_1.configure(image=indilog_1off)

def main2():
    global state
    state = state + 1
    if state == 1:
        GPIO.output(lamp, GPIO.LOW)
        btn2.configure(image=toggle2_on)
    elif state == 2:
        GPIO.output(lamp, GPIO.HIGH)
        state = 0
        btn2.configure(image=toggle2_off)

background = Label(root, image=backgr)
background.place(x=-1, y=-1)

smoke = Label(root, text="Init..", bg="white", font=('Helvetica', 45, "bold"))
smoke.place(x=310, y=500)

indicator = Label(root, text="%", bg="white", font=('Helvetica', 45, "bold"))
indicator.place(x=430, y=500)

lampind_1 = Label(root, bg="black", image=indi_1off)
lampind_1.place(x=563, y=100)

lampind_2 = Label(root, bg="black", image=indi_1off)
lampind_2.place(x=990, y=100)

lampind_3 = Label(root, bg="black", image=indi_1off)
lampind_3.place(x=1417, y=100)

lampind_4 = Label(root, bg="black", image=indi_1off)
lampind_4.place(x=1844, y=100)

smoke_1 = Label(root, bg='black', image=indilog_1off)
smoke_1.place(x=290,y=169)

smoke_2 = Label(root, bg='black', image=indilog_1off)
smoke_2.place(x=717,y=169)

smoke_3 = Label(root, bg='black', image=indilog_1off)
smoke_3.place(x=1134,y=169)

smoke_4 = Label(root, bg='black', image=indilog_1off)
smoke_4.place(x=1551,y=169)

btn = tk.Button(root, bg="black", bd=0, highlightthickness=0, image=toggle_off, command=main1)
btn.place(x=210,y=997)

btn2 = tk.Button(root, bg="black", bd=0, highlightthickness=0, image=toggle2_off, command=main2)
btn2.place(x=310,y=997)

root.after(1000, lambda: root.wm_attributes('-fullscreen', 'true'))
root.mainloop()