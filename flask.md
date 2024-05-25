# Flask 

*Flask* is Python micro web framework.


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
