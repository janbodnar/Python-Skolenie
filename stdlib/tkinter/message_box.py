#!/usr/bin/env python3

import tkinter
import tkinter.messagebox
import datetime

def showDate():
    
    now = datetime.datetime.now()
    msg = 'Today is: {}'.format(now)
    tkinter.messagebox.showinfo("Information", msg)

root = tkinter.Tk()
root.title('Message box')

btn = tkinter.Button(root, text="Show date", padx=5, pady=5, width=10,
    command=showDate)
btn.pack()

root.geometry('300x300+300+250')
root.mainloop()
