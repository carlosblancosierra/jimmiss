from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class UserDetails(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)  # can login
    timestamp = models.DateTimeField(auto_now_add=True)

    #
    #     # confirm     = models.BooleanField(default=False)
    #     # confirmed_date     = models.DateTimeField(default=False)
    #
    def __str__(self):
        return self.user.username
#
#     def get_full_name(self):
#         if self.full_name:
#             return self.full_name
#         return self.email
#
#     @property
#     def is_staff(self):
#         if self.is_admin:
#             return True
#         return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
