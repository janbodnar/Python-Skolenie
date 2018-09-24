#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import random

def onEnterButton(e):

    w = root.winfo_width()
    h = root.winfo_height()

    b_w = btn.winfo_width()
    b_h = btn.winfo_height()

    r_x = random.randrange(0, w - b_w)
    r_y = random.randrange(0, h - b_h)

    btn.place(x=r_x, y=r_y)


root = tkinter.Tk()
root.title('Jumping button')
root.resizable(False, False)

btn = tkinter.Button(root, text='Exit', width=10, command=root.quit)
btn.place(x=180, y=20)

btn.bind('<Enter>', onEnterButton)

root.geometry("600x600+30+30")
root.mainloop()
