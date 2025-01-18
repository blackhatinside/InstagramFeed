# InstagramFeed\InstagramFeed\celery.py

import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InstagramFeed.settings')

# Create celery app
app = Celery('InstagramFeed')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()