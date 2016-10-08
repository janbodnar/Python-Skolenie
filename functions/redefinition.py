#!/usr/bin/python3

# redefinition.py

from time import gmtime, strftime


def showMessage(msg):
    
    print (msg)
        
showMessage("Ready.")

def showMessage(msg):
    
    print (strftime("%H:%M:%S", gmtime()))
    print (msg)
    
showMessage("Processing.")  
