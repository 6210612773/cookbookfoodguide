from django.urls import path
from . import views
from .views import AddCommentView,AddRecipe

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
    path('mode', views.mode, name="mode"),
    path('<int:menu_id>',views.menu,name="menu"),
    path('<int:menu_id>/comment/',AddCommentView.as_view(),name="AddComment") ,
    path('addrecipe',AddRecipe.as_view(),name="addrecipe"),
    path('confirm',views.confirm,name="confirm"),

]