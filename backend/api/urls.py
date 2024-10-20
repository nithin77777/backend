from django.contrib import admin
from django.urls import path

from .views import index, RegisterView, LoginView
urlpatterns = [
    path('', index, name="index"),
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login_user'),

]
