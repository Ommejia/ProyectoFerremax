from django.db import models

# Create your models here.

class Product(models.Model):
    marca = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"