
from django.urls import path
from . import views

app_name = "about" 
urlpatterns =[
    path('', views.index, name="index"),
    path('ER/', views.ER, name="ER"),
    path('Goals/', views.Goals, name="Goals"),
    path('Personas/', views.Personas, name="Personas"),
    path('stories/', views.stories, name="stories"),
    path('Sitemap/', views.Sitemap, name="Sitemap"),
    path('Descriptions/', views.Descriptions, name="Descriptions"),
    path('Wireframes/', views.Wireframes, name="Wireframes"),
    path('non_funtional/', views.non_funtional, name="non_funtional"),

]