from flask import Flask
from database.flask_db import app


@app.route('/')
def hello():
    return '<h1>Hello World!<h1>'
