from celery import shared_task
from django.core.mail import send_mail
import os


@shared_task()
def send_email_task(subject, content, sender, recipients):
    send_mail(subject, content, sender, recipients)
    return "Email sent"


@shared_task()
def delete_blacklisted_tokens_task():
    os.system('python3 manage.py flushexpiredtokens')
