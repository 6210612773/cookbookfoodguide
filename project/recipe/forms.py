from .models import Comment, recipe
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
       model = Comment
       fields = [
           'post','body'
       ]