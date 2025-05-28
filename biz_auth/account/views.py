from http.client import responses
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import UserRegisterForm, SigninForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, OTP
from random import randint
from django.core.mail import send_mail


from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from drf_spectacular.utils import extend_schema



class SigninView(View):
    def get(self, request):
        form = SigninForm()
        return render(request, 'account/sign-in.html', {'form': form})

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(email=cleaned_data['email'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main:index')

            else:
                form.add_error('email', 'آدرس ایمیل اشتباه است')
                form.add_error('password', 'رمزعبور اشتباه است')

        return render(request, 'account/sign-in.html', {'form': form})

class SignupView(View):
    def get(self, request):
        form = SigninForm()
        return render(request, 'account/sign-up.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            random_code = randint(10000, 99999)
            OTP.objects.create(email=email, code=random_code)
            # send_mail(
            #     'Tykino',
            #     'لطفا کد جهت ثبتنام در وبسایت تیکیتو'
            #     'mohamad82abasi@gmail.com',
            #     [email],
            #     html_message=f"<h1>کد ورود شما : {random_code}</h1>",
            #     fail_silently=False,
            # )
            print(random_code)
        else:
            form.add_error('email', 'آدرس ایمیل اشتباه است')

        return render(request, 'account/sign-up.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')

            messages.success(request, 'حساب کاربری شما با موفقیت ایجاد شد. \n اکنون میتوانید وارد حساب کاربری خود شوید')
            return redirect(reverse('home:main'))
        else:
            messages.error(request, 'ثبت ‌نام انجام نشد. لطفاً اطلاعات را بررسی کنید.')
    else:
        form = UserRegisterForm()
    return render(request, 'account/registration.html', {'form': form})
# API Views


class UserCreateAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    parser_classes = [JSONParser ,MultiPartParser]
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    # parser_classes = [JSONParser]
    serializer_class = CustomTokenRefreshSerializer

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserSerializer
#     permissions_classes = [AllowAny]
#
# class UserProfileAPIView(RetrieveAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user


class UserProfileView(APIView):
    serializer_class = UserSerializer
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserEditProfileView(APIView):
    serializer_class = UserEditSerializer
    permission_classes = [IsAuthenticated,]
    parser_classes = [JSONParser,FormParser,MultiPartParser]
    def put(self, request):
        user = request.user
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    serializer_class = ChangePasswordSerializer
    permissions_classes = [IsAuthenticated,]

    def put(self, request ,username):
        password = request.data['old_password']
        new_password = request.data['new_password']

        obj = User.objects.get(username=username)
        if not obj.check_password(raw_password=password):
            return Response({'response' : 'Password not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            obj.set_password(new_password)
            obj.save()
            return Response({'response' : 'Password changed successfully'}, status=status.HTTP_200_OK)

