from rest_framework import serializers
from . models import *
from django.contrib.auth.admin import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'pk', 'status')
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['address', 'created_date']
  
class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuItem
		fields = ['name', 'description', 'price', 'qty', 'image']
  
# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'first_name', 'last_name', 'email']
  
class CourierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courier
		fields = '__all__'
  
class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['date', 'menu_items', 'tax', 'tip', 'total']
  
