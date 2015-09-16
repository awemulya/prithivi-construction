# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20150916_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='year',
            field=models.IntegerField(),
        ),
    ]
