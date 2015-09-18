# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('purpose', models.CharField(max_length=254)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('site', models.ForeignKey(related_name='demands', to='project.Project')),
            ],
        ),
        migrations.CreateModel(
            name='DemandRow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100, blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=50)),
                ('fulfilled_quantity', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('demand', models.ForeignKey(related_name='rows', to='inventory.Demand')),
                ('item', models.ForeignKey(to='inventory.Item')),
            ],
        ),
    ]
