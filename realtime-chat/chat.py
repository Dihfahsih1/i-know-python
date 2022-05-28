import threading
import socket
from tkinter import *
import time

root = Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
  pass 

def threadsendmsg():
  pass

startchatimage = PhotoImage(file="start.png")
buttons = Button(root, image=startchatimage, command=func, borderwidth=0)
buttons.place(x=90, y=10) 

message=StringVar()
messagebox=Entry(root, textvariable=message, font=('calibre',10,'normal'),border=2, width=2)
messagebox.place(x=10,y=444)

sendmessageimg = PhotoImage(file="start.png")

sendmessagebutton=Button(root, image=sendmessageimg, command=threadsendmsg, borderwidth=0)
sendmessagebutton.place(x=260, y=444)

fstbx=Listbox(root, height=20, width=43)
fstbx.place(x=15, y=80)


root.mainloop()
