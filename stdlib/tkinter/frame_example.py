#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Frame widget')

frame = tkinter.Frame(root, borderwidth=15)

btn = tkinter.Button(frame, text="Quit", padx=5, pady=5, width=10,
    command=root.destroy)
btn.pack()

frame.pack()

root.mainloop()
