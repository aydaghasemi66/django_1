
from allauth.account.views import LoginView, SignupView ,LogoutView
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "You've successfully signed up!")
        return redirect('home')



class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You've successfully logged out!")
        return response

class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # Specify your custom template name here

    def form_valid(self, form):
        # Add custom logic here when the form is valid
        # For example, you can send a custom message to the user
        messages.success(self.request, "You've successfully logged in!")

        # You can also add custom actions such as redirecting the user
        return redirect('home')


@login_required
def change_email(request):

    return render(request, 'account/change_email.html')