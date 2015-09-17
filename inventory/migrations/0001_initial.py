# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=254, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, related_name='children', to='inventory.Category', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Inventory Categories',
            },
        ),
        migrations.CreateModel(
            name='InventoryAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
                ('account_no', models.PositiveIntegerField()),
                ('current_balance', models.FloatField(default=0)),
                ('opening_balance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(default='consumable', max_length=15, choices=[('consumable', 'Consumable'), ('non-consumable', 'Non-Consumable')])),
                ('unit', models.CharField(default='pieces', max_length=50)),
                ('account', models.OneToOneField(null=True, related_name='item', to='inventory.InventoryAccount')),
                ('category', models.ForeignKey(null=True, to='inventory.Category', blank=True)),
            ],
        ),
    ]
