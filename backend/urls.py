import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from core.views import *
from core.routers import router
 
urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include(router.urls))
]
