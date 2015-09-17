# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_employee_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryVoucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voucher_no', models.PositiveIntegerField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryVoucherRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.PositiveIntegerField()),
                ('paid_date', models.DateField(default=datetime.datetime.today)),
                ('amount', models.FloatField()),
                ('start_date', models.DateField()),
                ('last_date', models.DateField()),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('salary_voucher', models.ForeignKey(related_name='rows', to='employee.SalaryVoucher')),
            ],
        ),
        migrations.AlterField(
            model_name='salary',
            name='date',
            field=models.DateField(default=datetime.date(2015, 9, 17)),
        ),
    ]
