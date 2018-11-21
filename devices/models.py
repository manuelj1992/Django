from django.db import models
from django.urls import reverse


class AppVersion(models.Model):
    version = models.CharField(max_length=255)
    platform = models.ForeignKey('devices.DevicesPlatform', on_delete=models.CASCADE, related_name='appversions')

    def __str__(self):
        return self.version + " for " + self.platform.__str__()


class ClientApp(models.Model):
    client = models.CharField(max_length=255)
    app_version = models.ManyToManyField('devices.AppVersion')

    def __str__(self):
        return self.client


class Device(models.Model):
    ACTIVE = 1
    INACTIVE = 0

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    udid = models.CharField(max_length=255, blank=True, null=True)

    slug = models.SlugField()

    platform = models.ForeignKey('devices.DevicesPlatform', on_delete=models.CASCADE, related_name='devices', blank=True, null=True)
    static_ip = models.CharField(max_length=25, blank=True, null=True)
    so_version = models.CharField(max_length=25, blank=True, null=True)

    device_model = models.CharField(max_length=255, blank=True, null=True)

    client_app = models.ForeignKey('devices.ClientApp', on_delete=models.CASCADE, related_name='devices', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return "_".join(self.name.split())


class DeviceImage(models.Model):
    device = models.ForeignKey(
        'devices.Device', on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()

    def __str__(self):
        return self.image.url


class AppPackage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)

    automation_name = models.CharField(max_length=255, blank=True, null=True)
    xcode_org_id = models.CharField(max_length=255, blank=True, null=True)
    xcode_signing_id = models.CharField(max_length=255, blank=True, null=True)

    app_package = models.CharField(max_length=255, blank=True, null=True)
    app_activity = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class DevicesPlatform(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    appium_port = models.IntegerField(blank=True, null=True)

    app_packages = models.ManyToManyField('devices.AppPackage')
    slug = models.SlugField()

    def __str__(self):
        return self.name
