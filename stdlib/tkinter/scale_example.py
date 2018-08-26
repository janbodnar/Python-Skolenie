#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

def onScale(val):
    
    v = int(val)
    lvar.set(v)

root = tkinter.Tk()
root.title('Scale example')

root.columnconfigure(0, pad=5)        
root.columnconfigure(1, pad=15) 
root.rowconfigure(0, pad=5)

scale = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL, 
    command=onScale)
scale.grid(column=0, row=0)    

lvar = tkinter.IntVar()
label = tkinter.Label(root, text=0, textvariable=lvar)    
label.grid(column=1, row=0)

root.geometry("300x250+300+300")
root.mainloop()
