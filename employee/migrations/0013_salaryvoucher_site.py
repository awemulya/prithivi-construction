# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('employee', '0012_auto_20150917_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryvoucher',
            name='site',
            field=models.ForeignKey(default=1, to='project.Project', related_name='salary_voucher'),
            preserve_default=False,
        ),
    ]
