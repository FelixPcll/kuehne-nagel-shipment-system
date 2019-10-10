from django.db import models

# Create your models here.


class Shipment(models.Model):
    track_ref = models.CharField(max_length=13, primary_key=True, unique=True)
    from_coutry = models.CharField(max_length=56)
    to_country = models.CharField(max_length=56)
    package_weight = models.FloatField(max_length=50)
    is_deleted = models.BooleanField(default=False, )
