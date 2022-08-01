from django.conf import settings
from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.CharField(max_length=200, default="")
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Courier(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    vehicle = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}"


class Order(models.Model):
    Profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Order {self.total} placed on {self.date}"
      
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    tax = models.DecimalField(decimal_places=2, max_digits=10)
    tip = models.DecimalField(decimal_places=2, max_digits=10)
    
