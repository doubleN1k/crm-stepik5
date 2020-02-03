import os

current_path = os.path.dirname(os.path.realpath(__file__))
db_path = f'sqlite:///{current_path}\\database5.db'
print(db_path)

class Config:
    DEBUG = True
    SECRET_KEY = 'qwedsfrwer'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False