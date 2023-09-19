from allauth.account.views import SignupView, LoginView, PasswordChangeView

from .forms import *

class CustomSignupView(SignupView):
    template_name = "account/signup.html" 
    form_class = CustomSignupForm  



class CustomChangePasswordView(PasswordChangeView):
    template_name = "account/change_password_custom.html"  # Customize the template as needed
    form_class = CustomChangePasswordForm  # Use the custom change password form you created


class CustomLoginView(LoginView):
    template_name = "account/login_custom.html"  # Customize the template as needed
    form_class = CustomLoginForm  # Use the custom login form you created
