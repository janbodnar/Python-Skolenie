# psycopg2

Psycopg is the most popular PostgreSQL database adapter for the Python programming  
language. Its main features are the complete implementation of the Python DB API 2.0  
specification and the thread safety (several threads can share the same connection).  

Basic terms:

1. **Connection**: A database connection allows  client software to communicate with database  
   server software. A connection is required  to send commands and receive answers, usually  
   in the form of a result set.   
3. **Cursor**: A database cursor is a mechanism that enables traversal over the records in  
   a database. Cursors facilitate subsequent processing in conjunction with the traversal,  
   such as retrieval, addition, and removal of database records.  
5. **Result Set**: A result set is the set of results returned by a query, usually in the same  
   format as the database the query is called on.  
7. **Query**: A database query is a request for data from a database. The request should come in   
   a database table or a combination of tables using a code known as the query language. This way,  
   the system can understand and process the query accordingly.




## Scalar value

```python
import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(host="localhost", database='testdb', user='postgres',
        password='s$cret')

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
```

---

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)
```


## execute 

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute(
        "CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Skoda', 9000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Bentley', 350000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")
```


## executemany

```python
import psycopg2

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute(
        "CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")

    query = "INSERT INTO cars (id, name, price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)

    con.commit()
```

## last row id 

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS words")
    cur.execute("CREATE TABLE words(id SERIAL PRIMARY KEY, word VARCHAR(255))")
    cur.execute("INSERT INTO words(word) VALUES('forest') RETURNING id")
    cur.execute("INSERT INTO words(word) VALUES('cloud') RETURNING id")
    cur.execute("INSERT INTO words(word) VALUES('valley') RETURNING id")

    last_row_id = cur.fetchone()[0]

    print(f"The last Id of the inserted row is {last_row_id}")
```

## fetch_all

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                    password='s$cret') as con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]}")
```

## fetch_one

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")
```

---

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars WHERE id = 1")

    row = cur.fetchone()

    print(f"{row[0]} {row[1]} {row[2]}")
```

## Dictionary cursor

```python
import psycopg2
import psycopg2.extras

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM cars")

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")
```


## Parameterized queries

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    uId = 1
    uPrice = 62300

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=%s WHERE id=%s", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
```

---

```python
import psycopg2

uid = 3

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars WHERE id=%(id)s", {'id': uid})
    row = cur.fetchone()

    print(f'{row[0]} {row[1]} {row[2]}')
```


## mogrify

```python

import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()

    print(cur.mogrify("SELECT name, price FROM cars WHERE id=%s", (2,)))
```

## Metadata

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()

    cur.execute('SELECT * FROM cars')

    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()

    print(f'{col_names[0]} {col_names[1]} {col_names[2]}')
```

---

```python
import psycopg2

with psycopg2.connect(database='testdb', user='postgres',
                      password='s$cret') as con:

    cur = con.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
```

## copy_to

```python
import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='postgres',
                    password='s$cret')

    cur = con.cursor()
    with open('cars.csv', 'w') as f:
        cur.copy_to(f, 'cars', sep="|")

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

except IOError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
```

# copy_from

```python

import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='postgres',
                    password='s$cret')

    cur = con.cursor()
    with open('cars.csv', 'r') as f:
        cur.copy_from(f, 'cars', sep="|")
        con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

except IOError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
```
