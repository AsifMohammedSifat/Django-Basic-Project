from django.contrib import admin
from django.urls import path
from .views import in_app

urlpatterns = [
    path('',in_app),
]