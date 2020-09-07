#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

def onMotion(e):

    msg = 'x: {} y: {}'.format(e.x, e.y)
    lvar.set(msg)

root = tkinter.Tk()
root.title('Mouse move event')

lvar = tkinter.StringVar()
lbl = tkinter.Label(root, text="coordinates", textvariable=lvar)
lbl.place(x=20, y=20)

root.bind('<Motion>', onMotion)

root.geometry("300x250+300+300")
root.mainloop()
