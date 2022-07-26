from rest_framework import serializers
from . models import *
from django.contrib.auth.admin import User

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['address', 'created_date']
  
class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuItem
		fields = ['name', 'description', 'price', 'qty']
  
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
  
class CourierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courier
		fields = '__all__'
  
class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
  
