from django.http import HttpResponse
from django.shortcuts import render

HTML_STRING = "<h1>Hello World</h1>"

def home(request):
    return render(request,"base.html")

def htmlString(request):
    return HttpResponse(HTML_STRING)

def global_template(request):
    return render(request,"base.html")

def inProject_template(request):
    return render(request,"in_project.html")