#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('test.db')    

with con:
    
    con.row_factory = sqlite3.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print("{} {} {}".format(row["id"], row["name"], row["population"]))
