# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='date',
            field=models.DateField(default=datetime.date(2015, 9, 17)),
        ),
    ]
