# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_consumptionrow_sn'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyPayment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('party', models.ForeignKey(to='inventory.Party', related_name='roes')),
            ],
        ),
    ]
