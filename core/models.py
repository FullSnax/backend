from django.conf import settings
from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.CharField(max_length=200, default="")
    

    def __str__(self):
        return f"{self.name}"


class Courier(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    vehicle = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}"


class Order(models.Model):
    Profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tip = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   
    def __str__(self):
        return f"Order is assigned to {self.courier} placed by {self.Profile}"
      
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_items = models.OneToOneField(MenuItem, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    # date = models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return f"The total is {self.total} with tax of {self.tax} and tip of {self.tip} containing {self.order}"
    
