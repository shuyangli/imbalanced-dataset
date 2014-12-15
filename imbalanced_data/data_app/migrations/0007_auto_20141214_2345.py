# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0006_auto_20141214_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testoutput',
            name='roc_auc',
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='accuracy_score',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='average_precision',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='f1_score',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='precision_score',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testoutput',
            name='recall_score',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
