from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from frontend.ListConverter import ListConverter

app = Flask(__name__, template_folder='../frontend/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///insurance_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'JFKLDSUIORU#@!(*#(FDSJK'
app.url_map.converters['list'] = ListConverter
db = SQLAlchemy(app)
