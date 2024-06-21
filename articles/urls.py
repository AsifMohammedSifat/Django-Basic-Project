from django.contrib import admin
from django.urls import path
from .views import in_app,show_objects,search_article

urlpatterns = [
    path('',in_app,name="in_app_templates"),
    path('objects/',show_objects,name="article_objects"),
    path('objects/<int:id>',show_objects),
    path('search/',search_article,name="search_article"),
]