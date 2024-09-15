# INCREMENTAL CODE FOR SECTION : 11 LECTURE : 44 - VALIDATING FORMS
# auth/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')