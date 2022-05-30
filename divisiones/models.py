from django.db import models


# Create your models here.
class Division(models.Model):
    title = models.CharField(max_length=120)
    code = models.CharField(max_length=120, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
