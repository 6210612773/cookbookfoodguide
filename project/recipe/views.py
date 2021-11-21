from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import *
from django.urls import reverse_lazy
from . import views
# Create your views here.

from django.contrib.auth.models import User

from .models import *

def index_recipe (request):
    return render(request,'recipe/index.html',{
        "recipes": recipe.objects.all(),
        })


def meat (request):
    return render(request,'recipe/meat.html',{
        "recipes": recipe.objects.all(),
        })


def dessert (request):
    return render(request,'recipe/dessert.html',{
        "recipes": recipe.objects.all(),
        })


def halal (request):
    return render(request,'recipe/halal.html',{
        "recipes": recipe.objects.all(),
        })


def beverag (request):
    return render(request,'recipe/beverag.html',{
        "recipes": recipe.objects.all(),
        })


def ovovegen (request):
    return render(request,'recipe/ovovegen.html',{
        "recipes": recipe.objects.all(),
        })


def vegy (request):
    return render(request,'recipe/vegy.html',{
        "recipes": recipe.objects.all(),
        })
    

def appetizer (request):
    return render(request,'recipe/appetizer.html',{
        "recipes": recipe.objects.all(),
        })


def complete (request):
    return render(request,'recipe/complete.html')


def menu (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)
    
    if  Recipe.price == None or Recipe.price == 0.0:
        Recipe.status = "free"
        Recipe.save()        
    else :
        Recipe.status = "price"
        Recipe.save()    
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
    howtodo=Recipe.HowToDo.split('>')
    ingredient=Recipe.ingredient_unit.split('>')

        

    return render(request,"recipe/menu.html",{
        "menu": Recipe,
        "comment": Comment.objects.all(), 
        'user':request.user, 
        'howtodo':howtodo , 
        'ingredient':ingredient
    })


def like (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)

    if request.user in Recipe.like.all():
        Recipe.like.remove(request.user)
    else:
        Recipe.like.add(request.user)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    


def result (request):
    All = recipe.objects.all()
    if not request.user.is_authenticated:
        no_user = User.objects.get(username="nologin")
        find = search.objects.get(user_id=no_user)
    else:
        find = search.objects.get(user_id=request.user)
    
    menuHave = []
    menuDontNeed = []
    output=[]

    for menu in All:
        for ingInMenu in menu.ingredientInmenu.all():
            for ingHave in find.Have.all():
                if menu not in menuHave:
                    if ingHave == ingInMenu:
                        menuHave.append(menu)  
                        output.append(menu) 
            for ingNo in find.DontNeed.all():
                if ingNo == ingInMenu:
                        menuDontNeed.append(menu)
    
    for delectDontNeed in menuHave:
        for check in menuDontNeed:
            if  check == delectDontNeed:
                output.remove(delectDontNeed)

    if not output:
        output=[0]

    return render(request,'recipe/result.html',{
                "have":menuHave,
                "Dont":menuDontNeed,
                "all":All,
                "filter" :output
                }) 


def myrecipe (request):
    return render(request,'recipe/myrecipe.html',{
        "user":request.user,
        "MenuAddByUser": Addrecipe.objects.all(),
        })


def mylike (request):
    return render(request,'recipe/mylike.html',{
        "my":request.user,
        "recipes": recipe.objects.all(),
        })


def confirm_slip (request,o_id):
    all = recipe.objects.all()
    User_Order=order.objects.get(pk=o_id)
    User_Order.confirm = order.status.confirm
    User_Order.save()

    for menu in all:
        if User_Order.order == menu:
            menu.member.add(User_Order.user)
            menu.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),)


def purchased (request):
    return render(request,'recipe/purchased.html',{
        "user":request.user,
        "recipes": recipe.objects.all(),
        })


def admin_order (request):
    return render(request,'recipe/admin_order.html',{
        "recipes": recipe.objects.all(),
        "order" : order.objects.all(),
        })


def admin_petition (request):
    return render(request,'recipe/admin_petition.html',{
        "petition" :petition.objects.all()
        })


def admin_addmenu (request):
    return render(request,'recipe/admin_addmenu.html',{
        "user_addmenu" :Addrecipe.objects.all()
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
    success_url = reverse_lazy('recipe:complete')
    template_name = 'recipe/add_confirm.html'

    def form_valid(self, form):
        form.instance.order_id = self.kwargs['menu_id']
        form.instance.user = self.request.user
        form.instance.price = (recipe.objects.get(id=self.kwargs['menu_id'])).price
        return super().form_valid(form)


class Search (CreateView):
    form_class = Search
    success_url = reverse_lazy('recipe:result')
    template_name = 'recipe/search.html'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            search.objects.filter(user=User.objects.get(username="nologin")).delete()
            form.instance.user = User.objects.get(username="nologin")
        else:
            search.objects.filter(user=self.request.user).delete()
            form.instance.user = self.request.user

        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'recipe/add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['menu_id']
        self.x=self.kwargs['menu_id']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):         
        return reverse_lazy('recipe:menu',args=[self.x])
    
    
class AddRecipe(CreateView):
    model = Addrecipe
    form_class = AddForm
    template_name = 'recipe/add_recipe.html'
    success_url = reverse_lazy('recipe:complete')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.confirm = order.status.no
        return super().form_valid(form)
    





