import profile
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import viewsets
from . serializer import *
from . import views
# Create your views here.

class ReactView(APIView):
	
	serializer_class = ReactSerializer

	def get(self, request):
		detail = [ {"name": detail.name,"detail": detail.detail}
		for detail in React.objects.all()]
		return Response(detail)

	def post(self, request):
		serializer = ReactSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
 
class ProfileView(APIView):
	
	serializer_class = ProfileSerializer

	def get(self, request):
		detail = [ {"address": detail.address,"created_date": detail.created_date}
		for detail in Profile.objects.all()]
		return Response(detail)

	def post(self, request):
		serializer = ProfileSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
 
class MenuItemView(APIView):
	
	serializer_class = MenuItemSerializer

	def get(self, request):
		detail = [ {"address": detail.address,"created_date": detail.created_date}
		for detail in MenuItem.objects.all()]
		return Response(detail)

	def post(self, request):
		serializer = MenuItemSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)

    
 
 
