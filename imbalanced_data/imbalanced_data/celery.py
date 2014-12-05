from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imbalanced_data.settings')

app = Celery('imbalanced_data', broker='redis://localhost:6379/0')

app.config_from_object('django.conf:settings')
# app.conf.update(
#   CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
# )
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
  #print('')
  pass