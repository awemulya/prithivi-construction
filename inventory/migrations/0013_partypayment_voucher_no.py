# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20150927_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='partypayment',
            name='voucher_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
