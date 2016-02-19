#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application. Run it using ::

    python hello_world.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
