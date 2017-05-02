from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from hives.models import Inspection, InspectionFrame

class Command(BaseCommand):
    help = 'Populate an inspection with last inspection frame positions.'

    def add_arguments(self, parser):
        parser.add_argument('inspection_id_with', type=int)
        parser.add_argument('inspection_id_new', type=int)

    def handle(self, *args, **options):
        pk_new = options["inspection_id_new"]
        pk_with = options["inspection_id_with"]
        try:
            inspection_new = Inspection.objects.get(pk=pk_new)
        except Inspection.DoesNotExist:
            raise CommandError('Inspection "%s" does not exist' % pk_new)

        try:
            inspection_with = Inspection.objects.get(pk=pk_with)
        except Inspection.DoesNotExist:
            raise CommandError('Inspection "%s" does not exist' % pk_with)

        if inspection_new.inspectionframe_set.count() > 0:
            raise CommandError('Inspection "%s" already has frames' % pk_new)
        if inspection_with.inspectionframe_set.count() == 0:
            raise CommandError('Inspection "%s" has no frames' % pk_with)

        count = 0
        for iframe in inspection_with.inspectionframe_set.all():
            count += 1

            if iframe.new_boxpos:
                new_iframe = InspectionFrame(
                        inspection_id=inspection_new.id,
                        boxpos_id=iframe.new_boxpos.id,
                        frame_id=iframe.frame.id
                )
            else:
                new_iframe = InspectionFrame(
                        inspection_id=inspection_new.id,
                        boxpos_id=iframe.boxpos.id,
                        frame_id=iframe.frame.id
                )
            new_iframe.save()
        self.stdout.write(self.style.SUCCESS('Successfully added %d frames' % (count)))

