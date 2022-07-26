import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from core.views import *
from core.routers import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
