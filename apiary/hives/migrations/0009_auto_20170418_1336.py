# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-18 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0008_boxposition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='hive',
            new_name='stand',
        ),
        migrations.RenameField(
            model_name='inspection',
            old_name='hive',
            new_name='stand',
        ),
    ]
