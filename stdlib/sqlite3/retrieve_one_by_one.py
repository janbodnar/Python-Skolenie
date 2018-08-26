#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print(row[0], row[1], row[2])
