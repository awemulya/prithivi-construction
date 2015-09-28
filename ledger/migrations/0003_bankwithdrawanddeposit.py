# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_bank_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankWithdrawAndDeposit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_deposit', models.BooleanField(default=True)),
                ('date', models.DateField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('voucher_no', models.PositiveIntegerField(blank=True, null=True)),
                ('bank', models.ForeignKey(related_name='rows', to='ledger.Bank')),
            ],
        ),
    ]
