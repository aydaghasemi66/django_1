from django.urls import path
from .views import*
app_name='accounts'
urlpatterns = [
     path('signup/', account_signup, name='account_signup'),
    path('logout/', accouont_logout, name='account_logout'),
    path('login/',account_login , name='account_login'),
    path('change_email/', change_email, name='account_email'),
  
]