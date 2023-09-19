from django.urls import path
from allauth.account.views import LogoutView,SignupView
from .views import*
app_name='accounts'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/',account_signup, name='account_signup'),
    path('login/',account_login , name='account_login'),
    path('change_email/', change_email, name='account_email'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/',password_reset_done, name='password_reset_done'),
    path('change-password/',change_password, name='change_password'),
  
  
]



    

