from django.contrib import admin

# Register your models here.
from .models import React
from .models import Profile
from .models import LineItem

admin.site.register(React)
admin.site.register(Profile)
admin.site.register(LineItem)