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
  created_date = models.DateField(auto_now_add=True)
  # phone_number = models.IntegerField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
			return f"{self.user}"

class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  image = models.ImageField(null=True, blank=True, upload_to="images/")
  qty = models.IntegerField(default=1)
  
  @property
  def get_photo_url(self):
    if self.image and hasattr(self.image):
        return self.image
    else:
        return "/static/images/nopic.jpg"
  
  def __str__(self):
      return f"{self.name}"
  
class Courier(models.Model):
  firstname = models.CharField(max_length=100, unique=True)
  vehicle = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.firstname}"
  
class Order(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  # status (icebox)
  menu_items = models.ManyToManyField(MenuItem)
  courier = models.ForeignKey(Courier, on_delete=models.CASCADE, default='')
  total = models.DecimalField(decimal_places=2, max_digits=10)
  delivery_fee = models.DecimalField(decimal_places=2, max_digits=5)
  service_fee = models.DecimalField(decimal_places=2, max_digits=5)
  tax = models.DecimalField(decimal_places=2, max_digits=5)
  tip = models.DecimalField(decimal_places=2, max_digits=5)
  
  def __str__(self):
      return f"Order {self.total} placed on {self.date}"
 
 

  
    


  
  
  
   
 

  
  