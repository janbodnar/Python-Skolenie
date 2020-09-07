#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
