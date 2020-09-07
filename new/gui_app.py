#!/usr/bin/python
# -*- coding: utf-8 -*-

# gui_app.py

from tkinter import Tk, BOTH, LEFT, N, W, E
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Button


class Example(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)  
        
        self.parent = parent        
        self.initUI()        
        
        
    def initUI(self):    

        self.parent.title("LabelFrame")
        self.pack(fill=BOTH, expand=True)
        
        labFrame = LabelFrame(self, text="Address")
        
        nameLbl = Label(labFrame, text="Street:")
        nameLbl.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.streetEntry = Entry(labFrame) 
        self.streetEntry.grid(row=0, column=1)
        
        addrLbl = Label(labFrame, text="Postal code:")
        addrLbl.grid(row=1, column=0, padx=10, sticky=E)
        self.postEntry = Entry(labFrame) 
        self.postEntry.grid(row=1, column=1)     
        
        labFrame.pack(anchor=N+W, ipadx=20, ipady=20, padx=15, pady=15)
        
        btn = Button(self, text="OK", command=self.buttonClick)
        btn.pack(pady=20)   
        
        
    def buttonClick(self):
         
        print(self.streetEntry.get())
        print(self.postEntry.get()) 
        
        print(type(self.streetEntry.get()))
        print(type(self.postEntry.get()))         
         

            
    
def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  


