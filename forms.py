"""
forms.py

In order for the custom validator messages to display, it is necessary with newer
version to add the novalidate option on the actual form.

In signup.html it would look like this:
    <form method = "POST" action = "/signup" novalidate>
Otherwise standard error messages will apply.

Reference:
https://stackoverflow.com/questions/50787904/how-to-override-the-html-default-please-fill-out-this-field-when-validation-fa

Though it appears latest version is to use InputRequired
https://stackoverflow.com/questions/23982917/flask-wtforms-difference-between-datarequired-and-inputrequired

WTForms Validator documentation:
https://wtforms.readthedocs.io/en/stable/validators.html
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, InputRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("You must enter your first name!")])
    last_name = StringField('Last Name', validators=[DataRequired()])
    """
    Per documentation: Validates an email address. Note that this uses a very primitive regular expression
    and should only be used in instances where you later verify by other means,
    such as email activation or lookups.
    """
    email = StringField("Email", [InputRequired("Please enter your email address"), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Passwords must be 6 chars or more")])
    submit = SubmitField('Sign me up!')

