# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-03-01 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_auto_20240301_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breg',
            name='bdate',
            field=models.CharField(max_length=30),
        ),
    ]
