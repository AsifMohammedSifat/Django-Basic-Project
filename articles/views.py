from django.shortcuts import render
from .models import article

# Create your views here.

def in_app(request):
    return render(request,"articles/article_detail.html")


def show_objects(request,id=None):
    context = {}
    if id is not None:
        object = article.objects.get(id=id)     
        context['object'] = object
    else:
        objects = article.objects.all()     
        context['objects'] = objects
    return render(request,"articles/article_objects.html",context)
