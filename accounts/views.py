from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_view(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is None:
            context = {"error":"No User Found!"}
            return render(request,"login.html",context)
        login(request,user)
        return redirect("article_objects")

    return render(request,"login.html")

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    return render(request,"logout.html")

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("Access")
        return redirect('login')
    context = {"form":form}
    return render(request,"register.html",context)