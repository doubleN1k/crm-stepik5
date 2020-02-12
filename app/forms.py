from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
print('forms')

class MailForm(FlaskForm):
    mail = StringField('e-mail', validators=[DataRequired(), Email()])
    subject = StringField('Тема', validators=[DataRequired()])
    text = TextAreaField('Текст письма', validators=[DataRequired()])
    submit = SubmitField('Отправить')


def password_check(form, field):
    pass


class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    pass


class ChangePassordForm(FlaskForm):
    pass
