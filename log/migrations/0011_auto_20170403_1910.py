# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-03 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0010_auto_20170403_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttable',
            name='endDateTime',
            field=models.DateTimeField(verbose_name='endDateTime'),
        ),
        migrations.AlterField(
            model_name='requesttable',
            name='startDateTime',
            field=models.DateTimeField(verbose_name='startDateTime'),
        ),
    ]
