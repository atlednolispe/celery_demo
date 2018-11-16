"""
$ celery beat -A celery_app -l INFO
$ celery -A celery_app -l INFO

$ celery -B -A celery_app worker -l INFO
"""
from celery import Celery


app = Celery('demo')
app.config_from_object('celery_app.config')
