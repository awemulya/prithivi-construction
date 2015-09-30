# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_partypayment_voucher_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserow',
            name='is_vatable',
            field=models.BooleanField(default=True),
        ),
    ]
