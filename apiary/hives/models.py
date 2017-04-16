from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField

class Hive(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Hive %s" % self.name

class HiveBox(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.PROTECT)
    box_type = models.CharField(max_length=3, choices=( ('BRD', "Brood"), ('SPR', "Super") ))

    #order

class Frame(models.Model):
    box = models.ForeignKey(HiveBox, on_delete=models.PROTECT)
    code = models.CharField(max_length=1)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.code

class Inspection(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    #weather
    #report

    def __str__(self):
        return "%s: %s" % (self.hive.name, self.timestamp.date())

class InspectionFrame(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT)
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT)
    img_front = FilerImageField(related_name="frame_fronts")
    img_back = FilerImageField(related_name="frame_backs")
    note = models.TextField(null=True, blank=True)


