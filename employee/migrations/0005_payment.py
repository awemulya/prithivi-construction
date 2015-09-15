# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('absent_days', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date(2015, 9, 15))),
                ('year', models.IntegerField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('employee', models.ForeignKey(related_name='payment', to='employee.Employee')),
            ],
        ),
    ]
