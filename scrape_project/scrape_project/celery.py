import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrape_project.settings')

app = Celery('scrape_project', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'scrape_remaining': {
        'task': 'scraper.tasks.scrape_remaining_articles',
        'schedule': 60*60*1,
    },
    'scrape_daily': {
        'task': 'scraper.tasks.scrape_remaining_articles',
        'schedule': 60*60*24,
    },
}


# Load task modules from all registered Django apps
app.autodiscover_tasks()


# celery -A scrape_project worker --loglevel=info
# celery -A scrape_project beat --loglevel=info

