from django.contrib import admin

from .models import Hive, HiveBox, Frame, Inspection, InspectionFrame

class HiveBoxInline(admin.StackedInline):
    model = HiveBox
    extra = 1

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 1

class InspectionFrameInline(admin.TabularInline):
    model = InspectionFrame
    extra = 1

class HiveAdmin(admin.ModelAdmin):
    inlines = [HiveBoxInline]

class HiveBoxAdmin(admin.ModelAdmin):
    inlines = [FrameInline]

class InspectionAdmin(admin.ModelAdmin):
    inlines = [InspectionFrameInline]

admin.site.register(Hive, HiveAdmin)
admin.site.register(HiveBox, HiveBoxAdmin)
admin.site.register(Inspection, InspectionAdmin)

