from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Home page'

@app.route('/about')
def about():
    return 'About page'

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
