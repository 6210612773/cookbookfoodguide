from django.urls import path


from .views import SignUpView,PasswordChangeView , CustomUserChangeView 
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', PasswordChangeView.as_view(),name='EditPassword'  ),
    path('editProfile/',CustomUserChangeView.as_view(),name='EditProfile' ),
]