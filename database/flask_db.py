from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../frontend/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///insurance_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
