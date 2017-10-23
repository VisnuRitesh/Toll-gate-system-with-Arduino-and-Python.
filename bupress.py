import serial
from datetime import datetime
from tkinter import *
#import Image, ImageTk
import io
import time
ser=serial.Serial('COM1',9600)
#file=open('toll.txt','w')
mw=Tk()
car=0
truck=0
bus=0
v=""
tm=""
cnt=0
sio=io.TextIOWrapper(io.BufferedRWPair(ser,ser))
#im = Image.open("index.jpeg")
#tkimage = ImageTk.PhotoImage(im.convert2byte(), palette=256)
Label(mw,text="Toll Gate System     ",font='Helvetica 22 bold').grid(row=0,column=0)
Label(mw,text="Time:",font='Helvetica 22 bold').grid(row=0,column=1)
Label(mw,text="Car",font='Helvetica 18 bold').grid(row=1,column=0)
Label(mw,text="Bus",font='Helvetica 18 bold').grid(row=1,column=1)
Label(mw,text="Truck/Container",font='Helvetica 18 bold').grid(row=1,column=2)
mw.minsize(width=300,height=300)
#image = ImageTk.PhotoImage(Image.open('index.jpeg'))
#Label(mw,image=image).grid(row=4,column=0)
Button(mw,text="Close",command=mw.destroy).grid(row=9,column=2)
while True:
    Label(mw,text=datetime.now().strftime('%d-%m-%Y %H:%M:%S'),font='Helvetica 22 bold').grid(row=0,column=2)
    if ser.inWaiting()>0:
        sio.flush()
        data=sio.read()
        if data=="1":
            cnt=cnt+1
            k=str(c)
            car=car+1
            v="Car"
            tm=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            h=k+v+" "+tm+"\n"
            #file.write(h)
        elif data=="2":
            truck=truck+1
            v="Bus"
            tm=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            tm=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            h=v+" "+tm+"\n"
        elif data=='3':
            bus=bus+1
            v="Truck/Container"
            tm=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            h=v+" "+tm+"\n"
        else:
            print(data)


        c=str(car)
        t=str(truck)
        b=str(bus)

        Label(mw,text=c,font='Helvetica 18 bold',foreground='red').grid(row=2,column=0)
        Label(mw,text=t,font='Helvetica 18 bold',foreground='blue').grid(row=2,column=1)
        Label(mw,text=b,font='Helvetica 18 bold',foreground='green').grid(row=2,column=2)
        Label(mw,text=v,font='Helvetica 18 bold').grid(row=3,column=0)
        Label(mw,text=tm,font='Helvetica 18 bold').grid(row=3,column=1)
        mw.update()
