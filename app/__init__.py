from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
mail = Mail(app)

from app import models, routes, forms, admin
