from django.contrib import admin
from configurations.models import AlertConf


class AlertConfAdmin(admin.ModelAdmin):
    model = AlertConf


admin.site.register(AlertConf, AlertConfAdmin)


