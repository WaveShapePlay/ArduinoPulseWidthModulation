import serial
from tkinter import *
import tkinter as tk
import time

#commPort = '/dev/cu.usbmodem14401'
commPort = 'COM4'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def inputMode():
    ser.write(b'd')
    time.sleep(1)
    
def turnOn_pwm():
    inputMode()
    value = '255'
    ser.write(value.encode())

def turnOff_pwm():
    inputMode()
    value = '0'
    ser.write(value.encode())

def entry_pwm():
    inputMode()
    value = entry_pwm.get()
    ser.write(value.encode())
    
# creating tkinter window 
root = Tk() 
root.title('PWM GUI')

btn_On = tk.Button(root, text="Turn On", command=turnOn_pwm)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOff_pwm)
btn_Off.grid(row=0, column=1)

btn_entry = tk.Button(root, text="Get Entry", command=entry_pwm)
btn_entry.grid(row=0, column=2)

entry_pwm = Entry(root,width=3)
entry_pwm.insert(0,"100")
entry_pwmLabel = tk.Label(root,text="analogWrite() value")
entry_pwmLabel.grid(row=2,column =0)
entry_pwm.grid(row=2,column = 1)

root.geometry("350x350")
root.mainloop()
