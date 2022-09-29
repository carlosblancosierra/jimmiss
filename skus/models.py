from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

from marcas.models import Marca
from divisiones.models import Division
from series.models import Serie
from composiciones.models import Composicion
from colores.models import Color
from tallas.models import Talla
from categorias.models import Categoria


# Create your models here.
def upload_location(instance, filename):
    return "sku-masters-img/%s/%s" % (instance.sku, filename)


class SkuMaster(models.Model):
    sku = models.CharField(max_length=120, unique=True)
    descripcion = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    costo = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    marca = models.ForeignKey(Marca, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='marca_skuproduct_set')
    division = models.ForeignKey(Division, blank=True, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='division_skuproduct_set')
    serie = models.ForeignKey(Serie, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='serie_skuproduct_set')
    composicion = models.ForeignKey(Composicion, blank=True, null=True,
                                    on_delete=models.SET_NULL,
                                    related_name='composicion_skuproduct_set')
    categoria = models.ForeignKey(Categoria, blank=True, null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='categoria_skuproduct_set')
    image = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                processors=[ResizeToFill(1200, 1200)],
                                format='JPEG',
                                options={'quality': 95})
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(1200, 1200)],
                                 format='JPEG',
                                 options={'quality': 95})
    image_2 = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                  processors=[ResizeToFill(1200, 1200)],
                                  format='JPEG',
                                  options={'quality': 95})
    image_3 = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                  processors=[ResizeToFill(1200, 1200)],
                                  format='JPEG',
                                  options={'quality': 95})
    image_4 = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                  processors=[ResizeToFill(1200, 1200)],
                                  format='JPEG',
                                  options={'quality': 95})
    image_5 = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                  processors=[ResizeToFill(1200, 1200)],
                                  format='JPEG',
                                  options={'quality': 95})
    image_6 = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                  processors=[ResizeToFill(1200, 1200)],
                                  format='JPEG',
                                  options={'quality': 95})

    image_alt_text = models.CharField(max_length=120, blank=True)
    meta_description = models.CharField(max_length=120, blank=True)
    primary_keyword = models.CharField(max_length=120, blank=True)
    secondary_keyword_1 = models.CharField(max_length=120, blank=True)
    seo_title = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["sku"]

    def get_absolute_url(self):
        return reverse("skus:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.descripcion


class SkuProduct(models.Model):
    master = models.ForeignKey(SkuMaster, blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name='master_skuproduct_set')
    color = models.ForeignKey(Color, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='color_skuproduct_set')
    talla = models.ForeignKey(Talla, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='talla_skuproduct_set')

    sku = models.CharField(max_length=120, unique=True, blank=True, null=True)

    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):

        if self.master:
            return self.master.sku + self.color.sku_sufix + self.talla.sku_sufix
        else:
            return self.color.sku_sufix + self.talla.sku_sufix

    def get_absolute_url(self):
        return f"/skus/{self.master.slug}"

    class Meta:
        ordering = ["master", "color", "talla"]


def pre_save_sku_product_receiver(sender, instance, *args, **kwargs):
    print(instance.sku)
    if instance.sku is None:
        instance.sku = instance.master.sku + instance.color.sku_sufix + instance.talla.sku_sufix


pre_save.connect(pre_save_sku_product_receiver, sender=SkuProduct)
