

from celery import Celery

from config import BROKER

app = Celery("tasks", broker=BROKER, timezone="Europe/London")
