from django.shortcuts import render

# Create your views here.

def in_app(request):
    return render(request,"articles/article_detail.html")