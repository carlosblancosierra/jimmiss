from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class Address(models.Model):
    nombre_completo = models.CharField(max_length=120)
    calle_numero = models.CharField(max_length=120)
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(max_length=120, null=True, blank=True)
    ciudad = models.CharField(max_length=120)
    colonia = models.CharField(max_length=120, null=True, blank=True)
    telefono = models.CharField(max_length=120, null=True, blank=True)
    pais = models.CharField(max_length=120, default="Mexico")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_completo + " " + self.calle_numero)

    # def get_address(self):
    #     return "{line1} {line2} {city} {state}, {postal} {country}".format(
    #         line1=self.address_line_1,
    #         line2=self.address_line_2 or "",
    #         city=self.city,
    #         state=self.state,
    #         postal=self.postal_code,
    #         country=self.country,
    #     )

    def get_absolute_url(self):
        return f"/addresses/{self.id}"
