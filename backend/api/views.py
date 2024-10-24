from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import logging 
# Create your views here.

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer


logger = logging.getLogger(__name__)

@api_view(['GET'])
def index(req):
    return JsonResponse("Success" ,safe=False, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, req):
        serializer = CustomUserSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            logger.exception(msg=f'after saving", {serializer.data}, {status.HTTP_201_CREATED}',exc_info=1)
            return Response({"status":"Success","data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            logger.error("Error at RegisterView.POST serialization","validation error" ,serializer.errors, status.HTTP_409_CONFLICT)
            # print(serializer.errors)
            return JsonResponse({"error":serializer.errors}, safe=False, status=status.HTTP_409_CONFLICT)
        
class LoginView(APIView):
    pass
       
