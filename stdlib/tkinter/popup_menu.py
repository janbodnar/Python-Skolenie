#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import datetime

def showDay():
    
    now = datetime.datetime.now()
    msg = 'Today is: {}'.format(now.strftime('%A'))
    tkinter.messagebox.showinfo("Information", msg)

def showMenu(e):

    pmenu.post(e.x_root, e.y_root)

root = tkinter.Tk()
root.title('popup menu')

pmenu = tkinter.Menu(root, tearoff=0)

pmenu.add_command(label="Show day", command=showDay)
pmenu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", showMenu)

root.geometry('300x300+300+250')
root.mainloop()
