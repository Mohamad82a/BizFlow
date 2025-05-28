from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
# from rest_framework.routers import DefaultRouter
from .views import (

    SigninView,
    SignupView,

    CustomTokenObtainPairView,
    UserProfileView,
    CustomTokenRefreshView,
    UserCreateAPIView,
    UserEditProfileView,
    ChangePasswordView,


)
from django.contrib import admin

app_name = 'account'

# router = DefaultRouter()
# router.register(r'users', UserProfileView)

urlpatterns = [

    path('signin', SigninView.as_view(), name='sign-in'),
    path('signup', SignupView.as_view(), name='sign-up'),


    # //////////
    # API Urls
    # //////////

    # # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('', include(router.urls)),

    path('register', UserCreateAPIView.as_view(), name='register'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('profile/edit', UserEditProfileView.as_view(), name='profile-edit'),
    path('profile/change_password/<str:username>', ChangePasswordView.as_view(), name='change-password'),
]