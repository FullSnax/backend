from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'menuitems', MenuItemViewSet)
router.register(r'couriers', CourierViewSet)
router.register(r'orders', OrderViewSet)