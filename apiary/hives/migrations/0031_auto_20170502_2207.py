# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-02 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0030_auto_20170502_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='framepack',
            name='ordered',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='framepack',
            name='supplier',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
