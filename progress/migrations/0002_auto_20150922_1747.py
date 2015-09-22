# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rows',
            name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
