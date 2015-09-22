# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_auto_20150922_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rows',
            name='project_status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project_status',
        ),
    ]
