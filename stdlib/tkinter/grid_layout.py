#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Grid')

root.columnconfigure(0, pad=5)        
root.columnconfigure(1, pad=5) 
root.columnconfigure(2, pad=5) 
root.rowconfigure(0, pad=5)

btn1 = tkinter.Button(root, text='Button 1')
btn1.grid(column=0, row=0)

btn2 = tkinter.Button(root, text='Button 2')
btn2.grid(column=1, row=0)

btn3 = tkinter.Button(root, text='Button 3')
btn3.grid(column=2, row=0)

btn4 = tkinter.Button(root, text='Button 4')
btn4.grid(column=0, row=1)

btn5 = tkinter.Button(root, text='Button 5')
btn5.grid(column=1, row=1)

btn6 = tkinter.Button(root, text='Button 6')
btn6.grid(column=2, row=1)

root.geometry('300x300+300+250')
root.mainloop()
