from django.urls import path, include
from .views import *
from rest_framework import renderers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('menuitems/', MenuItemView.as_view(), name='menu_items'),
  path('menuitems/<str:id>/', MenuItemDetailView.as_view(), name='menu_item'),
  path('orders/', OrderView.as_view(), name='orders'),
]
