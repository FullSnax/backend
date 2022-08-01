from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    ProfileCreate,
    LogoutAndBlacklistRefreshTokenForUserView,
    LogoutAllView,
    MyTokenObtainPairView
)
from core.views import LoginView, RegisterView

urlpatterns = [
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/obtain/", MyTokenObtainPairView().as_view(), name="token_create"),
    path("user/create/", ProfileCreate.as_view(), name="create_user"),
    path("token/blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name="blacklist",),
    path("logout_all/", LogoutAllView.as_view(), name="auth_logout_all"),
    path("login/", MyTokenObtainPairView.as_view(), name="auth_login"),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
