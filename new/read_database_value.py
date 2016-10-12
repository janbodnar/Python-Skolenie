#!/usr/bin/python3
# -*- coding: utf-8 -*-

# read_database_value.py

import sqlite3 as lite
import sys

uId = 1

con = lite.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("SELECT Psc FROM Adress WHERE Id=:Id", 
        {"Id": uId})        
    con.commit()
    
    row = cur.fetchone()
    print (row[0])

    print (type(row[0]))
