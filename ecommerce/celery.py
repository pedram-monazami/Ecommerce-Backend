from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

app = Celery('ecommerce')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'delete_blacklisted_tokens': {
        'task': 'landing.tasks.delete_blacklisted_tokens_task',
        'schedule': crontab(hour='13', minute='48'),
    }
}

app.autodiscover_tasks()
