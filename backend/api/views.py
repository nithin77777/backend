from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from .checks import user_is_valid
from .permissions import CustomPermission
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

    

def land_here(req):
    return HttpResponse(
        '''<div>
        <h1>This is the landing Page</h1>
        </div>'''
    )

@api_view(['GET'])
def index(req):
    return JsonResponse({"Success":True} , safe=True, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self,req):
        
        if req.method == 'POST':
            name = req.data.get('name')
            user_id = req.data.get('user_id')
            password = req.data.get('password')

            if not all([name, user_id, password]):
                return JsonResponse({"status":"Incomplete Credentials"}, safe=True, status=status.HTTP_400_BAD_REQUEST)
            if len(password) < 6:
                return JsonResponse({"error":"Password should be 6 characters minimum"}, safe=True, status=status.HTTP_400_BAD_REQUEST)
            
            if User.objects.filter(user_id=user_id).exists():
                return JsonResponse({"error": "User ID already taken."}, status=status.HTTP_409_CONFLICT)

            try:
                user = User.objects.create(name=name, user_id=user_id, password=make_password(password))
                return JsonResponse({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return JsonResponse({"error": str(e)},safe=True, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, req):
        if req.method == 'GET':
            users = User.objects.all().values('name', 'user_id')
            return JsonResponse({"users": list(users)},safe=True, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self,req):
        serializer = LoginSerializer(data=req.data)
        serializer.is_valid(raise_exception=True) 
        print(serializer.is_valid(raise_exception=True))  # This will raise an exception if invalid
        
        user_id = serializer.validated_data["user_id"]
        password = serializer.validated_data["password"]
        print(user_id, password)

        if user_is_valid(user_id, password):
            return JsonResponse(
                {"message": "Login is Successful", "status": "Success"},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"message": "Invalid Credentials", "status": "Error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

