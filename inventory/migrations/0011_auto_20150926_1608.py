# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_partypayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partypayment',
            name='party',
            field=models.ForeignKey(to='inventory.Party', related_name='rows'),
        ),
    ]
