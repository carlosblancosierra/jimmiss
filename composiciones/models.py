from django.db import models

# Create your models here.

class Composicion(models.Model):
    title = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
