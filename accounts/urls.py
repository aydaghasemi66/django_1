from django.urls import include, path
from .views import *

urlpatterns = [

    path("signup/", CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('change-password/', CustomChangePasswordView.as_view(), name='account_change_password'),
]






    

