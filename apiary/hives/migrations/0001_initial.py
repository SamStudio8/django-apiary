# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HiveBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_type', models.CharField(choices=[('BRD', 'Brood'), ('SPR', 'Super')], max_length=3)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hives.Hive')),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hives.Hive')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_front', models.ImageField(upload_to=b'')),
                ('img_back', models.ImageField(upload_to=b'')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hives.Frame')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hives.Inspection')),
            ],
        ),
        migrations.AddField(
            model_name='frame',
            name='box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hives.HiveBox'),
        ),
    ]
