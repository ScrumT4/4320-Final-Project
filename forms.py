from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length

class SignForm(FlaskForm):
    username= StringField('Username', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    
    password= StringField('Password', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    
class SeatForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    
    last_name = StringField('Last Name', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    row = RadioField('Row Select',
                       choices=['1', '2', '3','4','5','6','7','8','9','10','11','12'],
                       validators=[InputRequired()])
    seat = RadioField('Row Select',
                       choices=['1', '2', '3','4'],
                       validators=[InputRequired()])
    