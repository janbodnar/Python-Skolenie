#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute('PRAGMA table_info(cities)')
    
    data = cur.fetchall()
    
    for d in data:
        print(d[0], d[1], d[2])
