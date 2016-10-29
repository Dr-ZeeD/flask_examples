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

    <button type="button">Do AJAX call!</button>

    <!-- jQuery -->
    <script src="{{ url_for('static', filename='js/jquery.js') }}"></script>

    <script>
      $(document).ready(function(){
        $("button").click(function(){
          $.get("{{ url_for('api') }}", function(data, status){
            $("#modify-this").text(data);
          });
        });
      });
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
