from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app
from models import db, User, Group, Applicant
admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Applicant, db.session))

