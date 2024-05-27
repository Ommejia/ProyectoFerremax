from django.db import models

# Create your models here.

class Product(models.Model):
    marca = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name