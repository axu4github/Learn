# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
