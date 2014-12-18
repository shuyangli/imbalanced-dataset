# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0013_auto_20141218_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='has_header',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='ignore_first',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='analysis',
            field=models.ForeignKey(related_name='test_outputs', blank=True, to='data_app.Analysis'),
            preserve_default=True,
        ),
    ]
