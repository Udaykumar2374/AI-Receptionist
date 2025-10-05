import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aiassistant.settings")

app = Celery("aiassistant")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
