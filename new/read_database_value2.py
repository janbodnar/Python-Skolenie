#!/usr/bin/python3
# -*- coding: utf-8 -*-

# read_database_value2.py 

import sqlite3 as lite
import sys

uId = 2

con = lite.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", 
        {"Id": uId})        
    con.commit()
    
    row = cur.fetchone()
    print (row[0], row[1])

    print (type(row[0]))
    print (type(row[1]))
