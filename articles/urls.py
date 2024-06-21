from django.contrib import admin
from django.urls import path
from .views import in_app,show_objects

urlpatterns = [
    path('',in_app,name="in_app_templates"),
    path('objects/',show_objects,name="article_objects"),
    path('objects/<int:id>',show_objects),
]