# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0009_auto_20141215_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='testoutput',
            name='analysis',
            field=models.ForeignKey(to='data_app.Analysis', null=True),
            preserve_default=True,
        ),
    ]
