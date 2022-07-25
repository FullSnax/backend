from rest_framework import serializers
from . models import *
from django.contrib.auth.admin import User

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = React
		fields = ['name', 'detail']

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['address', 'created_date']
  
class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuItem
		fields = '__all__'
  
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
  
