#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a minimal example of a Flask application that renders an actual HTML
document with a form containing a fieldlist and buttons to add input fields.
Run it using ::

    python form_dynamic_fieldlist.py

Open your browser and head to http://127.0.0.1:5000/ and look at the result.
"""
from flask import Flask, render_template_string, flash
from flask_wtf import Form
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'Secret Key'


class NameForm(Form):
    names = FieldList(StringField('Name', validators=[DataRequired()]),
                      min_entries=0, max_entries=5)
    submit = SubmitField('Submit')


template_string = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Form Dynamic Fieldlist</title>

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
        <fieldset id="{{ form.names.id }}">
          <label class="control-label">Names</label>
          {% for name_field in form.names -%}
            <div class="form-group{% if name_field.errors %} has-error{% endif %}">
              {{ name_field(class='form-control', placeholder=name_field.label.text)|safe }}
              {% if name_field.errors -%}
                <span class="help-block">
                  {% for error in name_field.errors -%}
                    {{ error }}
                  {%- endfor %}
                </span>
              {%- endif %}
            </div>
          {%- endfor %}
        </fieldset>
        <div class="form-group">
          <button type="button" class="btn btn-default" id="add-name-field">
            Add Field
          </button>
          <button type="button" class="btn btn-default" id="remove-name-field">
            Remove Field
          </button>
        </div>
        <div class="form-group">
          {{ form.submit(class="btn btn-primary")|safe }}
        </div>
      </form>
    </div>

    <!-- jQuery -->
    <script src="{{ url_for('static', filename='js/jquery.js') }}"></script>
    <!-- Bootstrap JS -->
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script>
      $(document).ready(function() {
        var field_min_count = {{ form.names.min_entries|default(0, true) }};
        var field_max_count = {{ form.names.max_entries|default('null', true) }};
        var field_wrapper = $("fieldset#{{ form.names.id }}");
        var field_template = '<div class="form-group"><input class="form-control" id="names-{n}" name="names-{n}" placeholder="Name" type="text" value=""></div>';

        var add_field_button = $("button#add-name-field");
        var remove_field_button = $("button#remove-name-field");

        if (field_wrapper.children(".form-group").length <= field_min_count) {
          deactivate_button(remove_field_button);
        }

        function get_n_fields() {
          return field_wrapper.children("div.form-group").length;
        }

        function deactivate_button(button) {
          if (!button.attr("disabled")) {
            button.attr("disabled", true);
          }
        }

        function activate_button(button) {
          if (button.attr("disabled")) {
            button.removeAttr("disabled");
          }
        }

        add_field_button.click(function(event) {
          event.preventDefault();
          var n_fields = get_n_fields();
          field_wrapper.append(field_template.replace(/{n}/g, n_fields));
          activate_button(remove_field_button);
          if (field_max_count != null && n_fields + 1 >= field_max_count) {
            deactivate_button(add_field_button);
          }
        });

        remove_field_button.click(function(event) {
          event.preventDefault();
          var n_fields = get_n_fields();
          field_wrapper.children(".form-group").last().remove();
          activate_button(add_field_button);
          if (field_min_count != null && n_fields - 1 <= field_min_count) {
            deactivate_button(remove_field_button);
          }
        });
      });
    </script>
  </body>
</html>
"""


@app.route('/', methods=('GET', 'POST'))
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash('You entered {}.'.format(
            ', '.join(['<strong>{}</strong>'.format(name.data) for name in form.names])))
    return render_template_string(template_string, form=form)


if __name__ == '__main__':
    app.run()
