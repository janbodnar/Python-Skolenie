from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Home page'


@app.route('/users/<name>', methods=['POST'])
def create_user(name):

    msg = f'user {name} created'
    return make_response(msg, 201)


@app.route('/users/<name>', methods=['GET'])
def get_user(name):

    msg = f'Hello {name}'
    return make_response(msg, 200)
