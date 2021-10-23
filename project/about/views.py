
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User

def index (request):
    return render(request,'about/index.html',{
        ##"about": Subject.objects.all(),
        ##"user":request.user,
        })

def ER (request):
    return render(request,'about/ER.html',{})

def Goals (request):
    return render(request,'about/Goals.html',{})

def Personas (request):
    return render(request,'about/Personas.html',{})

def stories (request):
    return render(request,'about/stories.html',{})

def Sitemap (request):
    return render(request,'about/Sitemap.html',{})

def Descriptions (request):
    return render(request,'about/Descriptions.html',{})

def Wireframes (request):
    return render(request,'about/Wireframes.html',{})

def non_funtional (request):
    return render(request,'about/non_funtional.html',{})


