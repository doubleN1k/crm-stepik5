import re
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

def password_check(form, field):
    pass

class LoginForm(FlaskForm):
    pass

class RegistrationForm(FlaskForm):
    pass

class ChangePassordForm(FlaskForm):
    pass
