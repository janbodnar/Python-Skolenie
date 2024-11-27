# Flask 

*Flask* is Python micro web framework.

The flask application is run like this: `flask hello run`, provided the main app name is `hello.py`.  
If the applications name is `app.py`, we can directly run the application like: `flask run`.  

We can also run the application directly with `flask run` if we set the main application file to the  
`FLASK_APP` environment variable.   


Run in debug mode: `flask run --debug`.  


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

Query parameters are a way to pass information to a web server as part of the URL.  
They are typically used in web requests to filter, sort, or customize the response  
from the server. Query parameters are added to the end of the URL and follow 
a specific format.

Query parameters are added to the URL after a question mark (?). Each parameter is a  
key-value pair separated by an equals sign (=). Multiple parameters are separated 
by ampersands (&).

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

The example processes a plain form without a form library. Note that processing forms  
requires a lot of work including form validation and applying necessery security measures.    

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

The `endpoint` parameter specifies the name of the url to which we refer via the  
`url_for` function in the templates. If the parameter is not specified, it defaults  
to the template name, `show_user` in our case. The first parameter of the `@app.route`  
defines the slug, the string that is actually displayed in the browser.  

The `index.html` file:

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

The `show_user.html` file:

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

Return data as JSON:

```python
@app.route('/users2')
def users_json():

    con = get_db_connection()
    users = con.execute('SELECT * FROM users').fetchall()
    con.close()

    users_list = [dict(user) for user in users]

    return jsonify(users_list)
```

## .flaskenv

Run with `flask run`.  

```
FLASK_DEBUG=true
FLASK_RUN_PORT=1111
```

## The create_app factory method

In a Flask application, the create_app function is a common factory function used to  
create and configure an instance of the Flask application. It is particularly useful  
for setting up different configurations for development, testing, and production  
environments, and for organizing larger applications.

```python
from flask import Flask
from datetime import datetime

def create_app():

    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return 'hello there'
    
    @app.cli.command("now")
    def now():
        print(datetime.now())

    return app
```


## Form processing


The `app.py` file:

```python
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the form class
class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=100)])
    salary = FloatField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            occupation=form.occupation.data,
            salary=form.salary.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success', user_id=user.id))
    return render_template('index.html', form=form)

@app.route('/success/<int:user_id>')
def success(user_id):
    user = User.query.get_or_404(user_id)
    return f'User {user.first_name} {user.last_name} added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
```

The `index.html` file in `templates` directory:  

```html
<!doctype html>
<html lang="en">
  <head>
    <title>WTForms and SQLite Example</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <div class="form-container">
      <div class="form-wrapper">
        <h1>User Form</h1>
        <form method="POST">
          {{ form.hidden_tag() }}
          <div>
            <label>{{ form.first_name.label }}</label><br>
            {{ form.first_name(size=32) }}<br>
            {% if form.first_name.errors %}
              <ul class="errors">
                {% for error in form.first_name.errors %}
                  <li>{{ error }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
          <div>
            <label>{{ form.last_name.label }}</label><br>
            {{ form.last_name(size=32) }}<br>
            {% if form.last_name.errors %}
              <ul class="errors">
                {% for error in form.last_name.errors %}
                  <li>{{ error }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
          <div>
            <label>{{ form.occupation.label }}</label><br>
            {{ form.occupation(size=32) }}<br>
            {% if form.occupation.errors %}
              <ul class="errors">
                {% for error in form.occupation.errors %}
                  <li>{{ error }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
          <div>
            <label>{{ form.salary.label }}</label><br>
            {{ form.salary(size=32) }}<br>
            {% if form.salary.errors %}
              <ul class="errors">
                {% for error in form.salary.errors %}
                  <li>{{ error }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
          <div>
            {{ form.submit(class="button-primary") }}
          </div>
        </form>
      </div>
    </div>
  </body>
</html>
```

The `style.css` in `static` directory:  

```python
/* Reset some basic elements */
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: Arial, sans-serif;
  }
  
  /* Center the form container */
  .form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Full viewport height */
    background-color: #f0f0f0;
  }
  
  /* Style the form wrapper */
  .form-wrapper {
    width: 50%; /* Adjust the width as needed */
    max-width: 600px; /* Maximum width */
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  /* Style form elements */
  .form-wrapper label {
    font-weight: bold;
    margin-top: 10px;
  }
  
  .form-wrapper input[type="text"],
  .form-wrapper input[type="number"] {
    width: 100%;
    padding: 8px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .form-wrapper .button-primary {
    width: auto; /* Shrink the button width */
    padding: 8px 16px; /* Adjust padding */
    background-color: #007bff;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .form-wrapper .button-primary:hover {
    background-color: #0056b3;
  }
  
  .errors {
    color: red;
    list-style-type: none;
    padding: 0;
  }
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






