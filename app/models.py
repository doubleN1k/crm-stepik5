from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


@login.user_loader
def load_user(id):
    return db.session.query(User).get(id)

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    login = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise AttributeError("Вам не нужно знать пароль!")

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
    date_start = db.Column(db.DateTime, nullable=True)
    amount_student = db.Column(db.Integer, nullable=False)
    max_student = db.Column(db.Integer, nullable=False)
    applicant = db.relationship('Applicant', back_populates='group')

    def __repr__(self):
        return '{}'.format(self.title)


class Applicant(db.Model):
    __tablename__ = 'Applicant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_std = db.Column(db.String(200), nullable=False)
    tel_number_std = db.Column(db.String, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String, nullable=False)
    group_title = db.Column(db.Integer, db.ForeignKey('Group.title'))
    group = db.relationship('Group', back_populates='applicant')

    def __repr__(self):
        return '{}'.format(self.group_title)


# db.create_all()
if __name__ == '__main__':
    db.create_all()
    user1 = User(name='Nik', login='admin', email='bloodyn1k@yandex.ru', password='1234')
    # user2 = User(name='Max', login='moder', email='bloodyn1k@yandex.com', password_hash='789456123')
    db.session.add(user1)
    # db.session.add(user2)
    group1 = Group(title='Основы Python март', status='Идет набор', course='Python', amount_student=8, max_student=10)
    group2 = Group(title='Основы VueJS март', status='Набрано', course='VueJS', amount_student=10, max_student=10)
    db.session.add(group1)
    db.session.add(group2)
    db.session.commit()
    applicant1 = Applicant(name_std='Вася Курочкина', tel_number_std='+797847227', email='bloodyn1k@yandex.com',
                           course='Python', status='Новая', group_title='Основы Python март')
    applicant2 = Applicant(name_std='Оля Буравкина', tel_number_std='+797844527', email='bloodyn1k@yandex.com',
                           course='VueJS', status='Распределена', group_title='Основы VueJS март')
    db.session.add(applicant1)
    db.session.add(applicant2)
    db.session.commit()
