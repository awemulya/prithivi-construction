# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aweuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='aweuser',
            name='is_site_manager',
            field=models.BooleanField(default=False),
        ),
    ]
