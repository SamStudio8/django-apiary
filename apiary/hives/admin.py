from django.contrib import admin
import datetime

from .models import Stand, Box, BoxHistory, BoxPosition, Frame, Inspection, InspectionFrame, Queen

class BoxHistInline(admin.TabularInline):
    readonly_fields = ["stand", "order"]
    model = BoxHistory
    extra = 0
    can_delete = False
    def has_add_permission(self, request):
        return False

class BoxPosInline(admin.TabularInline):
    model = BoxPosition
    extra = 1

class BoxInline(admin.TabularInline):
    readonly_fields = ["current_order", "box_type", "code"]
    model = Box
    extra = 0
    can_delete = False
    def has_add_permission(self, request):
        return False

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 1

class InspectionFrameInline(admin.TabularInline):
    model = InspectionFrame
    extra = 1

class QueenAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('__str__', 'mark', 'stand')

class StandAdmin(admin.ModelAdmin):
    inlines = [BoxInline]

class BoxAdmin(admin.ModelAdmin):
    inlines = [BoxPosInline, BoxHistInline]

    def save_model(self, request, obj, form, change):
        latest = obj.boxhistory_set.latest()

        if latest.stand != obj.current_stand or latest.order != obj.current_order:
            bh = BoxHistory(box_id=obj.id, stand_id=obj.current_stand.id, order=obj.current_order,timestamp=datetime.datetime.now())
            bh.save()
        super(BoxAdmin, self).save_model(request, obj, form, change)

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionFrameInline]

    def save_model(self, request, obj, form, change):
        latest = Inspection.objects.latest()
        if obj.timestamp >= latest.timestamp:
            # If the inspection is newer or at least as old as the latest inspection
            # update the locations of the frames
            for iframe in obj.inspectionframe_set.all():
                if iframe.frame:
                    if iframe.new_boxpos:
                        iframe.frame.current_boxpos = iframe.new_boxpos
                        iframe.frame.save()
                    else:
                        iframe.frame.current_boxpos = iframe.boxpos
                        iframe.frame.save()
        super(InspectionAdmin, self).save_model(request, obj, form, change)

class FrameAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('full_code', 'current_boxpos')
    list_filter = ('current_boxpos__box', 'current_boxpos__box__current_stand',)

admin.site.register(Stand, StandAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Queen, QueenAdmin)

