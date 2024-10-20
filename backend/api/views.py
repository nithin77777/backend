from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.response import 

@api_view(['GET'])
def index(req):
    return JsonResponse("Success" ,safe=False, status=status.HTTP_200_OK)