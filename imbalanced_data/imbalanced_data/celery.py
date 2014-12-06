from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imbalanced_data.settings')

app = Celery('imbalanced_data')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#@app.task(bind=True)
#def debug_task(self):
  #print('')
#  pass