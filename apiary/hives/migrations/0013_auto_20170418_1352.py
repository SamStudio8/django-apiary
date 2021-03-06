# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-18 13:52
from __future__ import unicode_literals

from django.db import migrations

def make_boxpos_stubs(apps, editor):
    BoxPos = apps.get_model("hives", "BoxPosition")
    InspectionFrame = apps.get_model("hives", "InspectionFrame")
    for iframe in InspectionFrame.objects.all():
        bp = BoxPos.objects.get_or_create(box_id=iframe.frame.box.id, order=0, code="?")[0]
        bp.save()
        iframe.boxpos = bp
        iframe.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0012_auto_20170418_1350'),
    ]

    operations = [
        migrations.RunPython(make_boxpos_stubs),
    ]
