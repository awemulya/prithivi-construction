# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(blank=True, null=True, max_length=254)),
                ('phone_no', models.CharField(blank=True, null=True, max_length=100)),
                ('account', models.ForeignKey(to='ledger.Account', null=True)),
            ],
            options={
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(blank=True, null=True, max_length=254)),
                ('phone_no', models.CharField(blank=True, null=True, max_length=100)),
                ('account', models.ForeignKey(to='ledger.Account', null=True)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
    ]
