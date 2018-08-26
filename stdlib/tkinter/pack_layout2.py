#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Pack layout')

lbl1 = tkinter.Label(root, width=20, height=5, bg='SlateGray2')
lbl1.pack(side=tkinter.TOP, pady=15, padx=10)

lbl2 = tkinter.Label(root, width=20, height=5, bg='SlateGray3')
lbl2.pack(side=tkinter.TOP, padx=10)

lbl3 = tkinter.Label(root, width=20, height=5, bg='SlateGray4')
lbl3.pack(side=tkinter.TOP, pady=15, padx=10)

root.geometry('+300+250')
root.mainloop()
