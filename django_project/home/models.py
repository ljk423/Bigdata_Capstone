from django.db import models

# Create your models here.

class WeatherIndex(models.Model):
    date = models.IntegerField()
    seoul_temp = models.DecimalField(max_digits=4, decimal_places=1)
    busan_temp = models.DecimalField(max_digits=4, decimal_places=1)