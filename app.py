from flask import Flask
print(1)
from forms import LoginForm, RegistrationForm, ChangePassordForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from models import db
from admin import admin
from migrate import migrate
from views import *


'''if __name__ == '__main__':
    app.run()'''
