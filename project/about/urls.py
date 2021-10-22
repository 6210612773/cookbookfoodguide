
from django.urls import path
from . import views

app_name = "about" 
urlpatterns =[
    path('', views.index, name="index"),
    path('ER/', views.ER, name="ER"),
]