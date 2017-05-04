from django.contrib import admin
import datetime

from .models import Stand, Box, InspectionBox, BoxPosition, Frame, FramePack, Inspection, InspectionFrame, Queen

class InspectionBoxInline(admin.TabularInline):
    model = InspectionBox
    extra = 0

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

class FrameInline(admin.TabularInline):
    #readonly_fields = ["id", "code", "current_boxpos"]
    model = Frame
    extra = 0
    can_delete = False

class InspectionFrameInline(admin.TabularInline):
    model = InspectionFrame
    extra = 1

class QueenAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('__str__', 'mark', 'stand')

class StandAdmin(admin.ModelAdmin):
    inlines = [BoxInline]

class BoxAdmin(admin.ModelAdmin):
    inlines = [BoxPosInline, InspectionBoxInline]

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionBoxInline, InspectionFrameInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.save()
        formset.save_m2m()
        Inspection.my_post_save(form.instance.pk)

class FrameAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('full_code', 'current_boxpos', 'pack')
    list_filter = ('pack__frame_type', 'current_boxpos__box', 'current_boxpos__box__current_stand', 'pack__supplier')

class FramePackAdmin(admin.ModelAdmin):
    inlines = [FrameInline]


admin.site.register(Stand, StandAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(FramePack, FramePackAdmin)
admin.site.register(Queen, QueenAdmin)

