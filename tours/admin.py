from django.contrib import admin
from tours.models import Tour, Step


class TourAdmin(admin.ModelAdmin):
    model = Tour


class StepAdmin(admin.ModelAdmin):
    model = Step


admin.site.register(Tour, TourAdmin)
admin.site.register(Step, StepAdmin)

