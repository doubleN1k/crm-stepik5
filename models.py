from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from datetime import datetime
db = SQLAlchemy(app)


Group_Applicant = db.Table('Group_Applicant',
                      db.Column('group_id', db.Integer, db.ForeignKey('Group.id')),
                      db.Column('applicant_id', db.Integer, db.ForeignKey('Applicant.id'))
                      )

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    login = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200),nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Group(db.Model):
    __tablename__ = 'Group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String, nullable=False)
    course = db.Column(db.String, nullable=False)
    date_start = db.Column(db.String(10), nullable=False)
    amount_student = db.Column(db.Integer, nullable=False)
    max_student = db.Column(db.Integer, nullable=False)
    applicant = db.relationship('Applicant', secondary=Group_Applicant, back_populates='group')

class Applicant(db.Model):
    __tablename__ = 'Applicant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_std = db.Column(db.String(200), nullable=False)
    tel_number_std = db.Column(db.String, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    group = db.relationship('Group', secondary=Group_Applicant, back_populates='applicant')

db.create_all()
user1 = User(name='Nik', login='admin', email='bloodyn1k@yandex.ru', password_hash='123456789')
db.session.add(user1)
group1 = Group(title='VueJS март', status='Набрана', course='VueJS', date_start='01.03.2020', amount_student=10, max_student=10)
db.session.add(group1)
applicant1 = Applicant(name_std='Оля Бабушкина', tel_number_std='+797845127', email='bloodyn1k@yandex.ru', course='VueJS', status='Распределена')
db.session.add(applicant1)
db.session.commit()


