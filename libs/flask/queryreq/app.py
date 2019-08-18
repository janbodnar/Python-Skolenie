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


# curl localhost:5000/greet?name=Peter
# Hello Peter

# curl localhost:5000/greet
# Hello Guest
