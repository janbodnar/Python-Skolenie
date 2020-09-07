#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

uid = 2

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("SELECT name, population FROM cities WHERE id=:id", {"id": uid})        
    con.commit()
    
    row = cur.fetchone()
    print(row[0], row[1])
