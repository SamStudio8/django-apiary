from django.contrib import admin

from .models import Stand, Box, BoxPosition, Frame, Inspection, InspectionFrame

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

class StandAdmin(admin.ModelAdmin):
    inlines = [BoxInline]

class BoxAdmin(admin.ModelAdmin):
    inlines = [BoxPosInline]

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionFrameInline]

class FrameAdmin(admin.ModelAdmin):
    inlines = []

admin.site.register(Stand, StandAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Frame, FrameAdmin)

