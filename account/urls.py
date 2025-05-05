from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
from .views import *

app_name = 'account'

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register', UserCreateAPIView.as_view(), name='register'),
    path('profile', UserProfileAPIView.as_view(), name='profile'),
    path('profile/edit', UserEditProfileView.as_view(), name='profile-edit'),
    path('profile/change_password/<int:pk>', ChangePasswordView.as_view(), name='change-password'),
]