from django.forms import widgets
from django.http import request




from .models import Comment, recipe , Addrecipe ,petition,order,search
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
       'HowToDo','type','price','calorie')

       widgets = {'bankaccount': forms.TextInput}

class SendPetition(forms.ModelForm):

    class Meta:
        model = petition
        fields = ('petition',)

class SendComfirm(forms.ModelForm):
    class Meta:
        model = order
        fields = ('pic','date','time','name','bankaccount',)
        widgets = {'date': forms.SelectDateWidget,
                    'time': forms.TimeInput(attrs={'type': 'time'},),
                    }
        

class Search(forms.ModelForm):

    class Meta:
        model = search
        fields = ('Have','DontNeed')
        widgets = {'Have': forms.CheckboxSelectMultiple,
                    'DontNeed' : forms.CheckboxSelectMultiple}






        
       