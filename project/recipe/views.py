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

def index (request):
    return render(request,'recipe/index.html',{
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
    
    if  Recipe.price == None :
        Recipe.status = "free"
        Recipe.save()        
    else :
        Recipe.status = "price"
        Recipe.save()    
    x=Recipe.HowToDo.split('>')
    y=Recipe.ingredient_unit.split('>')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"recipe/menu.html",{
        "menu": Recipe,
        "comment": Comment.objects.all()
        , 'user':request.user, 'x':x , 'y':y
    })

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'recipe/add_comment.html'
    # success_url = reverse_lazy('home')
    
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
    

def like (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)

    if request.user in Recipe.like.all():
        pass
    else:
        Recipe.like.add(request.user)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

def addmember (request,menu_id):
    Recipe = get_object_or_404(recipe,pk=menu_id)
    if request.user in Recipe.member.all():
        pass
    else:
        Recipe.like.add(request.user)
    return HttpResponseRedirect(reverse("recipe:menu",args=(menu_id,)))

def result (request):
    All = recipe.objects.all()
    if not request.user.is_authenticated:
        x = User.objects.get(username="nologin")
        find = search.objects.get(user_id=x)
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
    
    for check in menuHave:
        for check2 in menuDontNeed:
            if  check2 == check:
                output.remove(check)
    if not output:
        output=[0]

    return render(request,'recipe/result.html',{
                "have":menuHave,
                "Dont":menuDontNeed,
                "all":All,
                "check" :output
                }) 

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
    

# def order (request):
#     return render(request,'recipe/order.html',{
#         "recipes": recipe.objects.all(),
#         })

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

def myrecipe (request):
    return render(request,'recipe/myrecipe.html',{"my":request.user,
        "add": Addrecipe.objects.all(),
        })

def mylike (request):
    return render(request,'recipe/mylike.html',{"my":request.user,
        "recipes": recipe.objects.all(),
        })

def check (request,o_id):
    all = recipe.objects.all()
    x=order.objects.get(pk=o_id)
    x.confirm = order.status.confirm
    x.save()

    for y in all:
        if x.order == y:
            y.member.add(x.user)
            y.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),)

def purchased (request):
    return render(request,'recipe/purchased.html',{"my":request.user,
        "recipes": recipe.objects.all(),
        })

def admin_order (request):
    return render(request,'recipe/admin_order.html',{
        "recipes": recipe.objects.all(),
        "order" : order.objects.all(),
        "pet" :petition.objects.all(),
        "add" :Addrecipe.objects.all()
        })

def admin_petition (request):
    return render(request,'recipe/admin_petition.html',{
        "recipes": recipe.objects.all(),
        "order" : order.objects.all(),
        "pet" :petition.objects.all(),
        "add" :Addrecipe.objects.all()
        })

def admin_addmenu (request):
    return render(request,'recipe/admin_addmenu.html',{
        "recipes": recipe.objects.all(),
        "order" : order.objects.all(),
        "pet" :petition.objects.all(),
        "add" :Addrecipe.objects.all()
        })



