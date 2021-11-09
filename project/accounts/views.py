
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView 
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editpassword.html'

class CustomUserChangeView(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editProfile.html'

