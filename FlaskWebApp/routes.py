from FlaskWebApp import app
from flask import request, render_template

@app.route('/')
def helloWeb():
    first_name = 'Rodny'
    last_name = 'German'
    return 'My name is {0} {1}'.format(first_name,last_name)
