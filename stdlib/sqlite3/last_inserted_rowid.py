#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")
        
    lid = cur.lastrowid
    print("The last Id of the inserted row is {}".format(lid))
