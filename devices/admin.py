from django.contrib import admin
from devices.models import Device, DeviceImage, \
    DevicesPlatform, AppPackage, ClientApp, AppVersion


class DeviceImageInLine(admin.TabularInline):
    model = DeviceImage


class DeviceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        DeviceImageInLine
    ]


class DevicesPlatformAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class AppPackageAdmin(admin.ModelAdmin):
    model = AppPackage


class ClientAppAdmin(admin.ModelAdmin):
    model = ClientApp

class AppVersionAdmin(admin.ModelAdmin):
    model = AppVersion


admin.site.register(Device, DeviceAdmin)
admin.site.register(DevicesPlatform, DevicesPlatformAdmin)
admin.site.register(ClientApp, ClientAppAdmin)
admin.site.register(AppPackage, AppPackageAdmin)
admin.site.register(AppVersion, AppVersionAdmin)