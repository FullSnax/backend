from django.contrib import admin

# Register your models here.
from .models import React, Profile, LineItem, Order, Courier

admin.site.register(React)
admin.site.register(Profile)
admin.site.register(LineItem)
admin.site.register(Order)
admin.site.register(Courier)
