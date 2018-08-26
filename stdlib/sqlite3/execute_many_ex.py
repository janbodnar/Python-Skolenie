#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys

cars = (
    ('Bratislava', 432000),
    ('Budapest', 1759000),
    ('Prague', 1280000),
    ('Warsaw', 1748000),
    ('Los Angeles', 3971000),
    ('New York', 8550000),
    ('Edinburgh', 464000),
    ('Suzhou', 4327066),
    ('Zhengzhou', 4122087),
    ('Berlin', 3671000)
)

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("CREATE TABLE cities(id INTEGER PRIMARY KEY, name TEXT, population INT)")
    cur.executemany("INSERT INTO cities(name, population) VALUES(?, ?)", cars)
