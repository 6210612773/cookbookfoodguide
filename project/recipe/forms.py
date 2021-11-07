from django.forms import widgets
from django.http import request
from .models import Comment, recipe
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
       model = Comment
       fields = ('body',)

       widgets = {'body': forms.Textarea}
       