from flask import render_template
from database.flask_db import app
from frontend.forms.basic_person import BasicPersonForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('default.html', title='Home')

@app.route('/add/person')
def add_basic_persion():
    form = BasicPersonForm()
    return render_template('add.html', title='Adding a Person', form=form)
