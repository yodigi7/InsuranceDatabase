from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class SearchGeneralPersonForm(FlaskForm):
    input = StringField('', validators=[Length(max=70)])
    search = SubmitField('Search')


if __name__ == '__main__':
    pass
