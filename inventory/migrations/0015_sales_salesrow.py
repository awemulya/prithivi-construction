# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_purchaserow_is_vatable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('voucher_no', models.PositiveIntegerField(null=True, blank=True)),
                ('credit', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('party', models.ForeignKey(related_name='sales', to='inventory.Party')),
            ],
        ),
        migrations.CreateModel(
            name='SalesRow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sn', models.PositiveIntegerField()),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('is_vatable', models.BooleanField(default=True)),
                ('discount', models.FloatField(default=0)),
                ('unit', models.CharField(default='pieces', max_length=50)),
                ('item', models.ForeignKey(to='inventory.Item')),
                ('sales', models.ForeignKey(related_name='rows', to='inventory.Sales')),
            ],
        ),
    ]
