#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    version = cur.fetchone()
    
    print("SQLite version: {}".format(version[0]))
