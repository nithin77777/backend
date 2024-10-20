from django.contrib import admin
from django.urls import path

from .views import index,register
urlpatterns = [
    path('', index, name="index"),
    path('signup/', register, name='register'),
    # path('login/', login, name='login'),

]
