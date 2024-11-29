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

```python
import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

# Commit changes
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
```


