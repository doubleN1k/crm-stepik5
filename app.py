from flask import Flask

from forms import LoginForm, RegistrationForm, ChangePassordForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from models import db, User

from views import *


if __name__ == '__main__':
    app.run()