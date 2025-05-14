# from celery.worker.control import active
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import User, Department, Role
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


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department']
        extra_kwargs = {
            'id': {'required': False},
        }

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'responsibility']
        extra_kwargs = {
            'id' : {'required': False},
        }


class UserSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','username', 'department', 'role','first_name', 'last_name', 'melicode', 'phone_number','email', 'active',)
        read_only_fields = ('id','active', 'department','role')
        extra_kwargs = {'password': {'write_only': True}}

    @extend_schema_field(DepartmentSerializer)
    def get_department(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data
        return None

    @extend_schema_field(RoleSerializer)
    def get_role(self, obj):
        if obj.role:
            return RoleSerializer(obj.role).data
        return None


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

class UserEditSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
        'id', 'username', 'department', 'role','first_name', 'last_name', 'melicode', 'phone_number', 'email',
        'active',)
        read_only_fields = ('id','active',)

    def get_department(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data
        return None

    def get_role(self, obj):
        if obj.role:
            return RoleSerializer(obj.role).data
        return None


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)