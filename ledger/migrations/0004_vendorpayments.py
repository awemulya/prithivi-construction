# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_bankwithdrawanddeposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorPayments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('voucher_no', models.PositiveIntegerField(null=True, blank=True)),
                ('bank', models.ForeignKey(to='ledger.Bank')),
                ('vendor', models.ForeignKey(related_name='rows', to='ledger.Vendor')),
            ],
        ),
    ]
