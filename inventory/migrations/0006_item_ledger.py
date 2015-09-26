# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
        ('inventory', '0005_auto_20150925_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ledger',
            field=models.ForeignKey(to='ledger.Account', null=True),
        ),
    ]
