from django.urls import path, include
from . import views
from core.views import *
from rest_framework import routers
from rest_framework import renderers

router = routers.DefaultRouter()
router.register(r'menuitems', MenuItemViewSet)



urlpatterns = [
  path('profile/', ProfileView.as_view(), name='profile'),
  # path('menuitem/', MenuItemView.as_view(), name='menu_item'),
  path('wel/', ReactView.as_view(), name="react"),
]
