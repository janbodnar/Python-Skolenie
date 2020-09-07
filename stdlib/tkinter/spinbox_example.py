#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

def onSelect():
    
    val = spinbox.get()
    lvar.set(val)

root = tkinter.Tk()
root.title('Spinbox example')

root.columnconfigure(0, pad=5)        
root.columnconfigure(1, pad=15) 
root.rowconfigure(0, pad=5)

spinbox = tkinter.Spinbox(root, from_=0, to=100, command=onSelect)
spinbox.grid(column=0, row=0)    

lvar = tkinter.StringVar()
label = tkinter.Label(root, text=0, textvariable=lvar)    
label.grid(column=1, row=0)

root.geometry("300x250+300+300")
root.mainloop()
