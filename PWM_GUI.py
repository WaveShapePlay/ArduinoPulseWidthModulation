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

padFrames = 5
buttonFrame = Frame(root)
buttonFrame.pack(pady = padFrames)
scaleBarFrame = Frame(root)
scaleBarFrame.pack(pady = padFrames)
entryFrame = Frame(root)
entryFrame.pack(pady = padFrames)
currntValFrame = Frame(root)
currntValFrame.pack(pady = padFrames)



defaultDuty = '128'
userDutyScale = StringVar()
userDutyScale.set(defaultDuty)

curretUserValue = StringVar()


class PWM_mode():
    
    def inputMode(self):
        ser.write(b'd')
        time.sleep(1)
        
    def turnOn_pwm(self):
        self.inputMode()
        value = '255'
        ser.write(value.encode())
        curretUserValue.set(value)

    def turnOff_pwm(self):
        self.inputMode()
        value = '0'
        ser.write(value.encode())
        curretUserValue.set(value)

    def slider_entry_pwm(self):
        self.inputMode()
        value = userDutyScale.get()
        ser.write(value.encode())
        curretUserValue.set(value)

    def entry_box_pwm(self):
        self.inputMode()
        value = entry_pwm.get()
        ser.write(value.encode())
        curretUserValue.set(value)

pwm = PWM_mode()

padyButtons = 10
btn_On = tk.Button(buttonFrame, text="Turn On", command=pwm.turnOn_pwm)
btn_On.grid(row=0, column=0, pady= padyButtons)

btn_Off = tk.Button(buttonFrame, text="Turn Off", command=pwm.turnOff_pwm)
btn_Off.grid(row=0, column=1,pady= padyButtons)

btn_SliderEntry = tk.Button(buttonFrame, text="Get Slider", command=pwm.slider_entry_pwm)
btn_SliderEntry.grid(row=0, column=2, pady= padyButtons)

btn_EntryBox = tk.Button(buttonFrame, text="Get Entry", command=pwm.entry_box_pwm)
btn_EntryBox.grid(row=0, column=3, pady= padyButtons)

scaleBar_pwm = tk.Scale(scaleBarFrame,from_=0,to = 255,orient=HORIZONTAL, variable = userDutyScale)
scaleBar_pwm.grid(row=0, column = 0)
scaleBar_Label = tk.Label(scaleBarFrame,text="analogWrite() value")
scaleBar_Label.grid(row=1,column =0)

entry_pwm = Entry(entryFrame,width=3)
entry_pwm.insert(0,"100")
entry_pwm.grid(row=0,column = 0)
entry_pwm_Label= tk.Label(entryFrame,text="Entry Value")
entry_pwm_Label.grid(row=1,column =0)

currentVal_textLable = tk.Label(CurrntValFrame,text ="The current value selected is:")
currentVal_Lable = tk.Label(CurrntValFrame,textvariable = curretUserValue)
currentVal_textLable.grid(row=0, column=0)
currentVal_Lable.grid(row=0, column=1)
curretUserValue.set(defaultDuty)

root.geometry("250x250")
root.mainloop()
