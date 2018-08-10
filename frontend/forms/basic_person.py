from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, Optional


class BasicPersonForm(FlaskForm):
    first_name = StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')
    address = StringField('Address')
    birth_date = DateField('Birth date', validators=[Optional()])
    is_prospect = BooleanField('Is Prospect')
    submit = SubmitField('Save')
