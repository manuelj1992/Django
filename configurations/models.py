from django.db import models
from django.urls import reverse


class AlertConf(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

