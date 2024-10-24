from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import 

@api_view(['GET'])
def index(req):
    return JsonResponse("Success" ,safe=False, status=status.HTTP_200_OK)

