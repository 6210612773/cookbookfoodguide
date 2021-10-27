from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User

def index (request):
    return render(request,'recipe/index.html',{
        
        })