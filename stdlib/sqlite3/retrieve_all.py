#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print(row)
