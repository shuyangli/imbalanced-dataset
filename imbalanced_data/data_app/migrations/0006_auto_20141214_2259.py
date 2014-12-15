# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0005_testoutput_precision_graph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifier',
            name='program_file',
        ),
        migrations.AddField(
            model_name='analysis',
            name='datasets',
            field=models.ManyToManyField(to='data_app.Dataset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='accuracy_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='average_precision',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='f1_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='precision_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='recall_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='roc_auc',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testoutput',
            name='roc_graph',
            field=models.ImageField(default=b'', upload_to=b'outputs', blank=True),
            preserve_default=True,
        ),
    ]
