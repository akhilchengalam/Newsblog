# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'get_latest_by': 'posted', 'ordering': ['posted']},
        ),
    ]
