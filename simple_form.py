#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application that renders an actual HTML
document with a form. Run it using ::

    python simple_form.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask, render_template_string, flash, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'Secret Key'


class NameForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


template_string = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Simple Form</title>

    <!-- Bootstrap CSS -->
    <link href="{{ url_for('static', filename='css/bootstrap.css') }}" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      {% with messages = get_flashed_messages() -%}
      {%- for message in messages -%}
      <div class="alert alert-info alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
        {{ message|safe }}
      </div>
      {%- endfor -%}
      {%- endwith %}
      <h1>Simple Form</h1>
      <form method="POST" action="/">
        {{ form.hidden_tag() }}
        <div class="form-group{% if form.name.errors %} has-error{% endif %}">
          {{ form.name.label }}
          {{ form.name(class='form-control', placeholder=form.name.label.text)|safe }}
          {% if form.name.errors -%}
          <span class="help-block">
            {% for error in form.name.errors -%}
            {{ error }}
            {%- endfor %}
          </span>
          {%- endif %}
        </div>
        {{ form.submit(class="btn btn-default")|safe }}
      </form>
    </div>

    <!-- jQuery -->
    <script src="{{ url_for('static', filename='js/jquery.js') }}"></script>
    <!-- Bootstrap JS -->
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
  </body>
</html>
"""


@app.route('/', methods=('GET', 'POST'))
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash('You entered <strong>{}</strong>.'.format(form.name.data))
    return render_template_string(template_string, form=form)


if __name__ == '__main__':
    app.run()
