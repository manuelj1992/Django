from django.db import models
from django.urls import reverse


class Device(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    u
    price = models.IntegerField()
    slug = models.SlugField()
    categories = models.ManyToManyField('devices.ProduCategory')

    dc = {
          "appPackage": "com.android.vending",
          "udid": "57U7N17B22013093",
          "platformName": "android",

          "appActivity": 'com.google.android.finsky.activities.MainActivity',
        }
    """
        Data about mobile, necessary to add in the reporting page.
    """
    client = 'CaixaBank'
    mobile_data = {
        'testname': 'HBAQX04_Broker_AndroidP8_r1',
        'cliente': '%s' % client,
        'mobile_model': 'HUAWEI P8 lite',
        'so_version': 'Android 7.0',
        'app_version': '5.7.1',
        'so': 'Android',
        'ip': '10.42.0.155',

    }
    TOUR = ['Abrir aplicación Caixabank',
            'Login con usuario de broker (53400952)',
            'Click en Inversiones',
            'Click en Valores',
            'Click en órdenes',
            'Validar y desconectar']


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        'devices.Device', on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()

    def __str__(self):
        return self.image.url


class DevicesPlatform(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    platform_name = models.CharField(max_length=255)
    appium_port = models.IntegerField(max_length=4)
    slug = models.SlugField()

    def __str__(self):
        return self.name
