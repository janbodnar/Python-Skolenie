#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE cities(id INTEGER PRIMARY KEY, name TEXT, population INT)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Bratislava', 432000)")

    cur.execute("INSERT INTO cities(name, population) VALUES('Budapest', 1759000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Prague', 1280000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Warsaw', 1748000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Los Angeles', 3971000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('New York', 8550000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Edinburgh', 464000)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Suzhou', 4327066)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Zhengzhou', 4122087)")
    cur.execute("INSERT INTO cities(name, population) VALUES('Berlin', 3671000)")
