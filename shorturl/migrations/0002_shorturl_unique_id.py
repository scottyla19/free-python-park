# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='unique_id',
            field=models.CharField(blank=True, editable=False, max_length=6, unique=True),
        ),
    ]