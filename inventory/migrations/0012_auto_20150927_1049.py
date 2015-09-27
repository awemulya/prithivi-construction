# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150926_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='party',
            field=models.ForeignKey(to='inventory.Party', related_name='purchase'),
        ),
    ]
