from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.MainWeatherIndex)
admin.site.register(models.AsthmaIndex)
admin.site.register(models.StrokeIndex)
admin.site.register(models.ColdIndex)
