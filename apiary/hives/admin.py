from django.contrib import admin

from .models import Stand, Box, BoxPosition, Frame, Inspection, InspectionFrame, Queen

class BoxPosInline(admin.TabularInline):
    model = BoxPosition
    extra = 1

class BoxInline(admin.StackedInline):
    model = Box
    extra = 1

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
    inlines = [BoxPosInline]

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionFrameInline]

    def save_model(self, request, obj, form, change):
        for iframe in obj.inspectionframe_set.all():
            if iframe.frame:
                iframe.frame.current_boxpos = iframe.boxpos
                iframe.frame.save()
        super(InspectionAdmin, self).save_model(request, obj, form, change)

class FrameAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('full_code', 'current_boxpos')
    list_filter = ('current_boxpos__box', 'current_boxpos__box__stand',)

admin.site.register(Stand, StandAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Queen, QueenAdmin)

