from django.shortcuts import render,get_object_or_404
from .models import article
from django.http import HttpResponse

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


def search_article(request,*args, **kwargs):
    # print(dir(request))
    context = {"object":None}
    try:
        id = int(request.GET.get('q')) 
    except:
        id = None

    # print(type(id))

                                # Way-1
    # if id is not None:
    #     # object = article.objects.get(id=id)
    #     object = get_object_or_404(article,id=id)
    #     context = {
    #         "object":object
    #     }
    # return render(request,"articles/article_search.html",context)

                                # Way-2
    if id is not None:
        try:
            object = article.objects.get(id=id)
            context = {
                "object":object
            }
        except:
            return HttpResponse("<h1>No Result Found</h1>")
            
    return render(request,"articles/article_search.html",context)
