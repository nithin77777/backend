from .models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'user_id', 'password']


class LoginSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)