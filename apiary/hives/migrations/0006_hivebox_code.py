# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-17 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0005_auto_20170416_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='hivebox',
            name='code',
            field=models.CharField(default='?', max_length=2),
            preserve_default=False,
        ),
    ]
