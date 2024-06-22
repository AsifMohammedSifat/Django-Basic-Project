from django.contrib import admin
from django.urls import path
from .views import in_app,show_objects,search_article,article_create

urlpatterns = [
    path('',in_app,name="in_app_templates"),
    path("create/", article_create, name="article_create"),
    path('objects/',show_objects,name="article_objects"),
    path('objects/<int:id>',show_objects),
    path('search/',search_article,name="search_article"),
]