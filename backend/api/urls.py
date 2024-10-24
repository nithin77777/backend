from django.contrib import admin
from django.urls import path

from .views import index, RegisterView
urlpatterns = [
    path('', index, name="index"),
    path('signup/', RegisterView.as_view(), name="RegisterView"),
    # path()
    
]
