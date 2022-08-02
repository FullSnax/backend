from django.contrib import admin
# from django.contrib.auth import Profile

# Register your models here.
from .models import *

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Courier)
