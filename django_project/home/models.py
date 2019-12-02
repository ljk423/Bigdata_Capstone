from django.db import models
from django.utils import timezone
# Create your models here.

class MainWeatherIndex(models.Model):
    name = models.CharField(default= "cold", max_length=30)
    date = models.DateTimeField(default=timezone.now)
    local_code = models.IntegerField()
    disease_index = models.IntegerField()
    next_page = models.CharField(null= True, max_length=200)
    image = models.CharField(null=True, max_length=200)

class AsthmaIndex(models.Model):
    date = models.DateTimeField(default=timezone.now)
    local_code = models.IntegerField()
    disease_index = models.IntegerField()

class ColdIndex(models.Model):
    date = models.DateTimeField(default=timezone.now)
    local_code = models.IntegerField()
    disease_index = models.IntegerField()

class StrokeIndex(models.Model):
    date = models.DateTimeField(default=timezone.now)
    local_code = models.IntegerField()
    disease_index = models.IntegerField()

