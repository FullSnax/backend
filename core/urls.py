from django.urls import path, include
from . import views
from core.views import *
from rest_framework import renderers

urlpatterns = [
  path('profile/', ProfileView.as_view(), name='profiles'),
  path('profile/<int:pk>/update', ProfileView.as_view(), name='profile_update'),
  path('menuitems/', MenuItemView.as_view(), name='menu_items'),
  path('orders/', OrderView.as_view(), name='orders'),
]
