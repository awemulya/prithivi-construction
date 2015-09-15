# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
