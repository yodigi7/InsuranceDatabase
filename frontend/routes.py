from flask import render_template, flash, redirect, url_for, request

from database.Person import Person
from database.Person_Work import PersonWork

from database.flask_db import app
from frontend.forms.basic_person import BasicPersonForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('default.html', title='Home')


@app.route('/add/person', methods=['GET', 'POST'])
def add_basic_persion():
    form = BasicPersonForm(request.form)
    if form.validate():
        flash('Person saved', 'success')
        print(form.first_name.data)
        Person(unique_id=1, first_name=form.first_name.data).add_to_database()
        return redirect(url_for('home'))
    return render_template('add.html', title='Adding a Person', form=form)


if __name__ == '__main__':
    pass
