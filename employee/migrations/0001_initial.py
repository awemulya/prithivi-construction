# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=20)),
                ('marital_status', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('role', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(to='employee.EmployeeRole'),
        ),
        migrations.AddField(
            model_name='employee',
            name='site',
            field=models.ForeignKey(to='project.Project', default=2, related_name='employee'),
        ),
    ]
