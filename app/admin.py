from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import User, Group, Applicant
print('admin')

class GroupModelView(ModelView):
    column_labels = dict(title='Название', status='Статус', course='Предмет', date_start='Старт',
                         amount_student='Набрано', max_student='Макс.человек', applicant='Заявки')
    form_choices = {
        'status': [
            ('Идет набор', 'Идет набор'),
            ('Набор закрыт', 'Набор закрыт')
        ]
    }


class ApplicantModelView(ModelView):
    column_labels = dict(name_std='Имя', tel_number_std='Телефон', email='Почта', course='Курс', status='Статус',
                         group='Группа')
    column_list = ('name_std', 'tel_number_std', 'email', 'course', 'status', 'group')
    form_choices = {
        'status': [
            ('Новая', 'Новая'),
            ('Ждет оплаты', 'Ждет оплаты'),
            ('Распределена', 'Распределена')
        ]
    }
    list_template = '/admin/add_mail_action.html'


class DashboardView(AdminIndexView):
    @expose()
    def dashboard_view(self):
        group_rows = db.session.query(Group).order_by(Group.id.desc()).limit(5)
        applicant_rows = db.session.query(Applicant).filter(Applicant.status == 'Новая').all()
        applicant_stat = {'distributed': db.session.query(Applicant).filter(Applicant.status == 'Распределена').count(),
                          'unpaid': db.session.query(Applicant).filter(Applicant.status == 'Ждет оплаты').count(),
                          'new': len(applicant_rows)}
        group_dashboard, applicant_dashboard = dict(), dict()
        for group in group_rows:
            group_dashboard[group.id] = {'title': group.title, 'amount_student': group.amount_student,
                                         'max_student': group.max_student}
        for applicant in applicant_rows:
            applicant_dashboard[applicant.id] = {'group_title': applicant.group_title, 'name_std': applicant.name_std}
        return self.render('admin/admin_dashboard.html', group_dashboard=group_dashboard,
                           applicant_dashboard=applicant_dashboard, applicant_stat=applicant_stat)


class EditMailView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/admin_mail_edit.html')


admin = Admin(app, index_view=DashboardView(), template_mode='bootstrap3', name='STEP-CRM')

admin.add_view(EditMailView(name='Рассылка', endpoint='sent_mail'))
admin.add_view(ApplicantModelView(Applicant, db.session, name='Заявки'))
admin.add_view(GroupModelView(Group, db.session, name='Группы'))
admin.add_view(ModelView(User, db.session, name='Пользователи'))
