# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0002_demand_demandrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('model_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(related_name='inventory_journal_entries', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'InventoryJournal Entries',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(blank=True, null=True, max_length=254)),
                ('phone_no', models.CharField(blank=True, null=True, max_length=100)),
                ('pan_no', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('voucher_no', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('party', models.ForeignKey(to='inventory.Party')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sn', models.PositiveIntegerField()),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('unit', models.CharField(default='pieces', max_length=50)),
                ('item', models.ForeignKey(to='inventory.Item')),
                ('purchase', models.ForeignKey(related_name='rows', to='inventory.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dr_amount', models.FloatField(blank=True, null=True)),
                ('cr_amount', models.FloatField(blank=True, null=True)),
                ('current_balance', models.FloatField(blank=True, null=True)),
                ('account', models.ForeignKey(to='inventory.InventoryAccount')),
                ('journal_entry', models.ForeignKey(related_name='transactions', to='inventory.JournalEntry')),
            ],
        ),
    ]
