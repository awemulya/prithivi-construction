# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
        ('inventory', '0003_journalentry_party_purchase_purchaserow_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='account',
            field=models.ForeignKey(null=True, to='ledger.Account'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='credit',
            field=models.BooleanField(default=False),
        ),
    ]
