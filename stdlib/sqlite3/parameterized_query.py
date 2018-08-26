#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

name = 'Bratislava'
population = 432001

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("UPDATE cities SET population=? WHERE name=?", (population, name))        
    con.commit()
    
    print("Number of rows updated: {}".format(cur.rowcount))
