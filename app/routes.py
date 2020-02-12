from flask import redirect, render_template, session
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.forms import LoginForm
from app.models import User


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect('/admin')
    return redirect('login', 301)


@app.route("/login", methods=["GET", "POST"])
def login():
    print(session.get('user'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.query(User).filter_by(email=login_form.mail.data).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            return redirect('/admin')
        else:
            login_form.mail.errors.append("Не верное имя или пароль")
    return render_template('/admin/auth.html', login_form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')