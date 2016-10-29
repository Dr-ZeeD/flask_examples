#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application that makes an ajax call. Run
it using ::

    python ajax.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask, render_template_string, jsonify
app = Flask(__name__)

index_template = '''\
<!DOCTYPE html>
<html>
  <body>

    <div id="modify-this">Hello, World?</div>

    <button type="button" onclick="loadDoc()">Do AJAX call!</button>

    <script>
      function loadDoc() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById("modify-this").innerHTML = xhttp.responseText;
          }
        };
        xhttp.open("GET", "{{ url_for('api') }}", true);
        xhttp.send();
      }
    </script>

  </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(index_template)


@app.route('/api')
def api():
	return 'Hello, World!'


if __name__ == '__main__':
    app.run()
