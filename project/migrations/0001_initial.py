# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150913_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('start_date', models.DateField(null=True)),
                ('completion_date', models.DateField(null=True)),
                ('incharge', models.ManyToManyField(to='user.AweUser')),
            ],
        ),
    ]
