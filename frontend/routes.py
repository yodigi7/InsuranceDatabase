from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import or_
from sqlalchemy.orm import load_only

from database.Person import Person
from database.Person_Driving import PersonDrivingAccident

from database.flask_db import app
from frontend.forms.add_basic_person import AddBasicPersonForm
from frontend.forms.add_person import AddPersonForm
from frontend.forms.get_person import GetBasicPersonForm
from frontend.forms.search_general_person import SearchGeneralPersonForm
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
    return render_template('find_people_results.html', title='All People', persons=persons)


@app.route('/find-people/<list:unique_ids>')
def find_people(unique_ids: list):
    persons = list(Person.query.filter(Person.unique_id.in_(unique_ids)))
    return render_template('find_people_results.html', title='All People', persons=persons)


@app.route('/search-general-person', methods=['GET', 'POST'])
def search_general():
    form = SearchGeneralPersonForm()
    if request.method == 'POST':
        print(form.input.data)
        return redirect(url_for('find_people', unique_ids=get_general_people_like(form.input.data)))


@app.route('/search-person', methods=['GET', 'POST'])
def search_person():
    form = SearchPersonForm()
    if request.method == 'POST':
        if not form.prefix.data and not form.first_name.data and not form.middle_name.data and \
                not form.last_name.data and not form.suffix.data and not form.address.data and \
                not form.mailing_address.data and not form.is_prospect.data and not form.birth_date.data:
            print('To all people')
            return redirect(url_for('all_people'))
        else:
            unique_ids = [x.unique_id for x in get_people_like(form)]
            # print(unique_ids)
            if unique_ids:
                return redirect(url_for('find_people', unique_ids=unique_ids))
            else:
                flash("Sorry there were no people found like that", 'warning')
    return render_template('search_person.html', title='Search Person', form=form)


@app.route('/get-person/<int:unique_id>', methods=['GET', 'POST'])
def get_person(unique_id):
    person = Person.query.get_or_404(unique_id)
    form = GetBasicPersonForm(obj=person)
    form.first_name.default = person.first_name
    if 'update_btn' in request.form and form.validate_on_submit():
        form.populate_obj(person)
        person.update()
        print("updated")
        flash('Person updated', 'success')
    elif 'delete' in request.form:
        person.delete()
        flash('Person deleted', 'success')
        return redirect(url_for('all_people'))
    elif form.is_submitted():
        print('error')
        for item in form.errors.items():
            flash(item, 'danger')
    return render_template('get_person.html', title='Get Person {}'.format(unique_id), person=person, form=form)


@app.route('/add-person', methods=['GET', 'POST'])
def add_person():
    form = AddPersonForm()
    if form.validate_on_submit():
        Person(prefix=form.prefix.data,
               first_name=form.first_name.data,
               middle_name=form.middle_name.data,
               last_name=form.last_name.data,
               suffix=form.suffix.data,
               address=form.address.data,
               mailing_address=form.mailing_address.data,
               birth_date=form.birth_date.data,
               is_prospect=form.is_prospect.data,
               social_security_number=form.social_security.data,
               height=str(form.height.data),
               weight=str(form.weight.data),
               can_use_credit_score=form.can_use_credit_score.data).add()
        flash('Person saved', 'success')
        return redirect(url_for('all_people'))
    elif request.method == 'POST':
        for item in form.errors.items():
            flash(item, 'danger')
            return redirect(url_for('add_person'))
    return render_template('add_person.html', title='Adding a Person', form=form)


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


def get_general_people_like(inp: str) -> list:
    return [x.unique_id for x in Person.query.filter(or_(Person.prefix.ilike('%{}%'.format(inp)),
                                                         Person.first_name.ilike('%{}%'.format(inp)),
                                                         Person.middle_name.ilike('%{}%'.format(inp)),
                                                         Person.last_name.ilike('%{}%'.format(inp)),
                                                         Person.suffix.ilike('%{}%'.format(inp)),
                                                         Person.address.ilike('%{}%'.format(inp)),
                                                         Person.mailing_address.ilike('%{}%'.format(inp)),
                                                         Person.birth_date.ilike('%{}%'.format(inp)),
                                                         Person.height.ilike('%{}%'.format(inp)),
                                                         Person.weight.ilike('%{}%'.format(inp)),
                                                         Person.social_security_number.ilike(
                                                             '%{}%'.format(inp)))).all()]


def get_people_like(form) -> list:
    query = Person.query
    if form.prefix.data:
        query = query.filter(Person.prefix.ilike('%{}%'.format(form.prefix.data)))
    if form.first_name.data:
        query = query.filter(Person.first_name.ilike('%{}%'.format(form.first_name.data)))
    if form.middle_name.data:
        query = query.filter(Person.middle_name.ilike('%{}%'.format(form.middle_name.data)))
    if form.last_name.data:
        query = query.filter(Person.last_name.ilike('%{}%'.format(form.last_name.data)))
    if form.suffix.data:
        query = query.filter(Person.suffix.ilike('%{}%'.format(form.suffix.data)))
    if form.address.data:
        query = query.filter(Person.address.ilike('%{}%'.format(form.address.data)))
    if form.mailing_address.data:
        query = query.filter(Person.mailing_address.ilike('%{}%'.format(form.mailing_address.data)))
    if form.birth_date.data:
        query = query.filter(Person.birth_date.ilike('%{}%'.format(form.birth_date.data)))
    if form.is_prospect.data:
        query = query.filter(Person.is_prospect == form.is_prospect.data)
    return query.all()


if __name__ == '__main__':
    pass
