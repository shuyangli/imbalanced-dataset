# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0015_auto_20141218_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='has_headers',
        ),
    ]
