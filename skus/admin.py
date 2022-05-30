from django.contrib import admin
from . import models


# Register your models here.

class SkuMasterModelAdmin(admin.ModelAdmin):
    list_display = ["sku", "descripcion", "marca", "division", "serie", "composicion", "costo", "precio"]

    search_fields = ["sku"]
    list_filter = ["marca", "division", "serie", "composicion", ]

    # readonly_fields = ['sku']

    class Meta:
        model = models.SkuMaster


admin.site.register(models.SkuMaster, SkuMasterModelAdmin)


class SkuProductModelAdmin(admin.ModelAdmin):
    list_display = ["sku", "master", "color", "talla"]

    # list_display = ["sku", "master", "division", "serie", "composicion", "color", "talla", "costo", "precio"]

    search_fields = ["sku", "master"]
    list_filter = ["color", "talla"]
    readonly_fields = ['sku']

    class Meta:
        model = models.SkuProduct


admin.site.register(models.SkuProduct, SkuProductModelAdmin)
