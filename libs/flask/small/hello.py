#!/usr/bin/python

from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route("/")
# def hello():
    # return "Hello World!"

@app.route("/")	
def home():
    return app.send_static_file('index.html')
	
# @app.route("/hello/<name>")
# def greet(name):
    # return "Hello {0}".format(name)
	
# @app.route("/hello/<name>")
# def greet(name):
    # return render_template('index.html', name=name)
	
@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)
	
if __name__ == "__main__":
    app.run()
