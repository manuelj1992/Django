from django.contrib import admin
from tours.models import Tour, Step, TourDevice


class TourAdmin(admin.ModelAdmin):
    model = Tour


class TourDeviceAdmin(admin.ModelAdmin):
    model = TourDevice


class StepAdmin(admin.ModelAdmin):
    model = Step


admin.site.register(Tour, TourAdmin)
admin.site.register(TourDevice, TourDeviceAdmin)
admin.site.register(Step, StepAdmin)

