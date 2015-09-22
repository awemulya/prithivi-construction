# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0004_auto_20150922_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='rows',
            name='progress_status',
            field=models.CharField(choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], default='started', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='progress_status',
            field=models.CharField(choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], default='started', max_length=50),
        ),
    ]
