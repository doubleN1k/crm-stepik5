from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from app import app
from models import db, User, Group, Applicant


class GroupModelView(ModelView):
    column_labels = dict(title='Название', status='Статус', course='Предмет', date_start='Старт',
                         amount_student='Набрано', max_student='Макс.человек', applicant='Заявки')


class ApplicantModelView(ModelView):
    column_labels = dict(name_std='Имя', tel_number_std='Телефон', email='Почта', course='Курс', status='Статус',
                         group='Группа')
    column_list = ('name_std', 'tel_number_std', 'email', 'course', 'status', 'group')


class DashboardView(AdminIndexView):
    @expose()
    def dashboard_view(self):
        group_rows = db.session.query(Group).limit(3)
        group_dashboard = {}
        for group in group_rows:
            group_dashboard[group.id]={'title': group.title},
        return self.render('admin/admin_dashboard.html')


admin = Admin(app, index_view=DashboardView(), template_mode='bootstrap3')

admin.add_view(ApplicantModelView(Applicant, db.session, name='Заявки'))
admin.add_view(GroupModelView(Group, db.session, name='Группы'))
admin.add_view(ModelView(User, db.session, name='Пользователи'))
