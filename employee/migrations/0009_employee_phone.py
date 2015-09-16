# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20150916_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=10, default=9841696114),
            preserve_default=False,
        ),
    ]
