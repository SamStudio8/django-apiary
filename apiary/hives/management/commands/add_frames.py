from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from hives.models import Frame, FramePack

class Command(BaseCommand):
    help = 'Add a FramePack'

    def add_arguments(self, parser):
        parser.add_argument('num_frames', type=int)
        parser.add_argument('frame_type', type=str)
        parser.add_argument('supplier', type=str)

    def handle(self, *args, **options):
        fp = FramePack(frame_type=options["frame_type"], supplier=options["supplier"], ordered=datetime.now())
        fp.save()
        for i in range(options["num_frames"]):
            f = Frame(pack_id=fp.id)
            f.save()

            if i == 0:
                first = f.id
        last = f.id
        self.stdout.write(self.style.SUCCESS('Successfully added Frames %d-%d' % (first, last)))
