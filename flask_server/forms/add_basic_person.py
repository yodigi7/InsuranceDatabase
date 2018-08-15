from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, Optional


class AddBasicPersonForm(FlaskForm):
    prefix = StringField('Prefix', validators=[Length(max=10)])
    first_name = StringField('First Name', validators=[Length(max=30)])
    middle_name = StringField('Middle Name', validators=[Length(max=30)])
    last_name = StringField('Last Name', validators=[Length(max=30)])
    suffix = StringField('Suffix', validators=[Length(max=20)])
    address = StringField('Address', validators=[Length(max=70)])
    mailing_address = StringField('Mailing Address (if different)', validators=[Length(max=70)])
    birth_date = DateField('Birth date', validators=[Optional()])
    is_prospect = BooleanField('Is Prospect')
    submit = SubmitField('Save')


if __name__ == '__main__':
    pass
