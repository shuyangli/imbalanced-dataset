# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0016_remove_dataset_has_headers'),
    ]

    operations = [
        migrations.AddField(
            model_name='testoutput',
            name='classifier',
            field=models.ForeignKey(related_name='test_outputs', default=5, blank=True, to='data_app.Classifier'),
            preserve_default=False,
        ),
    ]
