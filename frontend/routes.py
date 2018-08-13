from math import ceil

import requests
from flask import render_template, flash, redirect, url_for, request, jsonify, json
from sqlalchemy import or_

from database.Person import Person, json_to_person
from database.Person_Driving import json_to_accident, json_to_violation
from database.Person_Notes import json_to_note, PersonNotes
from database.Person_Work import json_to_work
from database.flask_db import app
from frontend.forms.add_basic_person import AddBasicPersonForm
from frontend.forms.add_person import AddPersonForm
from frontend.forms.get_person import GetBasicPersonForm
from frontend.forms.search_general_person import SearchGeneralPersonForm
from frontend.forms.search_person import SearchPersonForm


@app.route('/')
@app.route('/home')
def home():
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
        return redirect(url_for('find_people', unique_ids=get_general_people_like_or(form.input.data)))


@app.route('/search-person', methods=['GET', 'POST'])
def search_person():
    form = SearchPersonForm()
    if request.method == 'POST':
        if not form.prefix.data and not form.first_name.data and not form.middle_name.data and \
                not form.last_name.data and not form.suffix.data and not form.address.data and \
                not form.mailing_address.data and not form.is_prospect.data and not form.birth_date.data:
            return redirect(url_for('all_people'))
        else:
            unique_ids = [x.unique_id for x in get_people_like_and(form)]
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
        flash('Person updated', 'success')
    elif 'delete' in request.form:
        person.delete()
        flash('Person deleted', 'success')
        return redirect(url_for('all_people'))
    elif form.is_submitted():
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
               height=form.height.data,
               weight=form.weight.data,
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


@app.route('/api/person-driving-accident', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_person_driving_accident():
    if request.method == 'POST':
        input_json = request.get_json()
        person_driving_accident = json_to_accident(input_json)
        if 'unique_id' in input_json:
            person_driving_accident.person_id = input_json.get('person_id')
            person_driving_accident.paid_by = input_json.get('paid_by')
            person_driving_accident.description = input_json.get('description')
            person_driving_accident.injuries = input_json.get('injuries')
            person_driving_accident.percent_fault = input_json.get('percent_fault')
            person_driving_accident.date_occurred = input_json.get('date_occurred')
            person_driving_accident.update()
        return jsonify({'success': True})


@app.route('/api/person-notes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_person_notes():
    if request.method == 'POST':
        input_json = request.get_json()
        person_note = json_to_note(input_json)
        if 'unique_id' in input_json:
            person_note.person_id = input_json.get('person_id')
            person_note.paid_by = input_json.get('paid_by')
            person_note.description = input_json.get('description')
            person_note.injuries = input_json.get('injuries')
            person_note.percent_fault = input_json.get('percent_fault')
            person_note.date_occurred = input_json.get('date_occurred')
            person_note.update()
        return jsonify({'success': True})


@app.route('/api/person-notes/<int:person_id>', methods=['GET', 'DELETE'])
def delete_api_person_notes(person_id):
    person = PersonNotes.query.filter(PersonNotes.person_id == person_id).one()
    if request.method == 'DELETE':
        person.delete()
        return jsonify({'success': True})
    if request.method == 'GET':
        return jsonify(person.to_json())


@app.route('/api/person-work', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_person_work():
    if request.method == 'POST':
        input_json = request.get_json()
        person_work = json_to_work(input_json)
        if 'unique_id' in input_json:
            person_work.person_id = input_json.get('person_id')
            person_work.paid_by = input_json.get('paid_by')
            person_work.description = input_json.get('description')
            person_work.injuries = input_json.get('injuries')
            person_work.percent_fault = input_json.get('percent_fault')
            person_work.date_occurred = input_json.get('date_occurred')
            person_work.update()
            return jsonify({'success': True})


@app.route('/api/person-driving-violation', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_person_driving_violation():
    if request.method == 'POST':
        input_json = request.get_json()
        person_driving_violation = json_to_violation(input_json)
        if 'unique_id' in input_json:
            person_driving_violation.person_id = input_json.get('person_id')
            person_driving_violation.paid_by = input_json.get('paid_by')
            person_driving_violation.description = input_json.get('description')
            person_driving_violation.injuries = input_json.get('injuries')
            person_driving_violation.percent_fault = input_json.get('percent_fault')
            person_driving_violation.date_occurred = input_json.get('date_occurred')
            person_driving_violation.update()
        return jsonify({'success': True})


@app.route('/api/person', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_person():
    if request.method == 'POST':
        print(request.get_json())
        input_json = request.get_json()
        person = json_to_person(input_json)
        if 'unique_id' in input_json:
            person.prefix = input_json.get('prefix')
            person.first_name = input_json.get('first_name')
            person.middle_name = input_json.get('middle_name')
            person.last_name = input_json.get('last_name')
            person.suffix = input_json.get('suffix')
            person.address = input_json.get('address')
            person.mailing_address = input_json.get('mailing_address')
            person.birth_date = input_json.get('birth_date')
            person.height = input_json.get('height')
            person.weight = input_json.get('weight')
            person.is_prospect = input_json.get('is_prospect')
            person.social_security_number = input_json.get('social_security_number')
            person.can_use_credit_score = input_json.get('can_use_credit_score')
            person.update()
            if input_json.get('driving_accidents'):
                for driving_accident in input_json['driving_accidents'].values():
                    requests.post('/api/person-driving-accident', json=jsonify(driving_accident))
            if input_json.get('driving_violations'):
                for driving_violation in input_json['driving_violations'].values():
                    requests.post('/api/person-driving-violation', json=jsonify(driving_violation))
            if input_json.get('note'):
                requests.post('/api/person-note', json=jsonify(input_json['note'][0]))
            if input_json.get('work'):
                requests.post('/api/person-work', json=jsonify(input_json['work'][0]))
        return jsonify({'success': True})
    elif request.method == 'GET':
        page = 1
        everyone = Person.query
        total_pages = ceil(everyone.count()/20)
        if 'page' in request.args:
            page = int(request.args['page'])
        return_people = {
            'people': [x.to_json() for x in everyone.paginate(page, 20, False).items],
            'pages': total_pages
        }
        return jsonify(return_people)


def get_general_people_like_or(inp: str) -> list:
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


def get_people_like_and(form) -> list:
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
