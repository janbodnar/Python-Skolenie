#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Pack layout')

frame1 = tkinter.LabelFrame(root, text='Vertical layout', 
    relief=tkinter.GROOVE)

lbl1 = tkinter.Label(frame1, width=15, height=3, bg='SlateGray2')
lbl1.pack(side=tkinter.TOP, pady=15, padx=10)

lbl2 = tkinter.Label(frame1, width=15, height=3, bg='SlateGray3')
lbl2.pack(side=tkinter.TOP, padx=10)

lbl3 = tkinter.Label(frame1, width=15, height=3, bg='SlateGray4')
lbl3.pack(side=tkinter.TOP, pady=15, padx=10)

frame1.pack(pady=10)

frame2 = tkinter.LabelFrame(root, text='Horizontal layout', 
    relief=tkinter.GROOVE)

lbl4 = tkinter.Label(frame2, width=15, height=3, bg='SkyBlue2')
lbl4.pack(side=tkinter.LEFT, pady=15, padx=10)

lbl5 = tkinter.Label(frame2, width=15, height=3, bg='SkyBlue3')
lbl5.pack(side=tkinter.LEFT, padx=10)

lbl6 = tkinter.Label(frame2, width=15, height=3, bg='SkyBlue4')
lbl6.pack(side=tkinter.LEFT, pady=15, padx=10)

frame2.pack(padx=10, pady=10)

root.geometry('+300+250')
root.mainloop()
