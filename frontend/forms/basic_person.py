from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import Length


class BasicPersonForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=30)])
    middle_name = StringField('Middle Name', validators=[Length(max=30)])
    last_name = StringField('Last Name', validators=[Length(max=30)])
    address = StringField('Address', validators=[Length(max=70)])
    birth_date = DateField('Birth date')
    is_prospect = BooleanField('Is Prospect')
    submit = SubmitField('Save')
