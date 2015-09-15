# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('salary', models.FloatField(default=0.0)),
                ('date', models.DateField(default=datetime.date(2015, 9, 15))),
                ('employee', models.ForeignKey(to='employee.Employee', related_name='salary')),
            ],
        ),
    ]
