from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = "COP4813Online"

from FlaskWebApp import routes