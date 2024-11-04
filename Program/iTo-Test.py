from random import randint
import time
import RPi.GPIO as GPIO
from gpiozero import MCP3002
from guizero import App, Text

GPIO.setmode(GPIO.BCM)

#set_gpio
sensor_1 = MCP3002(0)

buzzer_1 = 4

GPIO.setup(buzzer_1, GPIO.OUT)
sef=int(sensor_1.value)*100
print(sensor_1.value)

#set_value
def kankaku():
#    luck = randint(1,100)

#make_def
    def buza_1():
        tk.Label(frame1, text=sef, bg="#cce0ef", fg="black", font=("tkMenuFont",14)).pack(pady=20)
        GPIO.output(buzzer_1, 1)
        print('smokey	|| condition of air is: ',sef,'% || contaminated	|| alarm = on')
        time.sleep(0.5)

def buza_2():
    GPIO.output(buzzer_2, 1)
    print('smokey	|| condition of air is: ',sensor_1.value,'% || contaminated	|| alarm = on')
    time.sleep(0.5)
    
def buza_3():
    GPIO.output(buzzer_3, 1)
    print('smokey	|| condition of air is: ',sensor_1.value,'% || contaminated	|| alarm = on')
    time.sleep(0.5)
    
def buza_4():
    GPIO.output(buzzer_4, 1)
    print('smokey	|| condition of air is: ',sensor_1.value,'% || contaminated	|| alarm = on')
    time.sleep(0.5)

def buza_5():
    GPIO.output(buzzer_5, 1)
    print('smokey	|| condition of air is: ',sensor_1.value,'% || contaminated	|| alarm = on')
    time.sleep(0.5)

def buza_6():
    GPIO.output(buzzer_6, 1)
    print('smokey	|| condition of air is: ',sensor_1.value,'% || contaminated	|| alarm = on')
    time.sleep(0.5)

#list
#buza = [buza_1, buza_2, buza_3, buza_4, buza_5, buza_6]
#sensor = [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6]

#make_ui

app = App('iTo')
text = Text(app, text=10)
text.repeat(1000, kankaku)
app.display()

#main_process
#while True:
#    if (sensor_1.value > 0.028):
#        buza_1()
#    elif (sensor_1.value <= 0.028):
#        GPIO.output(buzzer_1, 0)
#        time.sleep(0.2)
#        GPIO.output(buzzer_1, 0)
#        time.sleep(0.05)
#        GPIO.output(buzzer_1, 0)
#        time.sleep(0.2)
#        GPIO.output(buzzer_1, 0)
#        time.sleep(0.05)
#        print('fresh	|| condition of air is: ',sensor_1.value,'% || fresh	|| alarm = off')
#        time.sleep(0.5)        

#GPIO.cleanup()