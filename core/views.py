import profile
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from . import views
from django.contrib.auth.models import User

# Create your views here.

class ProfileView(APIView):

    serializer_class = ProfileSerializer

    def get(self, request):
        user = [
            {
                "username": profile.user.username,
                "created_date": profile.created_date,
                "address": profile.address,
                "first_name": profile.user.first_name,
                "last_name": profile.user.last_name,
                "email": profile.user.email,
            }
            for profile in Profile.objects.all()
        ]
        return Response(user)


# class UserView(APIView):

#     serializer_class = UserSerializer

# def get_user(user_id):
#   user = [
#         {
#             "user_id": user_id,
#             # "first_name": User.user.first_name,
#             # "last_name": User.user.last_name,
#             # "email": User.user.email,
#         }
#         for user in User.objects.all()
#     ]
#   return Response(user)


# def post(self, request):
#     serializer = MenuItemSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)


# class MenuItemView(APIView):

#     serializer_class = MenuItemSerializer

#     def get(self, request):
#         item = [
#             {
#                 "name": item.name,
#                 "description": item.description,
#                 "price": item.price,
#                 "image": item.image,
#                 "qty": item.qty,
#             }
#             for item in MenuItem.objects.all()
#         ]
#         return Response(item)

#     def post(self, request):
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
class MenuItemViewSet(ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
class CourierViewSet(ModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()
    
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

        
    
