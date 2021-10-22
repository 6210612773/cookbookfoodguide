from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email' ,'first_name','last_name')
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')