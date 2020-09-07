#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.configure(background='gray')
root.title("Rotunda")

rot_i = Image.open("rotunda.jpg")
rotunda = ImageTk.PhotoImage(rot_i)

label = tkinter.Label(image=rotunda)
label.image = rotunda
label.place(x=20, y=20)

root.mainloop()
