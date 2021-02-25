from FlaskWebApp import app
from flask import request, render_template

@app.route('/')
def helloWeb():
    first_name = 'Rodny'
    last_name = 'German'
    return "Welcome to my first app!"

@app.route("/page")
def page1():
    return "page1"
