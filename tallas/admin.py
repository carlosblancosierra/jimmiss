from django.contrib import admin
from . import models


# Register your models here.
class TallaModelAdmin(admin.ModelAdmin):
    list_display = ["title", "sku_sufix", "short", "order"]

    class Meta:
        model = models.Talla


admin.site.register(models.Talla, TallaModelAdmin)
