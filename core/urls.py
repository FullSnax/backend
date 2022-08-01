from django.urls import path, include
from .views import *
from rest_framework import renderers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  # path('profile/<int:pk>/update', ProfileView.as_view(), name='profile_update'),
  path('menuitems/', MenuItemView.as_view(), name='menu_items'),
  path('orders/', OrderView.as_view(), name='orders'),
]
