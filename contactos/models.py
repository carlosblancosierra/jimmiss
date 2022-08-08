from django.db import models


# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=255, blank=True, null=True)
    direccion_comercial = models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(max_length=1200, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return f"/contactos/{self.id}"