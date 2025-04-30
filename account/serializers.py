from celery.worker.control import active
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs['username'] = self.initial_data.get('username')
        attrs['password'] = self.initial_data.get('password')
        return super().validate(attrs)

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        attrs['refresh'] = self.initial_data.get('refresh')
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'melicode', 'phone_number','email', 'active',)
        read_only_fields = ('id','active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            melicode=validated_data['melicode'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            active=True
        )
        return user

