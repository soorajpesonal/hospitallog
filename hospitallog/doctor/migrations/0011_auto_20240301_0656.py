# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-03-01 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_reg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='pending', max_length=30),
        ),
    ]
