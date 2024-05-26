# Flask 

*Flask* is Python micro web framework.

The flask application is run like this: `flask hello run`, provided the main app name is `hello.py`.  
If the applications name is `app.py`, we can directly run the application like: `flask run`.  

We can also run the application directly with `flask run` if we set the main application file to the  
`FLASK_APP` environment variable.  


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

## Query params

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():

    return 'Home page'


@app.route('/greet', methods=['GET'])
def greet():

    name = request.args.get('name', 'Guest')
    msg = f'Hello {name}'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}
```

## Plain form 

```python
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/show-user', methods=['POST', 'GET'], endpoint='show-user')
def show_user():

    if request.method == 'POST':
        data = request.form
        return render_template("show_user.html", data=data)
```

```html
<html>

<body>
    <form action="{{ url_for('show-user') }}" method="POST">
        <div>
            <label for="first-name">First Name:</label>
            <input type="text" id="first-name" name="firstname" required>
        </div>
        <div>
            <label for="last-name">Last Name:</label>
            <input type="text" id="last-name" name="lastname" required>
        </div>
        <div>
            <label for="occupation">Occupation:</label>
            <input type="text" id="occupation" name="occupation" required>
        </div>

        <button type="submit">Submit</button>
    </form>

</body>

</html>
```


```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Show user</title>
</head>

<body>

    <ul>

        {% for k, v in data.items() %}
        <li>
            {{ k }} - {{ v }}
        </li>
        {% endfor %}

    </ul>

</body>

</html>
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

## Debug toolbar

`pip install flask-debugtoolbar`

```python
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 's$cret'

toolbar = DebugToolbarExtension(app)


@app.route("/")
def home():

    return render_template('home.html', message='This is home page')
```






