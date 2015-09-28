# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_salaryvoucher_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='employee',
        ),
        migrations.AlterField(
            model_name='salaryvoucherrow',
            name='employee',
            field=models.ForeignKey(related_name='payment', to='employee.Employee'),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
