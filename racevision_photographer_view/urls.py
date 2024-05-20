from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_runner', views.add_runner, name = 'add_runner'),
    path('validate_runner', views.validate_runner, name = 'validate_runner'),
]