#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Pack layout')

lbl1 = tkinter.Label(root, width=20, height=5, bg='SteelBlue2')
lbl1.pack(side=tkinter.LEFT, padx=10, pady=10)

lbl2 = tkinter.Label(root, width=20, height=5, bg='SteelBlue3')
lbl2.pack(side=tkinter.LEFT)

lbl3 = tkinter.Label(root, width=20, height=5, bg='SteelBlue4')
lbl3.pack(side=tkinter.LEFT, padx=10)

root.geometry('+300+250')
root.mainloop()
