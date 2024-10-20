from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def land_here(req):
    return HttpResponse(
        '''<div>
        <h1>This is the landing Page</h1>
        </div>'''
    )

@api_view(['GET'])
def index(req):
    return JsonResponse({"Success":True} , safe=True, status=status.HTTP_200_OK, content_type='application/json')