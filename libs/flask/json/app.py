from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Home page'


@app.route('/rmovie')
def random_movie():

    movies = {1: 'Toy story', 2: 'The Raid', 3: 'Hero',
              4: 'Ip Man', 5: 'Kung Fu Panda'}

    movie = random.choice(list(movies.items()))
    print(movie)

    return jsonify(movie)
