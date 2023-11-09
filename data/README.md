# Info


## Start PostgreSQL database on Windows

```
C:\Users\Jano\opt\postgre>bin\pg_ctl.exe -D data start
C:\Users\Jano\opt\postgre>bin\pg_ctl.exe -D data stop
```


## fetchall & rich

```python
#!/usr/bin/python

import psycopg2
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import date

con = psycopg2.connect(database='postgres',  user='postgres',  password='andrea')

with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM cars')
    rows = cur.fetchall()

    col_names = [cn[0] for cn in cur.description]

    now = f'{date.today()}'
    table = Table(title='Cars', box=box.MINIMAL, caption=now,
                caption_justify='left')

    for col_name in col_names:
        table.add_column(col_name)

    for row in rows:

        # table.add_row(str(row[0]), row[1], str(row[2]))
        # pars = [str(e) for e in (*row,)]
        pars = [str(e) for e in row]
        table.add_row(*pars)

    console = Console()
    console.print(table, justify='center')
```
