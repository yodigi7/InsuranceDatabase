from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, Optional


class GetBasicPersonForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=30)])
    middle_name = StringField('Middle Name', validators=[Length(max=30)])
    last_name = StringField('Last Name', validators=[Length(max=30)])
    address = StringField('Address', validators=[Length(max=70)])
    mailing_address = StringField('Mailing Address (if different)', validators=[Length(max=30)])
    birth_date = DateField('Birth date', validators=[Optional()])
    is_prospect = BooleanField('Is Prospect')
    save = SubmitField('Save')
    delete = SubmitField('Delete')
