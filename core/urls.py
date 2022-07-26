from django.urls import path, include
from . import views
from core.views import *
from rest_framework import renderers

urlpatterns = [
  path('profile/', ProfileView.as_view(), name='profiles'),
  path('menuitems/', MenuItemView.as_view(), name='menu_item'),
]
