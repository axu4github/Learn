# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20160628_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='context',
            field=models.TextField(max_length=1000),
        ),
    ]
