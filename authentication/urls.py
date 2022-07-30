from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ObtainTokenPairWithColorView, ProfileCreate, LogoutAndBlacklistRefreshTokenForUserView, HelloWorldView

urlpatterns = [
    # path('token/obtain', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('user/create/', ProfileCreate.as_view(), name="create_user"),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('hello/', HelloWorldView.as_view(), name='hello_world')
]