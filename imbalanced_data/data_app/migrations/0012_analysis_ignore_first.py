# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0011_auto_20141216_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='ignore_first',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
