# Create your models here.
from django.db import models
from django.urls import reverse
from Django.devices.models import ClientApp


class Tour(models.Model):
    ACTIVE = 1
    INACTIVE = 0

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=True, null=True)

    slug = models.SlugField()

    client_app = models.ForeignKey(ClientApp, on_delete=models.CASCADE, related_name='devices')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Steps(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    tour_name = models.ForeignKey("tours.Tour", on_delete=models.CASCADE, related_name='devices')
    position = models.IntegerField(blank=True, null=True)