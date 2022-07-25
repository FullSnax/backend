from django.contrib import admin

# Register your models here.
from .models import React, Profile, MenuItem, Order, Courier

admin.site.register(React)
admin.site.register(Profile)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Courier)
