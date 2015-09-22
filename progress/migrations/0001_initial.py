# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], max_length=50, default='started')),
                ('start_date', models.DateField(default=datetime.datetime.today)),
                ('deadline', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed')], max_length=50, default='started')),
                ('start_date', models.DateField(default=datetime.datetime.today)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('site', models.ForeignKey(to='project.Project', related_name='task')),
            ],
        ),
        migrations.AddField(
            model_name='rows',
            name='task',
            field=models.ForeignKey(to='progress.Task', related_name='rows'),
        ),
    ]
