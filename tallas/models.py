from django.db import models


# Create your models here.
class Talla(models.Model):
    title = models.CharField(max_length=120)
    sku_sufix = models.CharField(max_length=120)
    short = models.CharField(max_length=120, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
