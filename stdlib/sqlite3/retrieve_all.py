#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys


con = sqlite3.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print(row)
