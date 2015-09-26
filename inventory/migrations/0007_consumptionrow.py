# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_item_ledger'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumptionRow',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0)),
                ('date', models.DateField(null=True)),
                ('account', models.ForeignKey(related_name='rows', to='inventory.InventoryAccount')),
            ],
        ),
    ]
