#!/usr/bin/env python3

from flask import Flask, send_file

app = Flask(__name__)

@app.route('/image')
def get_image():

    filename = 'sid.png'
    return send_file(filename, mimetype='image/png')
