# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0003_auto_20161208_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='unique_id',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
