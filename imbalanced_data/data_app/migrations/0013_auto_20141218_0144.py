# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0012_analysis_ignore_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testoutput',
            name='analysis',
            field=models.ForeignKey(default=37, blank=True, to='data_app.Analysis'),
            preserve_default=False,
        ),
    ]
