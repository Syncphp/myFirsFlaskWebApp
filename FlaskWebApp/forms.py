from FlaskWebApp import app
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, RadioField, SelectField

class SampleForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    panther_id = IntegerField("Panther ID")
    start_date = DateField("Start Date", format="%m/%d/%Y")
    major = RadioField("Major",
                       choices=[('it', 'Information Technology'),
                                ('CS','Computer Science')])
    campus = SelectField("Campus",
                         choices=[('mmc', 'MMMC'),
                                  ('bbc', "BBC"),
                                  ('ec', 'Engineering Center')])

