#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application that makes an ajax call. Run
it using ::

    python ajax.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask, render_template_string, request
app = Flask(__name__)

index_template = '''\
<!DOCTYPE html>
<html>
  <body>

    <form id="get-form" action="{{ url_for('api') }}">
      <input name="_method" type="hidden" value="GET">
      <input type="submit" value="Get">
    </form>

    <form id="post-form" action="{{ url_for('api') }}">
      <input name="_method" type="hidden" value="POST">
      <input type="submit" value="Post">
    </form>

    <form id="patch-form" action="{{ url_for('api') }}">
      <input name="_method" type="hidden" value="PATCH">
      <input type="submit" value="Patch">
    </form>

    <form id="delete-form" action="{{ url_for('api') }}">
      <input name="_method" type="hidden" value="DELETE">
      <input type="submit" value="Delete">
    </form>

    <form id="invalid-form" action="{{ url_for('api') }}">
      <input name="_method" type="hidden" value="INVALID">
      <input type="submit" value="Invalid">
    </form>

    <!-- jQuery -->
    <script src="{{ url_for('static', filename='js/jquery.js') }}"></script>

    <script>
      $(document).ready(function() {
        $("form").submit(function(event) {
          event.preventDefault();
          var form = $(this);
          var formdata = form.serializeArray();
          var len = formdata.length;
          var dataObj = {}
          for (i=0; i<len; i++) {
            dataObj[formdata[i].name] = formdata[i].value;
          }

          $.ajax({
            url: form.attr('action'),
            method: dataObj._method,
          })
            .done(function(data, textStatus, jqXHR) {
              alert(data);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
              alert(errorThrown);
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


@app.route('/api', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def api():
	return request.method


if __name__ == '__main__':
    app.run()
