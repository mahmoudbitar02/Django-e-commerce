import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')


app.config_from_object('django.conf:settings')

app.autodiscover_tasks()  ## (settings.INSTALLED_APPS)
