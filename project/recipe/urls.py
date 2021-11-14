from django.urls import path

from . import views
from .views import AddCommentView,AddRecipe,SendPetition, SendConfirm ,Search

app_name = "recipe" 
urlpatterns =[
    path('', views.index, name="index"),
    path('meat', views.meat, name="meat"),
    path('norm', views.norm, name="norm"),
    path('hal', views.hal, name="hal"),
    path('bev', views.bev, name="bev"),
    path('oco', views.oco, name="oco"),
    path('vegy', views.vegy, name="vegy"),
    path('app', views.app, name="app"),
    path('<int:menu_id>',views.menu,name="menu"),
    path('<int:menu_id>/comment/',AddCommentView.as_view(),name="AddComment") ,
    path('addrecipe',AddRecipe.as_view(),name="addrecipe"),
    path('complete',views.confirm,name="complete"),
    path('<int:menu_id>/like',views.like,name="like"),
    path('send/', SendPetition.as_view(), name='send'),
    path('<int:menu_id>/confirm/',SendConfirm.as_view(), name='confirm'),
    path('search', Search.as_view(), name="search"),
    path('result', views.result, name="result"),
    path('myrecipe', views.myrecipe , name="myrecipe"),
    path('mylike', views.mylike, name="mylike"),
    path('purchased', views.purchased, name="purchased"),
    path('order', views.admin_order, name="order"),
    path('<int:o_id>/check',views.check,name="check"),
    path('useraddmenu', views.admin_addmenu, name="addmenu"),
    path('petition', views.admin_petition, name="petition"),



]
