from django.urls import path
from .views import*
app_name='accounts'
urlpatterns = [
     path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('change_email/', change_email, name='account_email'),
  
]