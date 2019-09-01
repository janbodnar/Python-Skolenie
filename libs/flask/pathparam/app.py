from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():

    return 'Home page'


@app.route("/greet/<name>")
def greet(name):

    print(request.view_args['name'])
    msg = f'Hello {name}'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}


# curl localhost:5000/greet/Peter
# Hello Peter
