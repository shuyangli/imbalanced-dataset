# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0014_auto_20141218_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='ignore_first',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='pos_label',
            field=models.IntegerField(default=4, blank=True),
            preserve_default=True,
        ),
    ]
