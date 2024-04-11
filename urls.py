"""
URL configuration for csitdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from random import randint


def index(request):
    #return HttpResponse(f"<h2>Hello from Django, random number is {randint(0,100)}</h2>")
    return HttpResponse(f"ok")

def summer(request,a,b):
    return HttpResponse(f"The sum is {a+b}")

def multiplication(request):
    #user= request.GET['user']
    
    
    user= request.GET.get('user')
    address= request.GET.get('address')

    #print(request.GET)
    return HttpResponse(f"<h1>username is {user} and address is {address} </h1>") 

def Home(request):
    #print(request.GET)
    user= request.GET.get('username') 
    password= request.GET.get('password') 
    address= request.GET.get('address')
    checked= request.GET.get('checked')

    context={
        "user":user,
        "password":password,
        "address":address,
        'checked_data':checked
        
    }
    return render(request, "base.html",context) 
def mypage(request):
    context = {
        'movie_list' :['ANIMAL','LEO','JAWAN','JAILER'],
        'favourite_movie':"LEO"
    }
    return render(request,'mypage.html',context)

  
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",mypage),
    path("home",Home),
    path('sum/<str:a>/<str:b>/', summer,),
    path('queryparams/',multiplication)
]
