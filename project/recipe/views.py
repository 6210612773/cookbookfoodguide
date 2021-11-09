from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import AddForm, CommentForm ,SendPetition,SendComfirm
from django.urls import reverse_lazy
from . import views
# Create your views here.

from django.contrib.auth.models import User

from .models import recipe,Comment,Addrecipe

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

def confirm (request):
    return render(request,'recipe/complete.html',{
        "recipes": recipe.objects.all(),
        })

def menu (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)
    if  Recipe.price == None:
        Recipe.status = "free"
    elif Recipe.price > 0 :
        Recipe.status = "price"
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
    return render(request,"recipe/menu.html",{
        "menu": Recipe,
        "comment": Comment.objects.all()
        , 'user':request.user
    })

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'recipe/add_comment.html'
    success_url = reverse_lazy('recipe:index')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['menu_id']
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddRecipe(CreateView):
    model = Addrecipe
    form_class = AddForm
    template_name = 'recipe/add_recipe.html'
    success_url = reverse_lazy('recipe:confirm')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def like (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)

    
    if request.user in Recipe.like.all():
        pass
    else:
        Recipe.like.add(request.user)
    return HttpResponseRedirect(reverse("recipe:menu",args=(menu_id,)))

def addmember (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)
    if request.user in Recipe.member.all():
        pass
    else:
        Recipe.like.add(request.user)
    return HttpResponseRedirect(reverse("recipe:menu",args=(menu_id,)))


def search (request):
    return render(request,'recipe/search.html',{
        "recipes": recipe.objects.all(),
        })

def order (request):
    return render(request,'recipe/order.html',{
        "recipes": recipe.objects.all(),
        })

class SendPetition (CreateView):
    form_class = SendPetition
    success_url = reverse_lazy('home')
    template_name = 'recipe/add_petition.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SendConfirm (CreateView):
    form_class = SendComfirm
    success_url = reverse_lazy('home')
    template_name = 'recipe/add_confirm.html'
        
    def form_valid(self, form):
        form.instance.order_id = self.kwargs['menu_id']
        form.instance.user = self.request.user
        form.instance.price = self.kwargs['menu_id']
        return super().form_valid(form)


