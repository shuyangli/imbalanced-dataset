# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0007_auto_20141214_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='datasets',
        ),
        migrations.AddField(
            model_name='analysis',
            name='dataset',
            field=models.ForeignKey(blank=True, to='data_app.Dataset', null=True),
            preserve_default=True,
        ),
    ]
