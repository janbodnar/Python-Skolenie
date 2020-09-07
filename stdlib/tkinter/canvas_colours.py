#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Canvas colours')

canvas = tkinter.Canvas(root)
canvas.create_rectangle(30, 10, 120, 80, 
    outline="#fb0", fill="#fb0")
canvas.create_rectangle(150, 10, 240, 80, 
    outline="#f50", fill="#f50")
canvas.create_rectangle(270, 10, 370, 80, 
    outline="#05f", fill="#05f")            
canvas.pack(fill=tkinter.BOTH, expand=1)

root.geometry("400x100+300+300")
root.mainloop()
