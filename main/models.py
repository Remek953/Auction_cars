from django.db import models


# Create your models here.
class Cars(models.Model):
    id              = models.IntegerField(primary_key=True)
    brand           = models.CharField(max_length=64)
    model           = models.CharField(max_length=64)
    year            = models.IntegerField()
    color           = models.CharField(max_length=64)
    city            = models.CharField(max_length=64)
    country         = models.CharField(max_length=64)
    price           = models.IntegerField()
    currency        = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "cars_list"




