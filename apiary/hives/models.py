from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField

class Hive(models.Model):
    name = models.CharField(max_length=50)
    #queen

    def __str__(self):
        return "Hive %s" % self.name

    @property
    def inspections(self):
        return self.inspection_set.order_by("-timestamp")

class HiveBox(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.PROTECT)
    box_type = models.CharField(max_length=3, choices=( ('BRD', "Brood"), ('SPR', "Super") ))


class Frame(models.Model):
    box = models.ForeignKey(HiveBox, on_delete=models.PROTECT)
    code = models.CharField(max_length=1)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.code

class Inspection(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    #weather
    #report

    def __str__(self):
        return "%s: %s" % (self.hive.name, self.timestamp.date())

    def get_frames_rname(self):
        return self.inspectionframe_set.order_by("frame__code")

    @staticmethod
    def pair_frames(inspection_a, inspection_b):
        pairs = {}
        for iframe in inspection_a.get_frames_rname():
            icode = iframe.frame.code
            pairs[icode] = [
                iframe,
                None
            ]
        for iframe in inspection_b.get_frames_rname():
            icode = iframe.frame.code
            if icode in pairs:
                pairs[icode][1] = iframe
            else:
                pairs[icode] = [
                    None,
                    iframe
                ]
        return pairs

    def list_notes(self):
        try:
            return self.notes.split("\n")
        except:
            return []

class InspectionFrame(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT)
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT)
    img_front = FilerImageField(related_name="frame_fronts")
    img_back = FilerImageField(related_name="frame_backs")
    note = models.TextField(null=True, blank=True)


