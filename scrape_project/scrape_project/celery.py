import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrape_project.settings')

app = Celery('scrape_project', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
#     'every_60_seconds_scrape_remaining_articles': {
#         'task': 'techchurch.tasks.scrape_remaining_articles',
#         'schedule': 60,
#     },
# }

# Load task modules from all registered Django apps
app.autodiscover_tasks()

# celery -A scrape_project worker -l INFO -P eventlet
# celery -A scrape_project beat --loglevel=INFO
