# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0004_auto_20141206_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='testoutput',
            name='precision_graph',
            field=models.ImageField(default=b'', upload_to=b'outputs', blank=True),
            preserve_default=True,
        ),
    ]
