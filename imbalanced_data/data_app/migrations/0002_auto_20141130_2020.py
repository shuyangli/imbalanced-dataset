# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataClassifier',
            new_name='Classifier',
        ),
        migrations.RenameField(
            model_name='analysis',
            old_name='data_classifiers',
            new_name='classifiers',
        ),
    ]
