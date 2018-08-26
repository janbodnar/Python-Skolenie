#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

def toggleTitle():

    isTitleShown = cbvar.get()

    if isTitleShown:
        root.title('Checkbutton example')
    else:
        root.title('')

root = tkinter.Tk()
root.title('Checkbutton example')

cbvar = tkinter.BooleanVar()
cbtn = tkinter.Checkbutton(root, text="Show", width=8, variable=cbvar,
    command=toggleTitle)
cbtn.select()
cbtn.pack()

root.geometry("300x250+300+300")
root.mainloop()
