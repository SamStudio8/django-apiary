# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-16 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0004_auto_20160823_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]