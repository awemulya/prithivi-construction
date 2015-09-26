# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_consumptionrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumptionrow',
            name='purpose',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
