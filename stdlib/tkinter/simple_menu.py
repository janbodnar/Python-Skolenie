#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import datetime

def showDay():
    
    now = datetime.datetime.now()
    msg = 'Today is: {}'.format(now.strftime('%A'))
    tkinter.messagebox.showinfo("Information", msg)

root = tkinter.Tk()
root.title('Menu')

menubar = tkinter.Menu(root)
root.config(menu=menubar)

fileMenu = tkinter.Menu(menubar)

fileMenu.add_command(label="Show day", command=showDay)
fileMenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=fileMenu)

root.geometry('300x300+300+250')
root.mainloop()
