from http.client import responses
from django.shortcuts import render
from elasticsearch.dsl.serializer import serializer
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
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def put(self, request ,pk):
        password = request.data['old_password']
        new_password = request.data['new_password']

        obj = User.objects.get(id=pk)
        if not obj.check_password(raw_password=password):
            return Response({'response' : 'Password not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            obj.set_password(new_password)
            obj.save()
            return Response({'response' : 'Password changed successfully'}, status=status.HTTP_200_OK)

