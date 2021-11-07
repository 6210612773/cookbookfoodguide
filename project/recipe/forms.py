from django.forms import widgets
from django.http import request
from .models import Comment, recipe , Addrecipe
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
       model = Comment
       fields = ('body',)

       widgets = {'body': forms.Textarea}
       

class AddForm(forms.ModelForm):
    class Meta:
       model = Addrecipe
       fields = ('bankaccount','menu','pic','ingredient_unit',
       'HowToDo','ingredientHave','type','price','calorie')

       widgets = {'bankaccount': forms.TextInput}
       