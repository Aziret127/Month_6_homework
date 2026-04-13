from django.urls import path
from .views import AuthorizationAPIView, RegistrationAPIView, ConfirmUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('/api/auth/', AuthorizationAPIView.as_view(), name='auth'),
    path('api/register/', RegistrationAPIView.as_view(), name='register'),
    path('api/confirm/', ConfirmUserAPIView.as_view(), name='confirm'),

     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]