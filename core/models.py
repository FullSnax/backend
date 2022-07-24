from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class React(models.Model):
	name = models.CharField(max_length=100)
	detail = models.CharField(max_length=100)

	def __str__(self):
			return f"The name is {self.name} and is {self.detail}"
 
class Profile(models.Model):
  address = models.CharField(max_length=100)
  created_date = models.DateField(auto_now_add=True)
  # phone_number = PhoneNumberField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  # def __str__(self):
	# 		return f"Profile address is {self.address}"

class LineItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  image = models.ImageField()
  qty = models.IntegerField()
  
class Courier(models.Model):
  firstname = models.CharField(max_length=100)
  car = models.CharField(max_length=100)
  
class Order(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  courier = models.OneToOneField(Courier, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  # status (icebox)
  lineitems = models.ManyToManyField(LineItem)
  total = models.DecimalField(decimal_places=2, max_digits=10)
  delivery_fee = models.DecimalField(decimal_places=2, max_digits=5)
  service_fee = models.DecimalField(decimal_places=2, max_digits=5)
  tax = models.DecimalField(decimal_places=2, max_digits=5)
  tip = models.DecimalField(decimal_places=2, max_digits=5)


  
  
  
   
 

  
  