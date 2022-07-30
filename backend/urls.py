from django.contrib import admin
from django.urls import path, include
from core.views import *
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
    
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/', include('core.urls')),
    # path('api/login/', LoginView.as_view(), name='auth_login'),
    #     path('__debug__/', include('debug_toolbar.urls')),
    #     path('api/token/obtain', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #     path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    #     path('api/logout/', BlacklistRefreshView.as_view(), name="logout"),
    #     path('api/register/', RegisterView.as_view(), name='auth_register'),
    #     path('', views.getRoutes),
    #     path('profile/', ProfileView.as_view(), name='profiles'),
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
