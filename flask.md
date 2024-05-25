# Flask 

*Flask* is Python micro web framework.


## Simple example

Featuring routes, error handling, text/image/JSON responses.  

```python
from flask import Flask, make_response, send_file, render_template, jsonify
from markupsafe import escape
import random

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Main page!</p>"


@app.route("/hello/<name>")
def hello(name):
    msg = f'Hello {escape(name)}!'
    return make_response(msg, 200)


@app.route("/sid")
def get_image():
    return send_file('images/sid.png', mimetype='image/png')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/rmovie')
def random_movie():

    movies = {1: 'Toy story', 2: 'The Raid', 3: 'Hero',
              4: 'Ip Man', 5: 'Kung Fu Panda'}

    movie = random.choice(list(movies.items()))
    print(movie)

    return jsonify(movie)
```


## SQLite database 

The `test.db` file in project directory: 

```sql
CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, occupation TEXT);
INSERT INTO users(name, occupation) VALUES('John Doe', 'gardener');
INSERT INTO users(name, occupation) VALUES('Roger Doe', 'driver');
INSERT INTO users(name, occupation) VALUES('Paul Novak', 'teacher');
INSERT INTO users(name, occupation) VALUES('Lucia Smith', 'teacher');
INSERT INTO users(name, occupation) VALUES('John Williams', 'accountant');
INSERT INTO users(name, occupation) VALUES('Martin Bielik', 'programmer');
```

The `app.py` file. 

```python
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    con = sqlite3.connect('test.db')
    con.row_factory = sqlite3.Row
    return con


@app.route('/users')
def index():

    con = get_db_connection()
    users = con.execute('SELECT * FROM users').fetchall()
    con.close()

    return render_template('show_users.html', users=users)
```

The `templates/show_users.html` file:  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of users</title>
</head>
<body>

    {% for user in users %}
        <ul>
            <li>{{ user['id'] }}</li>
            <li>{{ user['name'] }}</li>
            <li>{{ user['occupation'] }}</li>
        </ul>
    {% endfor %}
    
</body>
</html>
```








