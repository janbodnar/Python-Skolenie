#!/usr/bin/env python3

import tkinter
import tkinter.messagebox

def showDialog():

    name = evar.get()
    msg = 'Hello {}'.format(name)
    tkinter.messagebox.showinfo('Greeting', msg)

root = tkinter.Tk()
root.title('Entry example')

frame = tkinter.Frame(root, borderwidth=10)

label = tkinter.Label(frame, text='Enter your name:')
label.grid(column=0, row=0)

evar = tkinter.StringVar()
entry = tkinter.Entry(frame, textvariable=evar)
entry.grid(column=1, row=0)

btn = tkinter.Button(frame, text="Greet", width=8,
    command=showDialog)
btn.grid(column=0, row=1, pady=10)

frame.pack()

root.geometry("450x250+300+300")
root.mainloop()
