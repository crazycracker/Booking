# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-03 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0015_auto_20170403_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttable',
            name='endDateTime',
            field=models.CharField(max_length=30, verbose_name='endDateTime'),
        ),
        migrations.AlterField(
            model_name='requesttable',
            name='startDateTime',
            field=models.CharField(max_length=30, verbose_name='startDateTime'),
        ),
    ]