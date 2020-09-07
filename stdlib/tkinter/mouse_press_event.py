#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

def onButtonPress(e):

    msg = 'x: {} y: {}'.format(e.x, e.y)
    lvar.set(msg)

root = tkinter.Tk()
root.title('Mouse press event')

lvar = tkinter.StringVar()
lbl = tkinter.Label(root, textvariable=lvar)
lbl.place(x=20, y=20)

root.bind('<Button>', onButtonPress)

root.geometry("300x250+300+300")
root.mainloop()
