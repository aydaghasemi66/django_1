from allauth.account.views import SignupView, LoginView, PasswordChangeView

from .forms import *

class CustomSignupView(SignupView):
    template_name = "account/signup.html" 
    form_class = CustomSignupForm  



class CustomChangePasswordView(PasswordChangeView):
    template_name = "account/change_password_custom.html" 
    form_class = CustomChangePasswordForm  


class CustomLoginView(LoginView):
    template_name = "account/login_custom.html" 
    form_class = CustomLoginForm  
