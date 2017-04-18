from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from filer.fields.image import FilerImageField

class Stand(models.Model):
    name = models.CharField(max_length=50)
    #queen

    def __str__(self):
        return "Stand %s" % self.name

    @property
    def inspections(self):
        return self.inspection_set.order_by("-timestamp")

class Queen(models.Model):
    name = models.CharField(max_length=50)
    mark = models.CharField(max_length=1, choices=(
        ('W', "White ('1 or '6)"),
        ('Y', "Yellow ('2 or '7)"),
        ('R', "Red ('3 or '8)"),
        ('G', "Green ('4 or '9)"),
        ('B', "Blue ('5 or '0)"),
    ))
    born = models.DateField()
    breeder = models.CharField(max_length=32)
    price = models.FloatField()
    stand = models.ForeignKey(Stand, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "%s (%d)" % (self.name, self.born.year)

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
    current_boxpos = models.ForeignKey("BoxPosition", on_delete=models.PROTECT, blank=True, null=True)
    #supplier
    #date ordered/fitted
    #active = models.BooleanField()

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
        return "%s.%s.%s" % (self.box.stand.name, self.box.order, self.order)

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

    def get_box_frames_rname(self, box_id):
        return self.inspectionframe_set.filter(boxpos__box__id=box_id).order_by("boxpos__order")

    def get_frame_by_id(self, frame_id):
        try:
            return self.inspectionframe_set.get(frame_id=frame_id)
        except:
            return None

    @property
    def boxes(self):
        #TODO Make this return the boxes
        result = self.inspectionframe_set.values('boxpos__box','boxpos__box__code','boxpos__box__order').annotate(frame_count=Count('boxpos__box'))
        counts = {}
        for i, r in enumerate(result):
            counts[r["boxpos__box"]] = {
                "count": r["frame_count"],
                "order": r["boxpos__box__order"],
                "code": r["boxpos__box__code"],
            }
        return counts

    @staticmethod
    def pair_frames(inspection_a, inspection_b):
        pairs = {}

        boxes = inspection_a.boxes
        for ibox in boxes:
            boxcode = boxes[ibox]["code"]
            pairs[boxcode] = {}
            for i, iframe in enumerate(inspection_a.get_box_frames_rname(ibox)):
                if iframe.frame:
                    icode = iframe.frame.full_code
                    pairs[boxcode][icode] = [
                        iframe,
                        inspection_b.get_frame_by_id(iframe.frame.id),
                        i,
                    ]

        for box in pairs:
            pairs[box] = sorted(pairs[box].items(), key=lambda (k,v):v[2])
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
    class Meta:
        get_latest_by = 'inspection__timestamp'

