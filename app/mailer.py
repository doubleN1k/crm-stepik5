from app import app, mail
from flask_mail import Message


def send_mail(subject, email, text_body):
    with app.app_context():
        sender = app.config.get('MAIL_USERNAME')
        msg = Message(subject=subject, recipients=[email], sender=sender)
        msg.body = text_body
        print(msg)
        mail.send(msg)
