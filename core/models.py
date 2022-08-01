# from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
# Profile = get_user_model()

class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  image = models.ImageField(null=True, blank=True, upload_to="images/")
  image2 = models.CharField(max_length=100, default='')
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
  first_name = models.CharField(max_length=100, unique=True)
  vehicle = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.first_name}"
  
class Order(models.Model):
  Profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  menu_items = models.ManyToManyField(MenuItem)
  courier = models.ForeignKey(Courier, on_delete=models.CASCADE, default='')
  total = models.DecimalField(decimal_places=2, max_digits=10)
  tax = models.DecimalField(decimal_places=2, max_digits=10)
  tip = models.DecimalField(decimal_places=2, max_digits=10)
  
  def __str__(self):
      return f"Order {self.total} placed on {self.date}"
    
 
 
 

  
    


  
  
  
   
 

  
  