from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("authentication.urls")),
    path("api/", include("core.urls")),
    
    #     path('', views.getRoutes),
    #     path('profile/', ProfileView.as_view(), name='profiles'),
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
