# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0003_testoutput'),
    ]

    operations = [
        migrations.AddField(
            model_name='testoutput',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 2, 52, 58, 876965, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 2, 53, 5, 812825, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
