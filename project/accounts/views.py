
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editpassword.html'

class CustomUserChangeView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editProfile.html'
    def get_object(self):
        return self.request.user

