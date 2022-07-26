import profile
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import renderers
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
    
class MenuItemView(APIView):

    serializer_class = MenuItemSerializer
    # image_data = tf.gfile.FastGFile(filename, 'rb').read()

    def get(self, request):
        menu_items = [
            {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                # "image": item.image,
                "qty": item.qty,
            }
            for item in MenuItem.objects.all()
        ]
        return Response(menu_items)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# class OrderView(APIView):

#     serializer_class = OrderSerializer

#     def get(self, request):
#         user = [
#             {
#                 "username": profile.user.username,
#                 "created_date": profile.created_date,
#                 "address": profile.address,
#                 "first_name": profile.user.first_name,
#                 "last_name": profile.user.last_name,
#                 "email": profile.user.email,
#             }
#             for order in Order.objects.all()
#         ]
#         return Response(user)

