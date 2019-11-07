def action():
    print("Successful")

from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Online Booking Movie Tickets")
window.geometry('500x500')
lab1=Label(text="Language")
lab1.grid(column=0,row=0,sticky=W)
r1=Radiobutton(window,text='Hindi',value=1)
r2=Radiobutton(window,text='Kannada',value=2)
r3=Radiobutton(window,text='English',value=3)

r1.grid(row=1,column=0,sticky=W)
r2.grid(row=2,column=0,sticky=W)
r3.grid(row=3,column=0,sticky=W)

l2=Label(text="Movie names")
l2.grid(row=5,column=0,sticky=W)

c1=Checkbutton(window,text='Taree zamin par',variable='val1')
c2=Checkbutton(window,text='Jotejoteyali',variable='val2')
c1.grid(row=6,column=0,sticky=W)
c2.grid(row=7,column=0,sticky=W)

l3=Label(window,text="Select Number of Tickets")
l3.grid(row=9,column=0)

s=Spinbox(window,from_=1,to =10)
s.grid(row=10)

b=Button(text ="Submit",command=action)
b.grid(row=12,column=1)

