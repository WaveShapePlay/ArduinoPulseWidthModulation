import serial
from tkinter import *
import tkinter as tk
import time


commPort = '/dev/cu.usbmodem14401'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def user_pwm():
    ser.write(b'd')
    time.sleep(1)

def turnOn_pwm():
    ser.write(b'd')
    time.sleep(1)
    value = '0'
    ser.write(value.encode())

def turnOff_pwm():
    ser.write(b'd')
    time.sleep(1)
    value = '120'
    ser.write(value.encode())

def entry_pwm():
    ser.write(b'd')
    time.sleep(1)
    pwm_duty = entry_pwm.get()
    ser.write(value.encode(pwm_duty))
    
# creating tkinter window 
root = Tk() 
root.title('PWM GUI')

btn_On = tk.Button(root, text="Turn On", command=turnOn_pwm)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOff_pwm)
btn_Off.grid(row=0, column=1)

btn_entry = tk.Button(root, text="Get Entry", command=entry_pwm)
btn_entry.grid(row=0, column=2)
'''
pwm_State = IntVar()
chkBtn_pwm = tk.Checkbutton(root, text = "PWM",variable = state_pwm, command = user_pwm)
chkBtn_pwm.grid(row=0, column = 2)
'''
entry_pwm = Entry(root,width=3)
entry_pwm.insert(0,"5")
entry_pwmLabel = tk.Label(root,text="analogWrite() value")
entry_pwmLabel.grid(row=2,column =0)
entry_pwm.grid(row=2,column = 1)

root.geometry("350x350")
root.mainloop()
