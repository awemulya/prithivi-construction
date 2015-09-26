# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('inventory', '0004_auto_20150924_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryaccount',
            name='opening_balance',
        ),
        migrations.AddField(
            model_name='inventoryaccount',
            name='site',
            field=models.ForeignKey(default=1, related_name='inventory_account', to='project.Project'),
            preserve_default=False,
        ),
    ]
