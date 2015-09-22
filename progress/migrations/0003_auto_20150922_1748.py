# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0002_auto_20150922_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='rows',
            name='project_status',
            field=models.CharField(max_length=50, choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], default='started'),
        ),
        migrations.AddField(
            model_name='rows',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='project_status',
            field=models.CharField(max_length=50, choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], default='started'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
