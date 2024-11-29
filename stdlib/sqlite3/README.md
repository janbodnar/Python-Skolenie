# SQLite 

SQLite is a software library that provides a relational database management system.  
It's known for its lightweight, serverless, self-contained, and zero-configuration design,  
making it ideal for embedded systems and applications with minimal resource requirements.  
Unlike traditional databases like MySQL or PostgreSQL, SQLite doesn't require a separate  
server process, making it easy to deploy and use.

It's widely used in various applications, from mobile apps to desktop software, and even in  
embedded systems like IoT devices. If you're looking for a simple yet powerful way to manage  
data within your application, SQLite could be a great choice!

The `sqlite3` module in Python is a library that allows you to interact with SQLite databases.  
It's included in Python's standard library, which means you don't need to install anything extra  
to use it. This module provides a SQL interface compliant with the DB-API 2.0 specification,  
making it straightforward to execute SQL commands and manage your SQLite database.

Here are some key features and functions of the `sqlite3` module:
- **Connecting to a Database:** You can connect to an existing SQLite database or  
  create a new one using `sqlite3.connect(database)` where `database` is the name of the database file.  
- **Executing SQL Commands:** You can create tables, insert data, query data, and more  
  using methods like `cursor.execute(sql)`, where `sql` is your SQL command.  
- **Parameterized Queries:** To prevent SQL injection, you can use parameterized queries  
  by passing parameters as a tuple to the `execute` method.  
- **Transaction Management:** By default, SQLite is in autocommit mode. However, you can manage  
   transactions using `commit()` and `rollback()` methods to ensure data integrity.  
- **Data Fetching:** You can retrieve data using methods like `fetchone()`, `fetchall()`, and  
  `fetchmany(size)` to get query results.  

Here's a simple example of how to use the `sqlite3` module:


## Version 

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('test.db')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    version = cur.fetchone()
    
    print("SQLite version: {}".format(version[0])) 
    
except sqlite3.Error as e:
    
    print("Error {}:".format(e.args[0]))
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
```


```python
import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    version = cur.fetchone()
    
    print("SQLite version: {}".format(version[0]))
```

## Create table

```python
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
```
