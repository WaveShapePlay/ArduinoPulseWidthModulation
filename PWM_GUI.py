import serial
from tkinter import *
import tkinter as tk
import time

#commPort = '/dev/cu.usbmodem14401'
commPort = 'COM4'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

# creating tkinter window 
root = Tk() 
root.title('PWM GUI')

userDutyScale = StringVar()
userDutyScale.set('11')

class PWM_mode():
    
    def inputMode(self):
        ser.write(b'd')
        time.sleep(1)
        
    def turnOn_pwm(self):
        self.inputMode()
        value = '255'
        ser.write(value.encode())

    def turnOff_pwm(self):
        self.inputMode()
        value = '0'
        ser.write(value.encode())

    def entry_pwm(self):
        self.inputMode()
        value = userDutyScale.get()
        ser.write(value.encode())


pwm = PWM_mode()

btn_On = tk.Button(root, text="Turn On", command=pwm.turnOn_pwm)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=pwm.turnOff_pwm)
btn_Off.grid(row=0, column=1)


btn_entry = tk.Button(root, text="Get Entry", command=pwm.entry_pwm)
btn_entry.grid(row=0, column=2)

'''
entry_pwm = Entry(root,width=3)
entry_pwm.insert(0,"100")
entry_pwm.grid(row=2,column = 1)
'''

scaleBar_pwm = tk.Scale(root,from_=0,to = 255,orient=HORIZONTAL, variable = userDutyScale)
scaleBar_pwm.grid(row=2, column = 0)
scaleBar_Label = tk.Label(root,text="analogWrite() value")
scaleBar_Label.grid(row=3,column =0)
root.geometry("350x350")
root.mainloop()
