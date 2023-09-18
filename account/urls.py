from allauth.account.views import SignupView, LoginView, LogoutView 
from django.urls import path, include
from .views import *
from django.contrib import admin

app_name = 'account'


urlpatterns = [
    
    path('signup/', SignupView.as_view(), name='signup'),
    path('account/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]