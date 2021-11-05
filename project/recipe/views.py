from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User

from .models import recipe

def index (request):
    return render(request,'recipe/index.html',{
        "recipes": recipe.objects.all(),
        })

def mode (request):
    return render(request,'recipe/mode.html',{
        "recipes": recipe.objects.all(),
        })

def meat (request):
    return render(request,'recipe/meat.html',{
        "recipes": recipe.objects.all(),
        })

def norm (request):
    return render(request,'recipe/norm.html',{
        "recipes": recipe.objects.all(),
        })

def hal (request):
    return render(request,'recipe/hal.html',{
        "recipes": recipe.objects.all(),
        })
    
def bev (request):
    return render(request,'recipe/bev.html',{
        "recipes": recipe.objects.all(),
        })

def oco (request):
    return render(request,'recipe/oco.html',{
        "recipes": recipe.objects.all(),
        })

def vegy (request):
    return render(request,'recipe/vegy.html',{
        "recipes": recipe.objects.all(),
        })
    
def app (request):
    return render(request,'recipe/app.html',{
        "recipes": recipe.objects.all(),
        })

def menu (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)
    if  Recipe.price == None:
        Recipe.status="free"
    elif Recipe.price > 0 :
        Recipe.status="price"
    return render(request,"recipe/menu.html",{
        "menu": Recipe,
    })
    
