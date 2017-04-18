from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField

class Stand(models.Model):
    name = models.CharField(max_length=50)
    #queen

    def __str__(self):
        return "Stand %s" % self.name

    @property
    def inspections(self):
        return self.inspection_set.order_by("-timestamp")

class Box(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.PROTECT)
    box_type = models.CharField(max_length=3, choices=( ('BRD', "Brood"), ('SPR', "Super") ))
    code = models.CharField(max_length=2)
    order = models.PositiveSmallIntegerField()

    @property
    def full_code(self):
        return "%s.%s%s" % (self.stand.name, self.box_type, self.code)

    def __str__(self):
        return self.full_code

class Frame(models.Model):
    code = models.CharField(max_length=1)
    #supplier
    #date ordered/fitted

    @property
    def full_code(self):
        return "#%d.%s" % (self.id, self.code)

    def __str__(self):
        return self.full_code

class BoxPosition(models.Model):
    box = models.ForeignKey(Box, on_delete=models.PROTECT)
    code = models.CharField(max_length=1)
    order = models.PositiveSmallIntegerField()

    @property
    def full_code(self):
        return "%s %s.%s" % (self.box.box_type, self.box.code, self.code)

    def __str__(self):
        return self.full_code

class Inspection(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    #weather
    #report
    #temperament scale
    #queen = models.BooleanField()

    def __str__(self):
        return "%s: %s" % (self.stand.name, self.timestamp.date())

    def get_frames_rname(self):
        return self.inspectionframe_set.order_by("frame__code")

    @staticmethod
    def pair_frames(inspection_a, inspection_b):
        pairs = {}
        for iframe in inspection_a.get_frames_rname():
            icode = iframe.frame.full_code
            pairs[icode] = [
                iframe,
                None
            ]
        for iframe in inspection_b.get_frames_rname():
            icode = iframe.frame.full_code
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
    boxpos = models.ForeignKey(BoxPosition, on_delete=models.PROTECT)
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT, blank=True, null=True)
    img_front = FilerImageField(related_name="frame_fronts", blank=True, null=True)
    img_back = FilerImageField(related_name="frame_backs", blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    #store = models.NullBooleanField()
    #brood = models.NullBooleanField()
    #cover = models.FloatField(blank=True)

