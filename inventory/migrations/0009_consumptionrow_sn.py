# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_consumptionrow_purpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumptionrow',
            name='sn',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
