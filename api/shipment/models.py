from django.db import models

# Create your models here.


class Shipment(models.Model):
    track_ref = models.CharField(verbose_name='Track code', max_length=13, primary_key=True, unique=True)
    from_coutry = models.CharField(verbose_name='Country of dispatch', max_length=56)
    to_country = models.CharField(verbose_name='Country of destination', max_length=56)
    package_weight = models.FloatField(verbose_name='Package weight (kg)', max_length=50)
    is_up_to_date = models.BooleanField(verbose_name='Up to date', default=True)
