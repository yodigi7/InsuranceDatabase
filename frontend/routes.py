from flask import render_template, flash, redirect, url_for, request

from database.Person import Person
from database.Person_Work import PersonWork

from database.flask_db import app
from frontend.forms.add_basic_person import AddBasicPersonForm
from frontend.forms.get_person import GetBasicPersonForm


@app.route('/')
@app.route('/home')
def home():
    if request.args:
        print(request.args)
    return render_template('default.html', title='Home')


@app.route('/all-people')
def all_people():
    persons = list(Person.query.all())
    return render_template('all_people_results.html', title='All People', persons=persons)


@app.route('/search-person')
def search_person():
    persons = list(Person.query.all())
    return render_template('search_person.html', title='Search Person', persons=persons)


@app.route('/get-person/<int:unique_id>', methods=['GET', 'POST'])
def get_person(unique_id):
    person = Person.query.get_or_404(unique_id)
    form = GetBasicPersonForm()
    form.first_name.default = person.first_name
    print(request.form)
    if 'update' in request.form:
        person.first_name = form.first_name.data
        person.middle_name = form.middle_name.data
        person.last_name = form.last_name.data
        person.address = form.address.data
        person.mailing_address = form.mailing_address.data
        person.birth_date = form.birth_date.data
        person.is_prospect = form.is_prospect.data
        person.update()
        flash('Person updated', 'success')
    if 'delete' in request.form:
        person.delete()
        flash('Person deleted', 'success')
        return redirect(url_for('find_person'))
    return render_template('get_person.html', title='Get Person {}'.format(unique_id), person=person, form=form)


@app.route('/add-basic-person', methods=['GET', 'POST'])
def add_basic_person():
    form = AddBasicPersonForm()
    if form.validate_on_submit():
        Person(first_name=form.first_name.data,
               middle_name=form.middle_name.data,
               last_name=form.last_name.data,
               address=form.address.data,
               mailing_address=form.mailing_address.data,
               birth_date=form.birth_date.data,
               is_prospect=form.is_prospect.data).add()
        flash('Person saved', 'success')
        return redirect(url_for('find_person'))
    elif request.method == 'POST':
        for item in form.errors.items():
            flash(item, 'danger')
            return redirect(url_for('add_basic_person'))
    return render_template('add_basic_person.html', title='Adding a Person', form=form)


if __name__ == '__main__':
    pass
