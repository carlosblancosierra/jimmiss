from django.contrib import admin
from . import models


# Register your models here.

class ColorModelAdmin(admin.ModelAdmin):
    list_display = ["title", "sku_sufix", "hex"]

    class Meta:
        model = models.Color


admin.site.register(models.Color, ColorModelAdmin)
