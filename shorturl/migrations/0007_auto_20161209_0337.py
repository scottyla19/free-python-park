# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0006_shorturl_base_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='base_url',
            field=models.URLField(default='/shorturl/'),
        ),
    ]
