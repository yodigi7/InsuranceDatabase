from flask import render_template, flash, redirect, url_for, request

from database.Person import Person

from database.flask_db import app
from frontend.forms.add_basic_person import AddBasicPersonForm
from frontend.forms.get_person import GetBasicPersonForm
from frontend.forms.search_person import SearchPersonForm


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


@app.route('/find-people/<list:unique_ids>')
def find_people(unique_ids: list):
    persons = list(Person.query.filter(Person.unique_id.in_(unique_ids)))
    return render_template('find_people_results.html', title='All People', persons=persons)


@app.route('/search-person', methods=['GET', 'POST'])
def search_person():
    form = SearchPersonForm()
    if request.method == 'POST':
        pass
    return render_template('search_person.html', title='Search Person', form=form)


@app.route('/get-person/<int:unique_id>', methods=['GET', 'POST'])
def get_person(unique_id):
    person = Person.query.get_or_404(unique_id)
    form = GetBasicPersonForm(obj=person)
    form.first_name.default = person.first_name
    if 'update' in request.form and form.validate_on_submit():
        form.populate_obj(person)
        person.update()
        flash('Person updated', 'success')
    elif 'delete' in request.form:
        person.delete()
        flash('Person deleted', 'success')
        return redirect(url_for('all_people'))
    elif form.is_submitted():
        for item in form.errors.items():
            flash(item, 'danger')
    return find_people([1, 2, 3])
    # return render_template('get_person.html', title='Get Person {}'.format(unique_id), person=person, form=form)


@app.route('/add-basic-person', methods=['GET', 'POST'])
def add_basic_person():
    form = AddBasicPersonForm()
    if form.validate_on_submit():
        Person(prefix=form.prefix.data,
               first_name=form.first_name.data,
               middle_name=form.middle_name.data,
               last_name=form.last_name.data,
               suffix=form.suffix.data,
               address=form.address.data,
               mailing_address=form.mailing_address.data,
               birth_date=form.birth_date.data,
               is_prospect=form.is_prospect.data).add()
        flash('Person saved', 'success')
        return redirect(url_for('all_people'))
    elif request.method == 'POST':
        for item in form.errors.items():
            flash(item, 'danger')
            return redirect(url_for('add_basic_person'))
    return render_template('add_basic_person.html', title='Adding a Person', form=form)


if __name__ == '__main__':
    pass
