#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

try:
    con = sqlite3.connect(':memory:')

    cur = con.cursor()  

    cur.executescript('''
        DROP TABLE IF EXISTS cars;
        CREATE TABLE cars(id INT, name TEXT, price INT);
        INSERT INTO cars VALUES(1,'Audi',52642);
        INSERT INTO cars VALUES(2,'Mercedes',57127);
        INSERT INTO cars VALUES(3,'Skoda',9000);
        INSERT INTO cars VALUES(4,'Volvo',29000);
        INSERT INTO cars VALUES(5,'Bentley',350000);
        INSERT INTO cars VALUES(6,'Citroen',21000);
        INSERT INTO cars VALUES(7,'Hummer',41400);
        INSERT INTO cars VALUES(8,'Volkswagen',21600);
        ''')

    con.commit()
    
except sqlite3.Error as e:
    
    if con:
        con.rollback()
        
    print("Error executing script: {}".format(e.args[0]))
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
