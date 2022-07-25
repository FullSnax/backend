import profile
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import viewsets
from .serializer import *
from . import views
from django.contrib.auth.models import User

# Create your views here.


class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        detail = [
            {"name": detail.name, "detail": detail.detail}
            for detail in React.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class ProfileView(APIView):

    serializer_class = UserSerializer

def get(self, request):
  profile = [
        {
            "address": profile.address,
            "created_at": profile.created_date
        }
        for profile in Profile.objects.all()
    ]
  return Response(profile)

class UserView(APIView):

    serializer_class = UserSerializer

def get_user(user_id):
  user = [
        {
            "user_id": user_id,
            # "first_name": User.user.first_name,
            # "last_name": User.user.last_name,
            # "email": User.user.email,
        }
        for user in User.objects.all()
    ]
  return Response(user)


def post(self, request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


class MenuItemView(APIView):

    serializer_class = MenuItemSerializer

    def get(self, request):
        item = [
            {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "image": item.image,
                "qty": item.qty,
            }
            for item in MenuItem.objects.all()
        ]
        return Response(item)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
