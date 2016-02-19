#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application that renders an actual HTML
document. Run it using ::

    python render_templates.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask, render_template_string
app = Flask(__name__)


template_string = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Hello, World!</title>

    <!-- Bootstrap CSS -->
    <link href="{{ url_for('static', filename='css/bootstrap.css') }}" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <h1>Hello, World!</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia deserunt
        mollit anim id est laborum.
      </p>
    </div>

    <!-- jQuery -->
    <script src="{{ url_for('static', filename='js/jquery.js') }}"></script>
    <!-- Bootstrap JS -->
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
  </body>
</html>
"""


@app.route('/')
def hello_world():
    return render_template_string(template_string)


if __name__ == '__main__':
    app.run()
