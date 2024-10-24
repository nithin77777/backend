from django.http import JsonResponse

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["name", "user_id", "password"]
    


    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        
        return user
    
    def validate(self, data):
        name = data.get('name')
        user_id = data.get('user_id')
        password = data.get('password')

        if CustomUser.objects.filter(user_id=user_id).exists():
            return serializers.ValidationError({"error": "User ID already taken."}, status=status.HTTP_409_CONFLICT)

        if not all([name, user_id, password]):
           return serializers.ValidationError({"error": "Incomplete Credentials"}, safe=True, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 6:
            return serializers.ValidationError({"error": "Password should be 6 characters minimum"}, safe=True, status=status.HTTP_400_BAD_REQUEST)

        return data