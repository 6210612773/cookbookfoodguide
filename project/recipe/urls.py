from django.urls import path

from . import views
from .views import *

app_name = "recipe" 
urlpatterns =[
    path('', views.index_recipe, name="index"),
    path('meat', views.meat, name="meat"),
    path('norm', views.dessert, name="norm"),
    path('hal', views.halal, name="hal"),
    path('bev', views.beverag, name="bev"),
    path('oco', views.ovovegen, name="oco"),
    path('vegy', views.vegy, name="vegy"),
    path('app', views.appetizer, name="app"),
    path('<int:menu_id>',views.menu,name="menu"),
    path('<int:menu_id>/comment/',AddCommentView.as_view(),name="AddComment") ,
    path('addrecipe',AddRecipe.as_view(),name="addrecipe"),
    path('complete',views.complete,name="complete"),
    path('<int:menu_id>/like',views.like,name="like"),
    path('send/', SendPetition.as_view(), name='send'),
    path('<int:menu_id>/confirm/',SendConfirm.as_view(), name='confirm'),
    path('search', Search.as_view(), name="search"),
    path('result', views.result, name="result"),
    path('myrecipe', views.myrecipe , name="myrecipe"),
    path('mylike', views.mylike, name="mylike"),
    path('purchased', views.purchased, name="purchased"),
    path('order', views.admin_order, name="order"),
    path('<int:o_id>/check',views.confirm_slip,name="check"),
    path('useraddmenu', views.admin_addmenu, name="addmenu"),
    path('petition', views.admin_petition, name="petition"),



]
