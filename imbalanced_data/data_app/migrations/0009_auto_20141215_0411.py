# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0008_auto_20141215_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='has_headers',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='pos_label',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analysis',
            name='classifiers',
            field=models.ManyToManyField(to='data_app.Classifier', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analysis',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analysis',
            name='title',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
