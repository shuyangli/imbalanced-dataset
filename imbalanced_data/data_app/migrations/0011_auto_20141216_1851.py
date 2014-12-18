# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0010_testoutput_analysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='has_header',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='analysis',
            name='pos_label',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
