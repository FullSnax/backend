from django.db import models

# Create your models here.

class React(models.Model):
	name = models.CharField(max_length=500)
	detail = models.CharField(max_length=500)

	def __str__(self):
			return f"The name is {self.name} and is {self.detail}"