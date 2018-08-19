from math import ceil

import requests
from flask import request, jsonify, render_template
from sqlalchemy import or_

from database.Person import Person, json_to_person
from database.Person_Driving import json_to_accident, json_to_violation, PersonDrivingViolation, PersonDrivingAccident
from database.Person_Notes import json_to_note, PersonNotes
from database.Person_Phones import json_to_phone, PersonPhone
from database.Person_Work import json_to_work, PersonWork
from database.flask_db import app


@app.route('/api/phone', methods=['GET', 'POST'])
def api_person_phones():
    if request.method == 'POST':
        input_json = request.get_json()
        print(input_json)
        json_to_phone(input_json).add()
        return jsonify({'success': True})
    elif request.method == 'GET':
        page = 1
        every = PersonNotes.query
        if 'page' in request.args:
            page = int(request.args['page'])
        return jsonify({
            'phones': [x.to_json() for x in every.paginate(page, 20, False).items],
            'pages': (ceil(every.count() / 20))
        })


@app.route('/api/phone/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_phones_id(unique_id: int):
    person_phone = PersonPhone.query.filter(PersonPhone.unique_id == unique_id).one()
    if request.method == 'DELETE':
        person_phone.delete()
        return jsonify({'success': True})
    elif request.method == 'GET':
        return jsonify(person_phone.to_json())
    elif request.method == 'PUT':
        input_json = request.get_json()
        person_phone.person_id = input_json.get('person_id')
        person_phone.phone_number = input_json.get('phoneNumber')
        person_phone.type = input_json.get('type')
        return jsonify({'success': True})


@app.route('/api/phones-by-person/<int:unique_id>', methods=['GET'])
def api_person_phones_by_person_id(unique_id: int):
    phones = PersonPhone.query.filter(PersonPhone.person_id == unique_id).all()
    if request.method == 'GET':
        phones = [x.to_json() for x in phones]
        return jsonify({'phones': phones})


@app.route('/api/notes', methods=['GET', 'POST'])
def api_person_notes():
    if request.method == 'POST':
        input_json = request.get_json()
        json_to_note(input_json).add()
        return jsonify({'success': True})
    elif request.method == 'GET':
        page = 1
        every = PersonNotes.query
        if 'page' in request.args:
            page = int(request.args['page'])
        return jsonify({
            'notes': [x.to_json() for x in every.paginate(page, 20, False).items],
            'pages': (ceil(every.count() / 20))
        })


@app.route('/api/notes/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_notes_id(unique_id: int):
    person_note = PersonNotes.query.filter(PersonNotes.unique_id == unique_id).one()
    if request.method == 'DELETE':
        person_note.delete()
        return jsonify({'success': True})
    elif request.method == 'GET':
        return jsonify(person_note.to_json())
    elif request.method == 'PUT':
        input_json = request.get_json()
        person_note.person_id = input_json.get('person_id')
        person_note.paid_by = input_json.get('paid_by')
        person_note.description = input_json.get('description')
        person_note.injuries = input_json.get('injuries')
        person_note.percent_fault = input_json.get('percent_fault')
        person_note.date_occurred = input_json.get('date_occurred')
        person_note.update()
        return jsonify({'success': True})


@app.route('/api/work', methods=['GET', 'POST'])
def api_person_work():
    if request.method == 'POST':
        input_json = request.get_json()
        json_to_work(input_json).add()
        return jsonify({'success': True})
    elif request.method == 'GET':
        page = 1
        every = PersonWork.query
        if 'page' in request.args:
            page = int(request.args['page'])
        return jsonify({
            'work': [x.to_json() for x in every.paginate(page, 20, False).items],
            'pages': (ceil(every.count() / 20))
        })


@app.route('/api/work/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_work_id(unique_id: int):
    work = PersonWork.query.filter(PersonWork.unique_id == unique_id).one()
    if request.method == 'DELETE':
        work.delete()
        return jsonify({'success': True})
    elif request.method == 'GET':
        return jsonify(work.to_json())
    elif request.method == 'PUT':
        input_json = request.get_json()
        work.occupation = input_json.get('occupation')
        work.occupation_start = input_json.get('occupation_start')
        work.employer = input_json.get('employer')
        work.employer_start = input_json.get('employer_start')
        work.level_of_education = input_json.get('level_of_education')
        work.update()
        return jsonify({'success': True})


@app.route('/api/driving-accident', methods=['GET', 'POST'])
def api_person_driving_accident():
    if request.method == 'POST':
        json_to_accident(request.get_json()).add()
        return jsonify({'success': True})
    if request.method == 'GET':
        every = PersonDrivingAccident.query
        page = 1
        if 'page' in request.headers.keys():
            page = request.headers['page']
        return_json = {
            'accidents': [x.to_json() for x in every.paginate(page, 20, False).items],
            'pages': (ceil(every.count() / 20))
        }
        return jsonify(return_json)


@app.route('/api/driving-accident/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_driving_accident_id(unique_id: int):
    driving_accident = PersonDrivingAccident.query.filter(PersonDrivingAccident.unique_id == unique_id).one()
    if request.method == 'GET':
        return jsonify(driving_accident.to_json())
    elif request.method == 'DELETE':
        driving_accident.delete()
        return jsonify({'success': True})
    elif request.method == 'PUT':
        input_json = request.get_json()
        driving_accident.person_id = input_json.get('person_id')
        driving_accident.paid_by = input_json.get('paid_by')
        driving_accident.description = input_json.get('description')
        driving_accident.injuries = input_json.get('injuries')
        driving_accident.percent_fault = input_json.get('percent_fault')
        driving_accident.date_occurred = input_json.get('date_occurred')
        driving_accident.update()
        return jsonify({'success': True})


@app.route('/api/driving-violation', methods=['GET', 'POST'])
def api_person_driving_violation():
    if request.method == 'POST':
        json_to_violation(request.get_json()).add()
        return jsonify({'success': True})
    if request.method == 'GET':
        page = 1
        every = PersonDrivingViolation.query
        if 'page' in request.args:
            page = int(request.args['page'])
        return jsonify({
            'violations': [x.to_json() for x in every.paginate(page, 20, False).items],
            'pages': (ceil(every.count() / 20))
        })


@app.route('/api/driving-violation/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_driving_violation_id(unique_id: int):
    driving_violation = PersonDrivingViolation.query.filter(PersonDrivingViolation.unique_id == unique_id).one()
    if request.method == 'GET':
        return jsonify(driving_violation.to_json())
    elif request.method == 'DELETE':
        driving_violation.delete()
        return jsonify({'success': True})
    elif request.method == 'PUT':
        input_json = request.get_json()
        driving_violation.person_id = input_json.get('person_id')
        driving_violation.paid_by = input_json.get('paid_by')
        driving_violation.description = input_json.get('description')
        driving_violation.injuries = input_json.get('injuries')
        driving_violation.percent_fault = input_json.get('percent_fault')
        driving_violation.date_occurred = input_json.get('date_occurred')
        driving_violation.update()
        return jsonify({'success': True})


@app.route('/api/person', methods=['GET', 'POST'])
def api_person():
    if request.method == 'POST':
        print(request.get_json()['birthDate'])
        input_json = request.get_json()
        person = json_to_person(input_json)
        person.add()
        print(person)
        return jsonify({'success': True, 'unique_id': person.unique_id})
    elif request.method == 'GET':
        page = 1
        everyone = Person.query
        if 'page' in request.headers:
            page = int(request.headers['page'])
        return jsonify({
            'people': [x.to_json() for x in everyone.paginate(page, 20, False).items],
            'pages': (ceil(everyone.count() / 20))
        })


@app.route('/api/person/<int:unique_id>', methods=['GET', 'PUT', 'DELETE'])
def api_person_id(unique_id: int):
    person = Person.query.filter(Person.unique_id == unique_id).one()
    if request.method == 'PUT':
        input_json = request.get_json()
        print(input_json)
        person.prefix = input_json.get('prefix')
        person.first_name = input_json.get('firstName')
        person.middle_name = input_json.get('middleName')
        person.last_name = input_json.get('lastName')
        person.suffix = input_json.get('suffix')
        person.address = input_json.get('address')
        person.mailing_address = input_json.get('mailingAddress')
        person.birth_date = input_json.get('birthDate')
        person.height = input_json.get('height')
        person.weight = input_json.get('weight')
        person.customer_type = input_json.get('customerType')
        person.social_security_number = input_json.get('socialSecurityNumber')
        person.can_use_credit_score = input_json.get('canUseCreditScore')
        person.update()
        if input_json.get('driving_accidents'):
            for driving_accident in input_json['driving_accidents'].values():
                requests.put('/api/driving-accident/{}'.format(driving_accident['unique_id']),
                             json=jsonify(driving_accident))
        if input_json.get('driving_violations'):
            for driving_violation in input_json['driving_violations'].values():
                requests.put('/api/driving-violation/{}'.format(driving_violation['unique_id']),
                             json=jsonify(driving_violation))
        if input_json.get('note'):
            requests.put('/api/note', json=jsonify(input_json['note'][0]))
        if input_json.get('work'):
            requests.put('/api/work', json=jsonify(input_json['work'][0]))
        return jsonify({'success': True})
    elif request.method == 'GET':
        print(person.to_json()['birth_date'])
        return jsonify(person.to_json())
    elif request.method == 'DELETE':
        person.delete()
        return jsonify({'success': True})


@app.route('/api/search-person', methods=['POST'])
def search_person():
    unique_ids = [x.unique_id for x in get_people_like_and(request.get_json())]
    return jsonify({'ids': unique_ids})


@app.route('/api/search-general-person', methods=['POST'])
def search_general_person():
    print('here')
    print(request.data)
    unique_ids = [x.unique_id for x in get_general_people_like_or(request.get_json()['query'])]
    return jsonify({'ids': unique_ids})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    return render_template('index.html')


def get_general_people_like_or(inp: str) -> list:
    return Person.query.filter(or_(Person.prefix.ilike('%{}%'.format(inp)),
                                   Person.first_name.ilike('%{}%'.format(inp)),
                                   Person.middle_name.ilike('%{}%'.format(inp)),
                                   Person.last_name.ilike('%{}%'.format(inp)),
                                   Person.suffix.ilike('%{}%'.format(inp)),
                                   Person.address.ilike('%{}%'.format(inp)),
                                   Person.mailing_address.ilike('%{}%'.format(inp)),
                                   Person.birth_date.ilike('%{}%'.format(inp)),
                                   Person.height.ilike('%{}%'.format(inp)),
                                   Person.weight.ilike('%{}%'.format(inp)),
                                   Person.social_security_number.ilike('%{}%'.format(inp)))).all()


def get_people_like_and(input_json) -> list:
    query = Person.query
    print(input_json)
    if input_json['prefix']:
        query = query.filter(Person.prefix.ilike('%{}%'.format(input_json['prefix'])))
    if input_json['firstName']:
        query = query.filter(Person.first_name.ilike('%{}%'.format(input_json['firstName'])))
    if input_json['middleName']:
        query = query.filter(Person.middle_name.ilike('%{}%'.format(input_json['middleName'])))
    if input_json['lastName']:
        query = query.filter(Person.last_name.ilike('%{}%'.format(input_json['lastName'])))
    if input_json['suffix']:
        query = query.filter(Person.suffix.ilike('%{}%'.format(input_json['suffix'])))
    if input_json['address']:
        query = query.filter(Person.address.ilike('%{}%'.format(input_json['address'])))
    if input_json['mailingAddress']:
        query = query.filter(Person.mailing_address.ilike('%{}%'.format(input_json['mailingaddress'])))
    if input_json['birthDate']:
        query = query.filter(Person.birth_date.ilike('%{}%'.format(input_json['birthDate'])))
    if input_json['customerType']:
        query = query.filter(Person.is_prospect == input_json['customerType'])
    return query.all()


if __name__ == '__main__':
    pass
