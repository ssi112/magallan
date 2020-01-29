"""
forms.py
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class SignupForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign me up!')

