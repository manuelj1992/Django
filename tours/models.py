# Create your models here.
from django.db import models
from django.urls import reverse
from devices.models import ClientApp, Device


class Tour(models.Model):
    INACTIVE = 0
    ACTIVE = 1

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    client_app = models.ForeignKey(ClientApp, on_delete=models.CASCADE, related_name='tours')

    status = models.IntegerField(choices=((INACTIVE, 'Inactive'), (ACTIVE, 'Activa')), default=ACTIVE, verbose_name=('status'))

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.code + "_" + self.name


class TourDevice(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    NAV = '_Nav_'
    APP = '_'

    tour = models.ForeignKey('tours.Tour', on_delete=models.CASCADE, related_name='tours')
    type_tour = models.CharField(max_length=6, choices=((NAV, 'Navigation'), (APP, 'AppMobile')), default=APP,verbose_name=('types'))

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='tours')

    status = models.IntegerField(choices=((INACTIVE, 'Inactive'), (ACTIVE, 'Activa')), default=ACTIVE, verbose_name=('status'))

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.tour.__str__() + self.type_tour + self.device.__str__()


class Step(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    tour_name = models.ForeignKey("tours.TourDevice", on_delete=models.CASCADE, related_name='steps')
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
