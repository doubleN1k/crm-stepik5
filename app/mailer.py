from app import app, mail
from flask_mail import Message


def send_mail(subject, recipients, text_body):
    with app.app_context():
        msg = Message(subject, recipients, sender=recipients[0])
        msg.body = text_body
        mail.send(msg)