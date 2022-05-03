from django.db import models


# Create your models here.
class Color(models.Model):
    title = models.CharField(max_length=120)
    sku_sufix = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    hex = models.CharField(max_length=7)

    def __str__(self):
        return self.title
