from os import TMP_MAX
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class React(models.Model):
	name = models.CharField(max_length=100)
	detail = models.CharField(max_length=100)

	def __str__(self):
			return f"The name is {self.name} and is {self.detail}"
 
class Profile(models.Model):
  address = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  # def __str__(self):
	# 		return f"Profile address is {self.address}"


# class Orders(models.Model):
#   user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#   courier = models.ManyToManyField(Courier, on_delete=models.CASCADE)
#   date = models.DateField(auto_now_add=True)
#   # status (icebox)
#   lineitem = models.ManyToManyField(Lineitem, on_delete=models.CASCADE)
#   total = models.DecimalField(decimal_places=2)
#   delivery_fee = models.DecimalField(decimal_places=2)
#   service_fee = models.DecimalField(decimal_places=2)
#   tax = models.DecimalField(decimal_places=2)
#   tip = models.DecimalField(decimal_places=2)

class LineItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  image = models.ImageField()
  qty = models.IntegerField()
  
class Courier(models.Model):
  firstname = models.CharField(max_length=100)
  car = models.CharField(max_length=100)
  
  
   
 

  
  