from flask import abort, flash, session, request, redirect, render_template
from app import app
from models import User
from forms import LoginForm, RegistrationForm, ChangePassordForm


# ------------------------------------------------------
# Декораторы авторизации
def login_required(f):
    pass
    #(код декоратора)


def admin_only(f):
    pass
    #(код декоратора)


# ------------------------------------------------------
# Страница админки
@app.route('/')
#@login_required
def home():
    return 'home', 200
    #(код страницы админки)


# ------------------------------------------------------
# Страница аутентификации
@app.route("/login", methods=["GET", "POST"])
def login():
    return 'login', 200
    #(код страницы аутентификации)


# ------------------------------------------------------
# Страница выхода из админки
@app.route('/logout', methods=["POST"])
#@login_required
def logout():
    return 'logout', 200
    #(код выхода из админки)


# ------------------------------------------------------
# Страница добавления пользователя
@app.route("/registration", methods=["GET", "POST"])
#@admin_only
#@login_required
def registration():
    return 'registration', 200
    #(код страницы регистрации)


# ------------------------------------------------------
# Страница смены пароля
@app.route("/change-password", methods=["GET", "POST"])
#@login_required
def change_password():
    return 'change_password', 200
    #(код страницы смены пароля)