from django.urls import path
from . import views
from core.views import *
from rest_framework import renderers

urlpatterns = [
  path('profile/', ProfileView.as_view(), name='profile'),
]
