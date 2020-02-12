from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email


class MailForm(FlaskForm):
    mail = StringField('e-mail', validators=[DataRequired(), Email()])
    subject = StringField('Тема', validators=[DataRequired()])
    text = TextAreaField('Текст письма', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    mail = StringField('e-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    pass


class ChangePassordForm(FlaskForm):
    pass


def password_check(form, field):
    pass
