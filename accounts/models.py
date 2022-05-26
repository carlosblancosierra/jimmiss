from __future__ import unicode_literals
from django.db import models


# Create your models here.
# class UserData(models.Model):
#     username = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=255, unique=True)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     is_active = models.BooleanField(default=True)  # can login
#     staff = models.BooleanField(default=False)  # staff user non superuser
#     admin = models.BooleanField(default=False)  # superuser
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     nombre_comercial = models.CharField(max_length=255, blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     telefono = models.CharField(max_length=255, blank=True, null=True)
#
#     # confirm     = models.BooleanField(default=False)
#     # confirmed_date     = models.DateTimeField(default=False)
#
#     def __str__(self):
#         return self.email
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
