from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, Optional, NumberRange


class GetBasicPersonForm(FlaskForm):
    prefix = StringField('Prefix', validators=[Length(max=10)])
    first_name = StringField('First Name', validators=[Length(max=30)])
    middle_name = StringField('Middle Name', validators=[Length(max=30)])
    last_name = StringField('Last Name', validators=[Length(max=30)])
    suffix = StringField('Suffix', validators=[Length(max=20)])
    address = StringField('Address', validators=[Length(max=70)])
    mailing_address = StringField('Mailing Address (if different)', validators=[Length(max=30)])
    birth_date = DateField('Birth date', validators=[Optional()])
    is_prospect = BooleanField('Is Prospect')
    social_security = IntegerField('Social Security Number', validators=[NumberRange(min=100000000, max=999999999), Optional()])
    height = DecimalField('Height', validators=[NumberRange(min=0, max=9999), Optional()])
    weight = DecimalField('Weight', validators=[NumberRange(min=0, max=9999), Optional()])
    can_use_credit_score = BooleanField('Can Use Credit Score')
    update_btn = SubmitField('Update')
    delete = SubmitField('Delete')
